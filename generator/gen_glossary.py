# -*- coding: utf-8 -*-
"""
Builds two summary pages from the already-built lessons/N/index.html files:
  /glossary/index.html    — all English SEO terms with transcription, translation and source lesson
  /phrasebook/index.html  — all phrase cards ("фразы-спасатели") grouped by lesson

Run from anywhere:  python3 generator/gen_glossary.py
Re-run after any change to lessons/*/index.html.
"""
import html as htmlmod
import os
import re

from build import page
import ipa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON_COUNT = 16


def read_lesson(n):
    with open(os.path.join(REPO, "lessons", str(n), "index.html"), encoding="utf-8") as f:
        return f.read()


def strip(s):
    return htmlmod.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("'", "&rsquo;"))


def norm_term(t):
    t = strip(t).replace("★", "").strip()
    return re.sub(r"\s+", " ", t)


def clean_example(s):
    s = strip(s)
    s = s.strip("«»\"“”")
    return s.strip()


def rows_of(table_html):
    rows = re.findall(r"<tr>(.*?)</tr>", table_html, re.S)
    out = []
    for r in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if cells:
            out.append(cells)
    return out


def headers_of(table_html):
    return [strip(h) for h in re.findall(r"<th[^>]*>(.*?)</th>", table_html, re.S)]


def lesson_title(html_text):
    m = re.search(r"<h1>(.*?)</h1>", html_text, re.S)
    return strip(m.group(1)) if m else ""


# ------------------------------------------------------------------ glossary extraction
def span_texts(cell):
    en = re.search(r'<span class="en">(.*?)</span>', cell, re.S)
    ru = re.search(r'<span class="ru-sub">(.*?)</span>', cell, re.S)
    return (strip(en.group(1)) if en else None, strip(ru.group(1)) if ru else None)


def extract_terms(n, html_text):
    """Returns list of dicts: term, pron, ru, def_en, def_ru, example, star, lesson"""
    out = []
    for tb in re.findall(r"<table.*?</table>", html_text, re.S):
        hs = headers_of(tb)
        rows = rows_of(tb)
        if hs[:1] == ["Термин"] and len(hs) == 3 and hs[1] == "Перевод":
            # lesson 11: "Term (транскрипция)" | перевод | определение
            for c in rows:
                raw = strip(c[0])
                star = raw.startswith("★")
                raw = raw.replace("★", "").strip()
                m = re.match(r"^(.*?)\s*\(([^()]*[А-Яа-яЁё][^()]*)\)\s*$", raw)
                term, pron = (m.group(1).strip(), m.group(2).strip()) if m else (raw, "")
                out.append(dict(term=term, pron=pron, ru=strip(c[1]), def_en="", def_ru=strip(c[2]),
                                example="", star=star, lesson=n))
        elif hs[:2] == ["Термин", "Произношение"] and len(hs) == 4:
            # lesson 12: term + ru-sub | pron | def en + ru-sub | example
            for c in rows:
                star = "★" in strip(c[0])
                _, ru_term = span_texts(c[0])
                term = norm_term(re.sub(r'<span class="ru-sub">.*?</span>', "", c[0], flags=re.S))
                d_en, d_ru = span_texts(c[2])
                if d_en is None:
                    d_en = strip(c[2])
                out.append(dict(term=term, pron=strip(c[1]), ru=ru_term or "", def_en=d_en or "",
                                def_ru=d_ru or "", example=clean_example(c[3]), star=star, lesson=n))
        elif hs[:2] == ["Term", "Произношение"] and len(hs) == 5:
            # lessons 13, 14: term | pron | def EN | перевод RU | example
            for c in rows:
                out.append(dict(term=norm_term(c[0]), pron=strip(c[1]), ru="", def_en=strip(c[2]),
                                def_ru=strip(c[3]), example=clean_example(c[4]),
                                star="★" in strip(c[0]), lesson=n))
        elif hs[:2] == ["Term", "Произношение"] and len(hs) == 4:
            # lessons 15, 16: term | pron | def (en + ru-sub) | example
            for c in rows:
                d_en, d_ru = span_texts(c[2])
                if d_en is None:
                    d_en = strip(c[2])
                out.append(dict(term=norm_term(c[0]), pron=strip(c[1]), ru="", def_en=d_en or "",
                                def_ru=d_ru or "", example=clean_example(c[3]),
                                star="★" in strip(c[0]), lesson=n))
    return out


