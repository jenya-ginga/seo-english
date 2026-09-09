# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, accordion, write

phrases = {
  "Начало выступления": [
    ("Let me kick things off with…", "Позвольте мне начать с…"),
    ("I'd like to start by highlighting…", "Я хотел бы начать с выделения…"),
    ("To give you a big picture…", "Чтобы вы видели общую картину…"),
    ("Here's a high-level overview…", "Вот общий обзор…"),
    ("I'll quickly walk you through…", "Я быстро проведу вас через…"),
  ],
  "Переход между темами": [
    ("Moving on to…", "Переходя к…"),
    ("Now let's turn our attention to…", "Теперь давайте обратим внимание на…"),
    ("Speaking of…", "Говоря о…"),
    ("This brings me to my next point…", "Это подводит меня к следующему пункту…"),
    ("On a related note…", "По связанной теме…"),
  ],
  "Описание успехов и результатов": [
    ("We've achieved significant growth in…", "Мы достигли значительного роста в…"),
    ("The numbers speak for themselves…", "Цифры говорят сами за себя…"),
    ("We're proud to report…", "Мы с гордостью сообщаем…"),
    ("This represents a X% improvement…", "Это представляет улучшение на X%…"),
    ("We've made great strides in…", "Мы сделали большие успехи в…"),
  ],
  "Обсуждение проблем и вызовов": [
    ("We're facing some headwinds with…", "Мы сталкиваемся с некоторыми трудностями в…"),
    ("The main hurdle we're encountering…", "Главное препятствие, с которым мы сталкиваемся…"),
    ("We've hit a snag with…", "У нас возникла проблема с…"),
    ("This is proving challenging because…", "Это оказывается сложным, потому что…"),
    ("We're not where we want to be with…", "Мы не там, где хотели бы быть с…"),
  ],
  "Планирование и следующие шаги": [
    ("Going forward, we'll be focusing on…", "В дальнейшем мы сосредоточимся на…"),
    ("Our game plan for next month is…", "Наш план на следующий месяц…"),
    ("We're putting together a strategy to…", "Мы разрабатываем стратегию для…"),
    ("The next phase involves…", "Следующая фаза включает…"),
    ("We're rolling out improvements to…", "Мы внедряем улучшения для…"),
  ],
  "Выражение уверенности": [
    ("We're confident that…", "Мы уверены, что…"),
    ("All indicators suggest that…", "Все показатели предполагают, что…"),
    ("We have every reason to believe…", "У нас есть все основания полагать…"),
    ("The data supports our approach…", "Данные подтверждают наш подход…"),
    ("We're well positioned to…", "Мы хорошо готовы, чтобы…"),
  ],
  "Просьбы и предложения": [
    ("We could use your input on…", "Нам бы пригодился ваш вклад в…"),
    ("I'd appreciate your thoughts on…", "Я был бы благодарен за ваши мысли о…"),
    ("What's your take on…?", "Каково ваше мнение о…?"),
    ("Feel free to jump in with questions.", "Не стесняйтесь задавать вопросы."),
    ("I'm open to suggestions here.", "Я открыт для предложений по этому поводу."),
  ],
  "Завершение": [
    ("To wrap things up…", "Чтобы подвести итоги…"),
    ("In a nutshell…", "В двух словах…"),
    ("The key takeaway here is…", "Ключевой вывод здесь…"),
    ("I'll leave you with this thought…", "Оставлю вас с этой мыслью…"),
    ("That about covers everything.", "Это покрывает всё."),
  ],
  "Неформальные обороты (для внутренних встреч)": [
    ("Let me ping you about that later.", "Я напишу тебе об этом позже."),
    ("I'll keep you in the loop.", "Я буду держать тебя в курсе."),
    ("That's on my radar.", "Это у меня на радаре."),
    ("Let's circle back to this.", "Давайте вернёмся к этому позже."),
    ("I'm swamped with…", "Я завален…"),
    ("That's a quick win.", "Это быстрая победа."),
    ("We're on the right track.", "Мы на правильном пути."),
  ],
  "Цифры и статистика": [
    ("Roughly / Approximately…", "Примерно / Приблизительно…"),
    ("We're looking at around X…", "Мы говорим о примерно X…"),
    ("The numbers are trending upward / downward.", "Цифры имеют восходящий / нисходящий тренд."),
    ("We've seen a spike / dip in…", "Мы увидели всплеск / падение в…"),
    ("The metrics have plateaued.", "Метрики вышли на плато."),
  ],
}

phrase_cards_html = [phrase_card(title, pairs) for title, pairs in phrases.items()]
sec_phrases = section("phrases", "Полезные выражения для отчётов и презентаций",
                       "10 ситуаций, которые повторяются на каждой встрече",
                       phrase_grid(phrase_cards_html))

