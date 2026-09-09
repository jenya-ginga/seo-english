# -*- coding: utf-8 -*-
from build import page, section, info_card, phrase_card, phrase_grid, compare_card, accordion, table_scroll, write

# ---------------------------------------------------------------------------
# PART 1 — Warm-Up
# ---------------------------------------------------------------------------
warmup_rows = [
    ("So basically / Which means / That's why / On top of that",
     "The page is blocked in robots.txt. _______, Google can't index it.",
     "Страница закрыта в robots.txt. _______, Google не может её индексировать.",
     "That's why"),
    ("So basically / Which means / That's why / On top of that",
     "Traffic dropped 30%. _______ we lost 200 leads this month.",
     "Трафик упал на 30%. _______ мы потеряли 200 лидов.",
     "Which means"),
    ("So basically / Which means / That's why / On top of that",
     "The content is outdated. _______, the site is slow.",
     "Контент устарел. _______, сайт ещё и медленный.",
     "On top of that"),
]

def warmup_card(bank, en, ru, answer):
    return f'''<div class="info-card">
      <div class="info-head"><h3>Fill in the blank<small>вставьте нужную фразу</small></h3></div>
      <p class="idea">Используйте: <strong>So basically</strong> (короче говоря) / <strong>Which means</strong> (а это значит) / <strong>That's why</strong> (вот почему) / <strong>On top of that</strong> (вдобавок)</p>
      <div class="example-block"><span class="en">{en}</span><span class="ru">{ru}</span></div>
      <div class="chips"><span>Ответ: {answer}</span></div>
    </div>'''

warmup_body = "".join(warmup_card(*row) for row in warmup_rows)
sec_warmup = section("warmup", "Warm-Up", "5 минут — вставьте нужную связку в пропуск",
                      f'<div class="accordion-grid">{warmup_body}</div>')

# ---------------------------------------------------------------------------
# PART 2A — Semantic SEO Vocabulary (15 terms)
# ---------------------------------------------------------------------------
def def_cell(en, ru):
    return f'<span class="en">{en}</span><span class="ru-sub">{ru}</span>'

