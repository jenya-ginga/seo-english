# -*- coding: utf-8 -*-
"""
Generates /game/index.html — "Speaking Sprint", a party-game style
rapid-response speaking trainer covering all 15 lessons.

Run from the repo root:  python3 generator/gen_game.py
(Subject to the same build.py write() ROOT-path bug as every other
generator — relocate generator/lessons/... -> lessons/... isn't needed
here since this writes to "game/index.html", which still lands under
generator/game/index.html and must be copied to game/index.html.)
"""
import json
import os
from build import HEAD_FONTS, page, write

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "lesson_data.json"), "r", encoding="utf-8") as f:
    RAW = json.load(f)

LESSONS_META = RAW["lessons"]
TERMS = RAW["terms"]
SPEAK = RAW["clientQuestions"]

DATA_JSON = json.dumps({
    "lessons": LESSONS_META,
    "terms": TERMS,
    "speak": SPEAK,
}, ensure_ascii=False)

STYLE = '''
<style>
#sprint{margin-top:8px;}
#sprint .panel{background:var(--paper); border:1px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow); padding:28px 26px;}
#sprint h3{font-family:var(--serif); font-size:20px; margin:0 0 4px;}
#sprint .sub{color:var(--ink-soft); font-size:14.5px; margin:0 0 20px;}
#sprint .field{margin-bottom:20px;}
#sprint label.flabel{display:block; font-size:13px; font-weight:600; color:var(--ink); margin-bottom:8px; text-transform:uppercase; letter-spacing:.03em; font-family:var(--mono);}
#sprint textarea, #sprint input[type=text]{
  width:100%; border:1px solid var(--line); border-radius:var(--radius-sm); padding:10px 12px;
  font-family:var(--sans); font-size:15px; background:var(--bg); color:var(--ink); resize:vertical;
}
#sprint textarea{min-height:70px;}
#sprint .chiprow{display:flex; flex-wrap:wrap; gap:8px;}
#sprint .chiprow button{
  border:1px solid var(--line); background:var(--paper); color:var(--ink-soft);
  border-radius:20px; padding:7px 14px; font-size:13.5px; cursor:pointer; font-family:var(--sans);
  transition:all .15s ease;
}
#sprint .chiprow button.on{background:var(--accent-soft); border-color:var(--accent); color:var(--accent-ink); font-weight:600;}
#sprint .lesson-chip{max-width:none;}
#sprint .selectall{font-size:12.5px; color:var(--accent); background:none; border:none; cursor:pointer; text-decoration:underline; padding:0; font-family:var(--sans);}
#sprint .modebtns{display:flex; gap:10px; flex-wrap:wrap;}
#sprint .modebtn{
  flex:1; min-width:150px; border:1.5px solid var(--line); background:var(--paper); border-radius:var(--radius-sm);
  padding:14px 16px; text-align:left; cursor:pointer; font-family:var(--sans);
}
#sprint .modebtn.on{border-color:var(--accent); background:var(--accent-soft);}
#sprint .modebtn .mt{font-weight:650; font-size:14.5px; color:var(--ink);}
#sprint .modebtn .md{font-size:12.5px; color:var(--ink-soft); margin-top:3px;}
#sprint .timebtns{display:flex; gap:8px;}
#sprint .timebtn{border:1.5px solid var(--line); background:var(--paper); border-radius:20px; padding:8px 16px; cursor:pointer; font-family:var(--mono); font-size:14px; font-weight:600; color:var(--ink-soft);}
#sprint .timebtn.on{border-color:var(--accent); background:var(--accent-soft); color:var(--accent-ink);}
#sprint .startbtn{
  width:100%; background:var(--accent); color:#fff; border:none; border-radius:var(--radius-sm);
  padding:16px; font-size:16px; font-weight:650; cursor:pointer; font-family:var(--sans); margin-top:8px;
}
#sprint .startbtn:disabled{opacity:.45; cursor:not-allowed;}
#sprint .startbtn:hover:not(:disabled){filter:brightness(1.06);}
#sprint .warn-inline{font-size:13px; color:var(--warn); margin-top:8px;}

/* game screen */
#sprintGame{display:none;}
#sprintGame.active{display:block;}
#sprintSetup.hidden, #sprintEnd.hidden{display:none;}
.gp-scoreboard{display:flex; gap:12px; margin-bottom:18px;}
.gp-team{flex:1; background:var(--paper); border:1px solid var(--line); border-radius:var(--radius-sm); padding:14px 16px; text-align:center; position:relative;}
.gp-team.active{border-color:var(--accent); box-shadow:0 0 0 3px var(--accent-soft);}
.gp-team .gp-name{font-family:var(--mono); font-size:12.5px; color:var(--ink-soft); text-transform:uppercase; letter-spacing:.03em;}
.gp-team .gp-score{font-family:var(--serif); font-size:34px; font-weight:650; color:var(--ink); line-height:1.1; margin-top:2px;}
.gp-team .gp-turn{font-size:12px; color:var(--accent); margin-top:4px; font-weight:600; min-height:16px;}

.gp-card{background:var(--paper); border:1px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow); padding:36px 30px; text-align:center; position:relative; overflow:hidden;}
.gp-card .gp-kind{font-family:var(--mono); font-size:12px; letter-spacing:.05em; text-transform:uppercase; color:var(--accent); font-weight:700; margin-bottom:14px;}
.gp-card .gp-prompt{font-family:var(--serif); font-size:clamp(22px,4vw,32px); line-height:1.28; color:var(--ink); min-height:70px; display:flex; align-items:center; justify-content:center;}
.gp-card .gp-prompt.en{font-family:var(--sans); font-weight:600;}
.gp-card .gp-hint{margin-top:16px; font-size:14px; color:var(--ink-faint); min-height:20px;}
.gp-card .gp-answer{margin-top:12px; font-size:16px; color:var(--present); font-weight:600; min-height:22px;}
.gp-card .gp-lesson-tag{position:absolute; top:14px; right:18px; font-family:var(--mono); font-size:11px; color:var(--ink-faint);}

.gp-timerwrap{display:flex; align-items:center; justify-content:center; margin:22px 0 10px;}
.gp-timerbar{width:100%; max-width:420px; height:10px; background:var(--line-soft); border-radius:6px; overflow:hidden;}
.gp-timerbar .fill{height:100%; background:var(--present); width:100%; transition:width .1s linear, background .3s ease;}
.gp-timerbar .fill.low{background:var(--warn);}
.gp-timenum{font-family:var(--mono); font-weight:700; font-size:22px; min-width:44px; text-align:center;}

.gp-controls{display:flex; gap:10px; margin-top:22px; flex-wrap:wrap;}
.gp-controls button{
  flex:1; min-width:130px; border:none; border-radius:var(--radius-sm); padding:15px 14px;
  font-size:15px; font-weight:650; cursor:pointer; font-family:var(--sans);
}
.gp-btn-correct{background:var(--present); color:#fff;}
.gp-btn-skip{background:var(--warn-soft); color:var(--warn);}
.gp-btn-next{background:var(--line-soft); color:var(--ink-soft);}
.gp-btn-reveal{background:var(--accent-soft); color:var(--accent-ink);}
.gp-controls button:hover{filter:brightness(1.05);}
.gp-foot{display:flex; justify-content:space-between; align-items:center; margin-top:18px; font-size:13px; color:var(--ink-faint);}
.gp-foot button{background:none; border:none; color:var(--ink-faint); text-decoration:underline; cursor:pointer; font-family:var(--sans); font-size:13px; padding:0;}

/* end screen */
#sprintEnd .panel{text-align:center;}
#sprintEnd .winner{font-family:var(--serif); font-size:30px; font-weight:650; margin:6px 0 20px;}
#sprintEnd .finalscore{display:flex; gap:16px; justify-content:center; margin-bottom:22px;}
#sprintEnd .finalscore div{font-family:var(--mono); font-size:15px;}
#sprintEnd .again{background:var(--accent); color:#fff; border:none; border-radius:var(--radius-sm); padding:14px 26px; font-size:15px; font-weight:650; cursor:pointer; font-family:var(--sans);}

@media (max-width:560px){
  .gp-card{padding:26px 18px;}
  .gp-scoreboard{flex-direction:row;}
}
</style>
'''

