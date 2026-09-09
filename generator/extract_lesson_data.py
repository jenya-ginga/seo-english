#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts a speaking-practice question bank from the already-built
lessons/N/index.html files (N = 1..15) of the seo-english site.

Two question types are produced:
  - "term": a Russian prompt -> the player must say the English equivalent
            out loud, fast. Sourced from .phrase-card <span class="en">/
            <span class="ru"> pairs and from <table> rows inside
            .table-scroll blocks (2+ columns, first column mostly Latin,
            second column mostly Cyrillic).
  - "client": an English client question pulled from <li> items inside
              accordion bodies (role-play follow-up questions) that end
              with "?" and are mostly Latin script. The player must
              answer it out loud in English, immediately.

Run this ON THE DEVICE from the repo root:
    python3 generator/_tmp_extract_lessons.py > generator/lesson_data.json
"""
import json
import os
import re
import sys
import html as htmlmod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if False else None

LATIN_RE = re.compile(r'[A-Za-z]')
CYRILLIC_RE = re.compile(r'[А-Яа-яЁё]')


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return htmlmod.unescape(s).strip()


def mostly_latin(s, threshold=0.6):
    letters = re.findall(r'[A-Za-zА-Яа-яЁё]', s)
    if not letters:
        return False
    latin = len(LATIN_RE.findall(s))
    return latin / max(1, len(letters)) >= threshold


def mostly_cyrillic(s, threshold=0.4):
    letters = re.findall(r'[A-Za-zА-Яа-яЁё]', s)
    if not letters:
        return False
    cyr = len(CYRILLIC_RE.findall(s))
    return cyr / max(1, len(letters)) >= threshold


def extract_phrase_cards(html, lesson_title, lesson_num, seen):
    out = []
    for m in re.finditer(
        r'<span class="en">(.*?)</span>\s*<span class="ru">(.*?)</span>',
        html, re.S,
    ):
        en = strip_tags(m.group(1))
        ru = strip_tags(m.group(2)).lstrip('—- ').strip()
        if not en or not ru:
            continue
        if len(en) > 90 or len(ru) > 120:
            continue
        if '___' in en or '___' in ru or '\xa0' in en or '\xa0' in ru:
            continue
        if not mostly_cyrillic(ru, 0.4):
            # Some "en" cells embed the Russian gloss in parentheses instead
            # of a separate ru column, e.g. "Actually (на самом деле)" +
            # an English example sentence. Recover a clean term/translation
            # pair from that parenthetical instead of discarding the entry.
            pm = re.match(r'^(.*?)\s*\(([^)]+)\)\s*$', en)
            if pm and mostly_cyrillic(pm.group(2), 0.4):
                en2 = pm.group(1).strip()
                ru2 = pm.group(2).strip()
                if en2 and ru2 and len(en2) <= 90 and len(ru2) <= 120:
                    key2 = (lesson_num, en2.lower())
                    if key2 not in seen:
                        seen.add(key2)
                        out.append({"type": "term", "lesson": lesson_num, "lessonTitle": lesson_title, "en": en2, "ru": ru2})
            continue
        key = (lesson_num, en.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append({"type": "term", "lesson": lesson_num, "lessonTitle": lesson_title, "en": en, "ru": ru})
    return out


def extract_tables(html, lesson_title, lesson_num, seen):
    out = []
    for tbl in re.findall(r'<div class="table-scroll">(.*?)</div>\s*(?:</div>|<div class="note">|</section>)', html, re.S):
        rows = re.findall(r'<tr>(.*?)</tr>', tbl, re.S)
        if not rows:
            continue
        for row in rows[1:] if '<th>' in rows[0] else rows:
            cells = re.findall(r'<td>(.*?)</td>', row, re.S)
            if len(cells) < 2:
                continue
            c0 = strip_tags(cells[0])
            c1 = strip_tags(cells[1])
            if not c0 or not c1:
                continue
            if len(c0) > 90 or len(c1) > 140:
                continue
            if mostly_latin(c0) and mostly_cyrillic(c1):
                key = (lesson_num, c0.lower())
                if key in seen:
                    continue
                seen.add(key)
                out.append({"type": "term", "lesson": lesson_num, "lessonTitle": lesson_title, "en": c0, "ru": c1})
    return out


def extract_and_mask_tagged_client_lines(html, lesson_title, lesson_num, seen):
    """
    Two more lesson layouts quote a client line right next to a
    "<span class=\"tag-role\">" difficulty/speaker tag, mixed in among
    otherwise-legitimate specialist phrase-card content:

      - lesson 5: each <li> is <span class="tag-role">простой|каверзный</span>
        + <span class="en">"..."</span><span class="ru">...</span>, where the
        en/ru pair is the CLIENT's quoted line + its translation, not a
        specialist phrase to translate.
      - lesson 12 (and similar): <span class="tag-role">Client</span>
        immediately followed by <blockquote class="script">"..."</blockquote>
        — the blockquote is the client's line; a separate "Hint" en/ru pair
        that comes after it in the same xcard is legitimate specialist
        guidance and is left alone.

    Both patterns are masked out of the html this returns so the generic
    phrase-card/table extractors that run afterwards can't re-capture the
    same lines as "term" (specialist-says) content.
    """
    out = []

    def add_client(text):
        text = strip_tags(text).strip().strip('"“”‘’\'').strip()
        if not text or not mostly_latin(text, 0.75):
            return
        if len(text) < 15 or len(text) > 220:
            return
        key = (lesson_num, 'q:' + text.lower())
        if key in seen:
            return
        seen.add(key)
        out.append({"type": "client", "lesson": lesson_num, "lessonTitle": lesson_title, "en": text})

    # <li> items tagged with a role: some lessons (5) tag every line with a
    # difficulty ("простой"/"каверзный") and every one of those IS a client
    # line; others (15) tag lines with the actual speaker ("клиент" vs
    # "специалист") in the same dialogue — only the "клиент" ones should be
    # masked out as client content, "специалист" lines are legitimate
    # translate-practice material and must be left alone so the normal
    # phrase-card extractor still picks them up.
    CLIENT_ROLE_LABELS = {'клиент', 'client', 'простой', 'каверзный', 'сложный', 'средний'}
    SPECIALIST_ROLE_LABELS = {'специалист', 'specialist'}

    def li_repl(m):
        li_body = m.group(1)
        tr_m = re.search(r'<span class="tag-role">(.*?)</span>', li_body, re.S)
        if not tr_m:
            return m.group(0)
        role = strip_tags(tr_m.group(1)).strip().lower()
        if role in SPECIALIST_ROLE_LABELS:
            return m.group(0)  # leave untouched — normal term extraction applies
        if role in CLIENT_ROLE_LABELS:
            en_m = re.search(r'<span class="en">(.*?)</span>', li_body, re.S)
            if en_m:
                add_client(en_m.group(1))
            return ''  # mask — its en/ru pair must not become a "term"
        return m.group(0)  # unrecognised role label — safest to leave as-is

    html = re.sub(r'<li>(.*?)</li>', li_repl, html, flags=re.S)

    # tag-role="Client" immediately followed by a quoted <blockquote class="script">
    def bq_repl(m):
        add_client(m.group('bq'))
        return ''  # mask just the tag+blockquote; any following Hint stays intact

    html = re.sub(
        r'<span class="tag-role">Client</span>\s*<blockquote class="script">(?P<bq>.*?)</blockquote>',
        bq_repl, html, flags=re.S,
    )

    return out, html


CLIENT_QUESTION_CATEGORY_RE = re.compile(r'\d+\s*вопрос', re.I)


def extract_and_mask_client_question_categories(html, lesson_title, lesson_num, seen):
    """
    Some lessons (lesson 3) have accordion sections that are purely a
    categorised bank of CLIENT questions — the xcard-sub literally says
    "N вопросов" ("N questions"), e.g. "A · О результатах и сроках / 7
    вопросов". Inside those, every <span class="en">/<span class="ru">
    pair is a client line (quoted), NOT a specialist phrase to translate.

    This must run BEFORE extract_phrase_cards, and on its output html:
    it both (a) returns the client questions found, tagged "client", and
    (b) masks those xcard bodies out of the html it returns, so the
    generic phrase-card extractor never re-captures the same lines as
    "term" (specialist-says) content.
    """
    out = []

    def repl(m):
        sub = m.group('sub')
        body = m.group('body')
        if not CLIENT_QUESTION_CATEGORY_RE.search(sub):
            return m.group(0)
        for sp in re.findall(r'<span class="en">(.*?)</span>', body, re.S):
            text = strip_tags(sp).strip().strip('"“”‘’\'').strip()
            if not text or not mostly_latin(text, 0.75):
                continue
            if len(text) < 15 or len(text) > 220:
                continue
            key = (lesson_num, 'q:' + text.lower())
            if key in seen:
                continue
            seen.add(key)
            out.append({"type": "client", "lesson": lesson_num, "lessonTitle": lesson_title, "en": text})
        return ''  # mask this xcard body out entirely

    pattern = re.compile(
        r'<span class="xcard-title">.*?</span><span class="xcard-sub">(?P<sub>.*?)</span>.*?'
        r'<div class="xcard-body">(?P<body>.*?)</div>\s*</details>',
        re.S,
    )
    masked_html = pattern.sub(repl, html)
    return out, masked_html


def extract_client_questions(html, lesson_title, lesson_num, seen):
    """
    Only pulls lines that are genuinely something a CLIENT would say to the
    specialist (a question, an objection, a challenge) — never the
    specialist's own first-person report/rescue-phrase lines. Two lessons
    (2 and 3) use the same <li> markup for the specialist's OWN monologue
    ("First, I fixed...", "I hear you. Let me share some context…") — that
    is reading practice, not something to react to, so it is excluded here
    even though it technically matches the <li> pattern.
    """
    out = []
    for xcard in re.findall(r'<div class="xcard-body">(.*?)</div>\s*</details>', html, re.S):
        candidates = []  # (text, must_be_question)
        li_items = re.findall(r'<li>(.*?)</li>', xcard, re.S)
        if li_items:
            # <li> follow-up lines are only trustworthy as client-voiced
            # prompts when they are actual questions (this is how lesson 10's
            # case follow-ups are written). Lessons 2/3 use the same markup
            # for the specialist's own monologue/rescue phrases, which never
            # reliably end in "?" — requiring "?" filters those out too.
            for li in li_items:
                candidates.append((strip_tags(li), True))
        else:
            # "client says" chips: take the LAST chips block in each xcard
            # body, but ONLY when there are at least two chip blocks
            # (specialist phrases, then client phrases) — that pairing is
            # how the role-play lessons (7/8) lay out their dialogue lines,
            # and don't always phrase them as questions ("Our competitor is
            # killing it and they just launched"), so these don't require a
            # "?". A single chips block (as in some lesson 3 cards) is the
            # SPECIALIST's own rescue-phrase starters, not a client line —
            # skip those rather than risk mislabeling them.
            chip_blocks = re.findall(r'<div class="chips">(.*?)</div>', xcard, re.S)
            if len(chip_blocks) >= 2:
                last_block = chip_blocks[-1]
                for sp in re.findall(r'<span>(.*?)</span>', last_block, re.S):
                    candidates.append((strip_tags(sp), False))
        for raw, must_be_question in candidates:
            text = raw.strip().strip('"“”‘’\'').strip()
            if must_be_question and not text.endswith('?'):
                continue
            if not mostly_latin(text, 0.75):
                continue
            if len(text) < 25 or len(text) > 220:
                continue
            if text.count(' ') < 3:
                continue
            if '  ' in text or '___' in text or '\xa0' in text:
                continue
            key = (lesson_num, 'q:' + text.lower())
            if key in seen:
                continue
            seen.add(key)
            out.append({"type": "client", "lesson": lesson_num, "lessonTitle": lesson_title, "en": text})
    return out


def lesson_title_of(html, fallback):
    m = re.search(r'<h1>(.*?)</h1>', html, re.S)
    if m:
        t = strip_tags(m.group(1))
        if t:
            return t
    m = re.search(r'<title>(.*?)</title>', html, re.S)
    if m:
        return strip_tags(m.group(1))
    return fallback


def main():
    repo_root = os.getcwd()
    all_terms = []
    all_clients = []
    lessons_meta = []
    for n in range(1, 16):
        path = os.path.join(repo_root, "lessons", str(n), "index.html")
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        title = lesson_title_of(html, f"Урок {n}")
        seen = set()
        client_from_categories, html = extract_and_mask_client_question_categories(html, title, n, seen)
        client_from_tags, html = extract_and_mask_tagged_client_lines(html, title, n, seen)
        terms = extract_phrase_cards(html, title, n, seen)
        terms += extract_tables(html, title, n, seen)
        clients = client_from_categories + client_from_tags + extract_client_questions(html, title, n, seen)
        all_terms.extend(terms)
        all_clients.extend(clients)
        lessons_meta.append({"num": n, "title": title, "termCount": len(terms), "clientCount": len(clients)})

    data = {
        "lessons": lessons_meta,
        "terms": all_terms,
        "clientQuestions": all_clients,
    }
    print(json.dumps(data, ensure_ascii=False))
    print(f"terms={len(all_terms)} clientQuestions={len(all_clients)}", file=sys.stderr)


if __name__ == "__main__":
    main()
