# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, accordion, compare_card, table_scroll, write

# ---- Быстрые реакции ----
quick = {
  "Согласие и подтверждение": [
    ("Sounds good!", "Звучит хорошо!"), ("I'm on it.", "Я на этом (займусь этим)."),
    ("Got it, thanks!", "Понял, спасибо!"), ("Will do.", "Сделаю."),
    ("Makes sense.", "Имеет смысл."), ("Good call.", "Хорошая идея/решение."),
    ("Works for me.", "Меня устраивает."), ("Perfect, let's do it.", "Отлично, давайте сделаем."),
  ],
  "Нужно время / проверить": [
    ("Let me check.", "Дайте проверю."), ("I'll take a look.", "Я посмотрю."),
    ("Let me circle back on this.", "Дайте вернусь к этому позже."), ("Give me a sec.", "Дайте секунду."),
    ("I'll look into it.", "Я разберусь с этим."), ("Let me dig into this.", "Дайте покопаюсь в этом."),
    ("I'll get back to you.", "Я вернусь к вам (отвечу позже)."),
  ],
  "Когда не уверен": [
    ("Hmm, not sure about that.", "Хм, не уверен насчёт этого."),
    ("I'd need to double-check.", "Мне нужно перепроверить."),
    ("Let me verify that first.", "Дайте сначала проверю это."),
    ("Good question, let me find out.", "Хороший вопрос, дайте узнаю."),
  ],
  "Обозначаем дедлайны": [
    ("I'll have this done by Friday.", "Я сделаю это к пятнице."),
    ("You'll get it by end of day.", "Вы получите это к концу дня."),
    ("I'm aiming for Tuesday.", "Я нацелен на вторник."),
    ("Should be ready by tomorrow morning.", "Должно быть готово к завтрашнему утру."),
    ("Give me until 3pm.", "Дайте мне до 3pm."),
    ("This will take about 2 days.", "Это займёт около 2 дней."),
    ("Realistically, I'm looking at Thursday.", "Реалистично, я смотрю на четверг."),
  ],
}
sec_quick = section("quick", "Часть 1 · Быстрые реакции", "то, что должно отлетать от зубов в любой рабочей переписке",
                     phrase_grid([phrase_card(t, p) for t, p in quick.items()]))

# ---- Когда что-то пошло не так ----
wrong_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Формула<small>признай → объясни → покажи решение</small></h3></div>
  <p class="idea">Три шага в любом сложном разговоре: <strong>1.</strong> Признай проблему → <strong>2.</strong> Объясни причину → <strong>3.</strong> Покажи решение.</p>
  <div class="chips"><span>Let me explain what happened…</span><span>Here's the situation…</span><span>So here's what's going on…</span><span>I want to be upfront about this…</span></div>
</div>
{phrase_grid([
  phrase_card("Объясняем причину", [
    ("The root cause was…", "Корневая причина была…"),
    ("This happened because…", "Это случилось, потому что…"),
    ("The issue stems from…", "Проблема идёт от…"),
    ("We ran into…", "Мы столкнулись с…"),
    ("Turns out…", "Оказалось…"),
  ]),
  phrase_card("Показываем решение", [
    ("To fix it, we're doing…", "Чтобы исправить это, мы делаем…"),
    ("We're working on…", "Мы работаем над…"),
    ("We're already tackling…", "Мы уже занимаемся…"),
    ("The plan is to…", "План состоит в том, чтобы…"),
    ("We should be back on track by…", "Мы должны вернуться в колею к…"),
  ]),
])}
<div class="compare-card">
  <div class="compare-row"><span class="compare-tag">1</span><span><span class="en">Let me explain what happened. Traffic dropped by 30% last week. The root cause was the latest Google algorithm update that hit our category pages. To fix it, we're optimizing the content and fixing technical issues. We should be back on track by end of month.</span><span class="ru">Ситуация: трафик упал.</span></span></div>
  <div class="compare-row"><span class="compare-tag">2</span><span><span class="en">We want to be upfront about this. The rankings report is delayed. This happened because the API we use had downtime for 2 days. We're already tackling this manually and automating a backup solution. You'll have the report by tomorrow morning.</span><span class="ru">Ситуация: задержка в работе.</span></span></div>
