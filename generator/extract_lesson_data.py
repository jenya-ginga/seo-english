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


def extract_client_questions(html, lesson_title, lesson_num, seen):
    out = []
    for xcard in re.findall(r'<div class="xcard-body">(.*?)</div>\s*</details>', html, re.S):
        candidates = []
        li_items = re.findall(r'<li>(.*?)</li>', xcard, re.S)
        for li in li_items:
            candidates.append(strip_tags(li))
        # "client says" chips: take the LAST chips block in each xcard body when
        # there are two (specialist chips, then client chips) — client-facing
        # lines are what a specialist must react to out loud. Only used when
        # there were no <li> follow-up questions in this card (role-play
        # lessons use chips instead of <li> for their dialogue lines).
        if not li_items:
            chip_blocks = re.findall(r'<div class="chips">(.*?)</div>', xcard, re.S)
            if chip_blocks:
                last_block = chip_blocks[-1]
                for sp in re.findall(r'<span>(.*?)</span>', last_block, re.S):
                    candidates.append(strip_tags(sp))
        for raw in candidates:
            text = raw.strip().strip('"“”‘’\'').strip()
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
        terms = extract_phrase_cards(html, title, n, seen)
        terms += extract_tables(html, title, n, seen)
        clients = extract_client_questions(html, title, n, seen)
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
