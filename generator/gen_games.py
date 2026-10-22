# -*- coding: utf-8 -*-
"""
Builds /games/index.html ("Игровая") — five drag-and-drop games.
All material is taken from the existing lessons via gen_glossary (glossary terms + phrasebook cards),
so nothing is invented here. Re-run after any change to lessons: python3 generator/gen_games.py
"""
import json
import os
import re

import gen_glossary as G          # (re)builds glossary/phrasebook as a side effect — output is identical
from build import page

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def term_re(term):
    term = re.sub(r"\s*\([^)]*\)", "", term).strip()          # "Core Web Vitals (CWV)" -> "Core Web Vitals"
    return re.compile(r'(?<![A-Za-z0-9])' + re.escape(term) + r'(?![A-Za-z0-9])', re.I)


def short_hint(t):
    if t["ru"] and len(t["ru"]) <= 90:
        return t["ru"]
    d = t["def_ru"]
    if not d:
        return ""
    first = re.split(r"(?<=[.!?])\s", d)[0]
    return first if len(first) <= 150 else first[:147].rstrip() + "…"


# ---- 1. gaps: example sentences with the term blanked out
gaps = []
for i, t in enumerate(G.glossary):
    ex = t["example"]
    rx = term_re(t["term"])
    m = rx.search(ex) if ex else None
    if not m or len(rx.findall(ex)) != 1:      # the term must occur exactly once, or the blank leaks the answer
        continue
    gaps.append(dict(id=f"g{i}", before=ex[:m.start()], after=ex[m.end():], answer=m.group(0),
                     hint=short_hint(t)))

# ---- 2. term -> short Russian translation
pairs = [dict(id=f"p{i}", term=t["term"], ru=t["ru"])
         for i, t in enumerate(G.glossary)
         if t["ru"] and len(t["ru"]) <= 45 and re.search(r"[А-Яа-яЁё]", t["ru"])]

# ---- 5. Russian definition -> term
defs = [dict(id=f"d{i}", term=t["term"], **{"def": t["def_ru"]})
        for i, t in enumerate(G.glossary) if t["def_ru"] and 20 <= len(t["def_ru"]) <= 170]


def ru_clean(s):
    return re.sub(r"^[—–-]\s*", "", s).strip()


# ---- 3. build-a-phrase: complete phrases of 3-9 words (no open "…" stems)
build, seen_en = [], set()
for lesson, cards in G.pb_by_lesson.items():
    for title, items in cards:
        for en, ru in items:
            en, ru = en.strip(), ru_clean(ru)
            n = len(en.split())
            if "…" in en or not (3 <= n <= 9) or en in seen_en or not ru:
                continue
            seen_en.add(en)
            build.append(dict(en=en, ru=ru))

# ---- 4. sort phrases into situations: per lesson, cards with >=3 unique phrases; lesson needs >=3 such cards
sort = {}
for lesson, cards in G.pb_by_lesson.items():
    count = {}
    for title, items in cards:
        for en, ru in items:
            count[en] = count.get(en, 0) + 1
    good = []
    for title, items in cards:
        ph = [dict(en=en, ru=ru_clean(ru)) for en, ru in items if count[en] == 1]
        if len(ph) >= 3:
            good.append(dict(title=title, phrases=ph))
    if len(good) >= 3:
        sort[str(lesson)] = good

data = dict(gaps=gaps, pairs=pairs, defs=defs, build=build, sort=sort)
print(f"games data: gaps={len(gaps)} pairs={len(pairs)} defs={len(defs)} build={len(build)} sort-lessons={len(sort)}")
assert len(gaps) >= 12 and len(pairs) >= 12 and len(defs) >= 10 and len(build) >= 20 and len(sort) >= 2

data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

tabs = [
    ("gap", "Вставь слово", "термин в предложение"),
    ("match", "Слово → перевод", "соедини пары"),
    ("build", "Собери фразу", "блоки по порядку"),
    ("sort", "Ситуации", "фразы по группам"),
    ("defs", "Определение → термин", "угадай по описанию"),
]
tabs_html = "".join(
    f'<button type="button" class="pr-tab" role="tab" data-mode="{k}"><b>{a}</b><span>{b}</span></button>'
    for k, a, b in tabs)

body = f'''<div class="wrap wide pr-wrap">
  <div class="pr-tabs" id="pr-tabs" role="tablist" aria-label="Выбор игры">{tabs_html}</div>
  <div class="pr-stage" id="pr-stage" aria-live="polite"></div>
</div>
<script type="application/json" id="pdata">{data_json}</script>
<script src="/assets/games.js" defer></script>'''

html = page(
    title="Игровая — Global English для SEO",
    desc="Пять игр на перетаскивание: вставь термин в предложение, соедини слово с переводом, собери фразу из блоков, разложи фразы по ситуациям, угадай термин по определению.",
    brand="Global English · Игровая",
    eyebrow="Доп. раздел курса «Global English для SEO»",
    h1="Игровая",
    lede="Пять игр на перетаскивание: терминов и фраз из ваших уроков — в предложения, к переводам и по ситуациям. Работает мышью и пальцем.",
    navlinks=[("/", "Главная"), ("/game/", "Спринт-тренажёр"), ("/glossary/", "Глоссарий")],
    body=body,
    prev_href="/", prev_label="← На главную",
    next_href="/game/", next_label="Спринт-тренажёр →",
)
html = html.replace(
    "</head>",
    '<link rel="stylesheet" href="/assets/games.css">\n<script src="/assets/ambient.js" defer></script>\n</head>', 1)

out = os.path.join(REPO, "games", "index.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote games/index.html", len(html), "bytes")
