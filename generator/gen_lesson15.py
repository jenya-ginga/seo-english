# -*- coding: utf-8 -*-
from build import page, section, info_card, phrase_card, phrase_grid, compare_card, accordion, table_scroll, write

def defcell(en, ru):
    return f'<span style="display:block; font-family:var(--serif); font-style:italic; font-size:14.5px; line-height:1.5;">{en}</span><span class="ru-sub" style="font-size:12.5px; margin-top:6px;">{ru}</span>'

def termcell(term, priority=False):
    star = '★ ' if priority else ''
    cls = ' class="strong-cell"' if priority else ''
    return f'<td{cls}>{star}{term}</td>'

TERMS = [
  ("Satellite site", "сэтелайт сайт",
   "A standalone site, not disclosed as connected to the main one, built to rank on its own for a related query and send traffic (and sometimes link equity) to the money site.",
   "Отдельный сайт, формально не раскрытый как связанный с основным; сам ранжируется по смежному запросу и направляет трафик (иногда и ссылочный вес) на money site.",
   "“Our satellite ranks for &lsquo;antarctica cruise reviews&rsquo; on its own — it&rsquo;s not just a link donor.”", True),
  ("Money site", "мани сайт",
   "The main commercial site that a satellite or network is built to support.",
   "Основной коммерческий сайт, ради которого строится сателлит или сеть.",
   "“The satellite eventually sends traffic and trust signals to the money site.”", True),
  ("PBN (Private Blog Network)", "пи-би-эн",
   "A network of low-content &ldquo;feeder&rdquo; sites whose only purpose is to pass backlink equity to one target. Unlike a satellite, a PBN node isn&rsquo;t built to rank or get real traffic on its own.",
   "Сеть сайтов-«доноров» с минимальным контентом, единственная цель которых — передать ссылочный вес на одну цель. В отличие от сателлита, узел PBN не рассчитан на собственное ранжирование или реальный трафик.",
   "“Don&rsquo;t confuse the two: a PBN node exists only to pass link juice, our satellite exists to rank and convert on its own.”", False),
  ("Buffer site / sacrificial site", "буфер сайт / прокладка",
   "A site deliberately exposed to higher-risk or more aggressive tactics so that the money site (or the client relationship) is insulated from the fallout if it gets caught.",
   "Сайт, который намеренно подставляется под более рискованные/агрессивные методы, чтобы money site не пострадали, если его поймают.",
   "“Before we push an aggressive tactic, we test it on a buffer site first, not on anything the client can see as &lsquo;theirs.&rsquo;”", False),
  ("Footprint", "футпринт",
   "A technical trace (shared hosting, template, registrar, author bios, etc.) that links sites in a network together.",
   "Технический «след» (общий хостинг, шаблон, регистратор, авторы), по которому можно связать сайты сети друг с другом.",
   "“Same IP range and same theme — that&rsquo;s a classic footprint.”", True),
  ("Doorway pages / multi-domain doorway pattern", "дорвей-паттерн",
   "Google&rsquo;s term for multiple domains or pages — often near-duplicate — that funnel users toward the same destination without adding unique value.",
   "Термин Google для нескольких доменов или страниц (часто почти идентичных), которые направляют пользователей к одной и той же цели без уникальной ценности.",
   "“If we run five ranking sites in the same niche that all point to the same client, that starts to look like a doorway pattern.”", True),
  ("Link schemes / link spam policy", "линк-скемс",
   "Google&rsquo;s policy against any links placed specifically to manipulate rankings — including undisclosed affiliate/sponsored links and coordinated networks like PBNs.",
   "Политика Google против ссылок, размещенных специально для манипуляции ранжированием — включая нераскрытые партнёрские/спонсорские ссылки и скоординированные сети типа PBN.",
   "“A dofollow link to the same company from ten &lsquo;independent&rsquo; sites is exactly what the link spam policy targets.”", True),
  ("Site reputation abuse", "сайт репьютейшн эбьюз",
   "Google&rsquo;s term for hosting third-party content on an already-authoritative, existing domain mainly to rank it (aka &ldquo;parasite SEO&rdquo;). Requires an established host — does not apply to a fresh site you build yourself.",
   "Термин Google для размещения стороннего контента на уже авторитетном существующем домене ради ранжирования («parasite SEO»). Требует раскрученного хоста — не применяется к новому сайту, который вы строите сами.",
   "“CNN hosting a coupon subdomain is site reputation abuse. A brand-new ranking site we build from scratch is not — different risk, different name.”", False),
  ("Scaled content abuse", "сколд контент эбьюз",
   "Google&rsquo;s policy against generating many pages or sites mainly to manipulate rankings, with little added value for users — regardless of whether it&rsquo;s human- or AI-written.",
   "Политика Google против генерации большого числа страниц/сайтов преимущественно для манипуляции ранжированием без пользы для пользователя — независимо от способа написания.",
   "“Running near-identical ranking sites across a dozen niches is a scaled content abuse risk, not just a link risk.”", False),
  ("Undisclosed commercial relationship", "нераскрытая коммерческая связь",
   "Presenting a commercially-linked site or review as independent without disclosing the relationship. A consumer-protection issue (e.g. FTC-style endorsement rules), separate from Google&rsquo;s algorithmic risk.",
   "Представление коммерчески связанного сайта или обзора как независимого без раскрытия связи. Это уже не про алгоритмы Google, а про право потребителей на честную рекламу.",
   "“Even if Google never finds the footprint, an undisclosed paid relationship is a separate legal exposure.”", False),
  ("Co-citation", "коу-сайтейшн",
   "A brand being mentioned alongside other authoritative sources across independent pages.",
   "Совместное упоминание бренда рядом с другими авторитетными источниками на разных независимых страницах.",
   "“More co-citation across independent sites builds topical trust.”", False),
  ("Entity consolidation", "энтити консолидейшн",
   "Merging scattered signals about a brand into one recognizable entity in the knowledge graph.",
   "Объединение разрозненных сигналов о бренде в единую узнаваемую сущность в графе знаний.",
   "“Multiple sites reinforcing the same facts help with entity consolidation.”", False),
  ("Brand saturation", "брэнд сатурейшн",
   "Artificially flooding the information space with repeated brand mentions. (Informal industry term — not an official Google or LLM-provider policy label.)",
   "Искусственное «перенасыщение» инфополя повторяющимися упоминаниями бренда. (Разговорный термин индустрии, не официальное название политики.)",
   "“AI Overviews picked up on the brand saturation across the network.”", False),
  ("AI citation", "эй-ай сайтейшн",
   "A mention or link to a source inside an AI-generated answer (ChatGPT, AI Overviews, Perplexity).",
   "Упоминание или ссылка на источник внутри ответа, сгенерированного AI-системой.",
   "“We&rsquo;re seeing more AI citations since we diversified our sources.”", True),
  ("De-index / Penalize", "ди-индекс / пенэлайз",
   "To remove a site from the index, or lower its rankings, for violating guidelines.",
   "Удалить сайт из индекса или понизить его в результатах за нарушение правил.",
   "“Half the network got de-indexed within a month.”", False),
]