semantic_terms = [
    (True, "Topical Authority", "тематический авторитет", "ТОП-икл о-ТОР-ити",
     "Being seen as an expert on a whole topic — achieved by deep content coverage + historical data",
     "Статус эксперта по целой теме — достигается глубиной контента и историческими данными (трафик, CTR, обновления)",
     '"We need topical authority on \'car loans\' — not just one article."'),
    (True, "Topical Drift (Content Drift)", "", "ТОП-икл дрифт",
     "When a page starts ranking for topics it wasn't written for — a mismatch between content and actual clicks",
     "Когда страница начинает ранжироваться по темам, для которых не писалась — несоответствие контента реальным запросам",
     '"Our sports bar page ranks for \'pizza near me\' — that\'s topical drift."'),
    (True, "ABC Framework", "", "эй-би-си ФРЕЙМворк",
     "A = Anchors (incoming link text), B = Body (page content), C = Clicks (real GSC queries). Drift = mismatch between them.",
     "A = Анкоры (текст входящих ссылок), B = Тело страницы (контент), C = Клики (реальные запросы из GSC). Дрейф = несоответствие между ними.",
     '"Check ABC: A says \'sports bar\', B says \'sports bar\', C says \'pizza\' — that\'s drift."'),
    (True, "SILO Structure", "СИЛО-структура", "САЙ-ло",
     "Organizing a site into tightly related topic clusters — each cluster stays within its theme",
     "Организация сайта в тематически связанные кластеры — каждый кластер остаётся в рамках своей темы",
     '"The \'mortgages\' SILO should only link within itself — not to car loans."'),
    (True, "Cosine Similarity", "косинусное сходство", "КОЗ-айн си-МИЛ-ар-ити",
     "A score (0–1) measuring how semantically close two pieces of content are. &gt;0.85 = one article; 0.75–0.85 = separate articles in same SILO; &lt;0.65 = different topics",
     "Оценка (0–1) семантической близости двух текстов. &gt;0.85 = одна статья; 0.75–0.85 = разные статьи в одном SILO; &lt;0.65 = разные темы",
     '"Cosine is 0.88 — keep it as one page. Cosine 0.72 — split into two."'),
    (True, "Query Fan-Out", "веер запросов", "КВИА-ри фэн-аут",
     "Breaking one main topic into 10–50 sub-queries covering all user intentions. How AI systems plan their answers.",
     "Разбивка одной темы на 10–50 под-запросов, покрывающих все намерения пользователей. Так ИИ-системы планируют ответы.",
     '"Run a fan-out on \'car insurance\' — find all sub-intents before writing."'),
    (True, "Sub-intent", "под-интент", "саб-ин-ТЕНТ",
     "A specific user goal within a broader topic. One page = one sub-intent.",
     "Конкретная цель пользователя внутри более широкой темы. Одна страница = один под-интент.",
     '"\'How to get a car loan with bad credit\' — that\'s a sub-intent of \'car loans\'."'),
    (True, "Named Entity", "именованная сущность", "НЕЙмд ЭН-тити",
     "A real-world object with a unique name: person, brand, place, product. Google understands these through Knowledge Graph.",
     "Объект реального мира с уникальным именем: человек, бренд, место, продукт. Google распознаёт их через Knowledge Graph.",
     '"Dr. Sarah Lee, cardiologist — that\'s a named entity with real E-E-A-T value."'),
    (False, "Pillar Page", "хаб-страница", "ПИЛ-ёр пейдж",
     "The main broad page on a topic — links out to all cluster pages. Hub of the SILO.",
     "Главная широкая страница по теме — ссылается на все страницы кластера. Хаб SILO.",
     '"The pillar page on \'mortgages\' links to all subtopic pages."'),
    (False, "Topic Cluster", "тематический кластер", "ТОП-ик КЛАС-тёр",
     "A pillar page + all related sub-pages covering one topic area",
     "Pillar-страница + все связанные подстраницы, покрывающие одну тематическую область",
     '"We have a topic cluster on \'car finance\' — 1 pillar + 8 sub-pages."'),
    (False, "SDI Score", "СДИ-скор", "эс-ди-ай",
     "Semantic Drift Index: 60% Semantic + 30% Link + 10% Engagement. Measures how much a page has drifted from its intended topic.",
     "Индекс семантического дрейфа: 60% Семантика + 30% Ссылки + 10% Вовлечённость. Измеряет насколько страница ушла от темы.",
     '"SDI score is high — the page has significant topical drift."'),
    (False, "UMAP", "ЮМАП-карта", "ю-МЭП",
     "A visual map showing how pages are semantically connected. Isolated page on UMAP = structural drift.",
     "Визуальная карта семантических связей страниц. Изолированная страница на UMAP = структурный дрейф.",
     '"That page is isolated on UMAP — it needs internal links from semantic neighbors."'),
    (False, "E-E-A-T", "", "и-и-эй-ти",
     "Experience, Expertise, Authoritativeness, Trustworthiness — Google's content quality criteria. Critical for YMYL topics.",
     "Опыт, Экспертиза, Авторитетность, Доверие — критерии качества контента Google. Критичны для YMYL-тематик.",
     '"We need E-E-A-T signals: named author, credentials, date, sources."'),
    (False, "Knowledge Graph", "граф знаний", "НОЛ-идж граф",
     "Google's database of real-world entities and how they relate to each other. Powers AI answers and Knowledge Panels.",
     "База данных Google о реальных сущностях и их связях. Питает ИИ-ответы и панели знаний.",
     '"If your brand is in the Knowledge Graph, Google trusts it more."'),
]

def term_rows(terms):
    rows = []
    for star, term_en, term_ru, pron, def_en, def_ru, example in terms:
        prefix = "★ " if star else ""
        name_cell = f"{prefix}{term_en}"
        if term_ru:
            name_cell += f'<span class="ru-sub">{term_ru}</span>'
        rows.append([name_cell, pron, def_cell(def_en, def_ru), example])
    return rows

sec_semantic = section("semantic-vocab", "Semantic SEO Vocabulary", "12 минут — 15 терминов, ★ = приоритетный термин",
                        table_scroll(["Термин", "Произношение", "Определение", "Пример"], term_rows(semantic_terms)))

