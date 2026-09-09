# -*- coding: utf-8 -*-
from build import page, section, accordion, table_scroll, write

def verb_table(rows):
    # rows: (prep, meaning, en, ru)
    trs = "".join(
        f'<tr><td class="strong-cell">{prep}</td><td>{meaning}</td><td><span class="en">{en}</span><span class="ru-sub">{ru}</span></td></tr>'
        for prep, meaning, en, ru in rows
    )
    return f'<div class="xcard-scroll"><table class="xcard-table"><thead><tr><th>Предлог</th><th>Значение</th><th>Пример</th></tr></thead><tbody>{trs}</tbody></table></div>'

verbs = {
  "CALL": [
    ("off","отменять","We had to call off the link-building campaign due to budget cuts.","Нам пришлось отменить кампанию по наращиванию ссылок из-за сокращения бюджета."),
    ("back","перезванивать","I'll call the client back after I check the analytics.","Я перезвоню клиенту после того, как проверю аналитику."),
    ("on","призывать","The SEO manager called on the team to focus on core web vitals.","SEO-менеджер призвал команду сосредоточиться на Core Web Vitals."),
    ("for","требовать","This drop in rankings calls for an immediate site audit.","Это падение позиций требует немедленного аудита сайта."),
    ("out","называть / требовать объяснить","The report called out the pages with thin content.","В отчёте назвали страницы с «тонким» контентом."),
    ("in","вызывать","We called in an expert to fix the crawl errors.","Мы вызвали эксперта, чтобы исправить ошибки сканирования."),
    ("up","звонить","He called up the hosting support to resolve the server issue.","Он позвонил в поддержку хостинга, чтобы решить проблему с сервером."),
    ("around","обзванивать","I called around to find the best backlink opportunities.","Я обзвонил всех, чтобы найти лучшие возможности для обратных ссылок."),
  ],
  "SET": [
    ("up","организовывать / устанавливать","They set up a new SEO strategy.","Они организовали новую SEO-стратегию."),
    ("off","отправляться","We set off early to implement the changes before the algorithm update.","Мы отправились рано, чтобы внедрить изменения до обновления алгоритма."),
    ("out","излагать","She set out the project goals in the brief.","Она изложила цели проекта в брифе."),
    ("back","задерживать","The server crash set us back by two days.","Сбой сервера задержал нас на два дня."),
    ("aside","откладывать","Set aside some time for a technical audit next week.","Отложи немного времени на технический аудит на следующей неделе."),
    ("in","наступать","Winter traffic fluctuations have set in.","Наступили зимние колебания трафика."),
    ("down","записывать","He set down all the keywords in a spreadsheet.","Он записал все ключевые слова в таблицу."),
    ("about","приниматься за дело","She set about optimizing the meta tags.","Она принялась оптимизировать мета-теги."),
  ],
  "GET": [
    ("up","вставать","I get up early to check the rankings.","Я встаю рано, чтобы проверить позиции."),
    ("over","оправляться","The site hasn't gotten over the Google core update yet.","Сайт ещё не оправился после основного обновления Google."),
    ("along with","ладить","Our team gets along with the developers very well.","Наша команда очень хорошо ладит с разработчиками."),
    ("back","возвращаться","When did you get back from the conference?","Когда ты вернулся с конференции?"),
    ("away","уезжать / сбежать","We need to get away from old SEO tactics.","Нам нужно уйти от старых SEO-тактик."),
    ("through","дозваниваться / справляться","I couldn't get through to the support; but we'll get through this crisis.","Я не мог дозвониться в поддержку, но мы справимся с этим кризисом."),
    ("across","доносить мысль","He got his point across about the importance of page speed.","Он донёс свою мысль о важности скорости загрузки страниц."),
    ("by","справляться минимально","We can get by with this small budget for now.","Мы можем обойтись этим небольшим бюджетом пока что."),
  ],
  "RUN": [
    ("into","случайно встретить","I ran into an old colleague at the SEO meetup.","Я случайно встретил старого коллегу на встрече SEO-специалистов."),
    ("out of","закончиться","We've run out of time for this month's link building.","У нас закончилось время на линкбилдинг в этом месяце."),
    ("over","бегло просмотреть","Let's run over the main points of the report.","Давай быстро пробежимся по основным пунктам отчёта."),
    ("away","убежать","Some clients try to run away from technical issues.","Некоторые клиенты пытаются убежать от технических проблем."),
    ("through","пробежаться по чему-то","Let's run through the core web vitals checklist.","Давай пробежимся по чек-листу Core Web Vitals."),
    ("up","накапливать","He ran up a huge bill on SEO tools.","Он накопил огромный счёт за SEO-инструменты."),
    ("down","критиковать / разряжаться","Stop running down your competitor's site; focus on yours.","Перестань критиковать сайт конкурента; сосредоточься на своём."),
    ("by","обсудить","Let me run this idea by the client.","Дай я обсужу эту идею с клиентом."),
  ],
  "PUT": [
    ("off","откладывать","We had to put off the site migration until next month.","Нам пришлось отложить перенос сайта до следующего месяца."),
    ("on","надевать / включать","She put on her headphones to focus on the analytics.","Она надела наушники, чтобы сосредоточиться на аналитике."),
    ("up with","терпеть","I can't put up with this slow hosting anymore.","Я больше не могу терпеть этот медленный хостинг."),
    ("out","тушить","He put out the fire on the homepage.","Он потушил пожар (исправил критическую ошибку) на главной странице."),
    ("away","убрать на место","Put away your old keyword lists; we have new ones.","Убери свои старые списки ключевых слов; у нас есть новые."),
    ("down","записывать / унижать","Put down the new search volume in your notebook.","Запиши новый объём поиска в свой блокнот."),
    ("forward","выдвигать идею","She put forward a proposal to restructure the site.","Она выдвинула предложение по реструктуризации сайта."),
    ("up","размещать / строить","They put up a new landing page for the campaign.","Они разместили новую посадочную страницу для кампании."),
  ],
  "TURN": [
    ("into","превращаться","The old blog post turned into a comprehensive guide.","Старый пост в блоге превратился в подробное руководство."),
    ("down","отклонять / уменьшать","I turned down the low-quality guest post.","Я отклонил низкокачественный гостевой пост."),
    ("on","включать","Turn on the VPN to check regional rankings.","Включи VPN, чтобы проверить региональные позиции."),
    ("off","выключать","Don't turn off the crawl tool yet.","Не выключай инструмент сканирования пока."),
    ("out","оказываться","It turned out that the backlink was nofollow.","Оказалось, что обратная ссылка была nofollow."),
    ("around","меняться к лучшему","The site's traffic turned around after the redesign.","Трафик сайта пошёл в гору после редизайна."),
    ("up","усиливать","We need to turn up our link-building efforts.","Нам нужно увеличить наши усилия по линкбилдингу."),
  ],
  "GIVE": [
    ("away","выдавать, разоблачать","The thin content gave away the poor quality of the page.","Тонкий контент выдал низкое качество страницы."),
    ("back","возвращать","The tool gave back the data we needed.","Инструмент вернул данные, которые нам были нужны."),
    ("in","соглашаться","He gave in and accepted the client's unreasonable keyword demands.","Он согласился и принял необоснованные требования клиента по ключевым словам."),
    ("out","раздавать","The speaker gave out free SEO checklists at the conference.","Спикер раздавал бесплатные SEO-чек-листы на конференции."),
    ("off","выделять","This page gives off spammy signals to Google.","Эта страница посылает спамные сигналы Google."),
    ("up","сдаваться, отказываться","Don't give up on ranking for that keyword; try a different approach.","Не сдавайся в попытках ранжироваться по этому ключу; попробуй другой подход."),
    ("up on","терять надежду","He has given up on understanding the new algorithm.","Он потерял надежду понять новый алгоритм."),
  ],
  "BREAK": [
    ("away","вырваться","We need to break away from old SEO myths.","Нам нужно вырваться из старых SEO-мифов."),
    ("into","вломиться, проникнуть","The hacker tried to break into the CMS, but we blocked him.","Хакер пытался вломиться в CMS, но мы его заблокировали."),
    ("down","сломаться","The server broke down during peak traffic.","Сервер сломался в часы пикового трафика."),
    ("out","вырваться, стать известным","The news broke out about the new Google update.","Всплыли новости о новом обновлении Google."),
    ("off","внезапно прекратить","She broke off the conversation to check the analytics alert.","Она прервала разговор, чтобы проверить оповещение аналитики."),
    ("through","прорваться, преодолеть","He broke through all obstacles and reached the top of SERPs.","Он прорвался через все препятствия и достиг топа выдачи."),
    ("up","закончить отношения","They broke up after the agency lost the client.","Они разошлись после того, как агентство потеряло клиента."),
  ],
  "GO": [
    ("away","уходить","The old ranking factors are going away.","Старые факторы ранжирования уходят."),
    ("up","подниматься, увеличиваться","Our traffic went up after the fix.","Наш трафик вырос после исправления."),
    ("back","возвращаться","We are going back to the previous SEO strategy.","Мы возвращаемся к предыдущей SEO-стратегии."),
    ("on","продолжаться","Go on optimizing the site despite the difficulties.","Продолжай оптимизировать сайт, несмотря на трудности."),
    ("out","заканчиваться","The session has gone out.","Сессия закончилась (истекла)."),
    ("off","срабатывать","The alert went off when the site went down.","Сигнализация сработала, когда сайт упал."),
    ("after","преследовать, следовать","We are going after high-quality backlinks.","Мы охотимся за высококачественными обратными ссылками."),
    ("down","падать, снижаться","Rankings went down after the core update.","Позиции упали после основного обновления."),
  ],
  "HOLD": [
    ("on","подождать","Hold on a minute while I pull up the search console data.","Подожди минуту, пока я загружу данные Search Console."),
    ("back","сдерживать","He held back the report until he verified the numbers.","Он не публиковал отчёт, пока не проверил цифры."),
    ("out","не сдаваться","They held out for days despite the ranking drop.","Они держались несколько дней, несмотря на падение позиций."),
    ("up","задерживать","Slow loading holds up the page rendering.","Медленная загрузка задерживает рендеринг страницы."),
    ("off","откладывать","They held off the meeting until the audit was complete.","Они отложили встречу до завершения аудита."),
    ("onto","держаться за, сохранять","She held onto hope that the traffic would recover.","Она держалась за надежду, что трафик восстановится."),
    ("against","иметь обиду","Don't hold it against him; he's new to SEO.","Не держи на него обиды; он новичок в SEO."),
    ("down","удерживать (работу)","She held down two SEO projects simultaneously.","Она вела два SEO-проекта одновременно."),
  ],
  "COME": [
    ("up","появляться","An idea came up during the brainstorming session.","Идея появилась во время мозгового штурма."),
    ("across","наткнуться","I came across an interesting case study on voice search.","Я наткнулся на интересное исследование по голосовому поиску."),
    ("back","возвращаться","She came back from the conference with new insights.","Она вернулась с конференции с новыми идеями."),
    ("out","выходить, становиться известным","The new Google update came out yesterday.","Новое обновление Google вышло вчера."),
    ("in","входить","He came in with a fresh perspective on link building.","Он пришёл со свежим взглядом на линкбилдинг."),
    ("over","заходить в гости","The client came over to discuss the strategy.","Клиент приезжал, чтобы обсудить стратегию."),
    ("down","снижаться","Prices for SEO tools came down after the discount.","Цены на SEO-инструменты снизились после скидки."),
    ("along","продвигаться","The project came along well; want to come along to the meeting?","Проект продвигался хорошо; хочешь присоединиться к встрече?"),
  ],
  "TAKE": [
    ("off","снимать","Take off any noindex tags before launch.","Сними все теги noindex перед запуском."),
    ("on","брать на работу","The company is taking on new SEO specialists.","Компания нанимает новых SEO-специалистов."),
    ("over","принимать управление","Who will take over the project when you leave?","Кто примет проект, когда ты уйдёшь?"),
    ("in","понимать, усваивать","I couldn't take in all the information from the webinar at once.","Я не мог усвоить всю информацию с вебинара сразу."),
    ("out","вынимать","He took out his laptop to show the analytics.","Он достал свой ноутбук, чтобы показать аналитику."),
    ("back","возвращать","I need to take this book back to the library.","Мне нужно вернуть эту книгу в библиотеку."),
    ("up","начинать заниматься","She took up learning Python for SEO.","Она начала заниматься изучением Python для SEO."),
    ("down","записывать","Let me take down your suggestions.","Дай я запишу твои предложения."),
  ],
  "PICK": [
    ("up","подбирать / учить","She picked up SEO skills quickly.","Она быстро освоила навыки SEO."),
    ("out","выбирать","He picked out the best keywords for the campaign.","Он выбрал лучшие ключевые слова для кампании."),
    ("on","придираться","The algorithm seems to pick on sites with thin content.","Алгоритм, кажется, придирается к сайтам с тонким контентом."),
    ("at","ковырять / придираться","Stop picking at the design; focus on content.","Перестань ковыряться в дизайне; сосредоточься на контенте."),
    ("off","убирать по одному","We picked off low-quality backlinks one by one.","Мы убрали низкокачественные обратные ссылки одну за другой."),
    ("over","перебирать","She picked over the data to find the outliers.","Она перебрала данные, чтобы найти выбросы."),
    ("through","просматривать","He picked through old reports to find the mistake.","Он просмотрел старые отчёты, чтобы найти ошибку."),
    ("apart","разбирать / критиковать","Critics picked apart the new SEO strategy.","Критики разобрали новую SEO-стратегию."),
  ],
  "LOOK": [
    ("for","искать","I'm looking for the source of the traffic drop.","Я ищу источник падения трафика."),
    ("at","смотреть на","Look at this spike in impressions!","Посмотри на этот скачок показов!"),
    ("after","заботиться, присматривать","She looks after the client's website like it's her own.","Она заботится о сайте клиента, как о своём собственном."),
    ("like","выглядеть как","This graph looks like a steady growth pattern.","Этот график выглядит как модель устойчивого роста."),
    ("up","искать (информацию)","Look up the search volume for that term.","Найди объём поиска для этого термина."),
    ("down","смотреть свысока","He looked down and saw the error in the code.","Он опустил взгляд и увидел ошибку в коде."),
    ("back","вспоминать","She looked back at the old data to find a trend.","Она оглянулась на старые данные, чтобы найти тренд."),
    ("ahead","смотреть вперёд","Look ahead at the upcoming algorithm changes.","Смотри вперёд на предстоящие изменения алгоритма."),
  ],
  "BRING": [
    ("up","поднимать тему","They brought up the issue of duplicate content.","Они подняли проблему дублированного контента."),
    ("about","вызывать","The update brought about ranking fluctuations.","Обновление вызвало колебания позиций."),
    ("back","возвращать","The old data brought back insights.","Старые данные напомнили идеи."),
    ("in","приносить (доход)","The new landing page brought in a lot of organic traffic.","Новая посадочная страница принесла много органического трафика."),
    ("out","выявлять","The audit brought out hidden issues.","Аудит выявил скрытые проблемы."),
    ("down","снизить","The change brought down our rankings.","Изменение снизило наши позиции."),
    ("over","приносить с собой","The new developer brought over fresh ideas.","Новый разработчик принёс с собой свежие идеи."),
    ("forward","выдвигать предложение","They brought forward a proposal to restructure the site.","Они выдвинули предложение по реструктуризации сайта."),
  ],
  "KEEP": [
    ("on","продолжать","Keep on optimizing; you'll see results.","Продолжай оптимизировать; ты увидишь результаты."),
    ("up","поддерживать темп","You're doing great — keep it up!","У тебя отлично получается — продолжай в том же духе!"),
    ("away","держаться подальше","Keep away from black-hat techniques.","Держись подальше от чёрных методов SEO."),
    ("off","не касаться","Keep off toxic domains.","Держись подальше от токсичных доменов."),
    ("out","не пускать","Keep out of spam folders.","Не попадай в спам-папки."),
    ("back","скрывать","Keep back the negative data until we verify it.","Придержи негативные данные, пока мы их не проверим."),
    ("down","сдерживать","Keep your expectations down.","Сдерживай свои ожидания."),
    ("to","придерживаться","Keep to the keyword strategy we agreed on.","Придерживайся стратегии ключевых слов, которую мы согласовали."),
  ],
  "DO": [
    ("without","обходиться без","There's no budget for new tools, so we'll have to do without.","Нет бюджета на новые инструменты, так что нам придётся обходиться без них."),
    ("over","переделать","The client asked to do the report over.","Клиент попросил переделать отчёт."),
    ("in","сильно утомиться","I'm completely done in after that all-night site migration.","Я полностью вымотан после той ночной миграции сайта."),
    ("up","приводить в порядок","They are doing up an old website with a fresh design.","Они приводят в порядок старый сайт с новым дизайном."),
    ("away with","избавиться","Many sites want to do away with old Flash content.","Многие сайты хотят избавиться от старого Flash-контента."),
    ("over","грабить (взломать)","Their site was done over by cybercriminals.","Их сайт был взломан киберпреступниками."),
  ],
}