term_rows = []
for term, pron, en_def, ru_def, ex, priority in TERMS:
    star = '★ ' if priority else ''
    cls = ' class="strong-cell"' if priority else ''
    term_html = f'<td{cls}>{star}{term}</td>'
    pron_html = f'<td>{pron}</td>'
    def_html = f'<td>{defcell(en_def, ru_def)}</td>'
    ex_html = f'<td style="font-family:var(--serif); font-style:italic; font-size:14px; color:var(--ink-soft);">{ex}</td>'
    term_rows.append(f'<tr>{term_html}{pron_html}{def_html}{ex_html}</tr>')

terms_table = f'''<div class="table-scroll"><table><thead><tr>
  <th>Term</th><th>Произношение</th><th>Definition (EN) / Перевод (RU)</th><th>Example</th>
</tr></thead><tbody>{"".join(term_rows)}</tbody></table></div>
<p class="note">★ = самые важные для клиентских звонков и технических обсуждений</p>'''

sec_terms = section("terms", "Часть 1 · Satellite & Network Vocabulary", "словарь: 14 терминов, приоритетные — под ★ (15 мин)", terms_table)


# ---------------------------------------------------------------- PART 2
llm_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Как сети сателлитов пытаются влиять на ответы LLM</h3></div>
  <div class="example-block">
    <span class="en">LLMs and AI Overviews tend to weight how often — and how independently — a brand appears to be mentioned across the web. A satellite tries to simulate that independence by ranking on its own, under its own identity, while repeating brand mentions that eventually favor the money site.</span>
    <span class="ru">LLM и AI Overviews часто оценивают, насколько часто — и насколько «независимо» — упоминается бренд по всему интернету. Сателлит пытается сымитировать эту независимость, сам ранжируясь под собственным именем, при этом продвигая упоминания, которые в итоге выгодны money site.</span>
  </div>
  <div class="example-block">
    <span class="en">This is the same underlying mechanism we saw in the Reddit case in Lesson 10 — repeated, distributed mentions can look like consensus. This is a correlation observed in current industry studies, not a confirmed causal mechanism — strong brands may simply earn both mentions and citations independently.</span>
    <span class="ru">Это тот же механизм, что мы разбирали в кейсе про Reddit в Уроке 10 — распределённые повторяющиеся упоминания могут выглядеть как консенсус. Это корреляция, которую фиксируют текущие индустриальные исследования, а не подтверждённый причинный механизм — сильные бренды могут просто одновременно получать и упоминания, и цитирования по независимым причинам.</span>
  </div>