glossary = {
  "Технические термины": [
    ("Crawl errors <span class='ru-sub'>[крол эрэрз]</span>", "ошибки обхода"),
    ("Indexing rate <span class='ru-sub'>[индэксин рэйт]</span>", "скорость индексации"),
    ("hreflang implementation", "реализация hreflang"),
    ("Core Web Vitals", "основные веб-показатели"),
    ("LCP (Largest Contentful Paint)", "загрузка крупнейшего контента"),
    ("TTFB (Time to First Byte)", "время до первого байта"),
    ("Schema markup", "schema-разметка"),
    ("Structured data", "структурированные данные"),
    ("Mobile usability", "мобильная адаптивность"),
    ("JavaScript-related issues", "проблемы с JavaScript"),
    ("Site architecture", "архитектура сайта"),
    ("Crawl efficiency", "эффективность обхода"),
    ("Dynamic rendering", "динамический рендеринг"),
    ("AMP pages", "AMP-страницы"),
    ("Progressive Web App", "прогрессивное веб-приложение"),
  ],
  "Контент и ключевые слова": [
    ("Pillar pages", "основные страницы"),
    ("Content localization", "локализация контента"),
    ("Meta tags optimization", "оптимизация мета-тегов"),
    ("Keyword opportunities", "возможности по ключевым словам"),
    ("Search intent", "поисковое намерение"),
    ("Commercial intent", "коммерческое намерение"),
    ("Informational keywords", "информационные ключевые слова"),
    ("Long-tail keywords", "низкочастотные запросы"),
    ("Content gap analysis", "анализ пробелов в контенте"),
    ("Topical authority", "тематический авторитет"),
    ("Expert roundups", "сборники мнений экспертов"),
    ("Video transcripts", "расшифровки видео"),
    ("Cornerstone articles", "ключевые статьи"),
  ],
  "Ссылки и авторитетность": [
    ("Backlinks", "обратные ссылки"),
    ("Link-building", "построение ссылок"),
    ("Domain authority", "авторитет домена"),
    ("Link equity", "ссылочный вес"),
    ("Contextual links", "контекстные ссылки"),
    ("Guest posting", "гостевые публикации"),
    ("Link diversity", "разнообразие ссылок"),
    ("Natural links", "естественные ссылки"),
    ("Link-worthy content", "контент, достойный ссылок"),
    ("Directory listings", "листинги в каталогах"),
    ("Internal linking", "внутренние ссылки"),
    ("Broken links", "битые ссылки"),
  ],
  "Метрики и аналитика": [
    ("Organic traffic", "органический трафик"),
    ("Click-through rate (CTR)", "рейтинг кликов"),
    ("Conversion rate", "конверсия"),
    ("Bounce rate", "показатель отказов"),
    ("Ranking fluctuations", "колебания позиций"),
    ("Organic visibility", "видимость в органике"),
    ("Rich snippets", "расширенные сниппеты"),
    ("Featured snippets", "featured-сниппеты"),
    ("Mobile conversion rate", "конверсия с мобильных"),
    ("Forecasting accuracy", "точность прогнозирования"),
    ("Data accuracy", "точность данных"),
    ("Performance tracking", "отслеживание производительности"),
  ],
  "Международное SEO": [
    ("Global SEO", "глобальное SEO"),
    ("International markets", "международные рынки"),
    ("Local business schema", "схема для локального бизнеса"),
    ("Google My Business", "Google Мой бизнес"),
    ("Country-specific sites", "сайты для конкретных стран"),
    ("Region-specific features", "региональные особенности"),
    ("Cross-domain tracking", "кросс-доменное отслеживание"),
  ],
  "E-commerce SEO": [
    ("Product page schema", "схема для товарных страниц"),
    ("Duplicate content", "дублирующийся контент"),
    ("Category pagination", "пагинация категорий"),
    ("Product availability", "доступность товара"),
    ("Shopping feeds", "товарные фиды"),
    ("E-commerce tracking", "отслеживание e-commerce"),
  ],
  "Процессы и стратегия": [
    ("Site migration", "миграция сайта"),
    ("Technical audit", "технический аудит"),
    ("Competitor analysis", "анализ конкурентов"),
    ("Algorithm updates", "алгоритмические обновления"),
    ("Resource allocation", "распределение ресурсов"),
    ("Real-time alerting", "оповещения в реальном времени"),
    ("Automated reports", "автоматизированные отчёты"),
  ],
}
glossary_cards_html = [phrase_card(title, pairs) for title, pairs in glossary.items()]
sec_glossary = section("glossary", "SEO-словарь для отчётов", "по темам — от технических терминов до международного SEO",
                        phrase_grid(glossary_cards_html))

def blank():
    return '<span style="border-bottom:1.5px solid var(--line); display:inline-block; min-width:14ch;">&nbsp;</span>'

