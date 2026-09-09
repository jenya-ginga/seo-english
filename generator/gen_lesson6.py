# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, write

terms_body = phrase_grid([
  phrase_card("GEO — Generative Engine Optimization", [
    ("We're optimizing for AI Overviews now.", "Мы сейчас оптимизируем под AI Overviews."),
    ("Our content is GEO-ready.", "Наш контент готов для GEO."),
    ("We're targeting LLMs, not just Google.", "Мы таргетируемся на LLM, не только на Google."),
  ]),
  phrase_card("Semantic SEO", [
    ("We work with entities, not just keywords.", "Мы работаем с сущностями, а не просто ключевыми словами."),
    ("We're building topical authority.", "Мы строим тематический авторитет."),
    ("Our strategy covers the entire knowledge graph.", "Наша стратегия покрывает весь граф знаний."),
  ]),
  phrase_card("Entity-Based SEO", [
    ("Entity clustering", "кластеризация сущностей"), ("Semantic relevance", "семантическая релевантность"),
    ("Cosine similarity", "косинусная схожесть"), ("Knowledge Graph", "граф знаний"),
    ("Topical coverage", "тематическое покрытие"),
  ]),
  phrase_card("AI & Voice Search Optimization", [
    ("Voice search ready", "готово для голосового поиска"), ("Featured snippets", "избранные сниппеты"),
    ("AI-generated answers", "ответы, сгенерированные AI"), ("Conversational queries", "разговорные запросы"),
  ]),
])
sec_terms = section("terms", "GEO & Semantic SEO термины", "современный словарь: сущности, граф знаний, AI Overviews",
                     terms_body)

examples_body = '''
<div class="info-card">
  <div class="info-head"><h3>Отчёт клиенту</h3></div>
  <div class="example-block"><span class="en">We've shifted our strategy to semantic SEO. Instead of targeting individual keywords, we're building topical authority around your core product. This means we're optimizing for Google AND all major LLMs like ChatGPT and Claude. Your content will appear in AI Overviews, voice search results, and featured snippets.</span></div>
</div>
<div class="info-card">
  <div class="info-head"><h3>Объяснение подхода</h3></div>
  <div class="example-block"><span class="en">We're working with entities — actual concepts that Google's Knowledge Graph recognizes. We measure cosine similarity between topics to ensure semantic relevance. This approach future-proofs your SEO for generative AI.</span></div>
</div>
<div class="info-card">
  <div class="info-head"><h3>Внутренняя встреча</h3></div>
  <div class="example-block"><span class="en">Our topical coverage is at 75% for the main cluster. We need to fill content gaps to achieve full topical authority. I'm mapping out the entity relationships now.</span></div>
</div>'''
sec_examples = section("examples", "Примеры использования", "три ситуации — три регистра одной и той же идеи", examples_body)

geo_questions = [
  "What is Generative Engine Optimization (GEO) and how is it different from traditional SEO?",
  "Why is GEO so important for modern digital marketing?",
  "How can GEO help my business improve visibility in search engines and get more traffic?",
  "Which specific AI systems and answer engines does GEO target, and why is this important?",
  "How does GEO work, and how can we measure the success of our GEO efforts?",
  "What types of content and strategies are most effective for GEO?",
  "How can we ensure our content is cited and used as a source in AI systems and answer engines?",
  "How will GEO impact our existing SEO strategy, and how do we integrate it smoothly?",
  "What tools and methods can we use to track and analyze our GEO progress?",
  "How can we ensure our GEO strategy aligns with Google and Bing's guidelines?",
  "How can we adapt our GEO strategy for different languages and regions?",
  "What challenges and risks might arise when implementing GEO, and how do we overcome them?",
  "How can we study competitors' successes in GEO and apply that to our own strategy?",
  "How can we ensure our GEO strategy is future-proof and resilient to change?",
  "What is the main goal of Generative Engine Optimization (GEO)?",
  "How does GEO differ from traditional SEO in terms of content structure?",
  "What role does semantic analysis play in GEO?",
  "How do generative search engines evaluate the authority of a website?",
  "What are the key factors that influence a website's visibility in AI-driven search results?",
  "What are the best practices for creating content optimized for GEO?",
  "How can we monitor and measure the effectiveness of our GEO efforts?",
  "How can we leverage GEO to improve our brand's reputation online?",
]
q_html = "".join(f"<li>{q}</li>" for q in geo_questions)
practice_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Продай мне доп по GEO<small>ты — эксперт, преподаватель — клиент</small></h3></div>
  <p class="idea">Объясни клиенту, что такое GEO, в чём ценность, что он получит. Клиент задаёт вопросы из списка ниже (или свои) — отвечай вслух, без подготовки.</p>
</div>
<div class="phrase-card"><h4>Вопросы, которые может задать клиент</h4><ol style="margin:0; padding-left:20px; font-size:14.5px; color:var(--ink-soft); display:grid; gap:8px;">{q_html}</ol></div>'''
sec_practice = section("practice", "Практика", "продай GEO как апсейл — клиент атакует вопросами", practice_body)

body = "\n".join([sec_terms, sec_examples, sec_practice])

html = page(
    title="Урок 6 — GEO & Semantic SEO термины",
    desc="Словарь по GEO, Semantic SEO и Entity-Based SEO. Примеры для отчёта клиенту, объяснения подхода и внутренней встречи. Практика — продай GEO клиенту.",
    brand="Global English · Урок 6",
    eyebrow="Урок 6 из курса «Global English для SEO»",
    h1="GEO & Semantic SEO термины",
    lede="Как говорить о сущностях, графе знаний и AI Overviews так, чтобы клиент понял ценность, а не решил, что это баззворды.",
    navlinks=[("#terms","Термины"), ("#examples","Примеры"), ("#practice","Практика")],
    body=body,
    prev_href="/lessons/5/", prev_label="← Урок 5: Real Conversations",
    next_href="/lessons/7/", next_label="Урок 7: Role Play →",
)
write("lessons/6/index.html", html)
