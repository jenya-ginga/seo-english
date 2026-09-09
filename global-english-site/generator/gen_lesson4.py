# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, accordion, table_scroll, write

terms_body = phrase_grid([
  phrase_card("Работа с графиками", [
    ("Clicks", "клики"), ("Impressions", "показы"), ("CTR (Click-Through Rate)", "рейтинг кликов"),
    ("Average position", "средняя позиция"), ("Search queries", "поисковые запросы"),
  ]),
  phrase_card("Динамика изменений", [
    ("Traffic increased / dropped by X%", "трафик вырос / упал на X%"),
    ("Rankings improved / declined", "позиции улучшились / ухудшились"),
    ("Fluctuations", "колебания"), ("Spike", "резкий скачок вверх"),
    ("Drop / Dip", "резкое падение"), ("Plateau", "плато, стабилизация"), ("Trend", "тренд, тенденция"),
  ]),
  phrase_card("Описание графиков", [
    ("The line shows…", "линия показывает…"), ("We can see a spike on…", "мы видим скачок на…"),
    ("There's a downward trend…", "есть нисходящий тренд…"), ("The data indicates…", "данные указывают на…"),
    ("Sharp increase / decrease", "резкий рост / падение"), ("Gradual growth", "постепенный рост"),
    ("Steady decline", "стабильное снижение"),
  ]),
  phrase_card("Термины Google Search Console", [
    ("Total clicks / impressions", "всего кликов / показов"), ("Average CTR / position", "средний CTR / средняя позиция"),
    ("Previous period", "предыдущий период"), ("28 days vs previous 28 days", "28 дней против предыдущих 28 дней"),
    ("Year-over-year", "год к году"), ("Queries tab / Pages tab", "вкладка запросов / страниц"),
    ("Search appearance", "вид в поиске"), ("Date range", "период дат"),
  ]),
  phrase_card("Термины Rush Analytics (Rank Tracking)", [
    ("Current / previous position", "текущая / предыдущая позиция"), ("Search volume", "частотность запроса"),
    ("Position change", "изменение позиции"), ("URL ranking", "URL, который ранжируется"),
    ("↑13 (up 13) / ↓7 (down 7)", "вырос / упал на 13 / 7 позиций"),
    ("Moved from position X to Y", "переместился с позиции X на Y"),
    ("Gained / lost positions", "набрал / потерял позиции"),
  ]),
  phrase_card("Страницы в отчётах", [
    ("Top pages", "топовые страницы"), ("Growing pages", "растущие страницы"),
    ("Declining pages", "падающие страницы"), ("New entries", "новые вхождения в топ"),
    ("Dropped out", "выпали из топа"),
  ]),
])
sec_terms = section("terms", "Часть 1–3 · Основные термины", "графики, Google Search Console, Rush Analytics",
                     terms_body)

phrases_body = phrase_grid([
  phrase_card("Начало презентации", [
    ("Let me walk you through the data…", "Позвольте провести вас по данным…"),
    ("Here's what we're seeing in the console…", "Вот что мы видим в консоли…"),
    ("Let's break down the numbers…", "Давайте разберём цифры…"),
    ("Looking at the graph…", "Глядя на график…"),
  ]),
  phrase_card("Описание роста", [
    ("We're seeing strong growth in clicks…", "Мы видим сильный рост в кликах…"),
    ("Impressions are up by 40%…", "Показы выросли на 40%…"),
    ("Rankings improved across the board…", "Позиции улучшились по всем направлениям…"),
    ("There's a clear upward trend…", "Есть чёткий восходящий тренд…"),
    ("We're gaining traction on…", "Мы набираем обороты по…"),
  ]),
  phrase_card("Описание падения", [
    ("We saw a dip on [date]…", "Мы увидели падение [дата]…"),
    ("Traffic dropped temporarily…", "Трафик временно упал…"),
    ("There's a decline in positions for…", "Есть снижение позиций для…"),
    ("We lost some ground on…", "Мы потеряли немного позиций по…"),
    ("Rankings took a hit due to…", "Позиции пострадали из-за…"),
  ]),
  phrase_card("Объяснение причин", [
    ("This spike was caused by…", "Этот скачок был вызван…"),
    ("The algorithm update affected…", "Обновление алгоритма повлияло на…"),
    ("Seasonal trends show that…", "Сезонные тренды показывают, что…"),
    ("The drop correlates with…", "Падение коррелирует с…"),
  ]),
  phrase_card("Сравнение периодов", [
    ("Compared to last month…", "По сравнению с прошлым месяцем…"),
    ("This is a 30% increase from…", "Это рост на 30% от…"),
    ("We're outperforming the previous period…", "Мы превосходим предыдущий период…"),
    ("Year-over-year, we're up by…", "Год к году мы выросли на…"),
  ]),
])
sec_phrases = section("phrases", "Часть 4 · Фразы для объяснения графиков", "начало → рост → падение → причины → сравнение",
                       phrases_body)

