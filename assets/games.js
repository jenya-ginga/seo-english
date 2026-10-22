/* Игровая — 5 игр на перетаскивание. Данные берутся из #pdata (собираются из уроков генератором). */
(function () {
  'use strict';
  var DATA;
  try { DATA = JSON.parse(document.getElementById('pdata').textContent); } catch (e) { return; }
  var stage = document.getElementById('pr-stage');
  var tabsEl = document.getElementById('pr-tabs');
  if (!stage || !tabsEl) return;

  /* ---------- helpers ---------- */
  function h(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function sample(a, n) { return shuffle(a).slice(0, n); }
  function firstTok(s) { return String(s).toLowerCase().split(/[\s\/\-]+/)[0]; }
  function pickDistinct(items, n, keyFn) {
    var out = [], seen = {};
    shuffle(items).some(function (it) {
      var k = firstTok(keyFn(it));
      if (seen[k]) return false;
      seen[k] = 1; out.push(it);
      return out.length >= n;
    });
    return out;
  }
  function pctWord(n, forms) { // 1 ошибка / 2 ошибки / 5 ошибок
    var m10 = n % 10, m100 = n % 100;
    if (m10 === 1 && m100 !== 11) return forms[0];
    if (m10 >= 2 && m10 <= 4 && (m100 < 10 || m100 >= 20)) return forms[1];
    return forms[2];
  }

  var STORE = 'ge-games';
  function loadBest() { try { return JSON.parse(localStorage.getItem(STORE) || '{}'); } catch (e) { return {}; } }
  function saveBest(mode, score, total) {
    try {
      var b = loadBest(), prev = b[mode], pct = score / total;
      if (!prev || pct > prev.pct) b[mode] = { pct: pct, score: score, total: total };
      localStorage.setItem(STORE, JSON.stringify(b));
    } catch (e) {}
  }

  /* ---------- drag & drop engine (pointer events: мышь + палец; плюс «тап → тап») ---------- */
  function DnD(root, opts) {
    var st = null, ghost = null, selected = null, overZone = null;

    function zoneAt(x, y) {
      var e = document.elementFromPoint(x, y);
      var z = e && e.closest ? e.closest('.zone') : null;
      return z && root.contains(z) ? z : null;
    }
    function clearOver() { if (overZone) { overZone.classList.remove('over'); overZone = null; } }
    function setSel(chip) {
      if (selected) selected.classList.remove('selected');
      selected = chip || null;
      if (selected) selected.classList.add('selected');
      root.classList.toggle('has-selection', !!selected);
    }
    function cleanup(s) {
      if (ghost) { ghost.remove(); ghost = null; }
      if (s && s.chip) s.chip.classList.remove('dragging');
      clearOver();
      document.body.classList.remove('pr-dragging');
    }

    root.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      var chip = e.target.closest('.chip');
      if (!chip || !root.contains(chip) || chip.classList.contains('locked')) return;
      st = { chip: chip, x: e.clientX, y: e.clientY, id: e.pointerId, drag: false };
      try { chip.setPointerCapture(e.pointerId); } catch (_) {}
    });

    root.addEventListener('pointermove', function (e) {
      if (!st || e.pointerId !== st.id) return;
      if (!st.drag) {
        if (Math.hypot(e.clientX - st.x, e.clientY - st.y) < 6) return;
        st.drag = true;
        var r = st.chip.getBoundingClientRect();
        st.dx = st.x - r.left; st.dy = st.y - r.top;
        ghost = st.chip.cloneNode(true);
        ghost.className = 'chip ghost';
        ghost.style.width = r.width + 'px';
        document.body.appendChild(ghost);
        st.chip.classList.add('dragging');
        document.body.classList.add('pr-dragging');
        setSel(null);
      }
      ghost.style.transform = 'translate(' + (e.clientX - st.dx) + 'px,' + (e.clientY - st.dy) + 'px) rotate(-2deg)';
      var z = zoneAt(e.clientX, e.clientY);
      if (z !== overZone) { clearOver(); if (z) { z.classList.add('over'); overZone = z; } }
      if (e.clientY < 70) window.scrollBy(0, -14);
      else if (e.clientY > window.innerHeight - 70) window.scrollBy(0, 14);
    });

    function finish(e, cancel) {
      if (!st || e.pointerId !== st.id) return;
      var s = st; st = null;
      var z = (s.drag && !cancel) ? zoneAt(e.clientX, e.clientY) : null;
      cleanup(s);
      if (s.drag) {
        if (z) opts.onDrop(s.chip, z, e);
      } else if (!cancel) {
        tap(s.chip);
      }
    }
    root.addEventListener('pointerup', function (e) { finish(e, false); });
    root.addEventListener('pointercancel', function (e) { finish(e, true); });

    function tap(chip) {
      if (opts.onTap) { opts.onTap(chip); return; }
      setSel(selected === chip ? null : chip);
    }

    // клик по зоне при выбранной фишке (тап → тап) и клавиатура
    root.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (chip && root.contains(chip)) {
        if (e.detail === 0 && !chip.classList.contains('locked')) tap(chip); // активация с клавиатуры
        return;
      }
      var z = e.target.closest('.zone');
      if (z && root.contains(z) && selected) {
        var c = selected; setSel(null);
        opts.onDrop(c, z, e);
      }
    });
    root.addEventListener('keydown', function (e) {
      if ((e.key === 'Enter' || e.key === ' ') && e.target.classList && e.target.classList.contains('zone') && selected) {
        e.preventDefault();
        var c = selected; setSel(null);
        opts.onDrop(c, e.target, e);
      }
    });
    return { clearSel: function () { setSel(null); } };
  }

  /* ---------- общий каркас режима ---------- */
  var MODES = {};
  var current = null;

  function frame(modeKey, title, instr) {
    stage.innerHTML = '';
    var head = h('div', 'pr-head');
    head.appendChild(h('h2', 'pr-title', title));
    head.appendChild(h('p', 'pr-instr', instr));
    var status = h('div', 'pr-status');
    status.setAttribute('aria-live', 'polite');
    var board = h('div', 'pr-board');
    var foot = h('div', 'pr-foot');
    stage.appendChild(head); stage.appendChild(status); stage.appendChild(board); stage.appendChild(foot);
    var best = loadBest()[modeKey];
    if (best) head.appendChild(h('p', 'pr-best', 'Лучший результат: ' + best.score + ' из ' + best.total + ' с первой попытки'));
    return { head: head, status: status, board: board, foot: foot };
  }

  function Tracker(modeKey, f, total, again) {
    var solved = 0, mistakes = 0, first = 0, slipped = {};
    function render() {
      f.status.textContent = 'Готово: ' + solved + ' из ' + total + ' · Ошибок: ' + mistakes;
    }
    render();
    return {
      attempt: function (id, ok) {
        if (ok) { solved++; if (!slipped[id]) first++; }
        else { mistakes++; slipped[id] = true; }
        render();
        if (solved >= total) setTimeout(done, 450);
      },
      slip: function (id) { slipped[id] = true; },
      done: done
    };
    function done() {
      saveBest(modeKey, first, total);
      var card = h('div', 'pr-result');
      var ratio = first / total;
      var msg = ratio === 1 ? 'Чисто — без единой ошибки!' : ratio >= 0.6 ? 'Хороший результат, ещё раунд закрепит.' : 'Нормально для разгона — попробуйте ещё раз.';
      card.appendChild(h('div', 'pr-result-score', first + ' из ' + total));
      card.appendChild(h('div', 'pr-result-line', 'с первой попытки · ' + mistakes + ' ' + pctWord(mistakes, ['ошибка', 'ошибки', 'ошибок'])));
      card.appendChild(h('p', 'pr-result-msg', msg));
      var again_b = h('button', 'pr-btn', 'Ещё раунд'); again_b.type = 'button';
      again_b.addEventListener('click', again);
      card.appendChild(again_b);
      f.foot.innerHTML = '';
      f.foot.appendChild(card);
      card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  function chipEl(text, id) {
    var c = h('button', 'chip', text);
    c.type = 'button';
    c.dataset.id = id;
    return c;
  }
  function flash(el, cls) {
    el.classList.remove('bad'); void el.offsetWidth;
    el.classList.add(cls);
    setTimeout(function () { el.classList.remove(cls); }, 600);
  }

  /* ---------- 1. вставь слово в предложение ---------- */
  MODES.gap = function () {
    var f = frame('gap', 'Вставь слово в предложение',
      'Перетащите термин в пропуск. Можно и без перетаскивания: нажмите на слово, затем на пропуск.');
    var items = sample(DATA.gaps, 6);
    var extra = sample(DATA.gaps.filter(function (g) { return items.indexOf(g) < 0; }), 2);
    var tr = Tracker('gap', f, items.length, MODES.gap);

    var tools = h('label', 'pr-toggle');
    var cb = document.createElement('input'); cb.type = 'checkbox';
    tools.appendChild(cb); tools.appendChild(document.createTextNode(' Показать подсказки (легче)'));
    f.board.appendChild(tools);

    var pool = h('div', 'pr-pool pr-sticky');
    shuffle(items.map(function (g) { return chipEl(g.answer, g.id); })
      .concat(extra.map(function (g) { return chipEl(g.answer, 'x' + g.id); }))).forEach(function (c) { pool.appendChild(c); });
    f.board.appendChild(pool);

    var list = h('div', 'pr-sents no-hints');
    items.forEach(function (g) {
      var row = h('div', 'pr-sent');
      var p = h('p', 'pr-sent-text');
      p.appendChild(document.createTextNode(g.before));
      var z = h('span', 'zone blank', ' ');
      z.dataset.id = g.id; z.tabIndex = 0; z.setAttribute('role', 'button'); z.setAttribute('aria-label', 'Пропуск');
      p.appendChild(z);
      p.appendChild(document.createTextNode(g.after));
      row.appendChild(p);
      if (g.hint) row.appendChild(h('p', 'pr-hint', 'Подсказка: ' + g.hint));
      list.appendChild(row);
    });
    f.board.appendChild(list);
    cb.addEventListener('change', function () { list.classList.toggle('no-hints', !cb.checked); });

    DnD(f.board, {
      onDrop: function (chip, zone) {
        if (!zone.classList.contains('blank') || zone.classList.contains('ok')) return;
        var ok = chip.dataset.id === zone.dataset.id;
        if (ok) {
          zone.textContent = chip.textContent;
          zone.classList.add('ok'); zone.removeAttribute('tabindex');
          chip.remove();
        } else { flash(zone, 'bad'); flash(chip, 'bad'); }
        tr.attempt(zone.dataset.id, ok);
      }
    });
  };

  /* ---------- 2 и 5. соответствие: слово → перевод / определение → термин ---------- */
  function matchMode(key, title, instr, list, field, n) {
    var f = frame(key, title, instr);
    var items = pickDistinct(list, n, function (x) { return x.term; });
    var tr = Tracker(key, f, items.length, function () { MODES[key](); });
    var wrap = h('div', 'pr-match');
    var left = h('div', 'pr-pool pr-pool-col');
    shuffle(items).forEach(function (it) { left.appendChild(chipEl(it.term, it.id)); });
    var right = h('div', 'pr-targets');
    shuffle(items).forEach(function (it) {
      var z = h('div', 'zone target');
      z.dataset.id = it.id; z.tabIndex = 0; z.setAttribute('role', 'button');
      z.appendChild(h('span', 'pr-ztext', it[field]));
      z.appendChild(h('span', 'pr-zplaced', ''));
      right.appendChild(z);
    });
    wrap.appendChild(left); wrap.appendChild(right);
    f.board.appendChild(wrap);

    DnD(f.board, {
      onDrop: function (chip, zone) {
        if (!zone.classList.contains('target') || zone.classList.contains('ok')) return;
        var ok = chip.dataset.id === zone.dataset.id;
        if (ok) {
          zone.classList.add('ok'); zone.removeAttribute('tabindex');
          zone.querySelector('.pr-zplaced').textContent = chip.textContent;
          chip.remove();
        } else { flash(zone, 'bad'); flash(chip, 'bad'); }
        tr.attempt(zone.dataset.id, ok);
      }
    });
  }
  MODES.match = function () {
    matchMode('match', 'Слово → перевод',
      'Перетащите английский термин к его переводу. Нажать на слово, затем на перевод — тоже работает.',
      DATA.pairs, 'ru', 6);
  };
  MODES.defs = function () {
    matchMode('defs', 'Определение → термин',
      'Прочитайте определение и перетащите к нему подходящий термин.',
      DATA.defs, 'def', 5);
  };

  /* ---------- 3. собери фразу из блоков ---------- */
  MODES.build = function () {
    var f = frame('build', 'Собери фразу',
      'Расставьте блоки в правильном порядке. Перетаскивайте их в строку ответа и меняйте местами; нажатие по блоку тоже переносит его.');
    var phrases = sample(DATA.build, 5);
    var idx = 0, firstTry = 0, mistakes = 0, slipped = false, locked = false;
    var total = phrases.length;

    function status() { f.status.textContent = 'Фраза ' + Math.min(idx + 1, total) + ' из ' + total + ' · Ошибок: ' + mistakes; }

    function renderOne() {
      f.board.innerHTML = ''; f.foot.innerHTML = '';
      locked = false; slipped = false;
      status();
      var p = phrases[idx];
      var target = p.en.split(' ');
      f.board.appendChild(h('p', 'pr-ru', p.ru));
      var answer = h('div', 'zone answer'); answer.setAttribute('aria-label', 'Строка ответа');
      var tray = h('div', 'zone tray pr-pool');
      var order = shuffle(target.map(function (t, i) { return i; }));
      if (target.length > 1) { var guard = 0; while (order.join() === target.map(function (t, i) { return i; }).join() && guard++ < 8) order = shuffle(order); }
      order.forEach(function (i) { var c = chipEl(target[i], 'w' + i); tray.appendChild(c); });
      f.board.appendChild(answer); f.board.appendChild(tray);
      var msg = h('p', 'pr-msg'); msg.setAttribute('aria-live', 'polite');
      f.board.appendChild(msg);

      function words(zone) { return Array.prototype.map.call(zone.querySelectorAll('.chip'), function (c) { return c.textContent; }); }
      function setLocked() { Array.prototype.forEach.call(f.board.querySelectorAll('.chip'), function (c) { c.classList.add('locked'); }); }

      var dnd = DnD(f.board, {
        onTap: function (chip) {
          if (locked) return;
          (chip.parentNode === answer ? tray : answer).appendChild(chip);
          msg.textContent = '';
        },
        onDrop: function (chip, zone, e) {
          if (locked) return;
          if (zone === tray) { tray.appendChild(chip); }
          else if (zone === answer) {
            var kids = Array.prototype.filter.call(answer.children, function (c) { return c !== chip; });
            var before = null;
            for (var i = 0; i < kids.length; i++) {
              var r = kids[i].getBoundingClientRect();
              if (e.clientY < r.top || (e.clientY < r.bottom && e.clientX < r.left + r.width / 2)) { before = kids[i]; break; }
            }
            answer.insertBefore(chip, before);
          }
          msg.textContent = '';
        }
      });

      var bCheck = h('button', 'pr-btn', 'Проверить'); bCheck.type = 'button';
      var bReset = h('button', 'pr-btn ghost', 'Сбросить'); bReset.type = 'button';
      var bShow = h('button', 'pr-btn ghost', 'Показать ответ'); bShow.type = 'button';
      f.foot.appendChild(bCheck); f.foot.appendChild(bReset); f.foot.appendChild(bShow);

      function next() {
        idx++;
        if (idx >= total) { finishAll(); } else { renderOne(); }
      }
      function solvedUI(shown) {
        locked = true; setLocked(); answer.classList.add('ok');
        msg.textContent = '';
        f.board.appendChild(h('p', 'pr-final', p.en));
        f.foot.innerHTML = '';
        var bn = h('button', 'pr-btn', idx + 1 >= total ? 'Результат' : 'Дальше'); bn.type = 'button';
        bn.addEventListener('click', next);
        f.foot.appendChild(bn);
        bn.focus();
      }
      bCheck.addEventListener('click', function () {
        if (locked) return;
        var got = words(answer);
        if (got.length < target.length) { msg.textContent = 'Нужно использовать все блоки.'; flash(answer, 'bad'); return; }
        if (got.join(' ') === target.join(' ')) {
          if (!slipped) firstTry++;
          solvedUI(false);
        } else {
          slipped = true; mistakes++; status();
          msg.textContent = 'Порядок не совпал — поменяйте блоки местами.';
          flash(answer, 'bad');
        }
      });
      bReset.addEventListener('click', function () {
        if (locked) return;
        Array.prototype.slice.call(answer.querySelectorAll('.chip')).forEach(function (c) { tray.appendChild(c); });
        msg.textContent = '';
      });
      bShow.addEventListener('click', function () {
        if (locked) return;
        slipped = true;
        var all = Array.prototype.slice.call(f.board.querySelectorAll('.chip'));
        target.forEach(function (w) {
          for (var i = 0; i < all.length; i++) {
            if (all[i].textContent === w) { answer.appendChild(all[i]); all.splice(i, 1); break; }
          }
        });
        solvedUI(true);
      });
    }

    function finishAll() {
      saveBest('build', firstTry, total);
      f.board.innerHTML = ''; f.foot.innerHTML = '';
      f.status.textContent = 'Раунд завершён · Ошибок: ' + mistakes;
      var card = h('div', 'pr-result');
      var ratio = firstTry / total;
      card.appendChild(h('div', 'pr-result-score', firstTry + ' из ' + total));
      card.appendChild(h('div', 'pr-result-line', 'фраз собрано с первой попытки · ' + mistakes + ' ' + pctWord(mistakes, ['ошибка', 'ошибки', 'ошибок'])));
      card.appendChild(h('p', 'pr-result-msg', ratio === 1 ? 'Чисто — без единой ошибки!' : ratio >= 0.6 ? 'Хороший результат, ещё раунд закрепит.' : 'Нормально для разгона — попробуйте ещё раз.'));
      var b = h('button', 'pr-btn', 'Ещё раунд'); b.type = 'button';
      b.addEventListener('click', MODES.build);
      card.appendChild(b);
      f.board.appendChild(card);
    }
    renderOne();
  };

  /* ---------- 4. разложи фразы по ситуациям ---------- */
  MODES.sort = function () {
    var f = frame('sort', 'Какая это ситуация?',
      'Перетащите каждую фразу в подходящую ситуацию. Фразы взяты из разговорника.');
    var lessons = Object.keys(DATA.sort);
    var lk = lessons[Math.floor(Math.random() * lessons.length)];
    var cards = sample(DATA.sort[lk], 3);
    var chips = [];
    cards.forEach(function (c, ci) {
      sample(c.phrases, 3).forEach(function (p) {
        var ch = chipEl(p.en, 'c' + ci); ch.dataset.ru = p.ru; chips.push(ch);
      });
    });
    var tr = Tracker('sort', f, chips.length, MODES.sort);
    var pool = h('div', 'pr-pool');
    shuffle(chips).forEach(function (c, i) { c.dataset.uid = 'p' + i; pool.appendChild(c); });
    f.board.appendChild(pool);
    var buckets = h('div', 'pr-buckets');
    cards.forEach(function (c, ci) {
      var z = h('div', 'zone bucket'); z.dataset.id = 'c' + ci; z.tabIndex = 0; z.setAttribute('role', 'button');
      z.appendChild(h('div', 'pr-bucket-title', c.title));
      z.appendChild(h('ul', 'pr-bucket-list'));
      buckets.appendChild(z);
    });
    f.board.appendChild(buckets);

    DnD(f.board, {
      onDrop: function (chip, zone) {
        if (!zone.classList.contains('bucket')) return;
        var ok = chip.dataset.id === zone.dataset.id;
        if (ok) {
          var li = h('li', 'pr-placed');
          li.appendChild(h('span', 'pr-placed-en', chip.textContent));
          if (chip.dataset.ru) li.appendChild(h('span', 'pr-placed-ru', chip.dataset.ru));
          zone.querySelector('.pr-bucket-list').appendChild(li);
          chip.remove();
        } else { flash(zone, 'bad'); flash(chip, 'bad'); }
        tr.attempt(chip.dataset.uid, ok);
      }
    });
  };

  /* ---------- вкладки ---------- */
  var buttons = Array.prototype.slice.call(tabsEl.querySelectorAll('[data-mode]'));
  function openMode(key, push) {
    if (!MODES[key]) key = 'gap';
    current = key;
    buttons.forEach(function (b) {
      var on = b.dataset.mode === key;
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    MODES[key]();
    if (push) { try { history.replaceState(null, '', '#' + key); } catch (e) {} }
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () { openMode(b.dataset.mode, true); });
  });
  openMode((location.hash || '').replace('#', '') || 'gap', false);
})();
