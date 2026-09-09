# -*- coding: utf-8 -*-
from build import page, section, accordion, write

def scenario_body(context, spec_role, client_role, spec_phrases, client_phrases):
    sp = "".join(f"<span>{p}</span>" for p in spec_phrases)
    cp = "".join(f"<span>{p}</span>" for p in client_phrases)
    return f'''
    <p class="idea"><strong>Контекст:</strong> {context}</p>
    <h5>Роль специалиста</h5><p>{spec_role}</p>
    <h5>Роль клиента</h5><p>{client_role}</p>
    <h5>Фразы-помощники · специалист</h5><div class="chips">{sp}</div>
    <h5>Фразы-помощники · клиент</h5><div class="chips">{cp}</div>'''

scenarios = [
  dict(title="Zero Trust Kickoff", sub="A · Onboarding · крипто, старт без доверия", body=scenario_body(
    "Первый kick-off call с новым клиентом (криптообменник). Пакет уже куплен через sales team. Клиент не понимает, что именно купил и зачем это нужно. Доверия — ноль.",
    "Установить доверие. Объяснить, что входит в пакет, установить реалистичные ожидания по срокам (3–6 месяцев), договориться о процессе коммуникации.",
    "Скептичны после плохого опыта. Не уверены, что значит «full SEO package». Нужен трафик СЕЙЧАС. «Конкурент запустился 2 месяца назад и уже имеет больше трафика». Заняты, не хотят много встреч.",
    ["Let me walk you through exactly what's included in your package…", "I totally understand your concern about competitors…",
     "Results in SEO typically take 3-6 months, here's why…", "I know you're busy, let's set up a communication flow that works…",
     "Within this scope, we can prioritize…"],
    ["So what exactly did we buy?", "Our competitor is killing it and they just launched",
     "When will we see results? We need traffic NOW", "Can you guarantee results in 3 months?",
     "I'm super busy, can we just communicate via email?"],
  )),
  dict(title="Business vs SEO Competitors", sub="A · Onboarding · travel, путаница с конкурентами", body=scenario_body(
    "2-я неделя работы с клиентом (платформа авторских туров). Провели competitor analysis. Клиент в шоке: «Почему вы анализируете эти сайты? Это НЕ наши конкуренты!»",
    "Объяснить разницу между бизнес-конкурентами и SEO-конкурентами. Показать ценность подхода. Получить одобрение двигаться дальше.",
    "Знает свой рынок туризма. Реальные конкуренты — крупные турагентства. Специалист анализирует travel-блоги и мелкие сайты гидов — кажется неправильным. Агрессивно защищает позицию — 10 лет в индустрии.",
    ["I completely understand why you see it that way. Let me explain…", "Business competitors and SEO competitors are two different things…",
     "These sites are ranking for keywords your customers are searching…", "Think of it this way — these sites are stealing your traffic right now…",
     "Google doesn't care about business models, it cares about who answers the query"],
    ["These sites are NOT our competitors", "Our real competitors are [Brand A] and [Brand B]",
     "I know my market better than you", "Are you sure you know what you're doing?"],
  )),
  dict(title="Content is Not Converting", sub="B · Scope · SaaS, блог не даёт лидов", body=scenario_body(
    "Месяц работы с SaaS-платформой (инструменты для соцсетей). Опубликовано 10 информационных статей. Клиент смотрит analytics: «Этот трафик не конвертирует! Зачем мы тратим время на блог?»",
    "Объяснить продуктовую воронку. Показать, как информационный контент работает вместе с product pages. Убедить продолжать стратегию.",
    "Data-driven. Смотрит только на conversions. «Эти блог-посты имеют 0 конверсий». Считает, нужно фокусироваться только на product pages. PPC конвертирует на 5%, этот трафик — на 0.5%.",
    ["I get it — you need conversions. Let me show you how this content drives conversions…", "Think of it like a sales funnel — not everyone buys immediately…",
     "These articles build topical authority which helps ALL pages rank…", "This is top of funnel content that brings awareness…"],
    ["These blog posts have 0 conversions. Why are we doing this?", "Show me the money. Where are the leads?",
     "Our PPC converts at 5%, this traffic converts at 0.5%", "I need ROI, not vanity metrics"],
  )),
  dict(title="Link Building is Too Expensive", sub="B · Scope · крипто, цена ссылок", body=scenario_body(
    "Предложена link building campaign для криптобиржи. Клиент видит цены: «Почему так дорого?! Я могу купить ссылки на Fiverr по $5!»",
    "Объяснить разницу в качестве. Почему цена зависит от региона (US/EU vs Asia). Риски дешёвых ссылок — без апелляции к цене напрямую.",
    "Видит только цифры. «Ссылка есть ссылка, какая разница откуда?» Нашёл дешёвые альтернативы. Нужно обосновать расходы перед боссом.",
    ["Great question — let me explain what you're actually paying for…", "The difference between a $5 link and a quality link is like a fake watch vs a real Rolex…",
     "Region matters because Google evaluates a link based on relevance and authority…", "Cheap links can harm your rankings — Google penalizes spam…"],
    ["Why is this so expensive? I can buy links on Fiverr for $5!", "Can't we just buy cheaper links from Asia?",
     "This is eating our entire budget", "I need to justify these costs to my boss"],
  )),
  dict(title="Ghost Client", sub="C · Operations · travel, клиент не отвечает", body=scenario_body(
    "Клиент с платформой для авторских туров. 2 недели назад отправили вопросы для контента. Клиент не отвечает. Задачи заблокированы, дедлайн близко.",
    "Получить информацию, не звучать агрессивно. Показать, что задержка влияет на результаты. Найти способ избежать этого в будущем.",
    "Очень занят операционными задачами, SEO не в приоритете ежедневно. Искренне забывает. «Oh sorry, I've been swamped…» При выходе на связь: «Почему всё задерживается? Я думал, вы всё сами делаете?»",
    ["I understand you're busy. Let me make this as easy as possible…", "I need just 10 minutes to unblock 2 weeks of work…",
     "What if we schedule a regular weekly 15-min slot?", "Can you delegate someone to be a day-to-day contact?"],
    ["Oh sorry, I've been swamped…", "Can't you just figure it out without me?",
     "Just make something up, you're the experts", "Why is everything delayed?"],
  )),
  dict(title="Dev Team Bottleneck", sub="C · Operations · SaaS, тормозят разработчики", body=scenario_body(
    "Месяц назад отправили technical recommendations для SaaS-платформы. Dev team ничего не сделал. Клиент: «Почему позиции не улучшаются?»",
    "Объяснить, что bottleneck не на стороне SEO-команды. Не подставлять разработчиков. Показать impact задержки, найти решение.",
    "Не понимает технические детали. Думает, что SEO-команда должна «просто всё сделать». «Я плачу за результаты, не за отговорки». Рассматривает смену агентства.",
    ["I hear your frustration. Let me explain where we are…", "We've completed everything on our side. Here's what's pending…",
     "We don't have access to implement — we need the dev team…", "Can we get the dev team on this call to align?"],
    ["Why aren't rankings improving?", "I don't care about internal processes, I need results",
     "I'm paying you for results, not excuses", "Maybe we need another agency"],
  )),
  dict(title="Where Are My Results?!", sub="D · Results · крипто, 6 недель без видимого эффекта", body=scenario_body(
    "6 недель работы с криптообменником. Клиент ожидал результаты через месяц. Трафик растёт минимально. «Мне говорили — будут результаты!»",
    "Управлять ожиданиями. Показать ранние сигналы — impressions, позиции. Объяснить SEO timeline. Убедить продолжать.",
    "Ожидал быстрых побед, сравнивает с PPC. «Моя реклама работает немедленно! За что я плачу?» Рассматривает остановку проекта.",
    ["I understand — let me show you what's happening behind the scenes…", "SEO and PPC work on different timelines, here's why…",
     "We ARE seeing results, just not in traffic yet…", "We moved from position 35 to position 12 — we're climbing"],
    ["It's been 6 weeks and nothing changed!", "My paid ads work immediately!",
     "This is not working, maybe we should pause", "I need ROI soon or we're cutting this"],
  )),
  dict(title="Deadline Panic", sub="D · Results · travel, запуск через 2 недели", body=scenario_body(
    "Клиент с платформой авторских туров: «У нас product launch через 2 недели, и нам нужно rank #1 по [competitive term]! Это критично!»",
    "Честно управлять нереалистичным ожиданием. Предложить, что реально можно сделать. Не потерять клиента, объяснить ограничения Google.",
    "Под давлением от CEO. Не понимает SEO limitations. «Просто сделайте что нужно». «Можем заплатить extra?» Отчаянно готов потратить больше.",
    ["I understand this is critical. Let me be honest about what's possible…", "Google's algorithm works on its own timeline — we can't force it…",
     "Ranking #1 in 2 weeks is not possible. Here's what we CAN do…", "For immediate visibility, you'd need paid ads…"],
    ["We NEED to rank #1 in 2 weeks!", "This launch is make-or-break",
     "Can we pay extra to speed this up?", "Can you buy more links to rank faster?"],
  )),
  dict(title="Too Much Customization", sub="D · Results · SaaS, хочет полную кастомизацию", body=scenario_body(
    "Клиент с небольшим чеком (SaaS для соцсетей) постоянно просит custom reports, дополнительные встречи, изменения. «Can you customize this?», «Can we add weekly calls?»",
    "Показать, что включено в пакет. Профессионально установить границы, не обидев. Объяснить, что стандартизированные процессы = фокус на результатах.",
    "Привык к персонализации, не понимает, что пакет стандартизирован. «Но мне нужна [custom вещь]». «Другие агентства делают». Искренне считает это разумным.",
    ["I want to make sure you get maximum value from your package…", "Your package includes [standard reports/meetings]…",
     "Monthly calls work best because we need time to gather data…", "I can't add weekly calls, but I can send weekly email updates…"],
    ["Can you create a custom dashboard with these metrics?", "I need weekly calls to review everything",
     "I want to approve every content piece before publishing", "Other agencies do this as standard"],
  )),
  dict(title="GEO Upsell", sub="E · Advanced · крипто, продажа GEO", body=scenario_body(
    "3–4 месяц работы с криптобиржей, хорошие результаты, доверие установлено. Время предложить GEO.",
    "Объяснить GEO простыми словами без tech jargon. Показать, как это дополняет текущую работу. Дать примеры, получить интерес к proposal.",
    "Довольны результатами, открыты к новым идеям, но не понимают tech jargon. «What is GEO? Buzzword?» Не против потратить, если увидят value.",
    ["You know how ChatGPT and AI tools are everywhere now?", "GEO makes sure YOUR site is recommended when people ask AI…",
     "Traditional SEO optimizes for Google. GEO optimizes for AI answers.", "This complements what we're doing, doesn't replace…"],
    ["Wait, what? Generative what?", "Sounds expensive. Is it worth it?",
     "How is this different from what we're doing?", "Will this bring customers or just hype?"],
  )),
]