</div>'''
sec_wrong = section("wrong", "Часть 2 · Когда что-то пошло не так", "признать проблему — не значит расписаться в поражении",
                     wrong_body)

# ---- Трудные вопросы ----
tough_items = [
  {"title": "«Why isn't this working yet?»", "sub": "Почему это ещё не работает?", "body": '''
    <div class="chips"><span>Good question. Here's the thing…</span><span>I hear you. Let me share some context…</span><span>Fair point. From my experience…</span></div>
    <div class="example-block" style="margin-top:14px;"><span class="en">Good question. Here's the thing — SEO takes time. We implemented changes 3 weeks ago, but Google needs 2-3 months to fully process and rank the new content. The good news is we're already seeing early positive signals in impressions.</span></div>'''},
  {"title": "«When will we see results?»", "sub": "Когда мы увидим результаты?", "body": '''
    <div class="chips"><span>Based on what I'm seeing…</span><span>Realistically…</span><span>If everything goes smoothly…</span></div>
    <div class="example-block" style="margin-top:14px;"><span class="en">Realistically, we should see meaningful movement in 6-8 weeks. That said, we're already seeing some early wins — our click-through rate improved by 1.5%. If everything goes smoothly with the technical fixes, we might see results sooner.</span></div>'''},
  {"title": "«Why do we need more budget?»", "sub": "Почему нам нужен больший бюджет?", "body": '''
    <div class="chips"><span>Here's why this matters…</span><span>Without this, we're limited to…</span><span>The ROI would be…</span></div>
    <div class="example-block" style="margin-top:14px;"><span class="en">Here's why this matters. Right now we're limited to basic tools that only track 100 keywords. With the upgraded plan, we can track all 500 target keywords and get competitor insights. The ROI would be clear — we'd catch ranking drops faster and avoid losing traffic like we did last month.</span></div>'''},
]
sec_tough = section("tough", "Часть 3 · Отвечаем на трудные вопросы", "три вопроса, которые звучат на каждом втором созвоне",
                     accordion(tough_items, single=True, first_open=False))

# ---- Просим ресурсы ----
resources_body = phrase_grid([
  phrase_card("Просим время", [
    ("I need a few more days to…", "Мне нужно ещё несколько дней, чтобы…"),
    ("Can we push the deadline to…?", "Можем ли мы сдвинуть дедлайн на…?"),
    ("This will take longer than expected because…", "Это займёт больше времени, чем ожидалось, потому что…"),
    ("If we want this done right, we need…", "Если мы хотим сделать это правильно, нам нужно…"),
  ]),
  phrase_card("Просим бюджет", [
    ("We could use additional budget for…", "Нам бы пригодился дополнительный бюджет на…"),
    ("Investing in [X] would help us…", "Инвестиции в [X] помогли бы нам…"),
    ("Without this tool, we're flying blind on…", "Без этого инструмента мы летим вслепую по…"),
  ]),
  phrase_card("Просим помощь", [
    ("It would help if we had…", "Было бы полезно, если бы у нас был…"),
    ("We could use some backup on…", "Нам бы пригодилась помощь с…"),
    ("Can someone help us with…?", "Кто-нибудь может помочь нам с…?"),
    ("We need dev support for…", "Нам нужна поддержка разработчиков для…"),
  ]),
])
resources_body += '''
<div class="compare-card" style="margin-top:16px;">
  <div class="compare-row"><span class="compare-tag">время</span><span><span class="en">We need a few more days to finish the technical audit. The site is bigger than we thought — 2,000 pages instead of 500. If we want this done right, we need until Friday instead of Wednesday. We'll have the priority issues ready tomorrow so you can start working on those.</span></span></div>
  <div class="compare-row"><span class="compare-tag">бюджет</span><span><span class="en">We could use additional budget for Ahrefs. Right now we're limited to manually checking rankings, which takes 3 hours per week. Investing in Ahrefs would automate this and give us competitor insights. It's $200/month but saves us 12 hours monthly.</span></span></div>
  <div class="compare-row"><span class="compare-tag">доступы</span><span><span class="en">We need dev support for implementing schema markup. We have the code ready, but we can't deploy it ourselves. Can someone help us push this to production this week? It should take them about 30 minutes.</span></span></div>
</div>'''
sec_resources = section("resources", "Часть 4 · Просим ресурсы", "время, бюджет, помощь — без чувства вины",
                         resources_body)

