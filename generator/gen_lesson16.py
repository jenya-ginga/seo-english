# -*- coding: utf-8 -*-
from build import page, section, info_card, phrase_card, phrase_grid, compare_card, accordion, table_scroll, write


def e(s):
    """Plain text -> HTML: escape &,<,> and turn apostrophes into typographic ones."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("'", "&rsquo;")


def q(s):
    """English quote in typographic double quotes."""
    return "&ldquo;" + e(s) + "&rdquo;"


def defcell(en, ru):
    return (f'<span style="display:block; font-family:var(--serif-body); font-style:normal; font-weight:600; font-size:15.5px; line-height:1.55; color:var(--ink);">{e(en)}</span>'
            f'<span class="ru-sub" style="font-size:12.5px; margin-top:6px;">{e(ru)}</span>')


# ---------------------------------------------------------------- PART 1 (vocabulary)
TERMS = [
  ("Follow-up", "фоллоу-ап",
   "A message sent after a call to confirm what was discussed.",
   "Сообщение после звонка, фиксирующее обсуждённое.",
   "I'll send a follow-up right after the call.", True),
  ("Recap", "рикэп",
   "A short summary of what was agreed.",
   "Краткое резюме договорённостей.",
   "Here's a quick recap of today's call.", True),
  ("Action item", "экшн айтем",
   "A specific task with an owner and, usually, a deadline.",
   "Конкретная задача с ответственным и сроком.",
   "Action item: GSC access (you), audit draft (us).", True),
  ("Go live", "гоу лайв",
   "To become available on the site after a release.",
   "Выйти на сайте после релиза.",
   "The redirects went live on Tuesday.", False),
  ("ETA", "и-ти-эй",
   "Estimated date when something will be ready.",
   "Ожидаемая дата готовности.",
   "The ETA for the draft is Friday.", True),
  ("Blocker", "блокер",
   "Something that stops the work from moving forward.",
   "Препятствие, из-за которого работа стоит.",
   "The only blocker is CMS access.", True),
  ("Implementation", "имплементэйшн",
   "Putting a recommendation into practice on the site.",
   "Внедрение рекомендации на сайте.",
   "Implementation is on your developer's side.", False),
  ("Heads-up", "хэдз-ап",
   "An early warning about a possible problem.",
   "Предупреждение заранее.",
   "Just a heads-up: the release may slip.", True),
  ("Slip / move to", "слип / мув ту",
   "To happen later than planned.",
   "Сдвигаться по срокам.",
   "The deadline slipped by two days.", False),
  ("Out of scope", "аут оф скоуп",
   "Not included in the agreed work.",
   "Вне согласованного объёма.",
   "Development work is out of scope.", False),
  ("Sign-off", "сайн-офф",
   "Formal approval before the next stage.",
   "Финальное согласование.",
   "We need your sign-off before publishing.", False),
  ("Loop in", "луп ин",
   "To add a person to the conversation.",
   "Подключить человека к переписке.",
   "I'll loop in our developer.", True),
]

rows_html = ""
for term, pron, en_def, ru_def, ex, priority in TERMS:
    star = "★ " if priority else ""
    cls = ' class="strong-cell"' if priority else ""
    rows_html += (
        f'<tr><td{cls}>{star}{e(term)}</td><td>{e(pron)}</td>'
        f'<td>{defcell(en_def, ru_def)}</td>'
        f'<td style="font-family:var(--serif-body); font-style:normal; font-size:15px; line-height:1.55; color:var(--ink-soft);">{q(ex)}</td></tr>'
    )

terms_table = (
    '<div class="table-scroll"><table><thead><tr>'
    '<th>Term</th><th>Произношение</th><th>Definition (EN) / Перевод (RU)</th><th>Example</th>'
    f'</tr></thead><tbody>{rows_html}</tbody></table></div>'
)

sec_terms = section(
    "terms", "Часть 1 · Written Follow-up Vocabulary",
    "словарь: 12 терминов, приоритетные — под ★ (10 мин)",
    terms_table + '\n<p class="note">★ = самые важные для писем и сообщений клиенту</p>',
)


# ---------------------------------------------------------------- PART 2 (key phrases)
def pc(title, pairs):
    return phrase_card(title, [(q(en), ru_) for en, ru_ in pairs])

cards = [
  pc("A. Начало и recap", [
    ("Thanks for your time today. Here's a quick recap of what we agreed.",
     "Спасибо за уделённое время. Вот краткое резюме наших договорённостей."),
    ("Following up on our call, I'm summarizing the key points below.",
     "По итогам звонка резюмирую ключевые пункты ниже."),
    ("Please let me know if anything is missing or unclear.",
     "Дайте знать, если что-то упущено или неясно."),
  ]),
  pc("B. Задачи и сроки", [
    ("We'll send the audit draft by Friday. Could you share GSC access by Wednesday?",
     "Мы пришлём черновик аудита к пятнице. Не могли бы вы дать доступ к GSC до среды?"),
    ("Could your developer implement the redirect fixes by next Wednesday?",
     "Мог бы ваш разработчик внедрить исправления редиректов до следующей среды?"),
    ("Once we have access, we can start right away.",
     "Как только получим доступ, сразу начнём."),
  ]),
  pc("C. Задержка и сроки эффекта", [
    ("Quick heads-up: we're running a little behind on the audit.",
     "Небольшое предупреждение: мы немного отстаём по аудиту."),
    ("The delay is due to a failed crawl export. The new ETA is Tuesday.",
     "Задержка из-за сбоя выгрузки краула. Новая ожидаемая дата — вторник."),
    ("Changes can take a few weeks to show up in Search Console, so we'll re-check on the 15th.",
     "Изменения могут отобразиться в Search Console только через несколько недель, поэтому перепроверим 15-го."),
  ]),
  pc("D. Вежливое напоминание", [
    ("Just a gentle reminder about the access we requested last week.",
     "Мягкое напоминание о доступе, который мы запрашивали на прошлой неделе."),
    ("Without it, we won't be able to start the next stage on time.",
     "Без него мы не сможем вовремя начать следующий этап."),
    ("If it's easier, we can go through it on a quick call.",
     "Если так удобнее, можем разобрать это на коротком звонке."),
  ]),
  pc("E. «Это вне объёма»", [
    ("That's a great idea, but it's outside the current scope.",
     "Отличная идея, но она вне текущего объёма."),
    ("I can send a quick estimate if you'd like to add it.",
     "Могу прислать быструю оценку, если захотите добавить."),
    ("Let's keep the current plan on track and revisit this next month.",
     "Давайте выдержим текущий план и вернёмся к этому в следующем месяце."),
  ]),
]

avoid_rows = [
  ("не писать", "bad", q("As I already said / As per my last email"), "Звучит упрёком. Пишите: Just to confirm…"),
  ("не писать", "bad", q("Please be informed that…"), "Калька с русского канцелярита. Пишите: Just letting you know… или Quick update:"),
  ("не писать", "bad", q("I'm waiting for your answer"), "Звучит нетерпеливо. Пишите: Looking forward to hearing from you."),
  ("не писать", "bad", q("ASAP") + " без даты", "Пишите конкретно: by Thursday, 5 pm."),
  ("не писать", "bad", q("This will definitely boost your rankings"),
   "Обещание, которое нельзя дать. Пишите: This should help. We'll measure the effect in Search Console."),
]

sec_phrases = section(
    "phrases", "Часть 2 · Key Phrases for Written Updates",
    "5 моделей фраз для писем и сообщений клиенту (10 мин)",
    phrase_grid(cards)
    + '\n<h3 style="margin-top:28px;">Чего не писать</h3>\n'
    + compare_card([(t, c, en, e(ru_)) for t, c, en, ru_ in avoid_rows]),
)


# ---------------------------------------------------------------- PART 3 (templates)
def email_card(title, sub, subject_en, lines_en, subject_ru, lines_ru):
    en_html = f"<strong>Subject:</strong> {e(subject_en)}<br><br>" + "<br>".join(e(l) for l in lines_en)
    ru_html = f"<strong>Тема:</strong> {e(subject_ru)}<br><br>" + "<br>".join(e(l) for l in lines_ru)
    return f'''<div class="info-card">
  <div class="info-head"><h3>{title}<small>{sub}</small></h3></div>
  <div class="example-block"><span class="en">{en_html}</span><span class="ru">{ru_html}</span></div>
</div>'''

tpl1 = email_card(
    "Шаблон 1. Recap после звонка по аудиту", "письмо в тот же день",
    "Recap of today's call + next steps",
    ["Hi Anna,",
     "Thanks for your time today. Here's a quick recap of what we agreed:",
     "1. We'll send the technical audit by Friday.",
     "2. Could your developer implement the redirect fixes by next Wednesday?",
     "3. We'll re-check indexation in Search Console two weeks after the release.",
     "Please let me know if anything is missing.",
     "Best regards,",
     "[Name]"],
    "Резюме сегодняшнего звонка и дальнейшие шаги",
    ["Анна, здравствуйте!",
     "Спасибо за уделённое время. Краткое резюме договорённостей:",
     "1. Мы пришлём технический аудит к пятнице.",
     "2. Мог бы ваш разработчик внедрить исправления редиректов до следующей среды?",
     "3. Через две недели после релиза мы перепроверим индексацию в Search Console.",
     "Дайте знать, если что-то упущено.",
     "С уважением,",
     "[Имя]"],
)

tpl2 = email_card(
    "Шаблон 2. Сообщение о задержке", "предупредить заранее",
    "Heads-up: audit draft moving to Tuesday",
    ["Hi Anna,",
     "Quick heads-up: the audit draft will be ready on Tuesday instead of Friday. The delay is due to a failed crawl export, which we had to re-run. I wanted to flag this early so it doesn't come as a surprise. If anything changes, I'll let you know right away.",
     "Thanks for understanding."],
    "Предупреждение: черновик аудита переносится на вторник",
    ["Анна, здравствуйте!",
     "Небольшое предупреждение: черновик аудита будет готов во вторник вместо пятницы. Причина — сбой выгрузки краула, пришлось запускать заново. Хочу предупредить заранее, чтобы это не стало сюрпризом. Если что-то изменится, сразу сообщу.",
     "Спасибо за понимание."],
)

sec_templates = section(
    "templates", "Часть 3 · Two Ready-to-Use Templates",
    "два шаблона письма, которые можно адаптировать под свой проект (8 мин)",
    tpl1 + tpl2 + '<div class="note">Даты и сроки в шаблонах условные: подставляйте свои.</div>',
)


# ---------------------------------------------------------------- PART 4 (written practice)
def wp_item(num, title, sub, task_ru, sample_en, sample_ru):
    body = f'''<ul class="phrase-list">
      <li><span class="tag-role">задача</span><br><span class="ru">{e(task_ru)}</span></li>
      <li><span class="tag-role">образец ответа</span><br><span class="en">{q(sample_en)}</span><span class="ru">— {e(sample_ru)}</span></li>
    </ul>'''
    return dict(title=f"{num}. {title}", sub=sub, body=body)

wp_items = [
  wp_item(1, "The Silent Client", "напоминание о доступе",
    "Клиент две недели не присылает доступ к CMS, контент-календарь стоит. Напишите вежливое напоминание.",
    "Hi Mark, just a gentle reminder about the CMS access we requested two weeks ago. Without it, we can't publish the approved articles, so the content calendar is on hold. Could you send it by Thursday? If it's easier, we can set it up together on a quick call.",
    "Марк, мягкое напоминание о доступе к CMS, который мы запрашивали две недели назад. Без него мы не можем опубликовать согласованные статьи, поэтому контент-календарь на паузе. Не могли бы вы прислать доступ до четверга? Если удобнее, можем настроить вместе на коротком звонке."),
  wp_item(2, "The Blocker on Their Side", "задержка из-за разработчика клиента",
    "Внедрение разметки ждёт разработчика клиента, срок уплывает. Предупредите клиента.",
    "Quick heads-up: the schema rollout is blocked until your developer implements the changes we sent on Monday. I've looped them into this thread. Once it's live, we'll verify it right away.",
    "Небольшое предупреждение: внедрение разметки заблокировано, пока ваш разработчик не внесёт изменения, отправленные в понедельник. Я подключила его к этой переписке. Как только изменения выйдут, сразу проверим."),
  wp_item(3, "«Just One Small Thing»", "вне объёма",
    "В чате клиент просит заодно исправить Core Web Vitals. Это работа разработчиков, вне SEO-пакета. Ответьте мягко.",
    "That's a great idea, but fixing Core Web Vitals involves development work, which is outside the current scope. I can send our recommendations and a quick estimate by tomorrow. Meanwhile, we'll keep the current plan on track.",
    "Отличная идея, но исправление Core Web Vitals требует работы разработчиков и выходит за рамки текущего объёма. Могу прислать наши рекомендации и быструю оценку до завтра. Пока выдерживаем текущий план."),
  wp_item(4, "The Satellite Recap", "связка с уроком 15",
    "После звонка по сателлитам письменно зафиксируйте, что гарантируется, а что нет.",
    "Thanks for the call. To confirm in writing: the satellite is sold as is. Its guaranteed function is to technically pass link equity to your main site. Rankings, traffic and appearances in AI answers are not guaranteed and are not included in the price. Please reply to confirm you're comfortable with this.",
    "Спасибо за звонок. Фиксирую письменно: сателлит продаётся «как есть». Его гарантированная функция — технически передавать ссылочный вес на ваш основной сайт. Позиции, трафик и попадание в AI-ответы не гарантируются и не входят в стоимость. Пожалуйста, ответьте, подтверждая, что вас это устраивает."),
  wp_item(5, "The Dip After Release", "просадка после релиза",
    "После релиза редиректов в Search Console просели показы, клиент пишет в тревоге. Напишите спокойный апдейт без обещаний.",
    "Quick update: after Tuesday's release, we're seeing a short-term dip in impressions in Search Console. This can happen while Google re-processes changed URLs. We're monitoring it daily and will send you a summary on Friday. We'll share only what the data shows.",
    "Короткий апдейт: после вторничного релиза в Search Console видим краткосрочное снижение показов. Такое может быть, пока Google повторно обрабатывает изменённые URL. Мы отслеживаем это ежедневно и пришлём сводку в пятницу. Мы сообщим только то, что показывают данные."),
]

practice_intro = '''
<div class="info-card">
  <div class="info-head"><h3>Как работать<small>в парах</small></h3></div>
  <p class="idea">Прочитайте задачу, напишите ответ в 3–5 предложениях за 5 минут, затем сверьте с образцом и поменяйтесь ролями.</p>
</div>'''

sec_practice = section(
    "practice", "Часть 4 · Written Practice: 5 ситуаций",
    "письменные сценарии для пар (15 мин)",
    practice_intro + accordion(wp_items, single=True, first_open=False),
)


# ---------------------------------------------------------------- PART 5 (checklist / homework)
checklist = [
    "Тема письма конкретная (Recap + next steps).",
    "Каждая задача содержит кто, что и когда.",
    "Срок указан датой, не словом ASAP.",
    "Негарантируемое названо прямо, без слова bonus.",
    "Технические утверждения опираются на данные (GSC, краул), не на «кажется».",
    "Есть просьба подтвердить.",
]
check_html = "".join(f"<li>{e(c)}</li>" for c in checklist)

sec_check = section(
    "checklist", "Часть 5 · Чек-лист письма (домашнее задание)",
    "напишите recap по своему последнему реальному звонку (5–7 строк) и проверьте по списку",
    f'''<div class="info-card">
  <div class="info-head"><h3>Проверка перед отправкой<small>6 пунктов</small></h3></div>
  <ol class="idea" style="padding-left:22px; line-height:1.7;">{check_html}</ol>
</div>''',
)



LESSON_CSS = """<style>
/* lesson 16 only: readable English text (no italic display serif) */
.en{font-family:var(--serif-body) !important; font-style:normal !important; font-weight:600 !important; font-size:16px !important; line-height:1.6 !important; letter-spacing:0 !important;}
.ru, .ru-sub{font-size:14.5px; line-height:1.6;}
td{line-height:1.55;}
</style>"""

body = LESSON_CSS + "\n" + "\n".join([sec_terms, sec_phrases, sec_templates, sec_practice, sec_check])

html = page(
    title="Урок 16 — Письменный английский для SEO-специалиста",
    desc="Follow-up после звонка, статусы, сообщения о задержках, напоминания и мягкий отказ по объёму: словарь, фразы, шаблоны писем и письменные сценарии для SEO-специалиста.",
    brand="Global English · Урок 16",
    eyebrow="Урок 16 из курса «Global English для SEO»",
    h1="Письменный английский: follow-up, статусы и задержки",
    lede="Как закрепить договорённости письменно после звонка: recap, дедлайны и ETA, предупреждение о задержке, напоминание о доступах и мягкое «это вне объёма» — с опорой на данные Search Console и краула, без обещаний, которых нельзя дать.",
    navlinks=[("#terms", "Термины"), ("#phrases", "Фразы"), ("#templates", "Шаблоны"), ("#practice", "Практика"), ("#checklist", "Чек-лист")],
    body=body,
    prev_href="/lessons/15/", prev_label="← Урок 15: Сателлиты",
    next_href="/lessons/17/", next_label="Урок 17: Разбор отчёта →",
)
write("lessons/16/index.html", html)
