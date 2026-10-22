# -*- coding: utf-8 -*-
import os
import json
from build import HEAD_FONTS, ROOT
from sitenav import site_head

lessons = [
  ("Просто о временах: как сказать о действии", "/lessons/1/",
   "Как объяснить клиенту, что уже сделано, что происходит сейчас и что будет дальше."),
  ("Защищаем отчёты и работу", "/lessons/2/",
   "Фразы, которыми специалист защищает отчёт и свою работу перед клиентом."),
  ("Защищаем работу в сложных ситуациях", "/lessons/3/",
   "Как остудить недовольного клиента и не потерять хватку в споре."),
  ("Explaining Charts & Rankings", "/lessons/4/",
   "Объясняем графики, позиции и рейтинги на понятном клиенту языке."),
  ("Real Conversations: ответы клиентам без подготовки", "/lessons/5/",
   "Быстрые ответы на неожиданные вопросы — без пауз и подготовки."),
  ("GEO & Semantic SEO термины", "/lessons/6/",
   "Термины GEO и Semantic SEO, которые звучат уверенно в разговоре."),
  ("Role Play: Real Client Scenarios", "/lessons/7/",
   "Живые ролевые сценарии: клиент задаёт вопрос — специалист отвечает."),
  ("Role Play: Reverse Roles", "/lessons/8/",
   "Те же сценарии, но с другой стороны стола — играем за клиента."),
  ("Все фразовые глаголы в контексте SEO", "/lessons/9/",
   "Фразовые глаголы, без которых не обходится ни один созвон с клиентом."),
  ("Кейсы с нейтивом", "/lessons/10/",
   "Реальные кейсы агентства глазами нейтива — разбор от и до."),
  ("Словарик: связки и термины 2026", "/lessons/11/",
   "Словарь связок и терминов 2026 года — под рукой в любой момент."),
  ("Semantic SEO + GEO практика", "/lessons/12/",
   "Практика Semantic SEO и GEO: от теории — к разговору с клиентом."),
  ("Rendering & Page Speed + Technical SEO", "/lessons/13/",
   "Rendering, Page Speed и техническая часть — простыми словами для клиента."),
  ("Допродажа во время звонка", "/lessons/14/",
   "Как предложить больше услуг прямо во время звонка, без нажима."),
  ("Сателлиты в SEO и их влияние на LLM", "/lessons/15/",
   "Сателлиты в SEO и их вес в эпоху LLM-поиска."),
  ("Письменный английский: follow-up, статусы и задержки", "/lessons/16/",
   "Как закрепить договорённости письменно: recap, ETA, задержки и «это вне объёма»."),
]

STATS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stats.json"), encoding="utf-8"))
N_TERMS, N_PHRASES = STATS["terms"], STATS["phrases"]

done = sum(1 for _, h, _ in lessons if h)

def col_item(i, title, href, dek):
    num = f"№{i+1:02d}"
    if href:
        return f'''<a class="col-item" href="{href}">
      <span class="col-num">{num} · Урок</span>
      <span class="col-title">{title}</span>
      <span class="col-dek">{dek}</span>
    </a>'''
    return f'''<div class="col-item locked">
      <span class="col-num">{num} · Скоро</span>
      <span class="col-title">{title}</span>
      <span class="col-dek">{dek}</span>
    </div>'''

columns_html = "\n    ".join(col_item(i, t, h, d) for i, (t, h, d) in enumerate(lessons))

gazette_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Global English для SEO — платформа уроков</title>
<meta name="description" content="Английский для SEO-команды: времена, отчёты клиентам, живые диалоги, GEO-термины, ролевые игры и разбор реальных ситуаций из практики агентства.">
{HEAD_FONTS}
<script src="/assets/ambient.js" defer></script>
</head>
<body>

{site_head("/gazette/")}

