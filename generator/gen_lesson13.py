# -*- coding: utf-8 -*-
from build import page, section, info_card, phrase_card, phrase_grid, compare_card, accordion, table_scroll, write

# ---------------------------------------------------------------------------
# PART 1 — Warm-Up
# ---------------------------------------------------------------------------
warmup_qs = [
  ("What tool do you use to check page speed?", "Каким инструментом вы проверяете скорость страницы?"),
  ("What does LCP stand for? What's the target?", "Как расшифровывается LCP? Какое целевое значение?"),
  ("Can Googlebot always see JavaScript content? Why?", "Может ли Googlebot всегда видеть JS-контент? Почему?"),
  ("What's the difference between robots.txt and Basic Auth?", "В чём разница между robots.txt и Basic Auth?"),
]
warmup_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Diagnostic questions<small>отвечайте быстро — без подготовки</small></h3><span class="chip">⏱ 5 минут</span></div>
  <p class="idea">Не переживайте, если не можете ответить — к концу урока вы будете знать все ответы.</p>
</div>
{phrase_grid([phrase_card("Отвечайте вслух", warmup_qs)])}'''
sec_warmup = section("warmup", "Part 1 · Warm-Up", "разминка — 5 минут", warmup_body)

# ---------------------------------------------------------------------------
# PART 2A — Rendering & Core Web Vitals vocabulary
# ---------------------------------------------------------------------------
def term_row(star, term, pron, en, ru, ex):
    t = f"★ {term}" if star else term
    return (t, pron, en, ru, f'<span class="en">{ex}</span>')

cwv_rows = [
  term_row(True, "Core Web Vitals (CWV)", "кор веб ВАЙ-тлз",
    "Google's three main page experience metrics: LCP + CLS + INP. Bad CWV = lower rankings.",
    "Три главные метрики пользовательского опыта от Google: LCP + CLS + INP. Плохой CWV = более низкие позиции.",
    "&laquo;Our CWV is poor — that's hurting rankings on mobile.&raquo;"),
  term_row(True, "LCP — Largest Contentful Paint", "эл-си-пи",
    "Time until the main content (hero image / headline) loads. Target: under 2.5 seconds.",
    "Время до загрузки основного контента (главное изображение / заголовок). Цель: до 2.5 секунд.",
    "&laquo;LCP is 4.1s — above the 2.5s threshold. That costs us rankings.&raquo;"),
  term_row(True, "CLS — Cumulative Layout Shift", "си-эл-эс",
    "How much the page content shifts/jumps while loading. Target: below 0.1.",
    "Насколько сильно контент страницы смещается при загрузке. Цель: менее 0.1.",
    "&laquo;Buttons jump when ads load. CLS is 0.32 — that's poor.&raquo;"),
  term_row(True, "INP — Interaction to Next Paint", "ай-эн-пи",
    "How fast the page reacts when a user clicks, taps or types. Target: under 200ms.",
    "Скорость реакции страницы на клик, нажатие или ввод. Цель: менее 200 мс.",
    "&laquo;The filter takes 1.5s to respond. INP is critical — users leave.&raquo;"),
  term_row(False, "FCP — First Contentful Paint", "эф-си-пи",
    "When the first piece of content (any text or image) appears on screen.",
    "Момент когда первый контент (любой текст или изображение) появляется на экране.",
    "&laquo;FCP is 3.2s — users see a blank screen for too long.&raquo;"),
  term_row(True, "Rendering", "рен-дер-инг",
    "Turning HTML/CSS/JavaScript into what you see on screen. Googlebot renders pages separately from users.",
    "Превращение HTML/CSS/JavaScript в то, что видит пользователь. Googlebot рендерит страницы отдельно от пользователей.",
    "&laquo;The page renders fine in Chrome but Googlebot can't see the menu.&raquo;"),
  term_row(True, "CRP — Critical Rendering Path", "си-ар-пи",
    "The steps browser takes before showing content. Scripts in &lt;head&gt; block this path.",
    "Шаги браузера до отображения контента. Скрипты в &lt;head&gt; блокируют этот путь.",
    "&laquo;Scripts in &lt;head&gt; block the CRP. Add defer — it fixes FCP immediately.&raquo;"),
  term_row(True, "async / defer", "эй-синк / ди-фёр",
    "HTML attributes that allow scripts to load without blocking the page. async = independent; defer = runs after HTML is parsed.",
    "Атрибуты HTML, позволяющие скриптам загружаться без блокировки. async = независимый; defer = запускается после разбора HTML.",
    "&laquo;Add defer to all non-critical scripts. Fixes CRP immediately.&raquo;"),
  term_row(True, "DOM — Document Object Model", "ди-оу-эм",
    "The page structure after JavaScript runs — what the user and browser see. Different from raw HTML source.",
    "Структура страницы после выполнения JavaScript — то, что видит пользователь и браузер. Отличается от исходного HTML.",
    "&laquo;F12 shows the DOM — after JS. Ctrl+U shows raw HTML — before JS.&raquo;"),
  term_row(True, "JavaScript rendering", "джа-ва-скрипт рен-дер-инг",
    "Content built by JavaScript after page load. Risk: Googlebot sees JS content with a delay — hours to weeks after first crawl.",
    "Контент, построенный через JavaScript после загрузки. Риск: Googlebot видит, но с задержкой от часов до недель.",
    "&laquo;Product titles load via JS — AI sees an empty container.&raquo;"),
  term_row(False, "PageSpeed Insights", "пейдж-спид ин-сайтс",
    "Google's free tool to measure CWV — both lab data (Lighthouse) and field data (CrUX).",
    "Бесплатный инструмент Google для измерения CWV — лабораторные данные (Lighthouse) и полевые данные (CrUX).",
    "&laquo;Run PSI first. Compare to the competitor — then prioritize fixes.&raquo;"),
  term_row(False, "Crawl Budget", "кроул бад-жет",
    "How many pages Googlebot crawls per day. Large sites with thin/duplicate content waste crawl budget.",
    "Сколько страниц Googlebot обходит за день. Крупные сайты с тонким/дублирующим контентом тратят бюджет впустую.",
    "&laquo;50,000 pages, crawl budget 500/day — we need to prioritize key pages.&raquo;"),
]
cwv_table = table_scroll(
  ["Term", "Произношение", "Definition (EN)", "Перевод (RU)", "Example"],
  cwv_rows,
)
cwv_body = f'''
<div class="note">★ = самые важные для клиентских звонков и технических обсуждений</div>
{cwv_table}'''
sec_cwv = section("terms-cwv", "Part 2A · Rendering & Core Web Vitals", "словарь — 10 минут", cwv_body)

# ---------------------------------------------------------------------------
# PART 2B — Technical SEO vocabulary
# ---------------------------------------------------------------------------
tech_rows = [
  term_row(True, "robots.txt", "РО-ботс.тиэксти",
    "A file that tells Googlebot which pages NOT to crawl. Does NOT hide pages from Google index.",
    "Файл, который говорит Googlebot какие страницы НЕ обходить. НЕ скрывает страницы от индекса Google.",
    "&laquo;robots.txt blocks crawling — but the page can still be indexed from external links.&raquo;"),
  term_row(True, "Basic Auth", "бей-сик от",
    "Password protection on a server level — completely blocks Googlebot. Use for staging/test sites.",
    "Парольная защита на уровне сервера — полностью блокирует Googlebot. Используется для тестовых сайтов.",
    "&laquo;Use Basic Auth for staging — not robots.txt. It actually blocks access.&raquo;"),
  term_row(True, "301 Redirect", "три-ноль-один ри-ди-рект",
    "Permanent redirect — tells Google and users that a page has moved. Passes most link equity.",
    "Постоянный редирект — говорит Google и пользователям что страница переехала. Передаёт большую часть ссылочного веса.",
    "&laquo;Add 301 redirects for all old URLs after the domain migration.&raquo;"),
  term_row(False, "Canonical Tag (канонический тег)", "ка-НОН-икл тэг",
    "An HTML tag pointing to the preferred version of a page. Prevents duplicate content issues.",
    "HTML-тег, указывающий на предпочтительную версию страницы. Предотвращает проблемы с дублирующим контентом.",
    "&laquo;Set canonical to the main URL — remove duplicates from the index.&raquo;"),
  term_row(False, "Sitemap (карта сайта)", "САЙТ-мэп",
    "An XML file listing all pages you want Google to crawl and index. Submit in GSC.",
    "XML-файл со списком всех страниц, которые вы хотите чтобы Google обходил и индексировал. Отправляется через GSC.",
    "&laquo;Ping the sitemap after domain migration: google.com/ping?sitemap=URL&raquo;"),
  term_row(False, "Schema Markup (Schema-разметка)", "СКИ-ма МАР-кап",
    "Structured data code (JSON-LD) telling Google what the page is about. Enables rich snippets and AI answers.",
    "Код структурированных данных (JSON-LD), сообщающий Google что на странице. Включает расширенные сниппеты и ИИ-ответы.",
    "&laquo;Add FAQ schema — it improves chances of appearing in AI Overviews.&raquo;"),
  term_row(False, "Reverse DNS Lookup", "ри-вёрс ди-эн-эс",
    "Checking if an IP address truly belongs to Googlebot. Real Googlebot resolves to googlebot.com",
    "Проверка принадлежит ли IP-адрес реальному Googlebot. Настоящий Googlebot разрешается в googlebot.com",
    "&laquo;Suspicious crawler from that IP? Run reverse DNS — verify it's real Googlebot.&raquo;"),
]
tech_body = table_scroll(
  ["Term", "Произношение", "Definition (EN)", "Перевод (RU)", "Example"],
  tech_rows,
)
sec_tech = section("terms-technical", "Part 2B · Technical SEO Vocabulary", "быстрый обзор — 6 минут", tech_body)

# ---------------------------------------------------------------------------
# PART 3 — How to Explain It
# ---------------------------------------------------------------------------
explain_body = f'''
{info_card(
  "Why does page speed affect Google rankings?",
  "Почему скорость страницы влияет на позиции в Google?",
  "⏱ 6 минут",
  "Читаем вслух → закрываем → пересказываем.",
  "Here&rsquo;s the thing — Google measures three things called Core Web Vitals: LCP, CLS, and INP. These are user experience scores. So basically, if your main content takes more than 2.5 seconds to load — that&rsquo;s poor LCP. Which means Google gives your page a lower performance score. And that can cost you 5&ndash;10 positions on competitive queries. That&rsquo;s why fixing page speed isn&rsquo;t just a developer task — it&rsquo;s an SEO priority.",
  "Вот в чём дело — Google измеряет три показателя, которые называются Core Web Vitals: LCP, CLS и INP. Это оценки пользовательского опыта. Короче говоря, если основной контент загружается дольше 2.5 секунд — это плохой LCP. А это значит, Google даёт странице низкий performance score. Это может стоить 5&ndash;10 позиций на конкурентных запросах. Вот почему улучшение скорости — это не только задача разработчика, это SEO-приоритет.",
  ["Core Web Vitals", "LCP", "performance score", "SEO priority"],
)}
{info_card(
  "Why can&rsquo;t robots.txt fully hide a test site from Google?",
  "Почему robots.txt не может полностью скрыть тестовый сайт от Google?",
  "⏱ 6 минут",
  "Читаем вслух → закрываем → пересказываем.",
  "Actually, robots.txt only blocks crawling — it doesn&rsquo;t hide the page. The thing is, if someone links to your staging site, Google can still see that the URL exists. I mean, it might even show up in search results as an empty snippet. That&rsquo;s why we use Basic Auth instead. It&rsquo;s server-level password protection — Googlebot literally cannot access the page at all.",
  "На самом деле, robots.txt только блокирует обход — он не скрывает страницу. Дело в том, что если кто-то ссылается на ваш тестовый сайт, Google всё равно видит что URL существует. То есть он может даже появиться в поиске как пустой сниппет. Вот почему мы используем Basic Auth. Это парольная защита на уровне сервера — Googlebot буквально не может войти.",
  ["robots.txt", "Basic Auth", "staging site", "server-level protection"],
)}'''
sec_explain = section("explain", "Part 3 · How to Explain It", "как объяснить клиенту простыми словами — 6 минут", explain_body)

# ---------------------------------------------------------------------------
# PART 4 — Dialogue Practice
# ---------------------------------------------------------------------------
dialogue_rows = [
  ("CLIENT", "", "The site is slow but I don&rsquo;t know where to start.",
   "Сайт медленный, не знаю с чего начать."),
  ("YOU", "good", "Let&rsquo;s start with the CRP — the Critical Rendering Path. Basically, scripts in the &lt;head&gt; block the browser from showing content. Which means users see a blank screen while scripts load.",
   "Начнём с CRP — Critical Rendering Path. По сути, скрипты в &lt;head&gt; блокируют браузер от отображения контента. А это значит — пользователи видят пустой экран пока скрипты грузятся."),
  ("CLIENT", "", "What do I do with the scripts?",
   "Что делать со скриптами?"),
  ("YOU", "good", "Add async or defer to all non-critical scripts. That way the browser doesn&rsquo;t wait for them. On top of that, check if you actually need all your third-party scripts — some analytics tags alone add 500ms.",
   "Добавьте async или defer ко всем некритичным скриптам. Так браузер не будет их ждать. Вдобавок проверьте нужны ли все сторонние скрипты — некоторые теги аналитики сами по себе добавляют 500 мс."),
  ("CLIENT", "", "The content on product pages loads via JavaScript. Is that a problem?",
   "Контент на страницах продуктов загружается через JavaScript. Это проблема?"),
  ("YOU", "good", "Honestly, yes. Googlebot sees the raw HTML first — before JavaScript runs. I mean, if product titles and descriptions load via JS, Google might index an empty page. Check it with View Page Source — if the text isn&rsquo;t there, that&rsquo;s our problem.",
   "Честно говоря, да. Googlebot сначала видит исходный HTML — до выполнения JavaScript. То есть если заголовки и описания продуктов загружаются через JS, Google может проиндексировать пустую страницу. Проверьте через View Page Source — если текста нет, это наша проблема."),
]
dialogue_body = f'''
<div class="note">Диалог — разговор с разработчиком об оптимизации скриптов. 3 минуты чтение + 4 минуты ролевая игра.</div>
{compare_card(dialogue_rows)}
<div class="info-card" style="margin-top:16px;">
  <div class="info-head"><h3>2-phase model<small>двухфазная модель индексации JS-контента</small></h3></div>
  <p class="idea">Волна 1 — Google видит raw HTML. Волна 2 — WRS (Web Rendering Service) рендерит JavaScript, иногда с задержкой от часов до недель.</p>
  <div class="chips"><span>Wave 1 — raw HTML</span><span>Wave 2 — WRS renders JS</span></div>
