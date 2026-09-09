# -*- coding: utf-8 -*-
from build import page, section, accordion, write

def case_body(role, company, desc, customers, money, problem, character, script, followups, terms, hint):
    fu = "".join(f"<li>{q}</li>" for q in followups)
    tg = "".join(f"<span>{t}</span>" for t in terms)
    return f'''
    <p class="idea"><strong>{role}</strong> at <strong>{company}</strong></p>
    <h5>Что делает бизнес</h5><p>{desc}</p>
    <h5>Клиенты</h5><p>{customers}</p>
    <h5>Как зарабатывает</h5><p>{money}</p>
    <h5>Проблема</h5><p>{problem}</p>
    <h5>Характер клиента</h5><p>{character}</p>
    <h5>Реплика клиента (читать вслух)</h5>
    <blockquote class="script">{script}</blockquote>
    <h5>Уточняющие вопросы клиента</h5>
    <ul>{fu}</ul>
    <h5>Ключевые термины ответа</h5>
    <div class="chips">{tg}</div>
    <div class="note">{hint}</div>'''

cases = [
  dict(title="TaskFlow", sub="CASE 1 · SaaS · Project management tool", body=case_body(
    "Chief Marketing Officer", "TaskFlow",
    "Софт для управления проектами для малого бизнеса: задачи, дедлайны, файлы, коммуникация. Конкурирует с Notion, Asana и Monday.com, но дешевле.",
    "Команды 5–50 человек в агентствах, стартапах и сервисных бизнесах. Решение обычно принимает CEO или operations manager.",
    "Подписка за пользователя — around £8/user/month.",
    "Reddit-обсуждения про инструменты для управления проектами постоянно упоминают Notion — часто в первом комментарии. TaskFlow не рекомендуют никогда. Попытка постить о TaskFlow на Reddit закончилась баном аккаунта после двух постов. В AI-инструментах Notion всегда в топ-3 рекомендаций.",
    "Расстроенный маркетолог, который пытался «взломать» Reddit и не смог. Важны trial signups и monthly active users.",
    "Good morning. We make project management software — similar to Asana or Monday.com but more affordable. We noticed something strange. When we search Reddit for 'best project management tool for small teams', our competitor Notion appears in almost every thread. Then when our sales team asks ChatGPT to recommend tools, Notion always comes up. Our software has similar features and better pricing. But in every online conversation, we simply do not exist. We think our competitor is doing something on Reddit intentionally. Is that possible? And how do we respond?",
    ["How would you check if our competitor is artificially seeding Reddit?",
     "We tried posting on Reddit before — our account got banned after two posts. Why?",
     "Is there a legitimate way to build Reddit presence without getting banned?",
     "If we write more blog content, will that eventually help us appear in ChatGPT answers?"],
    ["Reddit seeding","community infiltration detection","organic community building","Reddit account strategy","LLM training data","brand share of voice","AEO content strategy","authenticity signals"],
    "ℹ️ Объяснить, как работает Reddit seeding (аккаунты с историей, естественный паттерн). Их забанили: новый аккаунт + прямая реклама. Легальная стратегия: ценный контент + органическое упоминание. Детекция: анализ истории аккаунтов в тредах через Reddit search.",
  )),
  dict(title="BrightSmile Dental Group", sub="CASE 2 · Local SEO · Dental clinic chain (12 локаций, Лондон)", body=case_body(
    "Marketing Manager", "BrightSmile Dental Group",
    "12 стоматологических клиник по Лондону: общая стоматология, ортодонтия, косметические процедуры. У каждой клиники своя команда врачей.",
    "Местные жители и работающие в радиусе 2–3 миль от каждой клиники. Большинство ищут через Google Maps.",
    "Приёмы пациентов — микс NHS и private. Private (Invisalign, имплантаты) — высокая маржа.",
    "Часть клиник появляется в Google Maps по запросу «dentist near me», часть — полностью невидима, включая новую клинику в Canary Wharf в очень оживлённом районе. Конкурент с одной клиникой появляется чаще, чем несколько клиник BrightSmile.",
    "Понимает healthcare-маркетинг, но ничего не знает про алгоритмы локального поиска. Важны новые записи на приём по каждой клинике.",
    "Hello. We own a group of dental clinics — twelve locations across Greater London. Each clinic has its own Google Business Profile. The problem is some locations appear in the Google Maps results and some never do. For example, our Canary Wharf clinic is invisible even though it is in a very busy area. We are losing patients to competitors who have smaller clinics but rank higher locally. What determines which clinics appear in Google Maps, and what can we do?",
    ["What is a local pack? Is that the same as Google Maps results?",
     "We have different phone numbers listed on different websites — is that a problem?",
     "Should each clinic have its own page on our main website?",
     "One of our clinics has only twelve Google reviews. How many do we actually need?"],
    ["Google Business Profile","local pack","NAP consistency","local citations","proximity / relevance / prominence","location pages","review velocity","local link building"],
    "ℹ️ Три фактора local pack: proximity, relevance, prominence. NAP consistency, GBP-оптимизация, отдельная location page для каждой клиники — обязательно. Мало отзывов — серьёзная проблема для prominence.",
  )),
  dict(title="WorkForce Pro", sub="CASE 3 · SaaS · B2B HR software (mid-market)", body=case_body(
    "Marketing", "WorkForce Pro",
    "Платформа для управления HR-операциями среднего бизнеса: payroll, расписания, отпуска, HR-документы. Как умный Excel для HR.",
    "HR-директора и operations-менеджеры в компаниях 50–500 человек: юрфирмы, логистика, ритейл.",
    "Подписка £200–£2,000/месяц в зависимости от размера компании.",
    "Почти все новые клиенты приходят с Google Ads — £40,000/месяц. У конкурентов огромные блоги с бесплатным органическим трафиком. Хотят снизить зависимость от платной рекламы, но не знают, с чего начать SEO.",
    "Маркетинговый и бизнес-бэкграунд. Понимает customer acquisition, но не техническое SEO. Важны cost per acquisition и MRR.",
    "Hi. We make HR software for mid-size companies — things like payroll, scheduling, and employee documents. Right now about ninety percent of our new customers come from Google Ads. We spend forty thousand pounds a month on ads. It works but it's very expensive. We want to build organic traffic so we depend less on paid advertising. Our competitors have big blogs with hundreds of articles about HR topics. Where do we start, and how long will it take to reduce our ad spend?",
    ["What is product-led SEO? Our developer mentioned it but I don't understand.",
     "Should we write for people who are ready to buy, or for people just learning about HR?",
     "How do we compete with big HR publications that have been writing for ten years?",
     "What is a realistic timeline — one year, two years?"],
    ["product-led SEO","BOFU/MOFU/TOFU","content-led growth","competitor content gap","topical authority","SaaS content funnel","alternative pages"],
    "ℹ️ Объяснить SaaS-специфику: BOFU-страницы ('alternatives to X', use cases, comparisons) дают быстрый ROI. Информационный блог — долго. Минимум 6–12 месяцев до значимых результатов.",
  )),
  dict(title="TradePeak", sub="CASE 4 · Finance · Forex & CFD broker (FCA-regulated)", body=case_body(
    "CEO", "TradePeak",
    "Регулируемый онлайн-брокер: forex, акции, commodities, индексы. Полностью лицензирован FCA (UK) — самым престижным финансовым регулятором.",
    "Розничные трейдеры — обычные люди, инвестирующие из дома, плюс часть профессиональных трейдеров.",
    "Заработок на «spread» — разнице между ценой покупки и продажи на каждой сделке.",
    "При поиске названия бренда в топе — не сайт компании, а анонимные статьи «Is TradePeak a scam?» с неверной информацией. У компании чистая репутация в FCA, но новые клиенты читают это и не регистрируются.",
    "Финансовый бэкграунд, гордится регуляторными статусами, не техчеловек. Важны account openings и регуляторная репутация.",
    "Hello. We are a regulated forex and CFD broker, licensed by the FCA. When someone types our brand name into Google, the first results are not our website. They see articles like 'Is TradePeak a scam?' or 'Avoid this broker'. Some of these articles have completely wrong information — we have never had a complaint filed with the FCA. This is destroying our conversion rate. New clients check Google before signing up and then they don't. How do we fix what appears when people search for our brand name?",
    ["What is brand SERP? I have not heard this term before.",
     "Can we legally force Google to remove those negative articles?",
     "If we create more content about our brand, will it push those articles down?",
     "What is the realistic timeline to see improvement?"],
    ["brand SERP","ORM","YMYL","E-E-A-T","knowledge panel","branded content strategy","digital PR","suppression strategy"],
    "ℹ️ Объяснить brand SERP management: Google не уберёт контент по запросу, но можно вытеснить своим. Финансы — YMYL, E-E-A-T критичен. Стратегия: Wikipedia, Crunchbase, пресс-релизы, branded content.",
  )),
  dict(title="SpinKing Casino", sub="CASE 5 · iGaming · Online casino (UK, UKGC-licensed)", body=case_body(
    "Head of Marketing", "SpinKing Casino",
    "Онлайн-казино, лицензировано UK Gambling Commission: слоты, рулетка, live dealer games.",
    "UK-взрослые 25–50, играющие онлайн ради развлечения. Находят через Google, ТВ-рекламу, сарафанное радио.",
    "House edge — статистически казино удерживает процент от ставок со временем.",
    "6 месяцев назад добавили 300 новых страниц (по одной на каждую слот-игру). С тех пор трафик упал на 30%, половина страниц не в индексе Google. Команда паникует, не понимает технических причин.",
    "Не технический человек. Важны регистрации игроков и revenue. Сказали, что у сайта «content problem», но не понимает, что это значит.",
    "Hi. We run a licensed online casino in the UK — we have a full UKGC licence. Six months ago we added about three hundred new pages — one page for each slot game we offer. Each page has the game name, a short description, and a big 'Play Now' button. Since then, Google Search Console shows that half of those pages are not in Google's index. Also, our traffic for terms like 'best online slots UK' dropped by about thirty percent. We thought more pages meant more traffic. What went wrong?",
    ["What is thin content? Our pages have text — isn't that enough?",
     "We have a Responsible Gambling page. Does Google care about that for rankings?",
     "Our competitor has similar slot pages but they rank fine. Why are we different?",
     "Should we delete the weak pages or is there a better option?"],
    ["thin content","crawl budget","YMYL","E-E-A-T","responsible gambling signals","content consolidation","indexing quota"],
    "ℹ️ 300 однотипных страниц = thin content + проблема crawl budget. Gambling — YMYL-ниша, Responsible Gambling сигналы важны. Стратегия: consolidate или enrich. Ошибка — не упомянуть YMYL.",
  )),
  dict(title="CardCompare UK", sub="CASE 6 · Finance affiliate · Credit card comparison site", body=case_body(
    "Founder", "CardCompare UK",
    "Сайт, который помогает подобрать кредитную карту: кэшбэк, travel, 0% interest. Сравнивает карты крупных UK-банков. Своих продуктов нет — чистый посредник.",
    "UK-взрослые, ищущие кредитную карту онлайн через запросы вроде «best cashback credit card UK».",
    "Партнёрские комиссии: £30–£150 за каждую успешную заявку по ссылке.",
    "В сентябре трафик упал на 70% за две недели — с 80,000 до 23,000 визитов в месяц. Контент не меняли. Позже узнали, что дело в Google 'Helpful Content Update', но до конца не понимают, что это.",
    "Финансовый профессионал, построивший сайт сам. Не разработчик и не SEO-эксперт. Важен месячный комиссионный доход.",
    "Hi. We run a website that compares credit cards in the UK — we earn commissions when users apply. In September last year, our organic traffic dropped by seventy percent in two weeks. We went from about eighty thousand visitors a month to twenty-three thousand. We did not change our content before this happened. I later read about something called the Google Helpful Content Update. Can you explain what that is and whether it is the reason our site was hit?",
    ["What is the difference between a site-wide signal and a page-level penalty?",
     "We hire freelancers to write our comparison articles. Is that the problem?",
     "Our competitors are also affiliates — why were they not affected?",
     "How long does it typically take to recover from this type of update?"],
    ["Helpful Content Update","site-wide quality signal","YMYL","E-E-A-T","affiliate content","original research","editorial depth","recovery timeline"],
    "ℹ️ HCU — site-wide сигнал, не page-level. Affiliate-сайты без firsthand experience — основная цель. Recovery: переписать контент, добавить E-E-A-T, ждать следующий core update. Срок — месяцы.",
  )),
  dict(title="NutriCore", sub="CASE 7 · Health & wellness · Supplement brand (D2C, EU)", body=case_body(
    "Founder", "NutriCore",
    "D2C бренд БАДов: витамины, минералы, добавки (Vitamin D, магний, омега-3, iммунные бустеры). Производство в Германии, продажи в Германии и Нидерландах.",
    "Взрослые 30–55, покупающие добавки онлайн ради общего здоровья, иммунитета и энергии.",
    "Прямые продажи через сайт, маржа около 60–70%.",
    "Google постоянно убирает страницы товаров из поиска, реклама отклоняется. Страницы про конкретные продукты (например, Vitamin D drops) полностью исчезли из Google. Продукты полностью легальны, причина непонятна.",
    "Бэкграунд в nutrition science, верит в свои продукты, но digital-маркетинг — challenge. Важны онлайн-продажи и доверие клиентов.",
    "Hello. We sell nutritional supplements directly to customers online — mainly in Germany and the Netherlands. We make claims on our product pages like 'supports immune system' and 'clinically tested'. Google keeps disapproving our ads, so organic search is our only real traffic channel. The problem is our rankings keep dropping and some of our key pages disappeared from Google. We have no idea why — the content is accurate and our products are completely legal. What is Google's problem with health supplement websites?",
    ["What does YMYL mean and why does it apply to us?",
     "We have a doctor who reviews our content. Is that enough for Google?",
     "What is an author bio and why does it matter for search rankings?",
     "Our page about Vitamin D disappeared from Google completely — how do we get it back?"],
    ["YMYL","E-E-A-T","medical claims","author credentials","health content guidelines","structured data","content audit for YMYL"],
    "ℹ️ Health = YMYL с максимальными E-E-A-T требованиями. Нужны авторы с credentials, ссылки на исследования, отказ от unsubstantiated claims. Страница исчезла — вероятно нарушение health content policy Google.",
  )),
  dict(title="OddsHub", sub="CASE 8 · iGaming · Sports betting affiliate (UK, IE, CA)", body=case_body(
    "Head of PR", "OddsHub",
    "Обзорный сайт про букмекеров (Bet365, William Hill, Paddy Power и т.д.) — фичи, бонусы, коэффициенты. Сам ставки не принимает.",
    "Спортивные фанаты в UK, Ирландии и Канаде, ищущие «best betting site for football».",
    "Партнёрские комиссии: £50–£200 за каждого нового клиента букмекера.",
    "В марте потеряли 60% Google-трафика за неделю. Конкурент в той же нише за тот же период трафик нарастил. Не знают, что вызвало падение и как восстановиться.",
    "Глубоко разбирается в беттинге, но SEO — загадка. Важны месячный комиссионный доход и цифры трафика.",
    "Hi. We run an affiliate website that reviews and compares sports betting sites — mainly for UK, Ireland and Canada. We were getting around two hundred thousand visitors a month from Google. Then in March we lost about sixty percent of that traffic in one week. We checked and there was a Google core update around that time. The strange thing is our competitor in the same niche actually gained traffic in the same period. What is the difference between us and them, and how do we find out?",
    ["We have about four hundred review pages — some bookmakers we reviewed no longer exist. What do we do with those?",
     "Our content is written by freelancers who have never actually placed a bet. Is that a problem?",
     "What is the difference between a core update and a spam update?",
     "How do we analyse what our competitor is doing better than us?"],
    ["core update","quality rater guidelines","firsthand experience","E-E-A-T","affiliate content","YMYL (gambling)","dead page cleanup","competitor gap analysis"],
    "ℹ️ Gambling affiliate = YMYL. Google проверяет firsthand experience у авторов. Страницы умерших букмекеров — сигнал low quality. Competitor analysis через Ahrefs — первый шаг. Recovery после core update: месяцы, не недели.",
  )),
  dict(title="Blu Collection", sub="CASE 9 · Travel · Boutique hotel chain (15 объектов, Южная Европа)", body=case_body(
    "Director of Marketing", "Blu Collection",
    "15 бутик-отелей в Испании, Португалии и Греции. Каждый отель уникален — локальная архитектура, 20–50 номеров.",
    "Состоятельные путешественники из UK, Германии и США 30–55 лет, ценящие аутентичность и дизайн.",
    "Бронирования номеров, F&B, частные мероприятия. Средний тариф £250–£600/ночь.",
    "При поиске названия отеля Booking.com часто выше собственного сайта — а Booking берёт 15–20% комиссии с брони. Хотят больше прямых бронирований через свой сайт.",
    "Hospitality-профессионал с отличным вкусом, но не разбирается в digital-механике. Важны direct booking rate и комиссионные издержки.",
    "Good morning. We own fifteen boutique hotels across Spain, Portugal and Greece. Most of our direct bookings used to come from Google — people searched for our hotel name and booked directly. Now when someone searches for hotels in our locations, they see Booking.com and Expedia first. Even when someone searches specifically for our hotel name, Booking.com sometimes ranks above our own website. We are losing money on commissions because guests book through those platforms instead of us. Is there anything we can do to get more direct bookings through Google?",
    ["What are Google Hotel Ads? Are they different from regular Google Ads?",
     "Should each of our fifteen hotels have a separate website, or is one website better?",
     "What is schema markup and does it help hotels specifically?",
     "We have excellent reviews on TripAdvisor — does that affect our Google rankings?"],
    ["branded search","direct booking strategy","hotel schema markup","Google Hotel Ads","OTA cannibalization","location pages","Google Business Profile (hotels)"],
    "ℹ️ OTA-каннибализация брендового трафика — системная проблема. Решения: Google Hotel Ads (price parity), сильные location pages, GBP-оптимизация, schema. Один сайт с location pages — правильная архитектура.",
  )),
]