items = scenarios
sec = section("scenarios", "10 сценариев", "работа в парах: специалист / клиент, 5–7 минут на сценарий, без подготовки",
              accordion(items, first_open=False))

body = f'''<section id="intro">
  <div class="wrap">
    <h2>Как играть</h2>
    <p class="section-kicker">важный контекст</p>
    <div class="info-card">
      <p class="idea">Все клиенты уже купили базовый SEO-пакет. Задача специалиста — работать в рамках пакета. Работа в парах: один играет Специалиста, другой — Клиента. 5–7 минут на сценарий, без подготовки — чистая импровизация. Группа даёт фидбек после каждой сцены.</p>
    </div>
  </div>
</section>
{sec}'''

html = page(
    title="Урок 7 — Role Play: Real Client Scenarios",
    desc="10 сценариев ролевой игры со специалистом и клиентом: онбординг, скоуп и ожидания, операционные блокеры, результаты и сроки, GEO-апсейл.",
    brand="Global English · Урок 7",
    eyebrow="Урок 7 из курса «Global English для SEO»",
    h1="Role Play: Real Client Scenarios",
    lede="Реальные ситуации из практики агентства — играешь специалиста или клиента, 5–7 минут импровизации, потом фидбек от группы.",
    navlinks=[("#intro","Как играть"), ("#scenarios","Сценарии")],
    body=body,
    prev_href="/lessons/6/", prev_label="← Урок 6: GEO-термины",
    next_href="/lessons/8/", next_label="Урок 8: Reverse Roles →",
)
write("lessons/7/index.html", html)