lessons_html = {n: read_lesson(n) for n in range(1, LESSON_COUNT + 1)}
titles = {n: lesson_title(h) for n, h in lessons_html.items()}

all_terms = []
for n in range(1, LESSON_COUNT + 1):
    all_terms.extend(extract_terms(n, lessons_html[n]))

# merge duplicates (same term in several lessons)
merged = {}
for t in all_terms:
    key = re.sub(r"[^a-z0-9а-яё]+", " ", t["term"].lower()).strip()
    if key not in merged:
        merged[key] = dict(t, lessons=[t["lesson"]])
        continue
    m = merged[key]
    if t["lesson"] not in m["lessons"]:
        m["lessons"].append(t["lesson"])
    for f in ("pron", "ru", "def_en", "def_ru", "example"):
        if not m[f] and t[f]:
            m[f] = t[f]
    m["star"] = m["star"] or t["star"]

glossary = sorted(merged.values(), key=lambda x: x["term"].lower())
for _t in glossary:
    _t.setdefault("category", "Из уроков")

# ---- extra terms from generator/terms/*.txt  (term | перевод | definition | example), "## Category" headers
def _key(term):
    return re.sub(r"[^a-z0-9а-яё]+", " ", re.sub(r"\([^)]*\)", "", term).lower()).strip()


def load_extra_terms():
    out, cat = [], ""
    tdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "terms")
    for fn in sorted(os.listdir(tdir)):
        if not fn.endswith(".txt"):
            continue
        with open(os.path.join(tdir, fn), encoding="utf-8") as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                if line.startswith("##"):
                    cat = line.lstrip("#").strip()
                    continue
                parts = [x.strip() for x in line.split(" | ")]
                assert len(parts) == 4, (fn, ln, line)
                term, ru, d_en, ex = parts
                out.append(dict(term=term, pron="", ru=ru, def_en=d_en, def_ru="", example=ex,
                                star=False, lessons=[], category=cat))
    return out


_seen = {_key(t["term"]) for t in glossary}
_extra, _dups = [], []
for _t in load_extra_terms():
    k = _key(_t["term"])
    if k in _seen:
        _dups.append(_t["term"]); continue
    _seen.add(k); _extra.append(_t)
if _dups:
    print("extra terms skipped as duplicates:", _dups)
glossary = sorted(glossary + _extra, key=lambda x: x["term"].lower())
CATEGORIES = ["Из уроков"] + [c for c in dict.fromkeys(t["category"] for t in _extra)]


def lesson_links(ls):
    return " ".join(f'<a class="gl-lesson" href="/lessons/{n}/">№{n:02d}</a>' for n in sorted(ls))


PRON_MISSING = {}


def gl_row(t):
    """One glossary card (grid layout)."""
    star = t["star"]
    ip, missing = ipa.term_ipa(t["term"])
    cyr, missing2 = ipa.term_cyr(t["term"])
    for w in set(missing) | set(missing2):
        PRON_MISSING.setdefault(w, t["term"])
    parts = []
    if t["ru"] and t["ru"].strip().lower() != t["term"].strip().lower():
        parts.append(f'<p class="gl-ru">{esc(t["ru"])}</p>')
    if t["def_en"]:
        parts.append(f'<p class="gl-def">{esc(t["def_en"])}</p>')
    if t["def_ru"]:
        parts.append(f'<p class="gl-def-ru">{esc(t["def_ru"])}</p>')
    if t["example"]:
        parts.append(f'<p class="gl-ex">&ldquo;{esc(t["example"])}&rdquo;</p>')
    first = t["term"][:1].upper()
    return (f'<article class="gl-card{" is-star" if star else ""}" data-letter="{esc(first)}" data-cat="{esc(t["category"])}">'
            f'<h3 class="gl-term">{"★ " if star else ""}{esc(t["term"])}</h3>'
            f'<div class="gl-pron" title="IPA (US): {esc(ip)}">{esc(cyr)}</div>'
            f'{"".join(parts)}'
            f'<div class="gl-meta">{lesson_links(t["lessons"]) if t["lessons"] else ""}<span class="gl-cat">{esc(t["category"])}</span></div></article>')