items = [{"title": v, "sub": f"{len(rows)} значений", "body": verb_table(rows)} for v, rows in verbs.items()]
sec_verbs = section("verbs", "17 глаголов · все значения", "выбери карточку — раскрой таблицу предлогов",
                     accordion(items, first_open=False))

make_body = table_scroll(["Сочетание", "Значение", "Пример из SEO"], [
  ["make over", "переделывать (сайт, дизайн)", "make over the site structure"],
  ["make in", "производить (контент)", "make in-house content"],
  ["make out", "разбирать, составлять", "make out a link profile"],
  ["make up", "составлять, компенсировать", "make up the content gap"],
  ["make for", "способствовать", "make for better CTR"],
  ["make of", "думать, оценивать", "what do you make of this algorithm?"],
])
sec_make = section("make", "Бонус: MAKE", "ещё шесть сочетаний, которые часто всплывают в обсуждении контента и стратегии",
                    make_body)

body = "\n".join([sec_verbs, sec_make])

html = page(
    title="Урок 9 — Все фразовые глаголы в контексте SEO",
    desc="17 фразовых глаголов (call, set, get, run, put, turn, give, break, go, hold, come, take, pick, look, bring, keep, do) разобраны по предлогам с примерами из повседневной работы SEO-специалиста.",
    brand="Global English · Урок 9",
    eyebrow="Урок 9 из курса «Global English для SEO»",
    h1="Все фразовые глаголы в контексте SEO",
    lede="Каждый глагол разобран по предлогам, и под каждый придуман пример, который пригодится в ежедневной работе: аналитика, оптимизация, ссылки, общение с клиентами и разработчиками.",
    navlinks=[("#verbs","Глаголы"), ("#make","Make")],
    body=body,
    prev_href="/lessons/8/", prev_label="← Урок 8: Reverse Roles",
    next_href="/lessons/10/", next_label="Урок 10: Кейсы с нейтивом →",
)
write("lessons/9/index.html", html)