BODY = f'''<section id="sprint">
  <div class="wrap">

    <div id="sprintSetup" class="panel">
      <h3>1. Игроки и команды</h3>
      <p class="sub">Впишите имена через запятую или с новой строки — разложим на 2 команды по очереди. Можно оставить пустым и просто передавать устройство по кругу.</p>
      <div class="field">
        <label class="flabel">Игроки (5–10 человек)</label>
        <textarea id="sprintPlayers" placeholder="Аня, Борис, Вика, Гоша, Дима..."></textarea>
      </div>

      <h3>2. Темы</h3>
      <p class="sub">Какие уроки берём в игру? <button class="selectall" id="sprintSelAll" type="button">выбрать все</button> · <button class="selectall" id="sprintSelNone" type="button">снять все</button></p>
      <div class="field">
        <div class="chiprow" id="sprintLessonChips"></div>
      </div>

      <h3>3. Формат карточек</h3>
      <div class="field">
        <div class="modebtns" id="sprintModeButtons">
          <button type="button" class="modebtn" data-mode="both">
            <div class="mt">Микс</div>
            <div class="md">И перевод, и реакция на реплику клиента</div>
          </button>
          <button type="button" class="modebtn" data-mode="term">
            <div class="mt">Только перевод</div>
            <div class="md">Видишь русскую фразу → говоришь по-английски</div>
          </button>
          <button type="button" class="modebtn" data-mode="speak">
            <div class="mt">Только реакция</div>
            <div class="md">Видишь реплику клиента (EN) → отвечаешь сразу</div>
          </button>
        </div>
      </div>

      <h3>4. Время на карточку</h3>
      <div class="field">
        <label class="flabel">Перевод (короткая фраза)</label>
        <div class="timebtns" id="sprintTimeButtons">
          <button type="button" class="timebtn" data-t="8">8 сек</button>
          <button type="button" class="timebtn" data-t="12">12 сек</button>
          <button type="button" class="timebtn" data-t="20">20 сек</button>
        </div>
      </div>
      <div class="field">
        <label class="flabel">Реакция на клиента (целое предложение)</label>
        <div class="timebtns" id="sprintSpeakTimeButtons">
          <button type="button" class="timebtn" data-t="20">20 сек</button>
          <button type="button" class="timebtn" data-t="30">30 сек</button>
          <button type="button" class="timebtn" data-t="40">40 сек</button>
        </div>
      </div>

      <button class="startbtn" id="sprintStart" type="button" disabled>Начать игру</button>
      <div class="warn-inline" id="sprintWarn" style="display:none;">Выберите хотя бы одну тему — без этого карточек не будет.</div>
    </div>

    <div id="sprintGame">
      <div class="gp-scoreboard" id="sprintScoreboard"></div>

      <div class="gp-card">
        <span class="gp-lesson-tag" id="sprintLessonTag"></span>
        <div class="gp-kind" id="sprintKind">Переведи на английский</div>
        <div class="gp-prompt" id="sprintPrompt">—</div>
        <div class="gp-answer" id="sprintAnswer"></div>
      </div>

      <div class="gp-timerwrap">
        <div class="gp-timerbar"><div class="fill" id="sprintFill"></div></div>
        <div class="gp-timenum" id="sprintTimenum">–</div>
      </div>

      <div class="gp-controls">
        <button class="gp-btn-correct" id="sprintCorrect" type="button">✅ Сказал(а)!</button>
        <button class="gp-btn-skip" id="sprintSkip" type="button">⏭ Пропустить</button>
      </div>
      <div class="gp-controls">
        <button class="gp-btn-reveal" id="sprintReveal" type="button">Показать ответ</button>
        <button class="gp-btn-next" id="sprintPause" type="button">⏸ Пауза</button>
      </div>

      <div class="gp-foot">
        <span id="sprintCounter"></span>
        <button id="sprintQuit" type="button">Закончить игру</button>
      </div>
    </div>

    <div id="sprintEnd">
      <div class="panel">
        <div class="gp-kind">Игра окончена</div>
        <div class="winner" id="sprintWinner">—</div>
        <div class="finalscore" id="sprintFinal"></div>
        <button class="again" id="sprintAgain" type="button">Играть ещё раз</button>
      </div>
    </div>

  </div>
</section>
{STYLE}
<script>
const SPRINT_DATA = {DATA_JSON};

(function(){{
  const els = {{
    setup: document.getElementById('sprintSetup'),
    game: document.getElementById('sprintGame'),
    end: document.getElementById('sprintEnd'),
    players: document.getElementById('sprintPlayers'),
    lessonChips: document.getElementById('sprintLessonChips'),
    selAll: document.getElementById('sprintSelAll'),
    selNone: document.getElementById('sprintSelNone'),
    modeButtons: document.getElementById('sprintModeButtons'),
    timeButtons: document.getElementById('sprintTimeButtons'),
    speakTimeButtons: document.getElementById('sprintSpeakTimeButtons'),
    start: document.getElementById('sprintStart'),
    warn: document.getElementById('sprintWarn'),
    scoreboard: document.getElementById('sprintScoreboard'),
    lessonTag: document.getElementById('sprintLessonTag'),
    kind: document.getElementById('sprintKind'),
    prompt: document.getElementById('sprintPrompt'),
    answer: document.getElementById('sprintAnswer'),
    fill: document.getElementById('sprintFill'),
    timenum: document.getElementById('sprintTimenum'),
    correct: document.getElementById('sprintCorrect'),
    skip: document.getElementById('sprintSkip'),
    reveal: document.getElementById('sprintReveal'),
    pause: document.getElementById('sprintPause'),
    counter: document.getElementById('sprintCounter'),
    quit: document.getElementById('sprintQuit'),
    winner: document.getElementById('sprintWinner'),
    final: document.getElementById('sprintFinal'),
    again: document.getElementById('sprintAgain'),
  }};

  let selectedLessons = new Set(SPRINT_DATA.lessons.map(l => l.num));
  let mode = 'both';
  let termSeconds = 12;
  let speakSeconds = 40;

  // --- build lesson chips ---
  SPRINT_DATA.lessons.forEach(l => {{
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'on';
    b.textContent = `${{l.num}}. ${{l.title.length > 28 ? l.title.slice(0,26) + '…' : l.title}}`;
    b.dataset.num = l.num;
    b.addEventListener('click', () => {{
      if (selectedLessons.has(l.num)) {{ selectedLessons.delete(l.num); b.classList.remove('on'); }}
      else {{ selectedLessons.add(l.num); b.classList.add('on'); }}
      validateStart();
    }});
    els.lessonChips.appendChild(b);
  }});
  els.selAll.addEventListener('click', () => {{
    selectedLessons = new Set(SPRINT_DATA.lessons.map(l => l.num));
    els.lessonChips.querySelectorAll('button').forEach(b => b.classList.add('on'));
    validateStart();
  }});
  els.selNone.addEventListener('click', () => {{
    selectedLessons.clear();
    els.lessonChips.querySelectorAll('button').forEach(b => b.classList.remove('on'));
    validateStart();
  }});

  els.modeButtons.querySelectorAll('.modebtn').forEach(b => {{
    if (b.dataset.mode === mode) b.classList.add('on');
    b.addEventListener('click', () => {{
      mode = b.dataset.mode;
      els.modeButtons.querySelectorAll('.modebtn').forEach(x => x.classList.toggle('on', x === b));
      validateStart();
    }});
  }});
  els.timeButtons.querySelectorAll('.timebtn').forEach(b => {{
    if (Number(b.dataset.t) === termSeconds) b.classList.add('on');
    b.addEventListener('click', () => {{
      termSeconds = Number(b.dataset.t);
      els.timeButtons.querySelectorAll('.timebtn').forEach(x => x.classList.toggle('on', x === b));
    }});
  }});
  els.speakTimeButtons.querySelectorAll('.timebtn').forEach(b => {{
    if (Number(b.dataset.t) === speakSeconds) b.classList.add('on');
    b.addEventListener('click', () => {{
      speakSeconds = Number(b.dataset.t);
      els.speakTimeButtons.querySelectorAll('.timebtn').forEach(x => x.classList.toggle('on', x === b));
    }});
  }});

  function poolForMode() {{
    let pool = [];
    if (mode === 'term' || mode === 'both') pool = pool.concat(SPRINT_DATA.terms);
    if (mode === 'speak' || mode === 'both') pool = pool.concat(SPRINT_DATA.speak);
    return pool.filter(q => selectedLessons.has(q.lesson));
  }}

  function validateStart() {{
    const n = poolForMode().length;
    els.start.disabled = n < 3;
    els.warn.style.display = n < 3 ? 'block' : 'none';
  }}
  validateStart();

  // --- teams / players ---
  let teams = [];       // [{{name, score, players:[names]}}]
  let activeTeam = 0;
  let turnCounters = []; // per-team index into players[] for whose turn it is

  function buildTeams() {{
    const raw = els.players.value.split(/[,\\n]/).map(s => s.trim()).filter(Boolean);
    teams = [
      {{ name: 'Команда А', score: 0, players: [] }},
      {{ name: 'Команда Б', score: 0, players: [] }},
    ];
    raw.forEach((name, i) => teams[i % 2].players.push(name));
    if (teams[0].players.length === 0) teams[0].players.push('Игрок');
    if (teams[1].players.length === 0) teams[1].players.push('Игрок');
    turnCounters = [0, 0];
  }}

  function currentPlayerName(teamIdx) {{
    const t = teams[teamIdx];
    return t.players[turnCounters[teamIdx] % t.players.length];
  }}

  function renderScoreboard() {{
    els.scoreboard.innerHTML = '';
    teams.forEach((t, i) => {{
      const div = document.createElement('div');
      div.className = 'gp-team' + (i === activeTeam ? ' active' : '');
      div.innerHTML = `
        <div class="gp-name">${{t.name}}</div>
        <div class="gp-score">${{t.score}}</div>
        <div class="gp-turn">${{i === activeTeam ? '▶ ход: ' + currentPlayerName(i) : ''}}</div>`;
      els.scoreboard.appendChild(div);
    }});
  }}

  // --- deck ---
  let deck = [];
  let deckPos = 0;
  let cardsPlayed = 0;
  let current = null;

  function shuffle(arr) {{
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }}
    return a;
  }}

  function refillDeck() {{
    deck = shuffle(poolForMode());
    deckPos = 0;
  }}

  function nextCard() {{
    if (deckPos >= deck.length) refillDeck();
    current = deck[deckPos++];
    cardsPlayed++;
    renderCard();
    startTimer();
  }}

  function renderCard() {{
    els.answer.textContent = '';
    els.lessonTag.textContent = 'Урок ' + current.lesson;
    els.counter.textContent = 'Карточка №' + cardsPlayed;
    if (current.type === 'term') {{
      els.kind.textContent = 'Скажи по-английски';
      els.prompt.className = 'gp-prompt';
      els.prompt.textContent = current.ru;
    }} else {{
      els.kind.textContent = 'Клиент говорит — реагируй сразу';
      els.prompt.className = 'gp-prompt en';
      els.prompt.textContent = current.en;
    }}
  }}

  function revealAnswer() {{
    els.answer.textContent = current.type === 'term' ? ('→ ' + current.en) : '';
  }}

  // --- timer ---
  let timerId = null;
  let timeLeft = 0;
  let currentDuration = 12;
  let paused = false;

  function durationFor(card) {{
    return card.type === 'term' ? termSeconds : speakSeconds;
  }}

  function startTimer() {{
    clearInterval(timerId);
    currentDuration = durationFor(current);
    timeLeft = currentDuration * 10; // deciseconds for smoother bar
    paused = false;
    els.pause.textContent = '⏸ Пауза';
    updateTimerUI();
    timerId = setInterval(() => {{
      if (paused) return;
      timeLeft -= 1;
      updateTimerUI();
      if (timeLeft <= 0) {{
        clearInterval(timerId);
        onTimeUp();
      }}
    }}, 100);
  }}

  function updateTimerUI() {{
    const pct = Math.max(0, (timeLeft / (currentDuration * 10)) * 100);
    els.fill.style.width = pct + '%';
    els.fill.classList.toggle('low', pct < 30);
    els.timenum.textContent = Math.ceil(timeLeft / 10);
  }}

  function onTimeUp() {{
    els.kind.textContent += '  ·  ⏱ время вышло';
  }}

  function advanceTurn(scored) {{
    if (scored) teams[activeTeam].score += 1;
    turnCounters[activeTeam] += 1;
    activeTeam = (activeTeam + 1) % teams.length;
    renderScoreboard();
    nextCard();
  }}

  els.correct.addEventListener('click', () => advanceTurn(true));
  els.skip.addEventListener('click', () => advanceTurn(false));
  els.reveal.addEventListener('click', revealAnswer);
  els.pause.addEventListener('click', () => {{
    paused = !paused;
    els.pause.textContent = paused ? '▶ Продолжить' : '⏸ Пауза';
  }});
  els.quit.addEventListener('click', endGame);
  els.again.addEventListener('click', () => {{
    els.end.classList.add('hidden');
    els.setup.classList.remove('hidden');
  }});

  function endGame() {{
    clearInterval(timerId);
    els.game.classList.remove('active');
    els.end.classList.remove('hidden');
    const sorted = teams.slice().sort((a, b) => b.score - a.score);
    if (sorted[0].score === sorted[1].score) {{
      els.winner.textContent = 'Ничья!';
    }} else {{
      els.winner.textContent = '🏆 ' + sorted[0].name + ' побеждает!';
    }}
    els.final.innerHTML = teams.map(t => `<div>${{t.name}}: <strong>${{t.score}}</strong></div>`).join('');
  }}

  els.start.addEventListener('click', () => {{
    buildTeams();
    activeTeam = 0;
    cardsPlayed = 0;
    refillDeck();
    els.setup.classList.add('hidden');
    els.game.classList.add('active');
    renderScoreboard();
    nextCard();
  }});
}})();
</script>
'''

html = page(
    title="Спринт-тренажёр — Global English для SEO",
    desc="Игровой тренажёр для группы 5–10 человек: быстрые карточки на перевод и реакцию на реплики клиента по материалам всех 15 уроков, командный счёт, таймер без долгих раздумий.",
    brand="Global English · Спринт",
    eyebrow="Финальная тренировка · все 15 уроков",
    h1="Спринт-тренажёр",
    lede="Командная игра на скорость: карточка — и сразу говоришь по-английски, без пауз на подумать. Для группы 5–10 человек, с таймером и счётом по командам.",
    navlinks=[("#sprint", "Играть")],
    body=BODY,
    prev_href="/lessons/15/", prev_label="← Урок 15: Сателлиты",
    next_href="/", next_label="На главную →",
)
write("game/index.html", html)
print("wrote game/index.html", len(html), "bytes")