SEARCH_CSS = '''<style>
.gl-search{width:100%;max-width:520px;font:inherit;font-size:16px;padding:12px 14px;border:1px solid var(--ink-soft);border-radius:var(--radius-sm);background:var(--paper);color:var(--ink);margin:6px 0 10px;}
.gl-count{font-size:13px;color:var(--ink-faint);margin:0 0 16px;}
.gl-lesson{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:600;border:1px solid var(--ink-soft);border-radius:2px;padding:2px 6px;margin:1px 2px;text-decoration:none;color:var(--ink);}
.gl-lesson:hover{background:var(--ink);color:var(--paper);}
.gl-empty{display:none;margin-top:16px;}
.gl-letters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px;}
.gl-letters button{font-family:var(--mono);font-size:12px;font-weight:600;border:1px solid var(--ink-soft);border-radius:2px;background:var(--paper);color:var(--ink);padding:4px 9px;cursor:pointer;}
.gl-letters button.on{background:var(--ink);color:var(--paper);}
.pb-jump{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 20px;}
.gl-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;}
@media (max-width:760px){.gl-grid{grid-template-columns:1fr;}}
.gl-card{display:flex;flex-direction:column;gap:7px;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:18px 20px;}
.gl-card.is-star{border-color:var(--accent);}
.gl-term{font-family:var(--serif);font-weight:700;font-size:20px;line-height:1.25;margin:0;color:var(--ink);}
.gl-pron{font-family:var(--sans);font-size:14.5px;color:var(--accent-ink);letter-spacing:.01em;cursor:help;}
.gl-ru{margin:2px 0 0;font-family:var(--sans);font-weight:600;font-size:15px;color:var(--ink);}
.gl-def{margin:0;font-family:var(--serif);font-style:italic;font-size:15px;line-height:1.5;color:var(--ink);}
.gl-def-ru{margin:0;font-family:var(--sans);font-size:13px;line-height:1.5;color:var(--ink-soft);}
.gl-ex{margin:2px 0 0;padding-left:12px;border-left:2px solid var(--line);font-family:var(--serif);font-style:italic;font-size:14px;line-height:1.5;color:var(--ink-soft);}
.gl-meta{margin-top:auto;padding-top:6px;display:flex;flex-wrap:wrap;gap:4px;align-items:center;}
.gl-cat{font-family:var(--sans);font-size:11.5px;color:var(--ink-faint);margin-left:2px;}
.gl-cats{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px;}
.gl-cats button{font-family:var(--sans);font-size:12.5px;border:1px solid var(--rule);border-radius:999px;background:var(--paper);color:var(--ink-soft);padding:5px 12px;cursor:pointer;}
.gl-cats button.on{background:var(--accent);border-color:var(--accent);color:var(--bg);}
</style>'''

cat_buttons = '<button type="button" class="on" data-c="">Все темы</button>' + "".join(
    f'<button type="button" data-c="{esc(c)}">{esc(c)}</button>' for c in CATEGORIES)
letters = sorted({t["term"][:1].upper() for t in glossary if t["term"][:1].isalpha()})
letter_buttons = '<button type="button" class="on" data-l="">Все</button>' + "".join(
    f'<button type="button" data-l="{l}">{l}</button>' for l in letters)

gl_cards = [gl_row(t) for t in glossary]
assert not PRON_MISSING, PRON_MISSING
gl_table = f'<div class="gl-grid" id="gl-grid">{"".join(gl_cards)}</div>'

