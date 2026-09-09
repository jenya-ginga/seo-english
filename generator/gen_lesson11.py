# -*- coding: utf-8 -*-
from build import page, section, phrase_card, phrase_grid, write

# Восемь категорий разговорных связок. Каждая пара — (EN-фраза с переводом в скобках, пример-предложение в контексте SEO).

softener = [
  ("Actually (на самом деле / вообще-то)", "It wasn't the update — it was the broken redirect."),
  ("The thing is, (дело в том, что)", "We can't fix this without dev support."),
  ("That said, (тем не менее / при этом)", "Traffic dropped. That said, conversions are fine."),
  ("Here's the thing: (вот в чём дело)", "Rankings are volatile right now."),
]

cause_effect = [
  ("So basically, (так что по сути / короче говоря)", "The page is too slow. So basically, users leave."),
  ("Which means (that) (что означает / а значит)", "We lost snippets, which means CTR dropped."),
  ("That's why (вот почему / именно поэтому)", "Robots.txt blocked it. That's why it's not indexed."),
  ("As a result, (в результате)", "We fixed 404s. As a result, crawlability improved."),
]

addition = [
  ("Plus, (плюс к этому / ещё)", "We fixed titles. Plus, we improved internal linking."),
  ("On top of that, (вдобавок к этому / мало того)", "The site is slow. On top of that, it's not mobile-friendly."),
  ("Also, (также / ещё)", "We also need to check the page experience report."),
]

explanation = [
  ("I mean, (я имею в виду / то есть)", "CTR dropped — I mean, fewer people click on us."),
  ("As in, (то есть / иными словами)", "It's a soft 404, as in, the page looks empty to Google."),
  ("To be clear, (чтобы было понятно / если говорить прямо)", "We're not losing traffic — we're just seeing a seasonal dip."),
]

opinion = [
  ("To be honest, (честно говоря)", "I didn't expect results this fast."),
  ("Honestly, (честно / по-честному)", "I think we should wait for the next core update."),
  ("My take is, (на мой взгляд / моё мнение такое)", "The competitor's new content hit us."),
  ("To be fair, (справедливости ради / надо признать)", "The drop isn't our fault — it's an algo shift."),
]

reactions = [
  ("That makes sense. (логично / понятно / это понятно)", "«We should focus on content first.» → «That makes sense.»"),
  ("Fair enough. (резонно / ладно, согласен)", "«We need more time for proper testing.» → «Fair enough.»"),
  ("Got it. (понял / принял)", "«Check the index status first.» → «Got it.»"),
  ("No worries. (ничего страшного / всё нормально)", "«Sorry for the delay.» → «No worries.»"),
  ("It depends. (зависит от ситуации / смотря как)", "«Will we hit page 1?» → «It depends on the competition.»"),
]

transitions = [
  ("By the way, (кстати / между прочим)", "Did we check the page experience report?"),
  ("Speaking of which, (кстати об этом / раз уж зашла речь)", "Speaking of backlinks, we got a new one from Forbes."),
  ("As for... (что касается... / по поводу...)", "As for your question about the budget, I suggest we move it to content."),
  ("Anyway, (в любом случае / ладно, возвращаясь к теме)", "Let's get back to the audit results."),
]

fillers = [
  ("You know, (ну, ты понимаешь / как бы)", "Rankings are, you know, a bit unstable right now."),
  ("How do I put it? (как бы это сказать? / как это выразить?)", "The client's reaction was... how do I put it? Emotional."),
  ("For what it's worth, (на мой взгляд / если это что-то значит)", "I think the site structure is okay."),
  ("At the end of the day, (в конечном счёте / если по-честному)", "The user experience matters most."),
]

sec1 = section("softener", "1 · Мягкое уточнение / поправка", "вместо сухого however",
               phrase_grid([phrase_card("Мягкое уточнение", softener)]))

sec2 = section("cause-effect", "2 · Причина / следствие", "вместо сухого therefore",
               phrase_grid([phrase_card("Причина и следствие", cause_effect)]))

sec3 = section("addition", "3 · Добавление", "вместо moreover / in addition",
               phrase_grid([phrase_card("Добавление мысли", addition)]))

sec4 = section("explanation", "4 · Пояснение / перефразирование", "когда нужно сказать то же самое проще",
               phrase_grid([phrase_card("Пояснение", explanation)]))

sec5 = section("opinion", "5 · Выражение мнения", "как звучать честно, а не резко",
               phrase_grid([phrase_card("Мнение", opinion)]))

sec6 = section("reactions", "6 · Реакции в диалоге", "короткие ответы, которые держат разговор живым",
               phrase_grid([phrase_card("Реакции", reactions)]))

sec7 = section("transitions", "7 · Переходы в разговоре", "как сменить тему, не обрывая нить",
               phrase_grid([phrase_card("Переходы", transitions)]))

sec8 = section("fillers", "8 · Заполнители пауз", "чтобы не молчать, пока формулируешь мысль",
               phrase_grid([phrase_card("Заполнители пауз", fillers)]))

body = "\n".join([sec1, sec2, sec3, sec4, sec5, sec6, sec7, sec8])

html = page(
    title="Урок 11 — Словарик: разговорные связки SEO-специалиста",
    desc="Американский разговорник SEO-специалиста: 8 категорий связок, которые реально используют в деловых звонках, на митингах и в чатах — вместо книжного however и therefore.",
    brand="Global English · Урок 11",
    eyebrow="Урок 11 из курса «Global English для SEO»",
    h1="Словарик: как звучать по-человечески",
    lede="Только то, что реально говорят американские коллеги в деловых звонках, на митингах и в чатах — восемь категорий связок вместо книжных however и therefore.",
    navlinks=[
        ("#softener", "Уточнение"),
        ("#cause-effect", "Причина/следствие"),
        ("#opinion", "Мнение"),
        ("#reactions", "Реакции"),
    ],
    body=body,
    prev_href="/lessons/10/", prev_label="← Урок 10: Кейсы с нейтивом",
    next_href="/lessons/12/", next_label="Урок 12: Semantic SEO + GEO →",
)
write("lessons/11/index.html", html)