formula_body = ''.join(
    f'''<div class="info-card"><div class="info-head"><h3>{i+1}. {name}<small>{sub}</small></h3></div><div class="chips">{"".join(f"<span>{p}</span>" for p in phrs)}</div></div>'''
    for i, (name, sub, phrs) in enumerate([
        ("Overview", "общая картина", ["Looking at the last 28 days…", "Overall, we're seeing…", "The main trend is…"]),
        ("Details", "конкретные цифры", ["Specifically, clicks went from X to Y…", "We gained 13 positions on this keyword…", "This page increased traffic by…"]),
        ("Insights", "что это значит", ["This indicates that…", "What this means is…", "The reason behind this is…"]),
        ("Action", "что делаем дальше", ["Moving forward, we'll…", "To build on this, we're…", "Our next step is…"]),
    ])
)
sec_formula = section("formula", "Часть 5 · Структура объяснения", "формула Overview → Details → Insights → Action — держит любой отчёт по графику собранным",
                       formula_body)

practice_body = '''
<div class="info-card">
  <div class="info-head"><h3>Персональные карточки<small>4 скриншота на каждого специалиста</small></h3></div>
  <p class="idea">Возьми 4 своих скриншота из реального проекта: 1) график динамики (28 дней в сравнении с предыдущими 28), 2) страницы с ростом, 3) страницы с падением, 4) проверка позиций по ключевым словам.</p>
  <p class="idea">Составь устный отчёт по формуле <strong>Overview → Details → Insights → Action</strong> — вслух, как будто отчитываешься перед клиентом на созвоне.</p>
</div>'''
sec_practice = section("practice", "Часть 6 · Практика", "разбор своих реальных скриншотов — приноси на встречу",
                        practice_body)

