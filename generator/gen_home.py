# -*- coding: utf-8 -*-
import os
from build import HEAD_FONTS, write

lessons = [
  ("Просто о временах: как сказать о действии", "/lessons/1/"),
  ("Защищаем отчёты и работу", "/lessons/2/"),
  ("Защищаем работу в сложных ситуациях", "/lessons/3/"),
  ("Explaining Charts & Rankings", "/lessons/4/"),
  ("Real Conversations: ответы клиентам без подготовки", "/lessons/5/"),
  ("GEO & Semantic SEO термины", "/lessons/6/"),
  ("Role Play: Real Client Scenarios", "/lessons/7/"),
  ("Role Play: Reverse Roles", "/lessons/8/"),
  ("Все фразовые глаголы в контексте SEO", "/lessons/9/"),
  ("Кейсы с нейтивом", "/lessons/10/"),
  ("Словарик: связки и термины 2026", "/lessons/11/"),
  ("Semantic SEO + GEO практика", "/lessons/12/"),
  ("Rendering & Page Speed + Technical SEO", "/lessons/13/"),
  ("Допродажа во время звонка", "/lessons/14/"),
  ("Сателлиты в SEO и их влияние на LLM", "/lessons/15/"),
]

lessons_js = ",\n  ".join(
    '{ title: %r, href: %r }' % (t, h) if h else '{ title: %r }' % (t,)
    for t, h in lessons
)
done = sum(1 for _, h in lessons if h)

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

<header class="hero">
  <div class="wrap">
    <div class="eyebrow">Внутренняя платформа команды</div>
    <h1>Английский для SEO-специалиста</h1>
    <p class="lede">Времена, отчёты клиентам, живые диалоги, GEO-термины, ролевые игры и разбор реальных ситуаций из практики агентства — в одном месте.</p>
    <p class="progress-note">Готово: <strong>{done} из {len(lessons)}</strong> уроков. Остальные наполняем постепенно.</p>
  </div>
</header>

<section id="lessons">
  <div class="wrap">
    <h2>Уроки</h2>
    <p class="section-kicker">жми на карточку, чтобы открыть урок</p>
    <div class="lessons-grid" id="lessonsGrid"></div>
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
      <div class="stub-card">
        <div class="stub-title">Тренажёр</div>
        <div class="stub-desc">Быстрые упражнения на времена и лексику для повторения.</div>
      </div>
    </div>
    <div class="note">Есть идея, что должно быть в доп. разделах? Пишите — добавим.</div>
  </div>
</section>

<footer>
  <div class="wrap">Global English for SEO — платформа команды</div>
</footer>

<script>
const lessons = [
  {lessons_js}
];

const grid = document.getElementById('lessonsGrid');
lessons.forEach((lesson, i) => {{
  const num = (i + 1 < 10 ? '0' : '') + (i + 1);
  const available = !!lesson.href;
  const tag = available ? 'a' : 'div';
  const el = document.createElement(tag);
  el.className = 'lesson-card' + (available ? '' : ' locked');
  if (available) el.href = lesson.href;
  el.innerHTML = `
    <span class="lesson-num">${{num}}</span>
    <div class="lesson-title">${{lesson.title}}</div>
    <span class="lesson-status"><span class="led"></span>${{available ? 'Открыт' : 'Скоро'}}</span>`;
  grid.appendChild(el);
}});
</script>

</body>
</html>
'''
write("index.html", html)