GL_JS = '''<script>
(function(){
  var q=document.getElementById('gl-q'), rows=[].slice.call(document.querySelectorAll('#gl-grid .gl-card')),
      cnt=document.getElementById('gl-count'), empty=document.getElementById('gl-empty'),
      btns=[].slice.call(document.querySelectorAll('.gl-letters button')), letter='',
      cbtns=[].slice.call(document.querySelectorAll('#gl-cats button')), cat='';
  function apply(){
    var s=q.value.trim().toLowerCase(), shown=0;
    rows.forEach(function(r){
      var ok=(!letter||r.getAttribute('data-letter')===letter)&&(!cat||r.getAttribute('data-cat')===cat)&&(!s||r.textContent.toLowerCase().indexOf(s)>-1);
      r.style.display=ok?'':'none'; if(ok) shown++;
    });
    cnt.textContent='Показано: '+shown+' из '+rows.length;
    empty.style.display=shown?'none':'block';
  }
  q.addEventListener('input',apply);
  btns.forEach(function(b){b.addEventListener('click',function(){
    letter=b.getAttribute('data-l'); btns.forEach(function(x){x.classList.toggle('on',x===b);}); apply();
  });});
  cbtns.forEach(function(b){b.addEventListener('click',function(){
    cat=b.getAttribute('data-c'); cbtns.forEach(function(x){x.classList.toggle('on',x===b);}); apply();
  });});
  apply();
})();
</script>'''

gl_body = f'''{SEARCH_CSS}
<section id="terms">
  <div class="wrap wide">
    <h2>Все термины · A–Z</h2>
    <p class="section-kicker">{len(glossary)} терминов: {sum(1 for t in glossary if t["lessons"])} из уроков и {sum(1 for t in glossary if not t["lessons"])} из практики SEO — с транскрипцией, переводом и примером</p>
    <input id="gl-q" class="gl-search" type="search" placeholder="Поиск: термин, перевод, пример…" autocomplete="off">
    <div class="gl-cats" id="gl-cats">{cat_buttons}</div>
    <div class="gl-letters">{letter_buttons}</div>
    <p id="gl-count" class="gl-count"></p>
    {gl_table}
    <div id="gl-empty" class="note gl-empty">Ничего не найдено. Попробуйте другое слово или сбросьте букву.</div>
    <p class="note">★ — самые важные для клиентских звонков. Транскрипция русскими буквами приблизительная (американский вариант), точная IPA — во всплывающей подсказке при наведении. Аббревиатуры читаются по буквам. Номер урока ведёт на страницу, где термин разобран; у остальных терминов указана тема.</p>
  </div>
</section>
{GL_JS}'''

gl_html = page(
    title="Глоссарий — Global English для SEO",
    desc="Все SEO-термины на английском в одном месте: транскрипция, перевод, определение, пример и ссылка на урок.",
    brand="Global English · Глоссарий",
    eyebrow="Доп. раздел курса «Global English для SEO»",
    h1="Глоссарий",
    lede="Все SEO-термины на английском — из уроков и из повседневной практики — в одном месте — с транскрипцией, переводом, определением и примером фразы. Ищите по слову или выбирайте букву.",
    navlinks=[("#terms", "Термины"), ("/phrasebook/", "Разговорник")],
    body=gl_body,
    prev_href="/", prev_label="← Все уроки",
    next_href="/phrasebook/", next_label="Разговорник →",
)

# ------------------------------------------------------------------ phrasebook extraction
CARD_RE = re.compile(r'<div class="phrase-card"><h4>(.*?)</h4>\s*<(ul|ol)[^>]*>(.*?)</\2></div>', re.S)
ITEM_RE = re.compile(r'<li><span class="en">(.*?)</span>\s*<span class="ru">(.*?)</span></li>', re.S)

pb_by_lesson = {}
total_cards_in_html = 0
for n in range(1, LESSON_COUNT + 1):
    h = lessons_html[n]
    total_cards_in_html += h.count('class="phrase-card"')
    cards = []
    for title, _tag, body in CARD_RE.findall(h):
        items = ITEM_RE.findall(body)
        if not items:  # English-only list (e.g. typical client questions in lesson 6)
            items = [(t, "") for t in re.findall(r"<li>(.*?)</li>", body, re.S)]
        if items:
            cards.append((title, items))
    if cards:
        pb_by_lesson[n] = cards

parsed_cards = sum(len(c) for c in pb_by_lesson.values())
assert parsed_cards == total_cards_in_html, (parsed_cards, total_cards_in_html)


def pb_card(title, items):
    lis = "".join(
        f'<li><span class="en">{en}</span>' + (f'<span class="ru">{ru}</span>' if ru else "") + "</li>"
        for en, ru in items)
    return f'<div class="phrase-card"><h4>{title}</h4><ul class="phrase-list">{lis}</ul></div>'


