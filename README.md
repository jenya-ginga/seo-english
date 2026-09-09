# Global English для SEO — платформа (15 уроков + спринт-тренажёр)

Статичный сайт, без сборки. Общий дизайн вынесен в `/assets/style.css`,
каждая страница — обычный HTML-файл, который его подключает.

## Структура

```
/index.html              — главная: меню из 15 уроков (открыты все) + спринт-тренажёр
/lessons/1/index.html    — Урок 1: Времена глаголов
/lessons/2/index.html    — Урок 2: Защищаем отчёты и работу
/lessons/3/index.html    — Урок 3: Защищаем работу в сложных ситуациях
/lessons/4/index.html    — Урок 4: Explaining Charts & Rankings
/lessons/5/index.html    — Урок 5: Real Conversations
/lessons/6/index.html    — Урок 6: GEO & Semantic SEO термины
/lessons/7/index.html    — Урок 7: Role Play — Real Client Scenarios
/lessons/8/index.html    — Урок 8: Role Play — Reverse Roles
/lessons/9/index.html    — Урок 9: Все фразовые глаголы в контексте SEO
/lessons/10/index.html   — Урок 10: Кейсы с нейтивом
/lessons/11/index.html   — Урок 11: Словарик (связки для живой речи + термины 2026)
/lessons/12/index.html   — Урок 12: Semantic SEO + GEO практика
/lessons/13/index.html   — Урок 13: Rendering & Page Speed + Technical SEO
/lessons/14/index.html   — Урок 14: Допродажа во время звонка
/lessons/15/index.html   — Урок 15: Сателлиты в SEO и их влияние на LLM
/game/index.html         — Спринт-тренажёр: игра для группы 5–10 человек по всем 15 урокам
/assets/style.css        — общая дизайн-система (шрифты, цвета, компоненты)
/vercel.json             — чистые URL (без .html, с завершающим /)
/generator/               — необязательно: Python-скрипты, которыми эти
                            страницы были сгенерированы (см. ниже)
```

Все 15 уроков открыты на главной.

## Как редактировать контент

Два варианта:

**Вариант A — руками.** Каждая `lessons/N/index.html` — обычный HTML.
Все компоненты (`.info-card`, `.phrase-card`, `.xcard`/аккордеон,
`.compare-card`, таблицы) описаны в `/assets/style.css` — используйте те
же классы, чтобы новый контент выглядел так же, как остальной сайт.

**Вариант B — через генератор.** В папке `generator/` лежат Python-скрипты
(`build.py` — общие функции, `gen_lessonN.py` — контент конкретного урока,
`gen_home.py` — главная). Правите словари/списки с текстом в нужном
`gen_lessonN.py` и запускаете:

```
python3 generator/gen_lessonN.py
```

Скрипт перезапишет `lessons/N/index.html`. Так проще всего добавлять новые
карточки, вопросы или менять формулировки без риска сломать вёрстку.

## Как добавить урок 11+

1. Скопируйте `generator/gen_lesson9.py` (или любой другой) как каркас,
   замените контент.
2. Запустите скрипт — получите `lessons/N/index.html`.
3. В `generator/gen_home.py` замените нужный слот `("Урок N", None)` на
   `("Название урока", "/lessons/N/")`, перезапустите — обновится главная.
4. Если редактируете вручную, без генератора — просто скопируйте один из
   `lessons/*/index.html` как шаблон и поправьте `href` в меню + карточку
   на главной.

## Доп. разделы

Блок «Доп. разделы» на главной — часть карточек всё ещё заглушки
(`.stub-card`), без ссылок. «Спринт-тренажёр» уже живой (`.stub-card.live`,
ведёт на `/game/`). Наполняются тем же паттерном: создать страницу,
добавить `href` в карточку, при необходимости — пункт в `.navlinks` в шапке.

## Спринт-тренажёр (`/game/`)

Игровой финальный тренажёр для группы 5–10 человек: карточки на перевод
(RU → EN) и на реакцию на реплику клиента (отвечаешь сразу по-английски),
таймер 8/12/20 сек, счёт по двум командам. Данные для карточек собираются
автоматически из уже готовых `lessons/*/index.html` — никакого отдельного
контента вручную не пишется.

Чтобы пересобрать после правок в уроках:

```
python3 generator/extract_lesson_data.py > generator/lesson_data.json
python3 generator/gen_game.py
```

`extract_lesson_data.py` парсит уже готовые `lessons/*/index.html`
(`.phrase-card`, таблицы, аккордеоны ролевых игр и кейсов) и собирает
`generator/lesson_data.json`. `gen_game.py` читает этот JSON и пишет
`game/index.html`. Пересборка нужна только если поменялся текст уроков —
иначе `generator/lesson_data.json` уже актуален.

## Как выложить: репозиторий jenya-ginga/seo-english

Репозиторий уже создан: **https://github.com/jenya-ginga/seo-english**
Локальная папка на компьютере: `seo-english` (в рабочей документации).

1. Скачайте эту папку с файлами (index.html, lessons/, assets/,
   vercel.json, README.md, generator/) и положите **всё её содержимое**
   прямо в корень локальной папки `seo-english` — так, чтобы `index.html`
   лежал по пути `seo-english/index.html`, а не в подпапке.
2. Если папка `seo-english` — это ещё не клон репозитория (GitHub Desktop
   её не отслеживает), откройте GitHub Desktop → File → Add local
   repository → укажите `seo-english`. Если репозиторий на GitHub не
   пустой, сначала сделайте `git clone https://github.com/jenya-ginga/seo-english.git`
   и переносите файлы уже в склонированную папку.
3. Задайте git-identity в этой папке (обязательно перед первым коммитом —
   иначе Vercel отклонит деплой с ошибкой "couldn't find a Git account for
   the commit author"):

   ```
   git config user.email "jenya-ginga@users.noreply.github.com"
   git config user.name "jenya-ginga"
   ```

4. В GitHub Desktop: увидите все новые файлы во вкладке Changes → внизу
   слева впишите сообщение коммита (например «Platform + 10 lessons») →
   **Commit to main** → **Push origin**.
5. На vercel.com → **Add New Project** → выберите репозиторий
   `jenya-ginga/seo-english`. Build Command / Output Directory / Install
   Command оставьте пустыми (серыми) — `vercel.json` уже всё описывает.
   **Deploy**.
6. Получите ссылку вида `https://seo-english-xxxx.vercel.app` — открытая,
   доступна всей команде без логина. Дальше при каждом пуше в `main`
   Vercel передеплоит сайт автоматически.