# ---- Работа с клиентом ----
client_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Клиент недоволен результатами<small>формула: Empathy → Explanation → Action</small></h3></div>
  <p class="idea">Сначала признать чувства клиента, потом объяснить, потом показать план. Не наоборот.</p>
  <div class="chips">
    <span>I totally understand your frustration…</span><span>We hear you…</span><span>I get it…</span><span>Fair point…</span>
    <span>You're absolutely right to feel this way…</span><span>I appreciate your honesty about this…</span>
    <span>This is a valid concern…</span><span>I can see why you'd be concerned…</span><span>That makes sense…</span>
    <span>I'm glad you brought this up…</span><span>You have every right to ask this…</span><span>I'd feel the same way in your position…</span>
  </div>
  <div class="example-block" style="margin-top:16px;"><span class="en">We totally understand your frustration — you expected to see results by now. Let me explain what's happening. SEO typically takes 3-6 months to show significant results, and we're only 2 months in. That said, we're not sitting idle. Here's what we're seeing: impressions are up 40%, which means Google is noticing our changes. Clicks will follow. Here's the action plan: we're doubling down on high-priority pages this month, and we'll send you weekly micro-updates so you can see the progress.</span></div>
</div>
{phrase_card("SEO — долгосрочная игра", [
  ("SEO is a marathon, not a sprint.", "SEO это марафон, а не спринт."),
  ("Think of it like working out — you don't see results after one week.", "Думайте об этом как о тренировках — вы не видите результаты после одной недели."),
  ("We're building a foundation that will pay off long-term.", "Мы строим фундамент, который окупится в долгосрочной перспективе."),
  ("Google needs time to trust the changes we made.", "Google нужно время, чтобы доверять изменениям, которые мы сделали."),
])}
<div class="info-card">
  <div class="info-head"><h3>Просим доступы<small>формула: Explain why → Show impact → Make it easy</small></h3></div>
  <div class="example-block"><span class="en">We need access to Google Search Console to track our rankings and fix technical issues. Without it, we're flying blind — we can't see what Google thinks about our site. This is blocking us from identifying problems that might be hurting our rankings. Can you add us as users? It takes 2 minutes, we can send you instructions.</span></div>
  <div class="example-block"><span class="en">We need 2 hours of dev time this week to fix our site speed issues. This is blocking our mobile rankings — we're loading in 8 seconds when Google wants under 3. We have the specific fixes documented, so the dev just needs to implement them. Can we prioritize this? It'll directly impact our traffic.</span></div>