</div>'''
sec_dialogue = section("dialogue", "Part 4 · Dialogue Practice", "практика диалога — 7 минут", dialogue_body)

# ---------------------------------------------------------------------------
# PART 5 — Client Questions
# ---------------------------------------------------------------------------
def qa(title, ru, en_q, bullets):
    li = "".join(f"<li>{b}</li>" for b in bullets)
    return {
      "title": title,
      "sub": ru,
      "body": f'''<blockquote class="script">&laquo;{en_q}&raquo;</blockquote>
      <h5>Ключевые пункты ответа</h5>
      <ul>{li}</ul>'''
    }

questions = [
  qa("Q1. Does site speed actually hurt rankings?",
     "Все говорят что наш сайт медленный. Это реально влияет на позиции в Google?",
     "Everyone says our site is slow. Does that actually hurt our Google rankings?",
     ["Да, скорость — официальный фактор с 2021 года (Core Web Vitals)",
      "Главная метрика: LCP ≤ 2.5 сек",
      "Ещё: CLS (смещение контента) и INP (отзывчивость)",
      "Если конкуренты быстрее — у них прямое преимущество"]),
  qa("Q2. How do we keep a test site out of Google?",
     "У нас есть тестовая версия сайта — как сделать чтобы Google её не проиндексировал?",
     "We have a test version of the site — how do we make sure Google doesn&rsquo;t index it?",
     ["robots.txt — не защита: страница остаётся публичной, Google может найти через внешние ссылки",
      "Basic Auth — закрывает на уровне сервера, Googlebot физически не получит контент",
      "noindex без Basic Auth тоже ненадёжно"]),
  qa("Q3. Developer says fast, PageSpeed says slow — who&rsquo;s right?",
     "Разработчик говорит что сайт грузится быстро, но Google PageSpeed говорит медленно. Кто прав?",
     "Our developer says the site loads fast — but Google PageSpeed says it&rsquo;s slow. Who&rsquo;s right?",
     ["Разработчик меряет на мощном ПК — это не реальность пользователя",
      "PageSpeed симулирует слабый мобильный (Moto G4, медленный 4G)",
      "Важнее всего CrUX — реальные данные пользователей за 28 дней",
      "Googlebot = Headless Chromium, меряет LCP, не просто FCP"]),
  qa("Q4. New CMS, broken features — what do we do?",
     "Мы перешли на новую CMS, но часть функционала перестала работать. Что делать?",
     "We launched on a new CMS but some features stopped working. What do we do?",
     ["Сначала оцениваем: критично ли это для SEO и конверсий",
      "Если нет — запускаемся, фиксируем как задачу после переезда",
      "Если да — откладываем запуск до восстановления",
      "В любом случае: тимлид и аккаунт-менеджер должны быть в курсе сразу"]),
  qa("Q5. How do we protect a staging site from indexing?",
     "Как защитить тестовый сайт от индексации Google?",
     "How do we protect a staging site from being indexed by Google?",
     ["Basic Auth — единственный надёжный способ: блокирует на уровне сервера",
      "robots.txt — только рекомендация боту, страница остаётся публичной",
      "noindex без Basic Auth — ненадёжно: Google может найти страницу через внешние ссылки"]),
  qa("Q6. Domain migration — what&rsquo;s the correct sequence?",
     "Мы переехали на новый домен. Какова правильная последовательность действий?",
     "We migrated to a new domain. What&rsquo;s the correct sequence?",
     ["6 шагов: GSC → canonical (группа со ссылками) → canonical (прочие) → canonical (с трафиком) → 301-редиректы через 2 недели → серверный редирект",
      "После запуска: ping sitemap через google.com/ping?sitemap=URL"]),
  qa("Q7. PageSpeed shows bad metrics — where do we start?",
     "PageSpeed показывает плохие метрики. С чего начать диагностику?",
     "PageSpeed shows bad metrics. Where do we start diagnosing?",
     ["Берём нашу медленную страницу + аналогичную страницу конкурента",
      "Прогоняем обе через WebPageTest на мобильном профиле",
      "В водопаде ищем: блокирующие скрипты в &lt;head&gt;, тяжёлые сторонние скрипты, высокий TTFB"]),
  qa("Q8. How do we check JS content is visible to Googlebot?",
     "Как проверить что JavaScript-контент виден Googlebot?",
     "How do we check that JavaScript content is visible to Googlebot?",
     ["GSC → Inspect URL → View Crawled Page → смотрим скриншот",
      "Если блоки есть в браузере но нет в GSC-версии — проблема рендеринга",
      "Дополнительно: Screaming Frog с JS-рендерингом"]),
  qa("Q9. Canonical is set — but does Googlebot actually see it?",
     "Canonical-тег прописан — но мы не уверены что Googlebot его видит.",
     "Our canonical tag is set — but we&rsquo;re not sure Googlebot actually sees it.",
     ["Ctrl+U (View Page Source) = исходный HTML до JS — это видит Googlebot при первом проходе",
      "F12 = DOM после JS — это видит пользователь",
      "Если canonical только в JS — Googlebot может не увидеть его до рендеринга",
      "Проверить финально: GSC → Inspect URL"]),
  qa("Q10. New CMS — what must be in the technical requirements?",
     "Мы переходим на новую CMS. Что обязательно должно быть в техническом задании?",
     "We&rsquo;re moving to a new CMS. What must be in the technical requirements?",
     ["Обязательно: сохранение URL-структуры, 301-редиректы, перенос Title/H1/Description, robots.txt, sitemap.xml, SSL, мобильная адаптация",
      "Не входит в этот этап: новый дизайн, дополнительная оптимизация скорости, Schema — если не было раньше"]),
]
questions_body = f'''
<div class="note">Каждый выбирает один вопрос и отвечает НА АНГЛИЙСКОМ, как будто разговаривает с реальным клиентом (60&ndash;90 секунд на человека).</div>
{accordion(questions, first_open=False)}'''
sec_questions = section("questions", "Part 5 · Client Questions", "отвечаем клиенту — 8 минут", questions_body)

# ---------------------------------------------------------------------------
body = "\n".join([sec_warmup, sec_cwv, sec_tech, sec_explain, sec_dialogue, sec_questions])

html = page(
    title="Урок 13 — Rendering & Page Speed + Technical SEO",
    desc="Core Web Vitals, rendering, robots.txt vs Basic Auth, редиректы и миграции — словарь и практика для разговоров с разработчиком и клиентом на технические темы.",
    brand="Global English · Урок 13",
    eyebrow="Урок 13 из курса «Global English для SEO»",
    h1="Rendering & Page Speed + Technical SEO",
    lede="Core Web Vitals, критический путь рендеринга, robots.txt против Basic Auth и правильная последовательность миграции — как объяснять это разработчику и клиенту на английском, без путаницы в терминах.",
    navlinks=[
      ("#warmup", "Warm-Up"),
      ("#terms-cwv", "CWV словарь"),
      ("#terms-technical", "Technical SEO"),
      ("#explain", "Как объяснить"),
      ("#dialogue", "Диалог"),
      ("#questions", "Вопросы клиента"),
    ],
    body=body,
    prev_href="/lessons/12/", prev_label="← Урок 12: Semantic SEO + GEO",
    next_href="/lessons/14/", next_label="Урок 14: Допродажа →",
)
write("lessons/13/index.html", html)
