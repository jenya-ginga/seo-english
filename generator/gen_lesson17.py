# -*- coding: utf-8 -*-
"""Lesson 17 — walking a client through a REAL monthly report (GSC, rank tracker, GA4, AI tracker).
Screenshots live in assets/lesson17/ (the project name/domain on them is blurred irreversibly).
Every figure used in the texts is checked by the asserts below against the numbers on the screenshots.
"""
import os
from PIL import Image
from build import page, section, phrase_card, phrase_grid, accordion, table_scroll

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(REPO, "assets", "lesson17")


def e(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("'", "&rsquo;")


def q(s):
    return "&ldquo;" + e(s) + "&rdquo;"


# ------------------------------------------------------------------ figures from the screenshots (proof-check)
def pct(new, old):
    return round((new - old) / old * 100, 1)

assert pct(17.2, 19.7) == -12.7          # non-branded clicks
assert pct(3.68, 4.16) == -11.5          # non-branded impressions
assert round(pct(15.5, 17.4)) == -11     # informational clicks
assert round(pct(3.59, 4.02)) == -11     # informational impressions (report: 10.7%)
assert pct(744, 1120) == -33.6           # commercial clicks (1.12K rounded)
assert round(pct(102, 148)) == -31       # commercial impressions
assert pct(11.7, 16.5) == -29.1          # commercial impressions in AI Overview / AI Mode
assert pct(1053, 1424) == -26.1 and pct(781, 1096) == -28.7
assert pct(715, 1094) == -34.6           # AI traffic views
assert pct(13, 35) == -62.9              # key events
assert pct(656, 1008) == -34.9           # chatgpt.com
assert pct(28, 70) == -60.0              # gemini
assert pct(10, 3) == 233.3               # perplexity (low base)
assert 744 / 17200 < 0.05                # commercial = ~4% of non-branded clicks
assert round(846 / 5229 * 100) == 16 and round(1396 / 5229 * 100) == 27 and round(2121 / 5229 * 100) == 41
assert round(3441 / 5229 * 100) == 66 and round(3757 / 5229 * 100) == 72


# ------------------------------------------------------------------ images
SHOTS = {
    1: ("01-gsc-overview.webp", "Search Console: клики и показы за 3 месяца"),
    2: ("02-gsc-nonbranded.webp", "Search Console: небрендовый трафик, 28 дней против предыдущих 28"),
    3: ("03-gsc-pages.webp", "Search Console: страницы с наибольшими потерями кликов"),
    4: ("04-gsc-info.webp", "Search Console: информационный раздел /articles/"),
    5: ("05-gsc-commercial.webp", "Search Console: коммерческие страницы, небренд"),
    6: ("06-aio-info.webp", "Search Console: показы в AI Overview и AI Mode, информационные страницы"),
    7: ("07-aio-commercial.webp", "Search Console: показы в AI Overview и AI Mode, коммерческие страницы"),
    8: ("08-rank-summary.webp", "Rush Analytics: сводка по 5 229 ключевым словам"),
    9: ("09-rank-info.webp", "Rush Analytics: информационный кластер, % запросов в топе"),
    10: ("10-rank-commercial.webp", "Rush Analytics: коммерческий кластер, % запросов в топе"),
    11: ("11-rank-hub-1.webp", "Rush Analytics: хабовая страница №1, % запросов в топе"),
    12: ("12-rank-hub-2.webp", "Rush Analytics: хабовая страница №2, % запросов в топе"),
    13: ("13-serp-manual.webp", "Google US: ручная проверка выдачи по главному коммерческому запросу"),
    14: ("14-ga4-chart.webp", "GA4: AI-трафик по источникам, февраль–сентябрь"),
    15: ("15-ga4-table.webp", "GA4: AI-трафик по источникам, 28 дней против предыдущих 28"),
    16: ("16-ai-visibility.webp", "AI-трекер: видимость бренда и домена за 3 месяца"),
    17: ("17-ai-competitors.webp", "AI-трекер: видимость бренда в сравнении с конкурентами"),
}


def fig(n):
    fn, cap = SHOTS[n]
    w, h = Image.open(os.path.join(IMG_DIR, fn)).size
    return (f'<figure class="shot"><a href="/assets/lesson17/{fn}" target="_blank" rel="noopener">'
            f'<img src="/assets/lesson17/{fn}" width="{w}" height="{h}" loading="lazy" alt="{e(cap)}"></a>'
            f'<figcaption>{e(cap)} · нажмите, чтобы открыть крупно</figcaption></figure>')


# ================================================================== PART 1 · vocabulary
TERMS = [
  ("Reporting period", "репортинг пириэд",
   "The time span that a report covers.", "Период, за который составлен отчёт.",
   "This reporting period overlapped with the September spam update.", True),
  ("Period-over-period", "пириэд-оувэр-пириэд",
   "A comparison with the previous period of the same length.", "Сравнение с предыдущим периодом такой же длины.",
   "Period-over-period, clicks are down 12.7%.", True),
  ("Non-branded traffic", "нон-брэндид трэфик",
   "Search traffic from queries that do not contain the brand name.", "Трафик по запросам без названия бренда.",
   "From here on, we only look at non-branded traffic.", True),
  ("Impression", "импрэшн",
   "One appearance of your page in the search results.", "Один показ страницы в выдаче.",
   "Impressions are down 11.5%, but position improved.", True),
  ("Click-through rate (CTR)", "клик-фру рэйт",
   "Clicks divided by impressions, shown as a percentage.", "Клики, делённые на показы, в процентах.",
   "CTR is flat at 0.5%.", True),
  ("Average position", "эвередж пэзишн",
   "The mean ranking of the site in the results; a lower number is better.", "Средняя позиция в выдаче; чем число меньше, тем лучше.",
   "Average position improved from 7.2 to 6.8.", True),
  ("Top-10 share", "топ-тэн шэр",
   "The percentage of tracked keywords that rank in the first ten results.", "Доля отслеживаемых запросов в топ-10.",
   "The Top-10 share dipped on October 4 and then recovered.", True),
  ("Spike", "спайк",
   "A sudden, short-lived peak on a chart.", "Резкий кратковременный пик на графике.",
   "The previous period had a one-off spike, so the drop looks bigger.", True),
  ("Dip", "дип",
   "A short decline that is usually followed by a recovery.", "Кратковременная просадка, после которой обычно идёт восстановление.",
   "There was a dip on October 4, in the middle of the update.", True),
  ("Flat", "флэт",
   "Not changing; a line with no clear trend up or down.", "Без изменений: ровная линия без тренда.",
   "Both lines are almost flat.", False),
  ("Volatility", "волатилити",
   "Frequent, large changes in rankings or results.", "Нестабильность выдачи: частые и сильные колебания.",
   "Volatility stays high for a week or more after an update ends.", False),
  ("Spam update", "спэм апдэйт",
   "A Google update that targets spammy practices.", "Обновление Google, направленное против спама.",
   "The drop matches the timing of the September spam update.", False),
  ("AI Overview", "эй-ай оувэрвью",
   "The AI-generated answer block above the regular Google results.", "Блок с ответом ИИ над обычной выдачей Google.",
   "The AI Overview takes up space above the classic results.", True),
  ("Referrer", "рэферер",
   "The source a visit came from; some AI tools no longer pass it.", "Источник перехода; часть ИИ-сервисов его больше не передаёт.",
   "ChatGPT stopped passing the referrer for some links.", False),
  ("Low base", "лоу бэйс",
   "A very small starting number, which makes a percentage change look huge.", "Очень малая исходная величина: процент роста выглядит огромным.",
   "Perplexity grew 233%, but from a low base.", True),
  ("Hub page", "хаб пэйдж",
   "A main page that groups and links to related content.", "Хабовая страница: главная страница темы со ссылками на связанные материалы.",
   "We keep strengthening the hub page with links.", False),
  ("Brand visibility", "брэнд визибилити",
   "How often AI answers name the brand.", "Как часто ИИ-ответы называют бренд.",
   "Brand visibility peaked in mid-September at about 20%.", False),
  ("Cluster", "кластер",
   "A group of related pages or keywords.", "Группа связанных страниц или запросов.",
   "The informational cluster is almost flat.", False),
]


def defcell(en, ru):
    return (f'<span style="display:block; font-family:var(--serif); font-style:italic; font-size:14.5px; line-height:1.5;">{e(en)}</span>'
            f'<span class="ru-sub" style="font-size:12.5px; margin-top:6px;">{e(ru)}</span>')


rows_html = ""
for term, pron, en_def, ru_def, ex, priority in TERMS:
    star = "★ " if priority else ""
    cls = ' class="strong-cell"' if priority else ""
    rows_html += (f'<tr><td{cls}>{star}{e(term)}</td><td>{e(pron)}</td><td>{defcell(en_def, ru_def)}</td>'
                  f'<td style="font-family:var(--serif); font-style:italic; font-size:14px; color:var(--ink-soft);">{q(ex)}</td></tr>')

terms_table = ('<div class="table-scroll"><table><thead><tr><th>Term</th><th>Произношение</th>'
               '<th>Definition (EN) / Перевод (RU)</th><th>Example</th></tr></thead>'
               f'<tbody>{rows_html}</tbody></table></div>')

sec_terms = section(
    "terms", "Часть 1 · Report Vocabulary",
    "18 слов, которые нужны, чтобы читать отчёт вслух; ★ — самые важные (10 мин)",
    '<div class="note" style="margin-top:0; margin-bottom:18px;"><strong>О материале.</strong> Урок построен на реальном '
    'отчёте за один отчётный период: настоящие цифры и настоящие скриншоты. Название проекта и домен на скриншотах '
    'скрыты, в тексте клиент называется просто «the client» и «the site».</div>'
    + terms_table + '\n<p class="note">★ = слова, без которых не обойтись при чтении графика</p>',
)


# ================================================================== PART 2 · numbers
number_rows = [
    ("62.2K clicks", "sixty-two point two thousand clicks", "K = thousand; округлённое значение с экрана читаем как есть"),
    ("13.1M impressions", "thirteen point one million impressions", "M = million, K = thousand"),
    ("0.5%", "zero point five percent", "«point», а не «comma»: у англичан десятичная точка"),
    ("7.3", "seven point three", "позиция: после точки цифры читаются по одной"),
    ("3.68M", "three point six eight million", "6 и 8 — по отдельности, не «sixty-eight»"),
    ("1,053", "one thousand fifty-three", "полное число без запятой в речи; «and» не обязателен"),
    ("5,229 keywords", "five thousand two hundred twenty-nine keywords", "для объёма выборки называем полностью"),
    ("−12.7%", "down twelve point seven percent", "минус в речи — «down» или «minus»; «down» звучит естественнее"),
    ("233%", "two hundred thirty-three percent", "для малой базы добавьте: «from a low base»"),
    ("20.09–17.10", "September twentieth to October seventeenth", "даты читаем порядковыми; месяц называем словом, в США месяц идёт первым"),
]
number_table = table_scroll(
    ["На экране", "Как сказать", "Заметка"],
    [(f'<strong>{e(a)}</strong>', f'<span class="en" style="font-family:var(--serif); font-style:italic;">{e(b)}</span>', e(c))
     for a, b, c in number_rows],
)

change_cards = [
    phrase_card("Что изменилось", [
        (q("Clicks went down from 19.7 thousand to 17.2 thousand."), "Клики упали с 19,7 тыс. до 17,2 тыс."),
        (q("Impressions are down 11.5 percent."), "Показы снизились на 11,5 %."),
        (q("CTR stayed flat at 0.5 percent."), "CTR остался на уровне 0,5 %."),
        (q("Perplexity grew from 3 to 10 views, but from a low base."), "У Perplexity просмотры выросли с 3 до 10, но от низкой базы."),
    ]),
    phrase_card("Позиция: вверх или вниз?", [
        (q("Average position improved from 7.2 to 6.8."), "Средняя позиция улучшилась с 7,2 до 6,8."),
        (q("We moved up, so the number went down."), "Мы поднялись, поэтому число уменьшилось."),
        (q("Position slipped slightly, from 20.2 to 20.5."), "Позиция немного просела, с 20,2 до 20,5."),
    ]),
    phrase_card("Осторожно с причинами", [
        (q("The timing matches the September update."), "По времени совпадает с сентябрьским обновлением."),
        (q("The main reason we see is the growing influence of AI Overview."), "Главная причина, которую мы видим, — растущее влияние AI Overview."),
        (q("It looks like a base effect: the previous period had a one-off spike."), "Похоже на эффект базы: в прошлом периоде был разовый пик."),
    ]),
]

sec_numbers = section(
    "numbers", "Часть 2 · Saying the Numbers",
    "как читать цифры, проценты и «лучше/хуже» (8 мин)",
    number_table + '\n<h3 style="margin-top:28px;">Три группы фраз, которые вы будете повторять весь отчёт</h3>\n' + phrase_grid(change_cards)
    + '\n<div class="note"><strong>Ловушка.</strong> «Position went up» — двусмысленно: число выросло или мы поднялись? '
      'Говорите «improved from 7.2 to 6.8» или «moved up from 7.2 to 6.8» — тогда клиент не запутается.</div>',
)


# ================================================================== PART 3 · walk-through of the real report
def screen(num, title, sub, shots, see_ru, say_en, say_ru, phrases):
    figs = "".join(fig(n) for n in shots)
    see = "".join(f"<li>{e(s)}</li>" for s in see_ru)
    pcard = phrase_card("Фразы из этого экрана", [(q(en), e(ru_)) for en, ru_ in phrases])
    body = f'''{figs}
    <h5>Что видно на экране</h5>
    <ul>{see}</ul>
    <h5>Как сказать клиенту</h5>
    <div class="example-block"><span class="en">{e(say_en)}</span><span class="ru">{e(say_ru)}</span></div>
    {pcard}'''
    return dict(title=f"{num}. {title}", sub=sub, body=body)


screens = [
  screen(1, "Общая картина: 3 месяца", "Search Console · клики и показы", [1],
    ["Клики 62,2 тыс., показы 13,1 млн, CTR 0,5 %, средняя позиция 7,3.",
     "Пик в конце августа; с конца сентября дневные значения чуть ниже, провалы глубже.",
     "Бренд и небренд показаны вместе. Дальше разбираем только небренд."],
    "Let's start with the big picture. Over the last three months, the site got 62.2 thousand clicks and 13.1 million impressions. "
    "Average CTR is 0.5 percent and average position is 7.3. Everything was stable until the end of September, with one spike in late August. "
    "Since then, the daily numbers are a bit lower and the dips are deeper, which matches the timing of the September spam update. "
    "This chart shows brand and non-brand together, so from now on we'll look at non-branded traffic only.",
    "Начнём с общей картины. За последние три месяца сайт получил 62,2 тыс. кликов и 13,1 млн показов. Средний CTR 0,5 %, средняя позиция 7,3. "
    "До конца сентября всё было стабильно, с одним пиком в конце августа. С тех пор дневные значения чуть ниже, а провалы глубже, "
    "что по времени совпадает с сентябрьским спам-обновлением. Здесь бренд и небренд вместе, поэтому дальше смотрим только небрендовый трафик.",
    [("Let's start with the big picture.", "Начнём с общей картины."),
     ("Everything was stable until the end of September.", "До конца сентября всё было стабильно."),
     ("The dips are deeper.", "Провалы глубже.")]),

  screen(2, "Небренд: 28 дней против предыдущих 28", "Search Console · сравнение периодов", [2],
    ["Клики 17,2 тыс. против 19,7 тыс. (−12,7 %), показы 3,68 млн против 4,16 млн (−11,5 %).",
     "CTR 0,5 % и там и там. Средняя позиция улучшилась: 6,8 против 7,2.",
     "Пунктир — предыдущий период, сплошная линия — текущий."],
    "Now the comparison: the last 28 days against the previous 28, non-branded only. Clicks went down from 19.7 thousand to 17.2 thousand, "
    "that's minus 12.7 percent. Impressions are down 11.5 percent. CTR is flat at 0.5 percent, and average position actually improved, from 7.2 to 6.8. "
    "So we're not losing rankings. We're losing impressions. Please keep in mind that almost this entire period fell on the September spam update, "
    "so we read the dips with that in mind.",
    "Теперь сравнение: последние 28 дней против предыдущих 28, только небренд. Клики снизились с 19,7 тыс. до 17,2 тыс., то есть на 12,7 %. "
    "Показы упали на 11,5 %. CTR без изменений, 0,5 %, а средняя позиция даже улучшилась: с 7,2 до 6,8. Значит, мы теряем не позиции, а показы. "
    "Учтите, что почти весь период пришёлся на сентябрьское спам-обновление, поэтому просадки читаем с поправкой.",
    [("We're not losing rankings. We're losing impressions.", "Мы теряем не позиции, а показы."),
     ("The dashed line is the previous period.", "Пунктирная линия — предыдущий период."),
     ("We read the dips with that in mind.", "Просадки читаем с поправкой на это.")]),

  screen(3, "Страницы с потерями", "Search Console · топ страниц, небренд", [3],
    ["Больше всего кликов потеряли информационные статьи: −371, −315, −319, −318.",
     "Три статьи из десяти выросли (+157, +71, +37).",
     "У двух статей (сравнение айсберга и ледника, факты про Фолкленды) в прошлом периоде был разовый пик."],
    "Most of the loss comes from a handful of informational articles. The article about the fastest ocean animal lost 371 clicks, and the leopard seal article lost 315. "
    "Two of the declines are partly a base effect, because the iceberg and Falkland Islands articles had one-off spikes in the previous period. "
    "On the positive side, three of the top ten pages grew. The Antarctica population article gained 157 clicks. We'll refresh the Falkland Islands article.",
    "Основная потеря — на нескольких информационных статьях. Статья про самое быстрое океанское животное потеряла 371 клик, статья про морского леопарда — 315. "
    "Два снижения частично объясняются эффектом базы: у статей про айсберги и Фолкленды в прошлом периоде были разовые пики. "
    "Из хорошего: три страницы из десяти выросли, статья про население Антарктиды прибавила 157 кликов. Статью про Фолкленды мы обновим.",
    [("Most of the loss comes from a handful of articles.", "Основная потеря — на нескольких статьях."),
     ("It's partly a base effect.", "Это частично эффект базы."),
     ("We'll refresh the article.", "Мы обновим статью.")]),

  screen(4, "Информационный раздел", "Search Console · /articles/", [4],
    ["Клики 15,5 тыс. против 17,4 тыс., показы 3,59 млн против 4,02 млн: падение примерно на 11 % и там и там.",
     "CTR не изменился (0,4 %), позиция улучшилась: 6,6 против 6,9.",
     "Показы падают, позиции растут: главная причина — растущее влияние AI Overview."],
    "The informational section behaves the same way. Clicks and impressions fell by about the same amount, roughly eleven percent, so CTR didn't change. "
    "Average position improved from 6.9 to 6.6. When impressions drop while positions improve, the main reason we see is the growing influence of AI Overview, "
    "the AI answer block above the regular results. Google keeps experimenting with it, so more users stay inside that block.",
    "Информационный раздел ведёт себя так же. Клики и показы упали примерно на одну величину, около 11 %, поэтому CTR не изменился. "
    "Средняя позиция улучшилась с 6,9 до 6,6. Когда показы падают, а позиции растут, главная причина, которую мы видим, — растущее влияние AI Overview, "
    "блока с ИИ-ответом над обычной выдачей. Google постоянно экспериментирует с ним, и всё больше пользователей остаются внутри этого блока.",
    [("Clicks and impressions fell by about the same amount.", "Клики и показы упали примерно одинаково."),
     ("Impressions drop while positions improve.", "Показы падают, а позиции растут."),
     ("More users stay inside that block.", "Больше пользователей остаются внутри этого блока.")]),

  screen(5, "Коммерческие страницы", "Search Console · небренд", [5],
    ["Клики 744 против 1,12 тыс., показы 102 тыс. против 148 тыс.",
     "CTR 0,7 % против 0,8 %, позиция 20,5 против 20,2.",
     "Коммерческий кластер просел сильнее информационного; падение совпадает по времени с обновлением."],
    "Commercial pages dropped more. Clicks fell from about 1,120 to 744, and impressions from 148 thousand to 102 thousand. "
    "Average position slipped slightly, from 20.2 to 20.5, and CTR from 0.8 to 0.7 percent. The drop matches the timing of the September update. "
    "For our main commercial query, the results page was heavily reshuffled. I'll show you that in the manual check in a minute.",
    "Коммерческие страницы просели сильнее. Клики упали примерно с 1 120 до 744, показы со 148 тыс. до 102 тыс. "
    "Средняя позиция немного просела, с 20,2 до 20,5, CTR — с 0,8 до 0,7 %. Падение совпадает по времени с сентябрьским обновлением. "
    "По главному коммерческому запросу выдачу сильно перестроили: покажу это в ручной проверке через минуту.",
    [("Commercial pages dropped more.", "Коммерческие страницы просели сильнее."),
     ("Position slipped slightly.", "Позиция немного просела."),
     ("The results page was heavily reshuffled.", "Выдачу сильно перестроили.")]),

  screen(6, "AI Overview и AI Mode", "Search Console · показы в ИИ-блоках", [6, 7],
    ["Информационные страницы: 911 тыс. против 912 тыс. показов, без изменений.",
     "В обычной выдаче те же страницы потеряли 10,7 % показов: ИИ-блоки держатся лучше.",
     "Коммерческие страницы: 11,7 тыс. против 16,5 тыс. (−29,1 %), но текущая линия ровная."],
    "Now AI Overview and AI Mode impressions. This is a separate Search Console report, not all of our AI traffic. "
    "Informational pages are cited steadily: 911 thousand impressions against 912 thousand, so no change. In the regular results, the same pages lost 10.7 percent of impressions, "
    "which means the AI blocks hold up better than the classic results. Commercial pages are down 29.1 percent, from 16.5 thousand to 11.7 thousand, "
    "but the current line is flat. The previous period just started much higher.",
    "Теперь показы в AI Overview и AI Mode. Это отдельный отчёт Search Console, а не весь ИИ-трафик. "
    "Информационные страницы цитируются стабильно: 911 тыс. показов против 912 тыс., без изменений. В обычной выдаче эти же страницы потеряли 10,7 % показов, "
    "то есть ИИ-блоки держатся лучше классической выдачи. Коммерческие страницы упали на 29,1 %, с 16,5 тыс. до 11,7 тыс., "
    "но текущая линия ровная: предыдущий период просто начинался гораздо выше.",
    [("This is a separate report, not all of our AI traffic.", "Это отдельный отчёт, а не весь ИИ-трафик."),
     ("Informational pages are cited steadily.", "Информационные страницы цитируются стабильно."),
     ("The previous period just started much higher.", "Предыдущий период просто начинался выше.")]),

  screen(7, "Позиции: сводка", "Rush Analytics · 5 229 запросов, США", [8],
    ["Топ-3: 846 (16 %), −13. Топ-5: 1 396 (27 %), −76. Топ-10: 2 121 (41 %), −161.",
     "Топ-30: 3 441 (66 %), −260. Топ-100: 3 757 (72 %), +56.",
     "Чем шире диапазон, тем больше потеря, но в топ-100 запросов стало больше."],
    "In the rank tracker we follow 5,229 keywords in the US. Top 3: 846 keywords, 16 percent, down 13. Top 5: 1,396 keywords, 27 percent, down 76. "
    "Top 10: 2,121 keywords, 41 percent, down 161. The wider the range, the bigger the loss. Top 30 is down 260. But Top 100 is actually up 56 keywords. "
    "One caveat: since September, Google has been feeding distorted results to rank trackers, about 8 percent according to Nozzle. "
    "So we read these charts as trends, and we checked the key queries by hand.",
    "В трекере позиций мы отслеживаем 5 229 запросов в США. Топ-3: 846 запросов, 16 %, минус 13. Топ-5: 1 396, 27 %, минус 76. "
    "Топ-10: 2 121, 41 %, минус 161. Чем шире диапазон, тем больше потеря: Топ-30 просел на 260. Зато в Топ-100 прибавилось 56 запросов. "
    "Оговорка: с сентября Google подмешивает искажённые результаты в выдачу для трекеров, около 8 % по данным Nozzle. "
    "Поэтому читаем графики как тренд, а важные запросы проверили вручную.",
    [("The wider the range, the bigger the loss.", "Чем шире диапазон, тем больше потеря."),
     ("Top 100 is actually up 56 keywords.", "Топ-100 при этом вырос на 56 запросов."),
     ("We read these charts as trends.", "Мы читаем эти графики как тренд.")]),

  screen(8, "Позиции по кластерам", "Rush Analytics · инфо и коммерция", [9, 10],
    ["Информационный кластер: линии почти плоские, топ-10 медленно снижается (с ~49 % до 45,41 %).",
     "На 18.10: топ-3 — 18,17 % (816), топ-5 — 30,13 % (1 353), топ-10 — 45,41 % (2 039).",
     "Коммерция: просадка топ-10 на 04.10, в разгар обновления, к 18.10 возврат к уровню 20.09."],
    "Let's look at the clusters. In the informational cluster the lines are almost flat. The Top 10 share is sliding slowly, from about 49 to 45 percent, "
    "while Top 5 and Top 3 are holding at 30 and 18 percent. The commercial cluster is at the same level as a month ago, but the results keep shaking. "
    "The Top 10 share dipped on October 4, in the middle of the update, and was back to the September level by October 18. "
    "Top 5 and Top 3 haven't fully recovered yet.",
    "Посмотрим на кластеры. В информационном кластере линии почти плоские. Доля топ-10 медленно снижается, примерно с 49 до 45 %, "
    "а топ-5 и топ-3 держатся на уровне 30 и 18 %. Коммерческий кластер остался на тех же уровнях, что месяц назад, но выдачу постоянно качает. "
    "Доля топ-10 просела 4 октября, в разгар обновления, и к 18 октября вернулась на сентябрьский уровень. "
    "Топ-5 и топ-3 пока восстановились не полностью.",
    [("The lines are almost flat.", "Линии почти плоские."),
     ("The results keep shaking.", "Выдачу постоянно качает."),
     ("It was back to the September level by October 18.", "К 18 октября вернулась на сентябрьский уровень.")]),

  screen(9, "Хабовые страницы", "Rush Analytics · два хаба", [11, 12],
    ["Первый хаб: доля топ-10 растёт, на 18.10 максимум периода (~3,8 %); в топ-3 запросов нет.",
     "Второй хаб: топ-10 упал с ~14 % (20.09) до ~8 % (04.10), частично вернулся к 11.10 и снова снизился к 18.10; в топ-3 впервые появились запросы.",
     "Замеры еженедельные, линии прыгают: это признак нестабильной выдачи, а не тренд."],
    "Two hub pages. On the first one, the Top 10 share grew and hit its maximum for the period on October 18, but there are no queries in the Top 3 at the last measurement. "
    "On the second hub, the Top 10 share fell from about 14 percent to a low of about 8 percent on October 4, then partly recovered. "
    "The measurements are weekly, so the lines go up and down every week. That shows an unstable results page, not a real trend.",
    "Две хабовые страницы. У первой доля топ-10 выросла и на 18 октября достигла максимума за период, но в топ-3 на последнем замере запросов нет. "
    "У второго хаба доля топ-10 упала примерно с 14 % до минимума около 8 % четвёртого октября, потом частично восстановилась. "
    "Замеры еженедельные, поэтому линии каждую неделю идут то вверх, то вниз. Это говорит о нестабильной выдаче, а не о реальном тренде.",
    [("It hit its maximum for the period.", "Достигла максимума за период."),
     ("It partly recovered.", "Частично восстановилась."),
     ("That shows an unstable results page, not a real trend.", "Это показывает нестабильную выдачу, а не тренд.")]),

  screen(10, "Ручная проверка выдачи", "Google US · главный коммерческий запрос", [13],
    ["Перед органикой: платная реклама, AI Overview, блок с подборкой круизов.",
     "Органических результатов всего 5; несколько конкурентов, которые держали топ в прошлом месяце, исчезли.",
     "Выше остались домены с большим авторитетом. План работ не меняется."],
    "We manually checked Google US for our main commercial query. Before the first organic result you see paid ads, an AI Overview and a block of cruise listings. "
    "There are only five organic results. Some competitors who held the top last month are gone from the top ten, but higher-authority domains are still above us. "
    "This doesn't change the plan. We keep strengthening the hub page with links, and we're preparing new commercial pages to diversify.",
    "Мы вручную проверили выдачу Google в США по главному коммерческому запросу. Перед первым органическим результатом идут платная реклама, AI Overview и блок с подборкой круизов. "
    "Органических результатов всего пять. Часть конкурентов, державших топ в прошлом месяце, пропала из топ-10, но выше нас остались домены с большим авторитетом. "
    "Это не меняет план: продолжаем усиливать хабовую страницу ссылками и готовим новые коммерческие страницы для диверсификации.",
    [("There are only five organic results.", "Органических результатов всего пять."),
     ("Higher-authority domains are still above us.", "Выше нас остались домены с большим авторитетом."),
     ("This doesn't change the plan.", "Это не меняет план.")]),

  screen(11, "AI-трафик в GA4", "Google Analytics 4 · сегмент AI Traffic", [14, 15],
    ["Просмотры 715 против 1 094 (−34,6 %), ключевые события 13 против 35 (−62,9 %).",
     "ChatGPT: 656 против 1 008 (−34,9 %). Gemini: 28 против 70 (−60 %). Perplexity: 10 против 3 (низкая база).",
     "ChatGPT перестал отдавать referrer и utm_source для части ссылок: измерять клики сложнее."],
    "Now LLM traffic from GA4, using the AI Traffic segment. ChatGPT is still the main source. Its line is uneven, with a dip in April and a peak in August. "
    "In the last 28 days, AI traffic views fell from 1,094 to 715, that's minus 34.6 percent, and key events from 35 to 13. ChatGPT made the biggest contribution: 656 views against 1,008. "
    "Gemini is down 60 percent, but the numbers are small, 28 versus 70. Perplexity grew from 3 to 10 views, but from a very low base. "
    "Also, ChatGPT stopped passing the referrer for some links, which makes click measurement harder.",
    "Теперь LLM-трафик из GA4, сегмент AI Traffic. ChatGPT остаётся основным источником. Линия неровная: провал в апреле, пик в августе. "
    "За последние 28 дней просмотры AI-трафика упали с 1 094 до 715, то есть на 34,6 %, а ключевые события с 35 до 13. Основной вклад дал ChatGPT: 656 просмотров против 1 008. "
    "Gemini просел на 60 %, но числа маленькие: 28 против 70. У Perplexity просмотры выросли с 3 до 10, но от очень низкой базы. "
    "К тому же ChatGPT перестал передавать referrer для части ссылок, из-за чего клики измерять сложнее.",
    [("ChatGPT is still the main source.", "ChatGPT остаётся основным источником."),
     ("The numbers are small.", "Числа маленькие."),
     ("That makes click measurement harder.", "Из-за этого клики измерять сложнее.")]),

  screen(12, "Видимость в ответах ИИ", "Rush Analytics AI-трекер · 7 платформ", [16, 17],
    ["Видимость бренда достигла максимума в середине сентября (~20 %), сейчас 15,8 %. Видимость домена растёт.",
     "Конкуренты: Quark 67,3 %, Lindblad 47,6 %, National Geographic 44,5 %. Наш бренд — 15,8 %, 88 упоминаний.",
     "Тональность упоминаний остаётся позитивной."],
    "Last block: visibility in AI answers, from the AI tracker, which monitors seven LLM platforms. Brand visibility peaked in mid-September at about 20 percent and is now 15.8 percent, "
    "so the brand is named a little less often. Domain visibility keeps growing: AI links to the site more often as a source. "
    "In the competitor table, Quark leads with 67.3 percent, then Lindblad with 47.6 and National Geographic with 44.5. Several expedition brands are ahead of us, "
    "and the sentiment toward our brand stays positive.",
    "Последний блок: видимость в ответах ИИ по данным AI-трекера, который мониторит семь LLM-платформ. Видимость бренда достигла максимума в середине сентября, около 20 %, сейчас 15,8 %: "
    "бренд называют чуть реже. Видимость домена продолжает расти: ИИ чаще ссылается на сайт как на источник. "
    "В таблице конкурентов лидирует Quark с 67,3 %, затем Lindblad с 47,6 % и National Geographic с 44,5 %. Несколько экспедиционных брендов выше нас, "
    "а тональность упоминаний нашего бренда остаётся позитивной.",
    [("Brand visibility peaked in mid-September.", "Видимость бренда достигла пика в середине сентября."),
     ("AI links to the site more often as a source.", "ИИ чаще ссылается на сайт как на источник."),
     ("Several brands are ahead of us.", "Несколько брендов выше нас.")]),
]

sec_walk = section(
    "walkthrough", "Часть 3 · Walk-through: the Real Report",
    "12 экранов отчёта: что видно, как сказать и фразы для заимствования (25 мин)",
    '<div class="note" style="margin-top:0; margin-bottom:18px;">Читайте вслух блок «Как сказать клиенту» (1–1,5 минуты на экран), затем закройте текст и перескажите по скриншоту.</div>'
    + accordion(screens, single=True, first_open=True),
)


# ================================================================== PART 4 · client questions
def qa(num, title, sub, question, answer_en, answer_ru):
    body = f'''<ul class="phrase-list">
      <li><span class="tag-role">клиент</span><br><span class="en">{q(question)}</span></li>
      <li><span class="tag-role">образец ответа</span><br><span class="en">{q(answer_en)}</span><span class="ru">— {e(answer_ru)}</span></li>
    </ul>'''
    return dict(title=f"{num}. {title}", sub=sub, body=body)


qa_items = [
  qa(1, "Positions up, traffic down?", "экран 2 · почему падают клики",
     "Our positions improved, but traffic is down. How is that possible?",
     "Good question. Average position improved from 7.2 to 6.8, so we're not losing rankings. What we're losing is impressions, about 11.5 percent. "
     "The main reason we see is the AI Overview taking up space above the classic results, so fewer people see and click the listings. "
     "That's why CTR stayed flat while both clicks and impressions went down.",
     "Хороший вопрос. Средняя позиция улучшилась с 7,2 до 6,8, значит, позиции мы не теряем. Теряем показы, около 11,5 %. "
     "Главная причина, которую мы видим, — AI Overview занимает место над обычной выдачей, поэтому меньше людей видят и кликают сниппеты. "
     "Поэтому CTR остался прежним, а клики и показы снизились."),
  qa(2, "Did Google penalize us?", "экраны 1–3 · спам-обновление",
     "Did Google penalize us in the September update?",
     "We don't see signs of a penalty. The drop matches the timing of the update, but the losses are concentrated in a few informational articles, and two of them were coming off one-off spikes. "
     "Results usually stay unstable for at least a week after an update ends, so we'll keep monitoring and update you in the next report.",
     "Признаков штрафа мы не видим. Падение совпадает по времени с обновлением, но потери сосредоточены на нескольких информационных статьях, и две из них шли после разовых пиков. "
     "После обновления выдача обычно остаётся нестабильной минимум неделю, поэтому продолжим мониторинг и расскажем в следующем отчёте."),
  qa(3, "Why are commercial pages down by a third?", "экран 5 · малая база",
     "Why did commercial pages drop by a third?",
     "Commercial pages are a small share of traffic, 744 clicks out of about 17,200 non-branded clicks, so a small base moves fast. "
     "The drop matches the update, and on our main query the results page was heavily reshuffled. Our plan doesn't change: we keep strengthening the hub page with links, "
     "and we're preparing briefs for two new commercial pages.",
     "Коммерческие страницы — небольшая доля трафика, 744 клика из примерно 17 200 небрендовых, поэтому малая база двигается быстро. "
     "Падение совпадает с обновлением, а по главному запросу выдачу сильно перестроили. План не меняется: продолжаем усиливать хабовую страницу ссылками "
     "и готовим ТЗ на две новые коммерческие страницы."),
  qa(4, "Should we worry about AI Overview?", "экран 6",
     "What's happening with AI Overviews? Should we worry?",
     "Our informational pages are cited steadily: impressions in AI Overview and AI Mode are flat at about 911 thousand, while classic impressions for the same pages fell 10.7 percent. "
     "So AI blocks are holding up better than the regular results. Commercial impressions in AI blocks are down 29 percent, but the current line is flat, because the previous period started higher.",
     "Информационные страницы цитируются стабильно: показы в AI Overview и AI Mode на уровне около 911 тыс., а в классической выдаче те же страницы потеряли 10,7 %. "
     "ИИ-блоки держатся лучше обычной выдачи. Коммерческие показы в ИИ-блоках упали на 29 %, но текущая линия ровная: предыдущий период начинался выше."),
  qa(5, "ChatGPT traffic is down 35%", "экран 11 · низкие числа",
     "ChatGPT traffic is down 35 percent. Is AI visibility worth investing in?",
     "I'd read it as a trend, not a verdict, because the numbers are small: 656 views in 28 days. ChatGPT and Gemini dropped together with organic results, which makes sense because they pull from live search results. "
     "Also, ChatGPT stopped passing the referrer for some links, so we can't measure every click. Meanwhile domain visibility in AI answers is growing: AI links to us more often as a source.",
     "Я бы читала это как тренд, а не приговор, потому что числа небольшие: 656 просмотров за 28 дней. ChatGPT и Gemini просели вместе с органикой, что логично: они берут данные из живой выдачи. "
     "К тому же ChatGPT перестал передавать referrer для части ссылок, поэтому мы видим не все клики. При этом видимость домена в ответах ИИ растёт: ИИ чаще ссылается на нас как на источник."),
  qa(6, "Why no single-keyword positions?", "экран 7 · как мы измеряем",
     "Why don't you report positions for individual keywords?",
     "Single keywords go up and down, and that doesn't show how a page or a cluster behaves. So we track the share of keywords in the Top 3, 5 and 10. "
     "Also, since September Google has been feeding distorted results to rank trackers, so we read the charts as trends and check important queries by hand.",
     "Отдельные запросы то растут, то падают, и по ним не видно, как ведёт себя страница или кластер. Поэтому мы смотрим долю запросов в топ-3, 5 и 10. "
     "К тому же с сентября Google подмешивает искажённые результаты для трекеров, поэтому графики читаем как тренд, а важные запросы проверяем вручную."),
  qa(7, "Competitors are above us. Plan?", "экран 10 · следующий период",
     "Competitors are still above us. What's the plan for next period?",
     "Higher-authority domains still outrank us on the main query. Next period we're focusing on four things: strengthening the hub page with links, briefs for new commercial and informational pages, "
     "keyword research for the middle of the funnel, such as comparisons and alternatives, and goals for the new CTA block, so we can measure conversions. We'll also monitor whether our links are live and indexed.",
     "Домены с большим авторитетом пока выше нас по главному запросу. В следующем периоде фокус на четырёх вещах: усиление хабовой страницы ссылками, ТЗ на новые коммерческие и информационные страницы, "
     "исследование ключевых слов середины воронки (сравнения и альтернативы) и цели для нового CTA-блока, чтобы измерять конверсии. Также проверяем, что ссылки стоят и проиндексированы."),
]

sec_qa = section(
    "qa", "Part 4 · Client Questions",
    "7 вопросов клиента к этому отчёту с образцами ответов (15 мин)",
    '<div class="note" style="margin-top:0; margin-bottom:18px;">Сначала ответьте сами за 30 секунд, потом сверьтесь с образцом. '
    'Обратите внимание на структуру: <strong>цифра → причина с оговоркой → что делаем дальше</strong>.</div>'
    + accordion(qa_items, single=True, first_open=False),
)


# ================================================================== PART 5 · drills + homework
gaps = [
  ("Average position ______ from 7.2 to 6.8.", "improved", "позиция улучшилась (не «went up»)"),
  ("Clicks are ______ 12.7 percent compared with the previous period.", "down", "клики снизились на 12,7 %"),
  ("Both lines are almost ______, with no clear trend.", "flat", "ровные линии"),
  ("The previous period had a one-off ______, so the drop looks bigger.", "spike", "разовый пик"),
  ("Perplexity grew 233 percent, but from a very low ______.", "base", "от низкой базы"),
  ("The drop ______ with the timing of the September update.", "matches / coincides", "совпадает по времени"),
  ("Results stay ______ for at least a week after an update ends.", "unstable / volatile", "нестабильна"),
  ("The number is small, so I'd read it as a ______, not a verdict.", "trend", "тренд, а не приговор"),
]
gap_html = "".join(
    f'<li><span class="en">{e(s)}</span><br><details class="ans"><summary>ответ</summary><span class="ru"><strong>{e(a)}</strong> — {e(ru_)}</span></details></li>'
    for s, a, ru_ in gaps)

drill_items = [
  dict(title="A. Заполните пропуски", sub="8 предложений из отчёта",
       body=f'<ul class="phrase-list">{gap_html}</ul>'),
  dict(title="B. Прочитайте экран за 60 секунд", sub="одиночная практика",
       body='<ul class="phrase-list">'
            '<li><span class="ru">Откройте любой скриншот из части 3, закройте текст и расскажите экран вслух за 60 секунд: '
            '<strong>что за график → главная цифра → сравнение → причина с оговоркой</strong>. Запишите на диктофон и сверьте с образцом.</span></li>'
            '<li><span class="ru">Проверка: назвали ли вы период сравнения («28 days against the previous 28»)? Сказали ли «improved», а не «went up», про позицию?</span></li></ul>'),
  dict(title="C. Ролевая игра: клиент на созвоне", sub="в паре, 15 минут",
       body='<ul class="phrase-list">'
            '<li><span class="tag-role">специалист</span><br><span class="ru">Проводит партнёра по трём экранам: общий трафик, один кластер, AI-трафик. По 90 секунд на экран.</span></li>'
            '<li><span class="tag-role">клиент</span><br><span class="ru">После каждого экрана задаёт один неудобный вопрос из части 4 (или свой). Специалист отвечает по схеме «цифра → причина с оговоркой → что делаем».</span></li>'
            '<li><span class="ru">Поменяйтесь ролями. Клиент в конце называет одно место, где ему было непонятно.</span></li></ul>'),
  dict(title="D. Следующий период: say the plan", sub="план работ → английский",
       body=phrase_card("Фразы для плана", [
           (q("Next period, we'll prepare briefs for two new commercial pages."), "В следующем периоде подготовим ТЗ на две новые коммерческие страницы."),
           (q("We'll research mid-funnel keywords: comparisons and alternatives."), "Исследуем запросы середины воронки: сравнения и альтернативы."),
           (q("We'll set up goals for the new CTA block."), "Настроим цели для нового CTA-блока."),
           (q("We'll monitor whether the links are live and indexed."), "Будем мониторить, что ссылки на месте и проиндексированы."),
           (q("We'll analyze the performance of the existing content."), "Проанализируем эффективность существующего контента."),
       ])),
]

check = [
    "Назвал период и базу сравнения («last 28 days against the previous 28»).",
    "Сказал, что именно смотрим: небренд, раздел, кластер.",
    "Позицию описал словами improved / slipped, а не «went up».",
    "Рядом с каждым падением есть причина с оговоркой («the main reason we see…»), без громких обещаний.",
    "Малые числа назвал малыми, рост от малой базы — «from a low base».",
    "Закончил экран тем, что делаем дальше.",
]
check_html = "".join(f"<li>{e(c)}</li>" for c in check)

sec_practice = section(
    "practice", "Часть 5 · Practice & Homework",
    "четыре упражнения по реальным данным и чек-лист для домашнего задания (20 мин)",
    accordion(drill_items, single=True, first_open=False)
    + f'''<div class="info-card" style="margin-top:24px;">
  <div class="info-head"><h3>Домашнее задание<small>отчёт вслух по своему проекту</small></h3></div>
  <p class="idea">Возьмите свой последний отчёт и расскажите 3 экрана на английском за 5 минут. Проверьте себя по списку:</p>
  <ol class="idea" style="padding-left:22px; line-height:1.7;">{check_html}</ol>
</div>''',
)

body = "\n".join([sec_terms, sec_numbers, sec_walk, sec_qa, sec_practice])

html = page(
    title="Урок 17 — Разбор реального отчёта вслух",
    desc="Как провести клиента по месячному отчёту на английском: Search Console, позиции, GA4, AI-трафик. Реальные скриншоты, образцы речи и ответы на вопросы клиента.",
    brand="Global English · Урок 17",
    eyebrow="Урок 17 из курса «Global English для SEO»",
    h1="Разбор реального отчёта вслух",
    lede="Берём настоящий отчёт за отчётный период и проходим его экран за экраном: как прочитать цифры, объяснить падение без паники, ответить на неудобные вопросы и закончить планом. Название проекта на скриншотах скрыто.",
    navlinks=[("#terms", "Термины"), ("#numbers", "Цифры"), ("#walkthrough", "Разбор"), ("#qa", "Вопросы"), ("#practice", "Практика")],
    body=body,
    prev_href="/lessons/16/", prev_label="← Урок 16: Follow-up и задержки",
    next_href="/", next_label="Все уроки →",
)
out = os.path.join(REPO, "lessons", "17", "index.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote lessons/17/index.html", len(html), "bytes")