</div>'''
sec_client = section("client", "Часть 5 · Работа с клиентом или менеджером", "эмпатия раньше объяснения — всегда",
                      client_body)

# ---- Дедлайны ----
deadlines_body = f'''
<div class="note warn">⚠️ Никогда не давай точные обещания! SEO зависит от Google, конкурентов и многих факторов вне нашего контроля.</div>
{phrase_grid([
  phrase_card("Смягчающие слова перед дедлайном", [
    ("Realistically…", "Реалистично…"), ("Roughly…", "Грубо говоря… / Примерно…"),
    ("Approximately…", "Приблизительно…"), ("Around…", "Около…"), ("About…", "Примерно…"),
    ("We're looking at…", "Мы смотрим на…"), ("Typically…", "Обычно…"),
    ("Usually…", "Как правило…"), ("Generally…", "В общем…"), ("Based on our experience…", "Основываясь на нашем опыте…"),
  ]),
  phrase_card("Фразы с условиями", [
    ("If everything goes smoothly…", "Если всё пойдёт гладко…"),
    ("Assuming no major Google updates…", "Предполагая, что не будет крупных обновлений Google…"),
    ("Under normal circumstances…", "При нормальных обстоятельствах…"),
    ("Barring any surprises…", "Если не будет сюрпризов…"),
    ("Best case scenario…", "В лучшем случае…"),
    ("Conservative estimate…", "Осторожная оценка…"),
  ]),
])}
{compare_card([
  ("плохо","bad","We will see results in 6 weeks.", "Мы увидим результаты через 6 недель."),
  ("плохо","bad","Rankings will improve by March.", "Позиции улучшатся к марту."),
  ("плохо","bad","You'll be on page 1 in 2 months.", "Вы будете на первой странице через 2 месяца."),
  ("хорошо","good","Realistically, we should see results in around 6-8 weeks.", "Реалистично, мы должны увидеть результаты примерно за 6-8 недель."),
  ("хорошо","good","Typically, rankings improve within 2-3 months.", "Обычно позиции улучшаются в течение 2-3 месяцев."),
  ("хорошо","good","Based on our experience, you'll likely see movement by March, if everything goes smoothly.", "Основываясь на нашем опыте, вы, скорее всего, увидите движение к марту, если всё пойдёт гладко."),
])}'''
sec_deadlines = section("deadlines", "Как говорить о дедлайнах", "смягчающие слова — не увиливание, а профессиональная честность",
                         deadlines_body)

# ---- Справочник причин/решений ----
ref_body = phrase_grid([
  phrase_card("Типичные причины · технические", [
    ("Google algorithm update that hit our category pages", "обновление алгоритма Google, которое затронуло наши страницы категорий"),
    ("Technical issues blocking Google crawlers", "технические проблемы, блокирующие краулеры Google"),
    ("Site migration wasn't handled properly", "миграция сайта не была проведена правильно"),
    ("Broken internal linking structure", "сломанная структура внутренних ссылок"),
    ("Server downtime during peak crawling hours", "простой сервера в часы пик краулинга"),
    ("Robots.txt accidentally blocking important pages", "robots.txt случайно блокирует важные страницы"),
  ]),
  phrase_card("Типичные причины · контент и конкуренты", [
    ("Duplicate content issues we didn't catch", "проблемы дублирующегося контента, которые мы не заметили"),
    ("Thin content pages with low value", "тонкие контентные страницы с низкой ценностью"),
    ("Missing key topical coverage", "отсутствие ключевого тематического покрытия"),
    ("Content not matching search intent", "контент не соответствует поисковому интенту"),
    ("Competitors launched aggressive link-building campaigns", "конкуренты запустили агрессивные кампании по построению ссылок"),
    ("Manual / algorithmic penalty", "ручной / алгоритмический штраф"),
  ]),
  phrase_card("Типичные решения · технические", [
    ("Fixing all critical crawl errors and indexation issues", "исправление всех критических ошибок обхода и проблем индексации"),
    ("Implementing proper 301 redirects for lost URLs", "внедрение правильных 301 редиректов для потерянных URL"),
    ("Improving site speed and Core Web Vitals", "улучшение скорости сайта и Core Web Vitals"),
    ("Restructuring internal linking for better crawlability", "реструктурирование внутренних ссылок для лучшей краулабельности"),
  ]),
  phrase_card("Типичные решения · контент и ссылки", [
    ("Optimizing all affected pages with fresh, relevant content", "оптимизация всех затронутых страниц свежим, релевантным контентом"),
    ("Building topical authority through pillar content strategy", "построение тематического авторитета через стратегию опорного контента"),
    ("Disavowing toxic backlinks and building quality ones", "отказ от токсичных обратных ссылок и построение качественных"),
    ("Setting up real-time monitoring for ranking drops", "настройка мониторинга в реальном времени для падений позиций"),
  ]),
])
ref_body += table_scroll(["Код", "Произношение", "Значение"], [
  ["404", "four-oh-four", "page not found"],
  ["302", "three-oh-two", "temporary redirect"],
  ["500", "five hundred", "server error"],
  ["503", "five-oh-three", "service unavailable"],
])
sec_ref = section("reference", "Справочник: причины и решения", "готовые формулировки для карточек и живых ответов",
                   ref_body)

# ---- Формула ответа 7 шагов ----
formula_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Пример полного ответа<small>«Why isn't this working yet? It's been 8 weeks!»</small></h3></div>
  <div class="example-block"><span class="en"><strong>Empathy:</strong> I totally understand your frustration — 8 weeks feels like a long time.</span></div>
  <div class="example-block"><span class="en"><strong>Transition:</strong> Let me break this down for you.</span></div>
  <div class="example-block"><span class="en"><strong>Problem:</strong> Here's the situation — we're 2 months into the campaign and you're not seeing the rankings you expected yet.</span></div>
  <div class="example-block"><span class="en"><strong>Explanation:</strong> SEO typically takes 3-6 months to show significant results. Google needs time to trust and validate the changes we've made. We're in the foundation-building phase right now.</span></div>
  <div class="example-block"><span class="en"><strong>Solution:</strong> That said, we're not sitting idle. We're already tackling this by optimizing 20 high-priority pages and building quality backlinks from authoritative sites.</span></div>
  <div class="example-block"><span class="en"><strong>Timeline:</strong> Based on our experience, we should typically see meaningful movement in roughly 4-6 more weeks, assuming no major algorithm updates.</span></div>
  <div class="example-block"><span class="en"><strong>Request:</strong> One thing that would help us move faster is getting access to Google Search Console — we're still waiting on that and it's blocking some of our technical optimizations.</span></div>
</div>
{table_scroll(["Шаг", "Задача", "Пример фразы"], [
  ["1 · Empathy","показать, что понимаешь клиента","I totally understand your frustration… / We hear you… / Fair point…"],
  ["2 · Transition","подвести к объяснению","Let me break this down for you… / Here's the thing…"],
  ["3 · Problem","чётко назвать проблему + факт","Here's the situation… / Right now…"],
  ["4 · Explanation","объяснить причину","The root cause was… / What's important to understand is…"],
  ["5 · Solution","показать, что делаем","To fix it, we're… / Our approach is to…"],
  ["6 · Timeline","реалистичный срок со смягчением","Realistically, we should see… / We're looking at roughly…"],
  ["7 · Request","опционально — попросить ресурс","To move faster, we need… / We're still waiting on…"],
])}
<div class="note">Критерии успешного ответа: все 7 шагов · эмпатия без сразу-защиты · плавный переход · понятная причина · конкретное решение · реалистичный срок со смягчающими словами · уверенно, но не агрессивно · без невозможных обещаний.</div>'''
sec_formula = section("formula", "Карточка-тренажёр: 7 шагов", "универсальный шаблон ответа на любой сложный вопрос",
                       formula_body)