</div>
<div class="note warn">Важно: это наблюдаемая корреляция из индустриальных исследований, а не подтверждённая причинно-следственная связь. Не выдавайте это клиенту за гарантированный механизм.</div>'''

sec_llm = section("llm", "Часть 2 · How Satellite Networks Try to Influence LLM Answers", "корреляция с кейсом Reddit из Урока 10 — не подтверждённая причинность (7 мин)", llm_body)


# ---------------------------------------------------------------- PART 3 (internal only)
internal_body = f'''
<div class="note warn">Внутренний контекст: как реально устроена наша модель сателлитов — рассказываем команде, в переводе. Только для команды — не для клиента.</div>
<div class="info-card">
  <div class="info-head"><h3>Как мы продаём<small>цена, гарантированная функция</small></h3></div>
  <p class="idea">Сателлит продаётся за $250 «как есть» (as is). Гарантированная функция одна — техническая передача ссылочного веса на money site клиента. Всё остальное — позиции, трафик, попадание в AI-ответы — не гарантируется и не входит в стоимость.</p>
</div>
<div class="info-card">
  <div class="info-head"><h3>Почему это нужно проговаривать явно, а не как «бонус»<small>формулировка на звонке</small></h3></div>
  <p class="idea">Практика показывает: если на звонке сказать «трафик/показы/нейронки — это приятный бонус», клиент слышит это как часть пакета, а не как опцию. При цене $250 подписываться под топ по оговорённым ключам мы не можем — значит, при продаже это нужно называть прямо не гарантируемым, а не бонусом, и дублировать письменно после звонка.</p>
</div>
<div class="info-card">
  <div class="info-head"><h3>Почему сателлит может умереть быстрее, чем клиент ожидает<small>buffer / прокладка</small></h3></div>
  <p class="idea">Помимо обычной алгоритмической непредсказуемости Google (см. Часть 2), у части сателлитов есть дополнительный источник риска: они используются как buffer / прокладка — площадка, на которой тестируются более агрессивные методы, прежде чем (или вместо того, чтобы) применять их напрямую на активах, которые клиент видит как «свои». Если такой метод попадает под спам-детекцию, страдает прокладка, а не money site клиента и не репутация аккаунта.</p>