<header class="masthead">
  <div class="wrap">
    <div class="masthead-topline">
      <span>Внутреннее издание агентства</span>
      <span>Выпуск {len(lessons)} уроков</span>
    </div>
    <h1 class="masthead-name">The SEO&nbsp;English Gazette</h1>
    <p class="masthead-tagline">«Times New Roman» отдыхает — учимся объясняться с клиентом на живом английском</p>
    <div class="dateline">
      <span>Готово: {done} из {len(lessons)} уроков</span>
      <span class="fleuron">❧</span>
      <span>Времена · отчёты · живые диалоги · GEO · ролевые игры</span>
    </div>
  </div>
</header>

<section id="lessons">
  <div class="wrap">
    <div class="front-grid">
      <div class="lead-col">
        <a class="lead-story" href="/game/">
          <div class="lead-kicker">Главная новость номера</div>
          <h2>Спринт-тренажёр: вся команда — в эфире за 15 уроков</h2>
          <p>Командная игра на скорость: карточки на перевод и на реакцию на реплики клиента, отдельный таймер под каждый тип задания, живой счёт и составы команд — для группы от 5 до 10 человек.</p>
          <span class="byline">Готово · Открыть тренажёр →</span>
        </a>
      </div>
      <div class="side-col">
        <div class="side-note">В этом номере</div>
        <ul class="brief-list">
          <li><a href="#lessons">Все {len(lessons)} уроков программы<span class="brief-tag">Полное содержание ниже</span></a></li>
          <li><a href="#sections">Доп. разделы<span class="brief-tag">Глоссарий и разговорник</span></a></li>
          <li><a href="/game/">Спринт-тренажёр для группы<span class="brief-tag">Игра · таймер · счёт</span></a></li>
        </ul>
      </div>
    </div>

    <h2>Содержание номера</h2>
    <p class="section-kicker">шестнадцать уроков — жми на заголовок, чтобы открыть</p>
    <div class="column-rule">
    {columns_html}
    </div>
  </div>
</section>

<section id="sections">
  <div class="wrap">
    <h2>Доп. разделы</h2>
    <p class="section-kicker">глоссарий, разговорник и тренажёр — готовы</p>
    <div class="sections-grid">
      <a class="stub-card live" href="/glossary/">
        <div class="stub-title">Глоссарий <span class="stub-ready">Готово</span></div>
        <div class="stub-desc">Все SEO-термины на английском в одном месте — с транскрипцией.</div>
      </a>
      <a class="stub-card live" href="/phrasebook/">
        <div class="stub-title">Разговорник по фразам <span class="stub-ready">Готово</span></div>
        <div class="stub-desc">Сводная шпаргалка фраз-спасателей из всех уроков.</div>
      </a>
      <a class="stub-card live" href="/game/">
        <div class="stub-title">Спринт-тренажёр <span class="stub-ready">Готово</span></div>
        <div class="stub-desc">Командная игра на скорость: карточки на перевод и реакцию на реплики клиента по всем 15 урокам, таймер, счёт.</div>
      </a>
    </div>
    <div class="note">Есть идея, что должно быть в доп. разделах? Пишите — добавим.</div>
  </div>
</section>

<footer>
  <div class="wrap">Global English for SEO — платформа команды</div>
</footer>