# ---- 30 сложных вопросов ----
questions = {
  "A · О результатах и сроках": [
    ("\"Why isn't this working yet? It's been 8 weeks!\"", "Почему это ещё не работает? Прошло 8 недель!"),
    ("\"When will we actually see results? Stop giving me vague timelines!\"", "Когда мы на самом деле увидим результаты? Хватит давать мне размытые сроки!"),
    ("\"Our competitor started SEO 2 months after us and they're already ranking. Why aren't we?\"", "Наш конкурент начал SEO на 2 месяца позже нас и уже ранжируется. Почему мы нет?"),
    ("\"We're spending $5,000/month and I see zero leads. Explain this!\"", "Мы тратим $5,000/месяц и я вижу нулевой приход лидов. Объясните это!"),
    ("\"Show me proof this is actually working, not just excuses.\"", "Покажите мне доказательство, что это действительно работает, а не просто отговорки."),
    ("\"My CEO wants to cut the SEO budget because we see no results. What do I tell him?\"", "Мой CEO хочет урезать SEO бюджет, потому что мы не видим результатов. Что мне ему сказать?"),
    ("\"This is taking too long. Can't we just buy some links to speed this up?\"", "Это занимает слишком много времени. Не можем ли мы просто купить ссылки, чтобы ускорить это?"),
  ],
  "B · Сравнение с конкурентами": [
    ("\"Company X does SEO in-house and gets better results. Why are we paying you?\"", "Компания X делает SEO внутри компании и получает лучшие результаты. Почему мы платим вам?"),
    ("\"I talked to another SEO agency and they guarantee page 1 in 3 months. Why can't you?\"", "Я говорил с другим SEO агентством, и они гарантируют страницу 1 за 3 месяца. Почему вы не можете?"),
    ("\"Our competitor's site is worse than ours, but they rank higher. This makes no sense!\"", "Сайт нашего конкурента хуже нашего, но они ранжируются выше. Это не имеет смысла!"),
    ("\"Why are we not #1 for our brand name? Even our competitors show up above us!\"", "Почему мы не #1 по нашему бренду? Даже наши конкуренты показываются выше нас!"),
  ],
  "C · О падениях и проблемах": [
    ("\"Traffic dropped 10% this week. What did you break?!\"", "Трафик упал на 10% на этой неделе. Что вы сломали?!"),
    ("\"We lost all our rankings overnight. This is unacceptable!\"", "Мы потеряли все наши позиции за ночь. Это неприемлемо!"),
    ("\"Our best-performing page disappeared from Google. Fix this NOW!\"", "Наша лучшая страница исчезла из Google. Исправьте это СЕЙЧАС!"),
    ("\"Why is our bounce rate so high? Your content must be bad!\"", "Почему наш показатель отказов такой высокий? Ваш контент, должно быть, плохой!"),
    ("\"Google says our site is slow. Isn't that your job to fix?\"", "Google говорит, что наш сайт медленный. Разве это не ваша работа исправить?"),
  ],
  "D · О бюджете и ресурсах": [
    ("\"You want MORE money? We're already paying you plenty!\"", "Вы хотите БОЛЬШЕ денег? Мы уже платим вам достаточно!"),
    ("\"Why do you need access to Search Console? Can't you just work with what you have?\"", "Зачем вам нужен доступ к Search Console? Не можете ли вы просто работать с тем, что есть?"),
    ("\"Another tool subscription? How many tools do you need?!\"", "Ещё одна подписка на инструмент? Сколько инструментов вам нужно?!"),
    ("\"Our developer says this will take 40 hours. That's way too expensive for SEO!\"", "Наш разработчик говорит, что это займёт 40 часов. Это слишком дорого для SEO!"),
    ("\"Can't you just do this yourself instead of asking for dev help?\"", "Не можете ли вы просто сделать это сами вместо того, чтобы просить помощи разработчика?"),
  ],
  "E · О стратегии и подходе": [
    ("\"Why are we writing blog posts? We need sales, not blog traffic!\"", "Зачем мы пишем блог-посты? Нам нужны продажи, а не трафик на блог!"),
    ("\"My friend said we should focus on local SEO, but you're doing something else. Who's right?\"", "Мой друг сказал, что нам следует сосредоточиться на локальном SEO, но вы делаете что-то другое. Кто прав?"),
    ("\"I read that keywords don't matter anymore. So why are we still doing keyword research?\"", "Я читал, что ключевые слова больше не важны. Так зачем мы всё ещё делаем исследование ключевых слов?"),
    ("\"ChatGPT can write content in 5 minutes. Why does your writer need 2 days?\"", "ChatGPT может написать контент за 5 минут. Почему вашему райтеру нужно 2 дня?"),
    ("\"This 'semantic SEO' sounds like marketing BS. Just get us rankings!\"", "Это 'семантическое SEO' звучит как маркетинговая чушь. Просто дайте нам позиции!"),
  ],
  "F · О коммуникации и процессах": [
    ("\"Your reports are too technical. I don't understand half of these terms!\"", "Ваши отчёты слишком технические. Я не понимаю половину этих терминов!"),
    ("\"You said you'd update me weekly, but I haven't heard from you in 10 days!\"", "Вы сказали, что будете обновлять меня еженедельно, но я не слышал от вас 10 дней!"),
    ("\"Every month you say 'give it more time.' When does this end?!\"", "Каждый месяц вы говорите 'дайте больше времени'. Когда это закончится?!"),
    ("\"I need a simple yes or no: Is this going to work or not?\"", "Мне нужен простой ответ да или нет: Это сработает или нет?"),
  ],
}
q_items = [{"title": cat, "sub": f"{len(qs)} вопросов", "body": '<ul class="phrase-list">' + "".join(f'<li><span class=\"en\">{en}</span><span class=\"ru\">— {ru}</span></li>' for en, ru in qs) + '</ul>'} for cat, qs in questions.items()]
sec_questions = section("questions", "Список сложных вопросов от клиента", "30 вопросов по 6 категориям — тренируй ответы формулой из 7 шагов",
                         accordion(q_items, first_open=False))