cheat_body = phrase_grid([
  phrase_card("Блок 1 · Overview (график)", [
    ("Looking at the last 28 days…", "Глядя на последние 28 дней…"),
    ("Total clicks are [число] / Impressions are [число]", "Всего кликов / показов [число]"),
    ("Up / down by [X]%", "Рост / падение на X%"),
    ("The trend is upward / downward", "Тренд восходящий / нисходящий"),
    ("There was a spike / dip on day [X]", "Был скачок / падение в день X"),
    ("Performance is stable", "Показатели стабильны"),
  ]),
  phrase_card("Блок 2 · Growing pages", [
    ("Now let's look at the pages performing well…", "Теперь давайте посмотрим на страницы, которые работают хорошо…"),
    ("[Page name] gained [X] clicks", "[Название] набрала X кликов"),
    ("This represents a [Z]% increase", "Это представляет рост на Z%"),
    ("This is our star performer", "Это наш звёздный исполнитель"),
    ("Massive jump in traffic", "Массивный скачок трафика"),
  ]),
  phrase_card("Блок 3 · Declining pages", [
    ("On the flip side…", "С другой стороны…"),
    ("[Page name] lost [X] clicks", "[Название] потеряла X кликов"),
    ("This page took a hit", "Эта страница пострадала"),
    ("Due to algorithm updates / technical issues", "Из-за обновлений алгоритма / технических проблем"),
    ("We're actively addressing this by…", "Мы активно занимаемся этим через…"),
    ("We'll refresh the content", "Мы обновим контент"),
  ]),
  phrase_card("Блок 4 · Rankings", [
    ("Keyword \"[name]\" moved from position [X] to [Y]", "Ключевое слово переместилось с позиции X на Y"),
    ("We gained / lost [X] positions", "Мы набрали / потеряли X позиций"),
    ("Jumped from [X] to [Y] / Climbed [X] spots", "Подскочили с X до Y / Поднялись на X мест"),
    ("This is a high-volume keyword", "Это высокочастотный ключ"),
    ("We broke into top 10", "Мы прорвались в топ-10"),
  ]),
  phrase_card("Блок 5 · Insights & Action", [
    ("What this data tells us is…", "То, что эти данные говорят нам…"),
    ("Our strategy is working", "Наша стратегия работает"),
    ("We're building momentum", "Мы набираем импульс"),
    ("Moving forward, we'll focus on…", "В дальнейшем мы сосредоточимся на…"),
    ("Create more content for [topic] / Build quality backlinks", "Создать больше контента для [тема] / Построить качественные ссылки"),
    ("Fix technical issues / Maintain these positions", "Исправить технические проблемы / Сохранить эти позиции"),
  ]),
])
sec_cheat = section("cheatsheet", "Шпаргалка по блокам", "5 блоков — от общей картины до плана действий", cheat_body)

key_body = phrase_grid([
  phrase_card("✅ Для роста", [
    ("Strong growth", "сильный рост"), ("We gained [X] positions", "мы набрали X позиций"),
    ("Traffic increased", "трафик вырос"), ("Up by [X]%", "рост на X%"),
    ("Jumped from X to Y", "подскочили с X до Y"), ("We're dominating", "мы доминируем"),
    ("Star performer", "звёздный исполнитель"), ("Massive increase", "массивный рост"),
  ]),
  phrase_card("⚠️ Для падения", [
    ("Lost [X] clicks", "потеряли X кликов"), ("Traffic dropped", "трафик упал"),
    ("Down by [X]%", "падение на X%"), ("This decline correlates with…", "это снижение связано с…"),
    ("We're addressing this", "мы занимаемся этим"), ("Took a hit", "пострадала"), ("Lost some ground", "потеряли позиции"),
  ]),
  phrase_card("📊 Для графиков", [
    ("Spike / Dip", "скачок вверх / падение"), ("Upward / downward trend", "восходящий / нисходящий тренд"),
    ("Fluctuations", "колебания"), ("Stable", "стабильно"), ("Peak", "пик"), ("Plateau", "плато"),
  ]),
])
sec_key = section("keyphrases", "Ключевые фразы с переводом", "три словаря, которые перекрывают почти весь разговор о цифрах",
                   key_body)

body = "\n".join([sec_terms, sec_phrases, sec_formula, sec_practice, sec_cheat, sec_key])

html = page(
    title="Урок 4 — Explaining Charts & Rankings",
    desc="Как объяснять графики Google Search Console и позиций: термины, фразы про рост и падение, формула Overview → Details → Insights → Action.",
    brand="Global English · Урок 4",
    eyebrow="Урок 4 из курса «Global English для SEO»",
    h1="Explaining Charts & Rankings",
    lede="Как объяснять графики консоли и позиций клиенту вслух: термины, фразы для роста и падения, формула Overview → Details → Insights → Action.",
    navlinks=[("#terms","Термины"), ("#phrases","Фразы"), ("#formula","Формула"), ("#cheatsheet","Шпаргалка"), ("#keyphrases","Ключевые фразы")],
    body=body,
    prev_href="/lessons/3/", prev_label="← Урок 3: Сложные ситуации",
    next_href="/lessons/5/", next_label="Урок 5: Real Conversations →",
)
write("lessons/4/index.html", html)