# ---------------------------------------------------------------------------
# PART 2B — GEO Vocabulary (11 terms)
# ---------------------------------------------------------------------------
geo_terms = [
    (True, "GEO", "", "джи-и-оу",
     "Optimizing content so AI systems (ChatGPT, Perplexity, Google AI) cite you as a source",
     "Оптимизация контента, чтобы ИИ-системы ссылались на вас как на источник",
     '"We need GEO — our competitor is cited in every AI answer."'),
    (True, "AI Overview", "", "эй-ай о-вью",
     "The AI-generated answer Google shows above all search results",
     "Блок с ИИ-ответом, который Google показывает над всей выдачей",
     '"We got a citation in the AI Overview — that\'s our GEO win."'),
    (True, "EAV Triplet", "EAV-триплет", "и-эй-ви",
     'Entity + Attribute + Value — the content structure AI reads best. Ex: "Perplexity — type — answer engine"',
     'Сущность + Атрибут + Значение — структура контента, которую ИИ читает лучше всего. Пример: «Perplexity — тип — ответный поисковик»',
     '"Write in EAV: not \'great tool\' but \'Tool X reduces reporting time by 8h/month for agencies with 20+ clients\'."'),
    (True, "Passage-level optimization", "", "пэ-сидж лев-ел",
     "Each paragraph is self-sufficient — AI can quote it without reading the whole article",
     "Каждый абзац самодостаточен — ИИ может процитировать его без контекста всей статьи",
     '"This paragraph has no EAV — AI can\'t quote it. Rewrite it."'),
    (True, "Citation", "цитата/источник", "сай-тей-шн",
     "A clickable link to your page inside an AI answer — the main KPI of GEO",
     "Кликабельная ссылка на вашу страницу внутри ИИ-ответа — главный KPI GEO",
     '"We got 3 citations in Perplexity this month — up from zero."'),
    (False, "RAG", "", "рэг",
     "Retrieval-Augmented Generation: AI searches sources first, then writes an answer based on them",
     "Генерация с поиском: ИИ сначала ищет источники, затем пишет ответ на их основе",
     '"Google uses RAG — it pulls from real pages, not just training data."'),
    (False, "LLM", "", "эл-эл-эм",
     "Large Language Model — AI that reads text and generates answers (GPT-5, Gemini, Claude)",
     "Большая языковая модель — ИИ, который читает текст и генерирует ответы",
     '"The LLM cited our article. That means our passage-level structure worked."'),
    (False, "AI Visibility", "АИ-видимость", "эй-ай виз-и-бил-ити",
     "How often your brand appears in AI answers — new SEO KPI alongside rankings",
     "Как часто ваш бренд появляется в ответах ИИ — новый SEO KPI рядом с позициями",
     '"Our AI visibility went from 3% to 18% share of voice."'),
    (False, "Citability", "цитируемость", "сай-та-БИЛ-ити",
     "How likely AI is to quote your content. Improved by facts, numbers, named entities, EAV structure.",
     "Насколько вероятно, что ИИ процитирует контент. Повышается через факты, числа, именованные сущности, EAV.",
     '"Low citability = no numbers, no entities. Add stats and named sources."'),
    (False, "Freshness Signal", "сигнал свежести", "фреш-нес СИГ-нал",
     "Date content was last updated — AI prefers fresh sources, especially for fast-changing topics",
     "Дата последнего обновления контента — ИИ предпочитает свежие источники, особенно по быстро меняющимся темам",
     '"Update the article date and add 2026 statistics — freshness signal matters."'),
]

sec_geo = section("geo-vocab", "GEO Vocabulary", "8 минут — 11 терминов Generative Engine Optimization",
                   table_scroll(["Термин", "Произношение", "Определение", "Пример"], term_rows(geo_terms)))

