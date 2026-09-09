# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, accordion, write

rescue = {
  "Когда нужно время подумать": [
    ("Let me think…", "Дайте подумать…"), ("Good question…", "Хороший вопрос…"),
    ("Here's the thing…", "Дело в том…"), ("Let me check that…", "Дайте я проверю…"),
    ("Hmm, let me see…", "Хм, посмотрим…"), ("That's a great question, actually…", "Это отличный вопрос, на самом деле…"),
    ("You know what…", "Знаете что…"),
  ],
  "Когда не знаешь слово": [
    ("What's the word… the thing that…", "Как это называется… та штука, которая…"),
    ("You know, the…", "Ну знаете, это…"), ("It's like… but for SEO", "Это как… но для SEO"),
    ("How can I put it…", "Как бы это сказать…"), ("I mean…", "Я имею в виду…"),
  ],
  "Когда нужно успокоить клиента": [
    ("I totally get it", "Я полностью понимаю"), ("I hear you", "Я вас слышу"),
    ("That makes sense", "Это логично"), ("I understand your concern", "Я понимаю вашу озабоченность"),
    ("Let me explain what's happening", "Позвольте объяснить, что происходит"),
    ("Here's what we can do", "Вот что мы можем сделать"), ("Don't worry", "Не волнуйтесь"),
    ("This is actually normal", "Это на самом деле нормально"),
  ],
  "Когда нужно выиграть время": [
    ("Let me pull up the data", "Дайте я открою данные"), ("Give me one second", "Дайте секунду"),
    ("I need to check something first", "Мне нужно сначала что-то проверить"),
    ("Can I get back to you on that?", "Могу я вернуться к вам по этому вопросу?"),
    ("Let me look into this", "Дайте я разберусь с этим"),
  ],
  "Когда объясняешь сложное": [
    ("Think of it like this…", "Представьте это так…"), ("In simple terms…", "Простыми словами…"),
    ("Here's what this means…", "Вот что это означает…"), ("The bottom line is…", "Суть в том…"),
    ("What this means for you is…", "Что это значит для вас…"), ("To put it simply…", "Говоря простыми словами…"),
  ],
  "Когда нужно дать негативную информацию": [
    ("Here's the situation…", "Вот ситуация…"), ("I won't sugarcoat it…", "Я не буду приукрашивать…"),
    ("To be honest…", "Если честно…"), ("The reality is…", "Реальность такова…"),
    ("Unfortunately…", "К сожалению…"), ("The challenge here is…", "Проблема здесь в том…"),
  ],
  "Когда продаёшь свою идею": [
    ("Here's what I'm thinking…", "Вот что я думаю…"), ("The way I see it…", "Как я это вижу…"),
    ("This would help us because…", "Это поможет нам, потому что…"),
    ("If we do this, you'll see…", "Если мы сделаем это, вы увидите…"), ("The benefit here is…", "Выгода здесь в том…"),
  ],
  "Универсальные связки": [
    ("So…", "Итак…"), ("Actually — by the way…", "На самом деле…"), ("Basically…", "В основном…"),
    ("The thing is…", "Дело в том…"), ("You see…", "Видите ли…"), ("Look…", "Смотрите…"), ("Listen…", "Послушайте…"),
  ],
}
sec_rescue = section("rescue", "Часть 1 · Словарь фраз-спасателей", "8 ситуаций, для каждой — готовые опоры",
                      phrase_grid([phrase_card(t, p) for t, p in rescue.items()]))

rules_body = '''
<div class="info-card">
  <div class="info-head"><h3>Формат</h3></div>
  <ul style="margin:0; padding-left:20px; color:var(--ink-soft); font-size:15px;">
    <li>У каждого специалиста 4 вопроса от клиента: 2 простых (разминка) + 2 каверзных (проверка на прочность)</li>
    <li>Ты отвечаешь <strong>без подготовки</strong> — как в реальной жизни</li>
    <li>Можно и нужно использовать фразы-спасатели из словаря выше</li>
  </ul>
  <div class="chips" style="margin-top:16px;">
    <span>✅ начать говорить, пусть с ошибками</span><span>✅ использовать фразы-костыли</span><span>✅ не паниковать при сложных вопросах</span>
    <span>❌ не нужна идеальная грамматика</span><span>❌ не нужно знать все слова</span>
  </div>
</div>'''
sec_rules = section("rules", "Часть 2 · Правила игры", "цель — говорить, а не молчать в поисках идеального ответа", rules_body)

def q(en, ru, tricky=False):
    tag = "каверзный" if tricky else "простой"
    return f'<li><span class="tag-role">{tag}</span><br><span class="en">{en}</span><span class="ru">— {ru}</span></li>'