# ---- Шпаргалка ----
cheat = table_scroll(["Ситуация", "Фраза"], [
  ["Согласен", "Sounds good! / I'm on it. / Will do."],
  ["Проверю", "Let me check. / I'll look into it. / Give me a sec."],
  ["Дедлайн", "I'll have this done by Friday. / Give me until 3pm."],
  ["Проблема", "Let me explain what happened…"],
  ["Причина", "The root cause was… / This happened because…"],
  ["Решение", "To fix it, we're doing… / We're working on…"],
  ["Трудный вопрос", "Good question. Here's the thing…"],
  ["Прошу время", "I need a few more days to…"],
  ["Прошу бюджет", "We could use additional budget for…"],
  ["Прошу помощь", "We need dev support for… / Can someone help us?"],
  ["GEO & Semantic", "We work with entities / Topical authority / AI Overviews"],
])
sec_cheat = section("cheatsheet", "Шпаргалка: быстрые фразы", "распечатай мысленно и держи под рукой",
                     cheat)

body = "\n".join([sec_quick, sec_wrong, sec_tough, sec_resources, sec_client, sec_deadlines, sec_ref, sec_formula, sec_questions, sec_cheat])

html = page(
    title="Урок 3 — Защищаем работу в сложных ситуациях",
    desc="Быстрые реакции, объяснение проблем, трудные вопросы клиента, просьбы о ресурсах, формула ответа из 7 шагов и 30 реальных вопросов клиентов.",
    brand="Global English · Урок 3",
    eyebrow="Урок 3 из курса «Global English для SEO»",
    h1="Защищаем работу в сложных ситуациях",
    lede="От «дайте проверю» до полноценного ответа на «мы платим вам $5000 и не видим лидов» — формулы, которые держат разговор под контролем.",
    navlinks=[("#quick","Реакции"), ("#wrong","Что пошло не так"), ("#tough","Трудные вопросы"),
              ("#deadlines","Дедлайны"), ("#formula","7 шагов"), ("#questions","30 вопросов"), ("#cheatsheet","Шпаргалка")],
    body=body,
    prev_href="/lessons/2/", prev_label="← Урок 2: Отчёты",
    next_href="/lessons/4/", next_label="Урок 4: Графики и позиции →",
)
write("lessons/3/index.html", html)