</div>'''

sec_internal = section("internal", "Часть 3 · Что стоит за моделью продажи (только для команды)", "не проговаривается клиенту в этом виде — внутренний контекст модели", internal_body)


# ---------------------------------------------------------------- PART 4
client_body = f'''
<div class="info-card">
  <div class="info-head"><h3>Объективное описание тактики<small>что можно сказать клиенту прямо</small></h3></div>
  <div class="example-block">
    <span class="en">&ldquo;A satellite is basically a separate site that ranks on its own and, underneath, is set up to send trust and traffic back to your main domain.&rdquo;</span>
    <span class="ru">— Сателлит — это, по сути, отдельный сайт, который сам ранжируется, а под капотом настроен так, чтобы направлять доверие и трафик на ваш основной домен.</span>
  </div>
  <div class="example-block">
    <span class="en">&ldquo;In theory, it can create the impression of an independent, third-party recommendation.&rdquo;</span>
    <span class="ru">— В теории это может создать впечатление независимой рекомендации от третьей стороны.</span>
  </div>
</div>
<div class="info-card">
  <div class="info-head"><h3>Продажа сателлита за $250: как говорить про то, что не входит в пакет<small>отдельная, более частая ситуация, чем role play ниже</small></h3></div>
  <p class="idea">Клиент покупает сателлит именно как ссылочный актив, а не как инструмент против конкурента.</p>
  <div class="note warn">Не говорить: «трафик/показы/нейронки — это приятный бонус». Слово «бонус» клиент слышит как часть пакета.</div>
  <p class="idea" style="margin-top:16px;"><strong>Говорить — до называния цены:</strong></p>
  <div class="example-block"><span class="ru">«Сателлит за $250 продаётся как есть — его гарантированная функция одна: он технически передаёт ссылочный вес на ваш основной сайт. Больше мы гарантировать не можем в принципе — по этой цене это невозможно.»</span></div>
  <p class="idea" style="margin-top:16px;"><strong>Говорить — если клиент сам спрашивает про трафик/топ/нейронки:</strong></p>
  <div class="example-block"><span class="ru">«Иногда сателлит начинает и сам получать трафик, попадать в топ или всплывать в ответах нейросетей — но мы не можем на это подписаться и не выбираем, у кого из сателлитов это случится. Это не входит в стоимость и не является тем, что вы покупаете.»</span></div>