specialists = [
  ("Вова", "Increase traffic · казино-сайт, 3 месяца", [
    ("\"Hey, quick question — how's the traffic looking this month?\"", "Привет, быстрый вопрос — как выглядит трафик в этом месяце?", False),
    ("\"Can you send me the rankings report by Friday?\"", "Можешь отправить мне отчёт по позициям к пятнице?", False),
    ("\"I talked to my friend who does SEO and he said we should be #1 by now. Why aren't we?\"", "Я говорил с другом, который занимается SEO, и он сказал, что мы уже должны были быть на первом месте. Почему мы не на первом?", True),
    ("\"Our competitor's site looks terrible but they rank higher than us. This makes no sense! What are we doing wrong?\"", "Сайт нашего конкурента выглядит ужасно, но они ранжируются выше нас. Это не имеет смысла! Что мы делаем не так?", True),
  ]),
  ("Алина", "Find new keywords · криптобиржа, 1 месяц", [
    ("\"Did you find any good keywords for us this week?\"", "Ты нашла какие-нибудь хорошие ключевые слова для нас на этой неделе?", False),
    ("\"How do you decide which keywords to target?\"", "Как ты решаешь, на какие ключевые слова таргетироваться?", False),
    ("\"These keywords you found have minimal search volume. Why should we waste time on them?\"", "Эти ключевые слова, которые ты нашла, имеют минимальный объём поиска. Зачем нам тратить на них время?", True),
    ("\"I used a free keyword tool and found 100 keywords in 5 minutes. Why do you waste time on it?\"", "Я использовал бесплатный инструмент для ключевых слов и нашёл 100 ключевиков за 5 минут. Зачем вы тратите время попусту?", True),
  ]),
  ("Денис", "Check the rankings · iGaming, 1 год", [
    ("\"Can you check our rankings for the main keywords?\"", "Можешь проверить наши позиции по основным ключевым словам?", False),
    ("\"Are we moving up or down this week?\"", "Мы движемся вверх или вниз на этой неделе?", False),
    ("\"We went from position 8 to position 11 this week. What happened?!\"", "Мы упали с позиции 8 на позицию 11 на этой неделе. Что произошло?!", True),
    ("\"Why do the rankings in your tool show position 5, but when I Google it myself I see position 15?\"", "Почему позиции в твоём инструменте показывают 5 место, а когда я сам гуглю, я вижу 15 позицию?", True),
  ]),
  ("Костя", "Optimize a page · trading-платформа, 6 месяцев", [
    ("\"What pages are you working on this week?\"", "Над какими страницами ты работаешь на этой неделе?", False),
    ("\"How long does it take to optimize one page?\"", "Сколько времени занимает оптимизация одной страницы?", False),
    ("\"You optimized this page 2 months ago and nothing changed. Was it a waste of time?\"", "Ты оптимизировал эту страницу 2 месяца назад, и ничего не изменилось. Это была пустая трата времени?", True),
    ("\"Can't we just use ChatGPT to optimize all pages in one day?\"", "Не можем ли мы просто использовать ChatGPT, чтобы оптимизировать все страницы за один день?", True),
  ]),
  ("Катя", "Send report to a client · финтех, 3-й ОП", [
    ("\"When will I get this month's report?\"", "Когда я получу отчёт за этот месяц?", False),
    ("\"Can you explain what CTR means in the report?\"", "Можешь объяснить, что означает CTR в отчёте?", False),
    ("\"These numbers in your report don't match what I see in my Google Analytics. Which one is correct?\"", "Эти цифры в твоём отчёте не совпадают с тем, что я вижу в своей Google Analytics. Какие правильные?", True),
    ("\"This report is 20 pages long. Can you just tell me: are we winning or losing?\"", "Этот отчёт на 20 страниц. Можешь просто сказать мне: мы выигрываем или проигрываем?", True),
  ]),
  ("Наташа", "Prepare a report · крипто-контент, 2-й ОП", [
    ("\"What will be in this month's report?\"", "Что будет в отчёте за этот месяц?", False),
    ("\"How's our traffic compared to last month?\"", "Как наш трафик по сравнению с прошлым месяцем?", False),
    ("\"I don't have time to read reports. Just tell me in 30 seconds: should I be happy or worried?\"", "У меня нет времени читать отчёты. Просто скажи мне за 30 секунд: мне радоваться или волноваться?", True),
    ("\"Your report says 'promising trends' but I see no increase in sales. What am I paying for?\"", "В твоём отчёте написано «многообещающие тенденции», но я не вижу роста продаж. За что я плачу?", True),
  ]),
  ("Аня", "Fix an issue · трейдинг-платформа, 4-й месяц", [
    ("\"What issue are you fixing right now?\"", "Какую проблему ты сейчас исправляешь?", False),
    ("\"How long will the fix take?\"", "Сколько времени займёт исправление?", False),
    ("\"We fixed this same issue 3 months ago. When will we see the effect?!\"", "Мы исправляли эту же проблему 3 месяца назад. Когда ждать эффект?!", True),
    ("\"Our developer says there's no issue and everything works fine. Are you making up problems to bill us more hours?\"", "Наш разработчик говорит, что никакой проблемы нет и всё работает отлично. Ты придумываешь проблемы, чтобы выставить нам больше часов?", True),
  ]),
  ("Валера", "Analyze the SERP · проект, 2-й месяц", [
    ("\"What did you find in the search results?\"", "Что ты нашёл в результатах поиска?", False),
    ("\"Who are our main competitors?\"", "Кто наши основные конкуренты?", False),
    ("\"All these competitors you found have been doing SEO for years. How can we possibly compete with them?\"", "Все эти конкуренты, которых ты нашёл, занимаются SEO годами. Как мы вообще можем с ними конкурировать?", True),
    ("\"I looked at the search results myself and saw mostly ads, no organic results. Does SEO even work for our niche?\"", "Я сам посмотрел результаты поиска и увидел в основном рекламу, никакой органики. SEO вообще работает для нашей ниши?", True),
  ]),
  ("Аля", "Build quality backlinks · финансовый проект", [
    ("\"How many backlinks did we get this month?\"", "Сколько обратных ссылок мы получили в этом месяце?", False),
    ("\"Where are these backlinks from?\"", "Откуда эти обратные ссылки?", False),
    ("\"I can buy 1000 backlinks for $50 on Fiverr. Why are you charging $2000 for 10 links?\"", "Я могу купить 1000 обратных ссылок за $50 на Fiverr. Почему ты берёшь $2000 за 10 ссылок?", True),
    ("\"We got 20 new backlinks but rankings didn't change at all. Are these links even working?\"", "Мы получили 20 новых обратных ссылок, но позиции вообще не изменились. Эти ссылки вообще работают?", True),
  ]),
  ("Специалист 10", "Improve conversions · финансовый проект, 3-й ОП", [
    ("\"What are you doing to improve conversions?\"", "Что ты делаешь для улучшения конверсий?", False),
    ("\"How's our conversion rate now?\"", "Какой у нас сейчас показатель конверсии?", False),
    ("\"You've been working on conversions for 2 months and they went down, not up. What's going on?\"", "Ты работаешь над конверсиями 2 месяца, а они упали, а не выросли. Что происходит?", True),
    ("\"Traffic is up 50% but sales are the same. Isn't this just meaningless traffic?\"", "Трафик вырос на 50%, но продажи те же. Это просто бессмысленный трафик, не так ли?", True),
  ]),
  ("Специалист 11", "Set up tracking · казино-аффилейт, 4-й ОП", [
    ("\"What tracking did you set up?\"", "Какое отслеживание ты настроила?", False),
    ("\"Can we see real-time data now?\"", "Мы теперь можем видеть данные в реальном времени?", False),
    ("\"The tracking stopped working after your setup. Did you break something?\"", "Отслеживание перестало работать после твоей настройки. Ты что-то сломала?", True),
    ("\"Why do we need all this tracking? Can't we just check Google Analytics like everyone else?\"", "Зачем нам всё это отслеживание? Не можем ли мы просто проверять Google Analytics, как все остальные?", True),
  ]),
]

