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
  dict(title="EuroHomes", sub="CASE 10 · Real Estate · International property portal (buy abroad)", body=case_body(
    "CEO", "EuroHomes",
    "Онлайн-портал недвижимости, где покупатели ищут дома и квартиры в Испании, Италии и Португалии. Работает с местными агентствами, которые размещают объекты на платформе. Как Rightmove — но для покупки недвижимости за рубежом.",
    "В основном покупатели из UK, Германии и Нидерландов 40–65 лет, ищущие дом для отдыха, для переезда на пенсию или для инвестиций в Южной Европе.",
    "Подписки агентств (ежемесячная плата за размещение объектов) и оплата за лиды (когда покупатель связывается с агентом через сайт).",
    "На сайте 50 000 объявлений о недвижимости. Google индексирует и показывает лишь небольшую часть. Техническое агентство сказало про «проблему дублированного контента» — многие страницы слишком похожи друг на друга. Не понимают, что делать.",
    "Из недвижимости, не из tech. Важны лиды и подписки агентств.",
    "Hello. We run a website where people can search for properties to buy in Spain, Italy and Portugal. We have around fifty thousand property listings — they update automatically from agent feeds. Our problem is that Google seems to index only a small percentage of our listings. Also, many of our listing pages look very similar to each other — same template, just different address and price. A technical SEO agency told us we have a 'duplicate content problem'. What does that mean? And how do we get Google to properly index and rank our property pages?",
    ["If we have fifty thousand pages, does Google visit all of them?",
     "What is a canonical tag? Our developer mentioned it but I don't understand the purpose.",
     "Some of our listings expire when properties are sold — should we delete those pages?",
     "Our competitor Rightmove has millions of pages and they rank fine. How do they do it?"],
    ["duplicate content","crawl budget","canonicalization","programmatic SEO","faceted navigation","expired listings strategy","internal linking at scale","indexing prioritisation"],
    "ℹ️ 50k страниц — programmatic SEO задача. Canonical, уникальный контент на шаблонных страницах, crawl budget management, стратегия expired listings (301 или aggregate). Rightmove = DR + unique UGC + established authority.",
  )),
  dict(title="Sterling Immigration", sub="CASE 11 · Legal services · Immigration law firm (3 UK офиса)", body=case_body(
    "Head of Business Development", "Sterling Immigration",
    "Юридическая фирма по иммиграции с офисами в Лондоне, Манчестере и Бирмингеме. Помогает с визами в UK, гражданством, ILR и иммиграционными апелляциями. Юристы — квалифицированные солиситоры, регулируемые SRA.",
    "Люди, подающие на визы UK (skilled worker, spouse, student), компании-спонсоры зарубежных сотрудников, и те, кто оспаривает иммиграционные решения.",
    "Фиксированная оплата за кейс — обычно £1,500–£5,000 в зависимости от сложности.",
    "Почти все клиенты приходят по рекомендациям или через дорогую рекламу в Google. Полгода вели блог о разных типах виз — почти нет трафика. Не понимают, почему стратегия не работает.",
    "Юридический бэкграунд, не digital. Осторожный и не любит риск по натуре. Важны новые обращения и объём кейсов.",
    "Good afternoon. We are an immigration law firm with offices in London, Manchester and Birmingham. We help people with UK visas, citizenship applications, and immigration appeals. Right now almost all our clients come from referrals or we pay a lot for Google Ads. We want to be found organically when someone searches 'immigration lawyer London' or 'UK visa help'. We tried blogging for six months — we wrote about different visa types — but we get almost no traffic. What are we doing wrong?",
    ["Should each of our three offices have its own page on the website?",
     "We are worried about publishing legal advice online — what if someone relies on wrong information?",
     "Our blog articles are about three hundred words each. Is that too short?",
     "There is a legal directory called Chambers — does being listed there help our SEO?"],
    ["local SEO for professional services","practice area pages","YMYL (legal)","E-E-A-T","content depth","location landing pages","legal directories as citations"],
    "ℹ️ Law firm SEO = local SEO + YMYL E-E-A-T. Три офиса → три location pages. 300 слов — катастрофически мало для юридической ниши (нужно 1500-3000). Chambers/Legal 500 — авторитетные citations. Disclaimer решает проблему страха перед публичными советами.",
  )),
  dict(title="CoinBridge Exchange", sub="CASE 12 · Crypto · Centralised exchange", body=case_body(
    "Chief Marketing Officer", "CoinBridge Exchange",
    "Регулируемая платформа для покупки, продажи и хранения криптовалют (Bitcoin, Ethereum). Как фондовая биржа — но для цифровых валют.",
    "Розничные инвесторы и крипто-энтузиасты, в основном в Европе, которые хотят покупать Bitcoin без крупных платформ вроде Coinbase.",
    "Комиссия 0.1–0.5% с каждой сделки пользователя.",
    "Когда команда спрашивает ChatGPT или Perplexity «какую крипто-биржу выбрать?», ответ всегда рекомендует Binance и Coinbase. Бренд не упоминается никогда — хотя биржа лицензирована, безопасна и с конкурентными комиссиями.",
    "Лично пользуется крипто, понимает продукт, но ничего не знает о работе Google или AI-инструментов. Важны новые регистрации пользователей.",
    "Good morning. We operate a crypto exchange — we have been live for two years. When our customers ask ChatGPT or Perplexity which exchange to use, the answer is always Binance or Coinbase. Our brand is never mentioned. Not once. We have good reviews on Trustpilot and we are regulated in Estonia. What can we do to appear in AI-generated answers? And is this even possible, or do only the biggest brands get mentioned?",
    ["What is the connection between Google rankings and being mentioned by AI?",
     "We have a blog but we mostly write about crypto news. Is that the wrong strategy?",
     "Someone told us to get mentions on Reddit and crypto forums. Does that actually help?",
     "How would you measure success — how do we know if it's working?"],
    ["AEO","LLM visibility","brand entity","E-E-A-T","third-party mentions","topical authority","structured data","AI answer engines"],
    "ℹ️ Спец должен объяснить: AI берёт данные из авторитетных источников — Wikipedia, Reddit, топ Google. SEO + digital PR + entity building — это путь к LLM visibility. Измеримость: Brand Radar, ручное тестирование промптов.",
  )),
  dict(title="PayFast", sub="CASE 13 · Fintech · B2B payment gateway (стартап, 8 месяцев)", body=case_body(
    "Co-Founder", "PayFast",
    "Сервис обработки платежей для интернет-магазинов. Если магазин одежды или SaaS-компания хочет принимать оплату картой от клиентов по всему миру — используют PayFast. Обрабатывают платежи в 30 валютах с комиссией ниже, чем у Stripe или PayPal.",
    "E-commerce бизнесы и SaaS-стартапы — обычно малые и средние компании, продающие онлайн.",
    "Комиссия 0.8% + £0.20 с каждой транзакции клиента-мерчанта.",
    "Запустились 8 месяцев назад. Продукт конкурентный, но почти никто не находит через Google. По запросам вроде «best payment gateway for e-commerce» сайта нет нигде — ни на первой, ни на второй странице. Отличная технология, но нулевая органическая видимость.",
    "Технический фаундер — сам строил продукт. Growth-маркетинг и SEO — новая территория. Важны регистрации мерчантов и объём транзакций.",
    "Good afternoon. We launched a payment gateway for e-commerce businesses eight months ago. We process payments in thirty currencies and our fees are lower than Stripe or PayPal. But when someone searches 'best payment gateway for e-commerce', we are not in the results. Not on page one, not on page two. Our website gets almost no organic traffic at all. We are a new company — is it even possible to rank for these terms? Or do we need to wait years before SEO can help us?",
    ["What is domain authority and why does our new site have a disadvantage?",
     "Should we focus on very specific keywords first instead of competitive ones?",
     "A consultant told us to buy five hundred backlinks. Is that a good idea?",
     "What would you do in the first three months if you were working on our project?"],
    ["domain authority","long-tail strategy","topical authority","digital PR","keyword difficulty","link building for startups","quick wins"],
    "ℹ️ Новый домен — реальный challenge. Стратегия: long-tail + low competition ниши сначала, параллельно digital PR для ссылок. 500 купленных ссылок для fintech — риск manual penalty. Честные сроки: 6-18 месяцев.",
  )),
  dict(title="Moda Linen", sub="CASE 14 · E-commerce · DTC fashion brand (США, 3000 SKU)", body=case_body(
    "Head of E-commerce", "Moda Linen",
    "Собственный бренд женской одежды — дизайн in-house, производство в Португалии. Продажи полностью через свой сайт, в основном клиентам в США. Стиль минималистичный, на основе льна, устойчивый. Около 3000 карточек товаров.",
    "Американки 28–45 лет, ценящие качество, устойчивость и минималистичную моду. Часто ищут в Google «linen summer dresses» или «minimalist women's clothing».",
    "Прямые продажи товаров с маржой 55–70%. Плюс Google Shopping и реклама в Instagram.",
    "Позиции по запросам вроде «linen dresses» и «minimalist fashion» заметно упали за последние 4 месяца. Google ведёт себя непоследовательно — то показывает страницы категорий, то карточки товаров по одному и тому же запросу. Расходы на рекламу растут, потому что упал органический трафик.",
    "Хорошо разбирается в моде и ритейле, понимает клиента, но техническое SEO — новая территория. Важны выручка сайта и ROAS.",
    "Hi. We sell women's clothing online — our own brand, made in Portugal, sold mainly in the US. We have about three thousand product pages. New collections come in every season, so old products go out of stock. Our problem: we used to rank well for terms like 'linen dresses' or 'minimalist fashion'. In the last four months our rankings for those terms dropped significantly. We also noticed that Google sometimes shows our category pages, sometimes product pages — it's inconsistent. What is happening and how do we stabilise our rankings?",
    ["What should we do with product pages when items go out of stock permanently?",
     "What is keyword cannibalization? Could that be our problem?",
     "Our product descriptions are about eighty words each. Is that enough?",
     "We have three thousand products — do we need unique content on every single page?"],
    ["keyword cannibalization","category vs product page hierarchy","out-of-stock strategy","faceted navigation","thin content at scale","collection page optimisation","product schema"],
    "ℹ️ Каннибализация category vs product pages — классика e-com. Category pages должны быть основными ranking pages. Out-of-stock: 301 на category или noindex. 80 слов = thin content. Приоритет: обогатить category pages.",
  )),
  dict(title="La Piazza Group", sub="CASE 15 · Local SEO · Italian restaurant group (5 точек, Лондон) · Reserve", body=case_body(
    "Co-Owner", "La Piazza Group",
    "Пять итальянских ресторанов в разных районах Лондона: Сохо, Ислингтон, Кэнэри-Уорф, Брикстон и Уимблдон. Каждый ресторан подаёт традиционную итальянскую кухню — пасту, пиццу, ризотто — на обед и ужин. У каждой точки своя команда и немного отличное меню.",
    "Местные жители, офисные работники и туристы, ищущие настоящую итальянскую еду. Большинство находят рестораны через Google Maps.",
    "Средний чек за столик (обед и ужин) и частные мероприятия — дни рождения, корпоративы.",
    "При поиске итальянских ресторанов в Google Maps рестораны иногда появляются, иногда нет. Точка в Брикстоне открыта три года, отличная еда и хорошие отзывы — но почти не видна. Более новый конкурент открылся полгода назад рядом и уже ранжируется выше. Также у точки в Кэнэри-Уорф в Google-профиле указаны неверные часы работы, которые они не устанавливали.",
    "Увлечённый ресторатор, разбирается в еде и гостеприимстве. Digital-маркетинг — не его мир. Важны число столиков за вечер и брони мероприятий.",
    "Hello. I own five Italian restaurants in London — Soho, Islington, Canary Wharf, Brixton, and Wimbledon. When I search Google Maps for Italian restaurants in each area, my restaurants sometimes appear and sometimes they don't. Our Brixton location has been open for three years and we have great food and good reviews. But it barely shows up on Google Maps. A place that opened six months ago near us appears in the top three. I also noticed that our Google listing for Canary Wharf shows the wrong opening hours — I didn't change that. What controls which restaurants Google shows? And why is a newer place beating us?",
    ["We have 4.2 stars with two hundred Google reviews. Is that not enough?",
     "What is the difference between appearing on Google Maps and appearing in regular Google search results?",
     "Should each restaurant have its own website, or is one website with five pages fine?",
     "Someone told us to reply to all our reviews — does that actually affect our rankings?"],
    ["local pack","Google Business Profile","proximity/relevance/prominence","review velocity","NAP consistency","GBP optimisation","location pages","local citations","GBP spam (wrong info)"],
    "ℹ️ Три фактора local pack: proximity, relevance, prominence. Неправильные часы в GBP — можно оспорить через GBP support. Отдельная location page для каждого ресторана обязательна. Ответы на отзывы — влияют на prominence сигнал.",
  )),
  dict(title="ShieldVPN", sub="CASE 16 · SaaS · VPN & privacy tool · Reserve (Reddit & LLM)", body=case_body(
    "Chief Marketing Officer", "ShieldVPN",
    "VPN-сервис. Приложение шифрует интернет-соединение и скрывает реальное местоположение пользователя. Люди используют его для приватности, доступа к стриминг-контенту из других стран, безопасности в публичном wifi. Конкурирует с NordVPN, Mullvad и ExpressVPN.",
    "Люди, заботящиеся о приватности, удалённые сотрудники, журналисты и жители стран с интернет-ограничениями. Обычно довольно tech-savvy аудитория.",
    "Ежемесячная или годовая подписка — обычно £5–£12 в месяц.",
    "Протестировали вопрос ChatGPT «какой VPN лучший для приватности?». Ответ рекомендовал NordVPN, Mullvad и ProtonVPN — и цитировал обсуждение с Reddit r/privacy как источник. В этом треде конкурент Mullvad упомянут 40+ раз. Бренд — ни разу. Тот же тред на Google — на 2-м месте по запросу «best privacy VPN». Конкурент получает и трафик Google, и рекомендации от ИИ — а они не получают ничего.",
    "Сам разбирается в privacy-технологиях, маркетинг-ориентирован, но не SEO-специалист. Важны рост подписчиков и отток (churn).",
    "Hi. We make a VPN product — we have been on the market for four years. Recently I tested something. I asked ChatGPT: 'What is the best VPN for privacy?' The answer mentioned NordVPN, Mullvad, and ProtonVPN. It quoted a Reddit thread from r/privacy. In that Reddit thread, our competitor Mullvad is mentioned over forty times. We are not mentioned once. I also checked — that Reddit thread ranks number two on Google for 'best privacy VPN'. So our competitor gets Google traffic, gets cited by AI, and we are invisible on both. What do we do?",
    ["Can we just go to Reddit and post about our product ourselves?",
     "Why do LLMs like ChatGPT use Reddit as a source? Isn't it just random people talking?",
     "If we get mentioned on Reddit, how long before ChatGPT starts recommending us?",
     "What is the difference between Reddit strategy and normal link building?"],
    ["Reddit SEO","LLM citation sources","UGC signals","brand mentions","community seeding","AEO","subreddit authority","share of voice"],
    "ℹ️ Reddit ранжируется в Google И является источником для LLM. Стратегия: органическое присутствие (ценные комментарии, не спам), digital PR, entity building. Это долго и нельзя купить быстро.",
  )),
  dict(title="SpendSmart", sub="CASE 17 · Fintech · Personal budgeting app · Reserve (Reddit & LLM)", body=case_body(
    "CEO", "SpendSmart",
    "Мобильное приложение для управления личными финансами — учёт расходов по категориям, цели накоплений, напоминания об оплате счетов. Доступно на iOS и Android. Как персональный финансовый коуч в кармане.",
    "Взрослые 22–40 лет в США и UK, желающие контролировать финансы, копить или выплатить долги. Часто молодые специалисты и семьи.",
    "Подписка £5/месяц или £40/год после бесплатного пробного периода.",
    "Протестировали несколько AI-инструментов. На вопрос «лучшее приложение для бюджета» ИИ рекомендует YNAB, а источники — треды Reddit r/personalfinance. У приложения рейтинг в App Store выше, чем у YNAB — 4.8 против 4.6. Но в AI-рекомендациях и на Reddit его просто не существует.",
    "Продуктовый фаундер — построил отличное приложение, но понимает, что этого недостаточно. Важны загрузки приложения и конверсия в платную подписку.",
    "Hello. We make a personal finance app — budget tracking, savings goals, bill reminders. Our main competitor is YNAB. I checked what happens when people ask Perplexity: 'best budgeting app'. Perplexity shows a summary and then links to three Reddit threads — all from r/personalfinance. In those threads, YNAB is the top recommendation in almost every comment. We appear maybe twice. Our app has better App Store reviews than YNAB. But in AI answers we basically don't exist. How is it possible that Reddit controls what AI recommends — and what can we do about it?",
    ["We have real customers who love our app — can we ask them to post on Reddit?",
     "YNAB has been around longer. Is this just about brand age?",
     "If I search our brand name on Reddit, there are almost no posts. Is that the problem?",
     "What would success look like in six months — how do we measure Reddit and AI visibility?"],
    ["Reddit share of voice","LLM recommendation sources","brand entity","community-led growth","Reddit seeding strategy","AEO","unprompted brand mentions","AI visibility tracking"],
    "ℹ️ App Store reviews ≠ LLM visibility. LLM берёт из Reddit, форумов, авторитетных медиа. Стратегия: Reddit присутствие + digital PR + brand упоминания. Просить клиентов писать на Reddit — риск бана.",
  )),
]

sec_cases = section("cases", "17 кейсов", "специалист читает роль клиента и отвечает вслух 2–3 минуты, потом группа даёт фидбек",
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
    <div class="note">17 полных ролевых кейсов — от SaaS и Local SEO до fintech, iGaming, health, travel, legal и crypto. Три кейса (15–17) помечены Reserve — для отработки Reddit/LLM-visibility тем.</div>
  </div>
</section>
{sec_cases}'''

html = page(
    title="Урок 10 — Кейсы с нейтивом",
    desc="17 полных ролевых кейсов для практики с носителем языка: SaaS, местное SEO, финансы, iGaming, health, travel — с деталями бизнеса, репликой клиента и ключевыми терминами ответа.",
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