cards_data = [
  ("SEO-специалист · Международные проекты", "hreflang, локализация, Европа", '''
    <p><em>Opening:</em> "Hey team, here's my update on our global SEO performance for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I fixed hreflang implementation errors across all international sites."</li>
      <li>"We also localized and optimized meta tags for 20 key pages in the German market."</li>
      <li>"And finally, I ''' + blank() + '''."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've seen a ''' + blank() + '''."</li>
      <li>"Our international click-through rate has improved by 1.2 percentage points."</li>
      <li>"Right now, we're ranking in top 5 for 15+ primary keywords in the European market."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"One thing we're still struggling with is the ''' + blank() + '''."</li>
      <li>"So, for next month, I'm gonna focus on French content localization."</li>
      <li>"We'll also implement local business schema and optimize for Google My Business integration in France."</li>
    </ul>'''),
  ("SEO-специалист · Техническая оптимизация", "crawl errors, schema, indexing", '''
    <p><em>Opening:</em> "Here's a quick update on our technical SEO progress for the last month."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First off, I resolved all critical crawl errors in Google Search Console."</li>
      <li>"We also optimized ''' + blank() + '''."</li>
      <li>"And finally, I implemented proper schema markup for all product categories."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've achieved a ''' + blank() + '''."</li>
      <li>"Our overall indexing rate has improved to 98% across all sites."</li>
      <li>"Right now, we're seeing 40% fewer JavaScript-related crawling issues."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"One challenge is the ''' + blank() + '''."</li>
      <li>"So, I'm gonna implement image lazy loading and CDN optimization next month."</li>
      <li>"We'll also audit and improve our site architecture for better crawl efficiency."</li>
    </ul>'''),
  ("SEO-специалист · Контент и ссылки", "topical authority, backlinks", '''
    <p><em>Opening:</em> "Let me walk you through our content and link-building results for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, we optimized ''' + blank() + '''."</li>
      <li>"We also created and promoted 5 link-worthy research studies."</li>
      <li>"And finally, I secured 8 quality backlinks from industry publications."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've seen a ''' + blank() + ''' for targeted topics."</li>
      <li>"Our domain authority has grown by 2 points this month."</li>
      <li>"Right now, our content is earning 15+ natural links per week."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"We're still struggling with link diversity in the Asian markets."</li>
      <li>"So, I'm gonna launch a guest posting campaign targeting Japanese sites."</li>
      <li>"We'll also optimize ''' + blank() + '''."</li>
    </ul>'''),
  ("SEO-специалист · Аналитика и данные", "gap-анализ, автоматизация отчётов", '''
    <p><em>Opening:</em> "Here's my analytics and performance overview for the last month."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I set up ''' + blank() + '''."</li>
      <li>"We also conducted a comprehensive competitor gap analysis."</li>
      <li>"And finally, I automated the weekly ranking and traffic reports."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've identified 45 new high-value keyword opportunities."</li>
      <li>"Our data accuracy for international markets has improved to 99%."</li>
      <li>"Right now, we're tracking ''' + blank() + '''."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"One issue is tracking cross-device user journeys accurately."</li>
      <li>"So, I'm gonna implement enhanced cross-domain tracking next month."</li>
      <li>"We'll also set up real-time alerting for ''' + blank() + '''."</li>
    </ul>'''),
  ("SEO-специалист · E-commerce проекты", "pagination, rich snippets", '''
    <p><em>Opening:</em> "Quick update on our e-commerce SEO performance for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First off, I optimized ''' + blank() + '''."</li>
      <li>"We also fixed duplicate content issues in category pagination."</li>
      <li>"And finally, I built 12 contextual links from product review sites."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've seen a ''' + blank() + ''' conversions."</li>
      <li>"Our rich snippet coverage has expanded to 60% of product pages."</li>
      <li>"Right now, we're ranking for 200+ new commercial intent keywords."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"We're still struggling with ''' + blank() + '''."</li>
      <li>"So, I'm gonna optimize product image SEO and video markup next month."</li>
      <li>"We'll also implement product availability schema for better CTR."</li>
    </ul>'''),
  ("SEO-специалист · Новые рынки", "локализация, cornerstone-статьи", '''
    <p><em>Opening:</em> "Here's our new markets expansion update for the last month."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I conducted technical SEO audits for 3 new country sites."</li>
      <li>"We also localized and published 15 cornerstone articles for the Brazilian market."</li>
      <li>"And finally, I ''' + blank() + '''."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've achieved ''' + blank() + '''."</li>
      <li>"Our Portuguese content is already driving 500+ monthly organic visits."</li>
      <li>"Right now, we're seeing a 4% conversion rate from the new market."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"The main challenge is the ''' + blank() + '''."</li>
      <li>"So, I'm gonna focus on local PR and relationship building next month."</li>
      <li>"We'll also optimize for region-specific search features and local directory listings."</li>
    </ul>'''),
  ("SEO-специалист · Ребилдинг и миграции", "301-редиректы, стабилизация позиций", '''
    <p><em>Opening:</em> "Let me update you on our site migration progress for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I planned and executed the technical migration of the Spanish subdomain."</li>
      <li>"We also preserved and redirected all existing backlinks to new URLs."</li>
      <li>"And finally, I updated ''' + blank() + '''."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've recovered ''' + blank() + '''."</li>
      <li>"Our keyword rankings have stabilized faster than expected."</li>
      <li>"Right now, we're seeing improved crawling efficiency on the new setup."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"We're still monitoring some ranking fluctuations for long-tail keywords."</li>
      <li>"So, I'm gonna continue detailed ''' + blank() + ''' next month."</li>
      <li>"We'll also optimize the new site structure based on initial data."</li>
    </ul>'''),
  ("SEO-специалист · Мобильная оптимизация", "usability, PWA, mobile CTR", '''
    <p><em>Opening:</em> "Here's our mobile SEO performance report for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First off, I ''' + blank() + '''."</li>
      <li>"We also fixed mobile usability issues across 50+ key pages."</li>
      <li>"And finally, I implemented mobile-specific schema markup."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've seen a ''' + blank() + '''."</li>
      <li>"Our mobile conversion rate has increased by 18% this month."</li>
      <li>"Right now, we're ranking for 150+ new mobile-first keywords."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"One challenge is the high bounce rate on mobile product pages."</li>
      <li>"So, I'm gonna optimize ''' + blank() + '''."</li>
      <li>"We'll also implement progressive web app features for better engagement."</li>
    </ul>'''),
  ("SEO-специалист · Блог и образовательный контент", "guides, партнёрства, topical authority", '''
    <p><em>Opening:</em> "Here's our content and blog performance for the last month."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I optimized ''' + blank() + '''."</li>
      <li>"We also published 8 new comprehensive guides with expert interviews."</li>
      <li>"And finally, I built educational content partnerships with 3 industry experts."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've seen a 35% increase in organic blog traffic."</li>
      <li>"Our blog content now drives ''' + blank() + '''."</li>
      <li>"Right now, we're ranking for 300+ new informational keywords."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"The main challenge is ''' + blank() + '''."</li>
      <li>"So, I'm gonna focus on emerging topics and expert roundups next month."</li>
      <li>"We'll also optimize our content hub structure for better topical authority."</li>
    </ul>'''),
  ("SEO-специалист · Анализ и стратегия", "форкастинг, конкурентная разведка", '''
    <p><em>Opening:</em> "Let me walk you through our strategic SEO insights for [Month]."</p>
    <h5>Key Activities</h5>
    <ul>
      <li>"First, I analyzed ''' + blank() + '''."</li>
      <li>"We also identified 5 new content gap opportunities in emerging markets."</li>
      <li>"And finally, I developed a new link-building strategy based on competitor analysis."</li>
    </ul>
    <h5>Current Metrics</h5>
    <ul>
      <li>"As a result, we've improved our forecasting accuracy to 90%."</li>
      <li>"Our strategic recommendations have led to ''' + blank() + '''."</li>
      <li>"Right now, we're ahead of 3 major industry trends that will impact us next quarter."</li>
    </ul>
    <h5>Next Steps</h5>
    <ul>
      <li>"We need better tools for real-time competitor intelligence."</li>
      <li>"So, I'm gonna implement ''' + blank() + '''."</li>
      <li>"We'll also monitor Google Search status dashboard and adjust our technical SEO priorities accordingly."</li>
    </ul>'''),
]
items = [{"title": t, "sub": s, "body": b} for t, s, b in cards_data]
sec_practice = section("practice", "Практика: 10 карточек", "заполни пропуски своими цифрами и фактами, проговори вслух как настоящий апдейт клиенту",
                        accordion(items))

body = "\n".join([sec_phrases, sec_glossary, sec_practice])

html = page(
    title="Урок 2 — Защищаем отчёты и работу",
    desc="Фразы для презентаций и отчётов клиенту: начало, переходы, успехи, проблемы, планы. Плюс SEO-словарь и 10 практических карточек.",
    brand="Global English · Урок 2",
    eyebrow="Урок 2 из курса «Global English для SEO»",
    h1="Защищаем отчёты и работу",
    lede="Фразы, которые превращают сухие цифры в уверенную презентацию: как начать, как перейти к следующей теме, как подать проблему и как закончить на уверенной ноте.",
    navlinks=[("#phrases","Выражения"), ("#glossary","Словарь"), ("#practice","Практика")],
    body=body,
    prev_href="/lessons/1/", prev_label="← Урок 1: Времена",
    next_href="/lessons/3/", next_label="Урок 3: Сложные ситуации →",
)
write("lessons/2/index.html", html)