items = []
for name, ctx, qs in specialists:
    body = '<p class="idea">Контекст: ' + ctx + '</p><ul class="phrase-list">' + "".join(q(en, ru, tr) for en, ru, tr in qs) + '</ul>'
    items.append({"title": name, "sub": ctx.split(" · ")[0], "body": body})
sec_cards = section("cards", "Карточки специалистов", "4 вопроса без подготовки — 2 разминочных, 2 каверзных",
                     accordion(items, first_open=False))

body = "\n".join([sec_rescue, sec_rules, sec_cards])

html = page(
    title="Урок 5 — Real Conversations: ответы клиентам без подготовки",
    desc="Словарь фраз-спасателей на все случаи живого разговора + 11 карточек специалистов с вопросами клиентов без подготовки.",
    brand="Global English · Урок 5",
    eyebrow="Урок 5 из курса «Global English для SEO»",
    h1="Real Conversations: ответы без подготовки",
    lede="Фразы-спасатели на случай, когда нужно выиграть время, не знаешь слово или пришёл каверзный вопрос — плюс живая практика в парах.",
    navlinks=[("#rescue","Фразы-спасатели"), ("#rules","Правила"), ("#cards","Карточки")],
    body=body,
    prev_href="/lessons/4/", prev_label="← Урок 4: Графики",
    next_href="/lessons/6/", next_label="Урок 6: GEO-термины →",
)
write("lessons/5/index.html", html)