</div>'''

sec_client = section("client", "Часть 4 · Explaining This to a Client", "честная формулировка риска и того, что не входит в пакет за $250 (10 мин)", client_body)


# ---------------------------------------------------------------- PART 5 (role play)
def rp_item(num, ru_title, client_en, client_ru, spec_en, spec_ru):
    body = f'''<ul class="phrase-list">
      <li><span class="tag-role">клиент</span><br><span class="en">{client_en}</span><span class="ru">— {client_ru}</span></li>
      <li><span class="tag-role">специалист</span><br><span class="en">{spec_en}</span><span class="ru">— {spec_ru}</span></li>
    </ul>'''
    return dict(title=f"{num}. {ru_title}", sub="", body=body)

rp_items = [
  rp_item(1, "Клиент хочет гарантии в договоре",
    "&ldquo;Let&rsquo;s just put it in the contract — top 3 rankings within 90 days.&rdquo;",
    "Давайте просто пропишем в договоре — топ-3 за 90 дней.",
    "&ldquo;I can&rsquo;t put a ranking guarantee in writing — no one legitimately can. What I can commit to in writing is the link transfer and build quality.&rdquo;",
    "Я не могу прописать гарантию позиций — никто честно не может. Что я могу прописать — это передачу ссылочного веса и качество сборки."),
  rp_item(2, "Клиент хочет масштабировать — 10 сателлитов разом",
    "&ldquo;If one satellite helps, ten should help ten times more — let&rsquo;s just build a bunch fast.&rdquo;",
    "Если один сателлит помогает, десять помогут в десять раз больше — давайте просто быстро наштампуем.",
    "&ldquo;More satellites in the same space is exactly the coordinated pattern that gets flagged. It doesn&rsquo;t multiply the benefit, it multiplies the risk of losing all of them at once.&rdquo;",
    "Больше сателлитов в одной нише — это ровно тот скоординированный паттерн, который палят. Это не умножает пользу, это умножает риск потерять всё разом."),
  rp_item(3, "У конкурента только что деиндексировали сеть",
    "&ldquo;I just saw [competitor]&rsquo;s whole network disappear from Google overnight. Could that happen to us?&rdquo;",
    "Я только что увидел, что вся сеть [конкурента] пропала из Google за одну ночь. С нами так может быть?",
    "&ldquo;That&rsquo;s the fragility we talked about — a network like that lives or dies together. Yours is built to stand on its own, so it doesn&rsquo;t carry that collapse risk.&rdquo;",
    "Это та самая хрупкость, о которой мы говорили — такая сеть живёт и умирает вместе. Ваш сайт построен так, чтобы стоять сам по себе, поэтому у него нет этого риска обвала."),
  rp_item(4, "Разработчик клиента назвал это «чёрным SEO»",
    "&ldquo;My developer looked at this and said it looks like black hat SEO. Should I be worried?&rdquo;",
    "Мой разработчик посмотрел на это и сказал, что похоже на чёрное SEO. Мне стоит волноваться?",
    "&ldquo;Let&rsquo;s go through exactly what this site does and doesn&rsquo;t do, and where the real risk actually sits — I&rsquo;d rather walk through it together than have you guessing.&rdquo;",
    "Давайте пройдёмся по тому, что этот сайт реально делает и не делает, и где на самом деле риск — лучше разобрать вместе, чем гадать."),
  rp_item(5, "Клиент спрашивает про легальность",
    "&ldquo;Is this even legal? Do we need to disclose something here?&rdquo;",
    "Это вообще законно? Нам нужно что-то раскрывать?",
    "&ldquo;The link-passing part is standard SEO practice. Where disclosure would matter is if we presented this as a fully independent site — and that&rsquo;s not what we&rsquo;re doing here.&rdquo;",
    "Часть с передачей ссылочного веса — стандартная SEO-практика. Раскрытие было бы важно, если бы мы выдавали это за полностью независимый сайт — а мы этого не делаем."),
]

roleplay_intro = '''
<div class="info-card">
  <div class="info-head"><h3>Контекст<small>The Competitor Satellite Question</small></h3></div>
  <p class="idea">Клиент (B2B SaaS) заметил, что конкурент почти всегда всплывает в ответах ChatGPT и AI Overviews, а его бренд — почти никогда. Клиент узнал, что у конкурента «целая сеть мелких сайтов», и хочет сделать так же — быстро.</p>
  <p class="idea"><strong>Роль специалиста:</strong> объяснить, что это такое, обозначить флоу работ; конкурент строит по сути дорвеи — однотипные сайты с однотипным наполнением — это риск, мы же строим сателлиты.</p>
  <p class="idea"><strong>Роль клиента</strong> (Head of Growth, конкурентный, нетерпеливый): хочет быстрый результат, постоянно ссылается на конкурента, скептичен насчёт «долгого органического пути», прямо спрашивает: «почему нам просто не сделать то же самое?»</p>
</div>'''

sec_roleplay = section("roleplay", "Часть 5 · Role Play: &ldquo;The Competitor Satellite Question&rdquo;", "B2B SaaS, конкурент топит в AI-ответах, клиент торопится (8 мин)",
                        roleplay_intro + accordion(rp_items, single=True, first_open=False))


body = "\n".join([sec_terms, sec_llm, sec_internal, sec_client, sec_roleplay])

html = page(
    title="Урок 15 — Сателлиты в SEO и их влияние на LLM",
    desc="Продвинутая терминология сателлитных сетей (satellite, PBN, footprint, doorway pattern, link spam policy, site reputation abuse), как они пытаются влиять на цитирования в LLM и AI Overviews, и как честно объяснять этот риск клиенту.",
    brand="Global English · Урок 15",
    eyebrow="Урок 15 из курса «Global English для SEO»",
    h1="Сателлиты в SEO и их влияние на LLM",
    lede="Satellite Networks, Footprints & AI/LLM Citations — продвинутая терминология сетей сателлитов, риски по политикам Google, влияние на AI-цитирования и честный разговор с клиентом о том, что реально гарантируется, а что нет.",
    navlinks=[("#terms","Термины"), ("#llm","LLM"), ("#internal","Внутри"), ("#client","Клиенту"), ("#roleplay","Role Play")],
    body=body,
    prev_href="/lessons/14/", prev_label="← Урок 14: Допродажа",
    next_href="/", next_label="Все уроки →",
)
write("lessons/15/index.html", html)
