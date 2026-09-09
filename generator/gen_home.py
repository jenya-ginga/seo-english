# -*- coding: utf-8 -*-
import os
from build import HEAD_FONTS, write

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
]

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

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Global English для SEO — платформа уроков</title>
<meta name="description" content="Английский для SEO-команды: времена, отчёты клиентам, живые диалоги, GEO-термины, ролевые игры и разбор реальных ситуаций из практики агентства.">
{HEAD_FONTS}
</head>
<body>

<nav class="topnav">
  <div class="wrap">
    <a href="/" class="brand"><span class="dot"></span>Global English для SEO</a>
    <div class="navlinks">
      <a class="navlink" href="#lessons">Уроки</a>
      <a class="navlink" href="#sections">Доп. разделы</a>
    </div>
  </div>
</nav>

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
    <p class="section-kicker">пятнадцать уроков — жми на заголовок, чтобы открыть</p>
    <div class="column-rule">
    {columns_html}
    </div>
  </div>
</section>

<section id="sections">
  <div class="wrap">
    <h2>Доп. разделы</h2>
    <p class="section-kicker">наполним позже</p>
    <div class="sections-grid">
      <div class="stub-card">
        <div class="stub-title">Глоссарий</div>
        <div class="stub-desc">Все SEO-термины на английском в одном месте — с транскрипцией.</div>
      </div>
      <div class="stub-card">
        <div class="stub-title">Разговорник по фразам</div>
        <div class="stub-desc">Сводная шпаргалка фраз-спасателей из всех уроков.</div>
      </div>
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
write("index.html", html)