# ---------------------------------------------------------------------------
# PART 3 — How to Explain It
# ---------------------------------------------------------------------------
explain_cards = [
    info_card(
        "What is Topical Authority?", "читаем вслух → закрываем → пересказываем", "01", "",
        "\"Here's the thing — Google doesn't just rank individual pages. It ranks sites that demonstrate deep expertise on a whole topic. Which means if you write 20 articles about car loans — all well-structured, regularly updated, with real data — Google starts to trust you as an authority on that topic. That's topical authority. And that's why we build SILO structures, not just individual pages.\"",
        "«Вот в чём дело — Google ранжирует не просто отдельные страницы. Он ранжирует сайты, которые демонстрируют глубокую экспертизу по всей теме. А это значит, если вы написали 20 статей про автокредиты — все хорошо структурированные, регулярно обновляемые, с реальными данными — Google начинает доверять вам как эксперту в этой теме. Это и есть topical authority. И вот почему мы строим SILO-структуры, а не просто отдельные страницы.»",
        [],
    ),
    info_card(
        "What is Topical Drift and how do you catch it?", "читаем вслух → закрываем → пересказываем", "02", "",
        "\"So basically, topical drift is when a page starts attracting queries it wasn't written for. We use the ABC framework to catch it: A is Anchors — the text of links pointing to the page; B is Body — the actual content; C is Clicks — real queries from Google Search Console. If C doesn't match B, you have drift. For example, a page about 'sports bars' that gets clicks for 'pizza near me'. That's drift. Which means we either fix the content or create a new page for that topic.\"",
        "«Короче говоря, topical drift — это когда страница начинает привлекать запросы, для которых она не писалась. Мы используем ABC-фреймворк чтобы это поймать: A — Анкоры (тексты ссылок на страницу); B — Тело (реальный контент); C — Клики (реальные запросы из GSC). Если C не совпадает с B — у вас дрейф. Например, страница про «спортивные бары» получает клики по «пицца рядом». Это дрейф. А это значит, нам нужно либо починить контент, либо создать новую страницу под этот топик.»",
        [],
    ),
    info_card(
        "What is GEO and how is it different from SEO?", "читаем вслух → закрываем → пересказываем", "03", "",
        "\"GEO stands for Generative Engine Optimization. To be clear, it's not replacing SEO — it's an extra layer. With SEO, you want to rank on page one. With GEO, you want AI systems like ChatGPT or Google AI Overviews to cite your content in their answers. The thing is, AI doesn't click links — it reads paragraphs and quotes the most factual, structured ones. That's why we write in EAV format: Entity, Attribute, Value — like 'Tool X reduces reporting time by 8 hours for agencies with 20+ clients'. That's citable. Vague text like 'great for teams' is not.\"",
        "«GEO расшифровывается как Generative Engine Optimization. Если говорить прямо, это не замена SEO — это дополнительный уровень. В SEO вы хотите попасть на первую страницу. В GEO вы хотите чтобы ИИ-системы типа ChatGPT или Google AI Overviews цитировали ваш контент в своих ответах. Дело в том, что ИИ не кликает по ссылкам — он читает абзацы и цитирует самые фактурные, структурированные. Вот почему мы пишем в формате EAV: Сущность, Атрибут, Значение — например «Инструмент X сокращает время отчётности на 8 часов для агентств с 20+ клиентами». Это цитируемо. Расплывчатый текст типа «отлично для команд» — нет.»",
        [],
    ),
]
sec_explain = section("explain", "How to Explain It", "8 минут — три объяснения EN+RU, читаем вслух, закрываем, пересказываем",
                       f'<div class="accordion-grid">{"".join(explain_cards)}</div>')

# ---------------------------------------------------------------------------
# PART 4 — Client Questions
# ---------------------------------------------------------------------------
def client_body(client_en, client_ru, hint_en, hint_ru):
    return f'''
    <span class="tag-role">Client</span>
    <blockquote class="script">{client_en}</blockquote>
    <div class="example-block"><span class="ru">{client_ru}</span></div>
    <h5>Hint</h5>
    <div class="example-block"><span class="en">{hint_en}</span><span class="ru">{hint_ru}</span></div>'''