pb_sections = []
jump = []
total_phrases = 0
for n, cards in pb_by_lesson.items():
    total_phrases += sum(len(i) for _, i in cards)
    jump.append(f'<a class="gl-lesson" href="#l{n}">№{n:02d}</a>')
    pb_sections.append(
        f'<section id="l{n}" class="pb-lesson">\n  <div class="wrap">\n'
        f'    <h2>Урок {n} · {esc(titles[n])}</h2>\n'
        f'    <p class="section-kicker"><a href="/lessons/{n}/">открыть урок →</a></p>\n'
        f'    <div class="phrase-grid">{"".join(pb_card(t, i) for t, i in cards)}</div>\n'
        f'  </div>\n</section>'
    )

PB_JS = '''<script>
(function(){
  var q=document.getElementById('pb-q'), cnt=document.getElementById('pb-count'), empty=document.getElementById('pb-empty'),
      secs=[].slice.call(document.querySelectorAll('.pb-lesson'));
  var total=document.querySelectorAll('.pb-lesson .phrase-list li').length;
  function apply(){
    var s=q.value.trim().toLowerCase(), shown=0;
    secs.forEach(function(sec){
      var secShown=0;
      [].slice.call(sec.querySelectorAll('.phrase-card')).forEach(function(card){
        var any=0;
        [].slice.call(card.querySelectorAll('li')).forEach(function(li){
          var ok=!s||li.textContent.toLowerCase().indexOf(s)>-1||card.querySelector('h4').textContent.toLowerCase().indexOf(s)>-1;
          li.style.display=ok?'':'none'; if(ok){any++;}
        });
        card.style.display=any?'':'none'; secShown+=any;
      });
      sec.style.display=secShown?'':'none'; shown+=secShown;
    });
    cnt.textContent='Показано фраз: '+shown+' из '+total;
    empty.style.display=shown?'none':'block';
  }
  q.addEventListener('input',apply); apply();
})();
</script>'''

pb_body = f'''{SEARCH_CSS}
<section id="search">
  <div class="wrap">
    <h2>Поиск по фразам</h2>
    <p class="section-kicker">{total_phrases} фраз из {len(pb_by_lesson)} уроков — ищите на английском или по-русски</p>
    <input id="pb-q" class="gl-search" type="search" placeholder="Например: delay, ETA, понимаю, budget…" autocomplete="off">
    <p id="pb-count" class="gl-count"></p>
    <div class="pb-jump">{"".join(jump)}</div>
    <div id="pb-empty" class="note gl-empty">Ничего не найдено. Попробуйте другое слово.</div>
  </div>
</section>
{"".join(pb_sections)}
{PB_JS}'''

pb_html = page(
    title="Разговорник по фразам — Global English для SEO",
    desc="Сводная шпаргалка фраз-спасателей из всех уроков: английская фраза и перевод, сгруппированы по урокам, с поиском.",
    brand="Global English · Разговорник",
    eyebrow="Доп. раздел курса «Global English для SEO»",
    h1="Разговорник по фразам",
    lede="Сводная шпаргалка фраз-спасателей из всех уроков: что сказать клиенту, когда нужно ответить сразу. Фразы сгруппированы по урокам, внутри работает поиск.",
    navlinks=[("#search", "Поиск"), ("/glossary/", "Глоссарий")],
    body=pb_body,
    prev_href="/glossary/", prev_label="← Глоссарий",
    next_href="/", next_label="Все уроки →",
)


def write_root(rel, content):
    full = os.path.join(REPO, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel, len(content), "bytes")


# music plays everywhere except the lessons
gl_html = gl_html.replace("</head>", '<script src="/assets/ambient.js" defer></script>\n</head>', 1)
import json as _json
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stats.json"), "w", encoding="utf-8") as _f:
    _json.dump({"terms": len(glossary), "phrases": total_phrases}, _f)
write_root("glossary/index.html", gl_html)
pb_html = pb_html.replace("</head>", '<script src="/assets/ambient.js" defer></script>\n</head>', 1)
write_root("phrasebook/index.html", pb_html)
print("glossary terms:", len(glossary), "| raw rows:", len(all_terms))
print("phrasebook:", parsed_cards, "cards,", total_phrases, "phrases,", len(pb_by_lesson), "lessons")