sec_cases = section("cases", "9 кейсов", "специалист читает роль клиента и отвечает вслух 2–3 минуты, потом группа даёт фидбек",
                     accordion(cases, first_open=False))

body = f'''<section id="intro">
  <div class="wrap">
    <h2>Как это работает</h2>
    <p class="section-kicker">роли: специалист + носитель языка в роли клиента</p>
    <div class="info-card">
      <ol style="margin:0; padding-left:20px; color:var(--ink-soft); font-size:15px; display:grid; gap:8px;">
        <li>Каждый специалист получает одну карточку кейса. Ниша и имя клиента — в заголовке карточки.</li>
        <li>Партнёр читает раздел «кто вы» (роль клиента), затем зачитывает реплику клиента вслух.</li>
        <li>Специалист отвечает на английском 2–3 минуты. Можно задавать клиенту уточняющие вопросы.</li>
        <li>Если ответ расплывчатый — клиент задаёт уточняющий вопрос из списка.</li>
        <li>После ответа — 3-минутный дебриф в группе на английском.</li>
      </ol>
    </div>
    <div class="note">В исходном материале 10 кейсов — десятый (Real Estate · EuroHomes) прислали не полностью, добавим отдельно, когда будет весь текст.</div>
  </div>
</section>
{sec_cases}'''

html = page(
    title="Урок 10 — Кейсы с нейтивом",
    desc="9 полных ролевых кейсов для практики с носителем языка: SaaS, местное SEO, финансы, iGaming, health, travel — с деталями бизнеса, репликой клиента и ключевыми терминами ответа.",
    brand="Global English · Урок 10",
    eyebrow="Урок 10 из курса «Global English для SEO»",
    h1="Кейсы с нейтивом",
    lede="Реальные ниши, реальные проблемы: от Reddit-seeding у SaaS-конкурента до каннибализации брендового трафика Booking.com. Разбор с носителем языка в роли клиента.",
    navlinks=[("#intro","Как это работает"), ("#cases","Кейсы")],
    body=body,
    prev_href="/lessons/9/", prev_label="← Урок 9: Фразовые глаголы",
    next_href="/lessons/11/", next_label="Урок 11: Словарик →",
)
write("lessons/10/index.html", html)