</body>
</html>
'''


# ---------- gazette cover moves to /gazette/ (extra section) ----------
gazette_html = gazette_html.replace(
    "<title>Global English для SEO — платформа уроков</title>",
    "<title>The SEO English Gazette — Global English для SEO</title>", 1)
gazette_html = gazette_html.replace(
    '<a class="navlink" href="#lessons">Уроки</a>',
    '<a class="navlink" href="/">Главная</a>\n      <a class="navlink" href="#lessons">Уроки</a>', 1)
gazette_html = gazette_html.replace(
    '<div class="wrap">Global English for SEO — платформа команды</div>',
    '<div class="wrap"><a class="footer-back" href="/">← На главную</a></div>', 1)

# ---------- classic home ----------
def lesson_card(i, title, href, dek):
    return f'''<a class="hm-card" href="{href}">
        <span class="hm-num">Урок {i+1}</span>
        <span class="hm-card-title">{title}</span>
        <span class="hm-card-dek">{dek}</span>
      </a>'''

cards_html = "\n      ".join(lesson_card(i, t, h, d) for i, (t, h, d) in enumerate(lessons))

extras = [
  ("/glossary/", "Глоссарий", f"{N_TERMS} SEO-терминов на английском: транскрипция, перевод, определение, пример. Поиск, темы и фильтр по буквам."),
  ("/phrasebook/", "Разговорник", f"Шпаргалка фраз-спасателей из всех уроков: {N_PHRASES} фраз, поиск и быстрый переход к уроку."),
  ("/games/", "Игровая", "Пять игр на перетаскивание: вставь термин в предложение, соедини слово с переводом, собери фразу из блоков, разложи фразы по ситуациям."),
  ("/game/", "Спринт-тренажёр", "Командная игра на скорость по урокам 1–15: карточки, таймер и счёт для группы от 5 до 10 человек."),
  ("/gazette/", "Газета курса", "Прежняя обложка в стиле газеты — «The SEO English Gazette»."),
]
extras_html = "\n      ".join(
    f'''<a class="hm-card hm-extra" href="{h}">
        <span class="hm-card-title">{t}</span>
        <span class="hm-card-dek">{d}</span>
      </a>''' for h, t, d in extras)

home_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Global English для SEO — уроки английского для SEO-команды</title>
<meta name="description" content="Английский для SEO-команды: {len(lessons)} уроков, глоссарий, разговорник и спринт-тренажёр. Времена, отчёты клиентам, живые диалоги, GEO и Semantic SEO, ролевые игры.">
{HEAD_FONTS}
<script src="/assets/ambient.js" defer></script>
</head>
<body class="home">

{site_head("/")}

<main>
  <div class="wrap wide hm-hero">
    <p class="hm-eyebrow">Английский для SEO-команды</p>
    <h1 class="hm-title">Global English для SEO</h1>
    <p class="hm-lede">Как объяснить клиенту позиции, отчёты и задержки на живом английском — без пауз и заученных фраз. {len(lessons)} практических уроков, глоссарий, разговорник и командный тренажёр.</p>
    <div class="hm-actions">
      <a class="hm-btn" href="/lessons/1/">Начать с урока 1</a>
      <a class="hm-btn ghost" href="/game/">Спринт-тренажёр</a>
    </div>
    <dl class="hm-stats">
      <div><dt>{len(lessons)}</dt><dd>уроков</dd></div>
      <div><dt>{N_TERMS}</dt><dd>терминов в глоссарии</dd></div>
      <div><dt>{N_PHRASES}</dt><dd>фраз в разговорнике</dd></div>
      <div><dt>1</dt><dd>командный тренажёр</dd></div>
    </dl>
  </div>

  <div class="wrap wide hm-block" id="lessons">
    <h2 class="hm-h2">Все уроки</h2>
    <p class="hm-sub">Можно идти по порядку или открыть нужную тему.</p>
    <div class="hm-grid">
      {cards_html}
    </div>
  </div>

  <div class="wrap wide hm-block" id="sections">
    <h2 class="hm-h2">Дополнительные разделы</h2>
    <p class="hm-sub">Справочники и практика к урокам.</p>
    <div class="hm-grid hm-grid-extra">
      {extras_html}
    </div>
  </div>
</main>

<footer class="hm-footer">
  <div class="wrap wide">Global English для SEO — платформа команды</div>
</footer>

</body>
</html>
'''

_repo = os.path.dirname(ROOT)
def write_root(path, content):
    full = os.path.join(_repo, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")

write_root("index.html", home_html)
write_root("gazette/index.html", gazette_html)