client_questions = [
    dict(title="Rankings aren't growing", sub="#1 · много контента, нет роста", body=client_body(
        '"We publish a lot of content but our rankings don\'t grow. Why?"',
        "Мы публикуем много контента, но позиции не растут. Почему?",
        "Talk about topical authority, SILO structure, and depth vs. quantity.",
        "Говорите про topical authority, SILO-структуру и глубину vs. количество.")),
    dict(title="Wrong visitors suddenly", sub="#2 · страница ушла в дрейф", body=client_body(
        '"One of our pages suddenly started attracting completely wrong visitors. What happened?"',
        "Одна из наших страниц вдруг начала привлекать совершенно не тех посетителей. Что произошло?",
        "Explain topical drift using the ABC framework — anchors, body, clicks.",
        "Объясните topical drift через ABC-фреймворк — анкоры, тело страницы, клики.")),
    dict(title="Not appearing in AI answers", sub="#3 · нет видимости в ChatGPT/Google AI", body=client_body(
        '"We don\'t appear in ChatGPT or Google AI answers. How do we fix that?"',
        "Нас нет в ответах ChatGPT или Google AI. Как это исправить?",
        "Explain GEO, EAV structure, passage-level optimization, and citability.",
        "Объясните GEO, EAV-структуру, оптимизацию на уровне абзацев и цитируемость.")),
    dict(title="Do we need a SILO?", sub="#4 · сомнения в структуре", body=client_body(
        '"What is a SILO and do we really need one?"',
        "Что такое SILO и нам это действительно нужно?",
        "Explain SILO as topic clusters with a pillar page + internal linking. Mention cosine similarity.",
        "Объясните SILO как тематические кластеры с pillar-страницей + внутренняя перелинковка. Упомяните cosine similarity.")),
    dict(title="What is E-E-A-T?", sub="#5 · как улучшить доверие", body=client_body(
        '"What is E-E-A-T and how do we improve it?"',
        "Что такое E-E-A-T и как его улучшить?",
        "Experience, Expertise, Authoritativeness, Trustworthiness — give 2–3 specific examples.",
        "Опыт, Экспертиза, Авторитетность, Доверие — приведите 2–3 конкретных примера.")),
    dict(title="Competitor ranks higher with less", sub="#6 · короткие статьи, но выше в топе", body=client_body(
        '"Our competitor writes shorter articles but ranks higher. How is that possible?"',
        "Конкурент пишет короткие статьи, но ранжируется выше. Как это возможно?",
        "Talk about topical authority, EAV structure, passage-level quality, and citability.",
        "Говорите про topical authority, EAV-структуру, качество абзацев и цитируемость.")),
]
sec_client = section("client-questions", "Client Questions", "1.5 минуты на человека — выбери вопрос, ответь вслух как реальному клиенту",
                      accordion(client_questions, first_open=False))

# ---------------------------------------------------------------------------
# Phrase Bank
# ---------------------------------------------------------------------------
phrase_pairs = [
    ("So basically,", "короче говоря"),
    ("Which means", "а это значит"),
    ("Here's the thing —", "вот в чём дело"),
    ("To be clear,", "если говорить прямо"),
    ("That's why", "вот почему"),
    ("Honestly,", "честно говоря"),
    ("On top of that,", "вдобавок к этому"),
    ("Think of it as...", "представьте это как..."),
]
sec_phrases = section("phrase-bank", "Phrase Bank", "8 связок для explain-мода",
                       phrase_grid([phrase_card("Связки для объяснений", phrase_pairs)]))

# ---------------------------------------------------------------------------
# PART 6 — Quick Review
# ---------------------------------------------------------------------------
review_rows = [
    ["Topical Drift", "Страница ушла в запросы, для которых не писалась", "B"],
    ["ABC Framework", "Анкоры + Тело + Клики — три сигнала для диагностики дрейфа", "C"],
    ["SILO", "Организация сайта в связанные тематические кластеры", "A"],
    ["Cosine Similarity", "Мера семантической близости двух текстов (0–1)", "D"],
    ["Query Fan-Out", "Разбивка темы на 10–50 под-запросов", "E"],
]
sec_review = section("quick-review", "Quick Review", "2 минуты — соедините термин с определением",
                      table_scroll(["Термин", "Определение", "Ответ"], review_rows))

# ---------------------------------------------------------------------------
body = "\n".join([sec_warmup, sec_semantic, sec_geo, sec_explain, sec_client, sec_phrases, sec_review])

html = page(
    title="Урок 12 — Semantic SEO + GEO практика",
    desc="Практика по Semantic SEO и GEO: 24 термина, три готовых объяснения клиенту, 6 клиентских вопросов для отработки вслух и quick review.",
    brand="Global English · Урок 12",
    eyebrow="Урок 12 из курса «Global English для SEO»",
    h1="Semantic SEO & GEO: практика и мануалы",
    lede="Полный словарь Semantic SEO и GEO, три готовых объяснения для клиента (topical authority, topical drift, GEO vs SEO) и шесть реальных клиентских вопросов — отвечаем вслух, без подготовки.",
    navlinks=[
        ("#semantic-vocab", "Semantic SEO"),
        ("#geo-vocab", "GEO"),
        ("#explain", "Как объяснить"),
        ("#client-questions", "Вопросы клиента"),
        ("#phrase-bank", "Фразы"),
        ("#quick-review", "Проверка"),
    ],
    body=body,
    prev_href="/lessons/11/", prev_label="← Урок 11: Словарик",
    next_href="/lessons/13/", next_label="Урок 13: Rendering & Page Speed →",
)
write("lessons/12/index.html", html)
