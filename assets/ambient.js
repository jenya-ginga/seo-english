/*
 * Ambient lounge player for Global English для SEO.
 *
 * - Generates calm, royalty-free lounge music in the browser (Web Audio API): soft electric-piano
 *   chords, a warm pad, a low bass, brushed ticks, sparse chimes and a quiet "breeze" layer.
 * - If a real recording exists at /assets/lounge.mp3 it is played instead (loop).
 * - Browsers block sound before the first click/tap/key press, so the music starts on entry when
 *   the browser allows it and otherwise on the first interaction anywhere on the page.
 * - A small round button (bottom-right) mutes/unmutes; the choice and volume are remembered.
 */
(function () {
  'use strict';

  var KEY_PREF = 'ge-music';        // 'on' | 'off'
  var KEY_VOL = 'ge-music-vol';     // 0..1
  var KEY_POS = 'ge-music-pos';     // mp3 position (sessionStorage)
  var FILE = '/assets/lounge.mp3';
  var DEFAULT_VOL = 0.65;

  function store(k, v, session) {
    try {
      var s = session ? window.sessionStorage : window.localStorage;
      if (v === undefined) return s.getItem(k);
      s.setItem(k, v);
    } catch (e) { return null; }
    return null;
  }

  // ---------------------------------------------------------------- generative engine
  function makeIR(ctx, seconds) {
    var rate = ctx.sampleRate, len = Math.floor(rate * seconds);
    var buf = ctx.createBuffer(2, len, rate);
    for (var c = 0; c < 2; c++) {
      var d = buf.getChannelData(c), lp = 0;
      for (var i = 0; i < len; i++) {
        var n = Math.random() * 2 - 1;
        lp += (n - lp) * 0.35;                     // darker tail
        d[i] = lp * Math.pow(1 - i / len, 2.8);
      }
    }
    return buf;
  }

  function midi(n) { return 440 * Math.pow(2, (n - 69) / 12); }

  // chords: bass note + voicing (MIDI)
  var PROG_A = [
    { bass: 48, notes: [55, 59, 62, 64, 67] },   // Cmaj9
    { bass: 45, notes: [52, 55, 59, 60, 64] },   // Am9
    { bass: 50, notes: [53, 57, 60, 64, 65] },   // Dm9
    { bass: 43, notes: [53, 59, 62, 64, 67] }    // G13
  ];
  var PROG_B = [
    { bass: 41, notes: [57, 60, 64, 67, 69] },   // Fmaj9
    { bass: 40, notes: [52, 55, 59, 62, 66] },   // Em9
    { bass: 50, notes: [53, 57, 60, 64, 65] },   // Dm9
    { bass: 43, notes: [53, 59, 62, 64, 67] }    // G13
  ];
  var MELODY = [72, 74, 76, 79, 81, 84];         // C major pentatonic, C5..C6

  function createEngine(ctx, dest) {
    var BPM = 66, beat = 60 / BPM, step = beat / 2;
    var master = ctx.createGain(); master.gain.value = 0;
    var comp = ctx.createDynamicsCompressor();
    comp.threshold.value = -22; comp.knee.value = 24; comp.ratio.value = 3;
    comp.attack.value = 0.02; comp.release.value = 0.4;
    var tone = ctx.createBiquadFilter(); tone.type = 'lowpass'; tone.frequency.value = 2800; tone.Q.value = 0.4;
    var bus = ctx.createGain();
    var dry = ctx.createGain(); dry.gain.value = 0.85;
    var conv = ctx.createConvolver(); conv.buffer = makeIR(ctx, 3.4);
    var wet = ctx.createGain(); wet.gain.value = 0.45;
    bus.connect(dry); dry.connect(tone);
    bus.connect(conv); conv.connect(wet); wet.connect(tone);
    tone.connect(master); master.connect(comp); comp.connect(dest);

    // shared noise buffer
    var noise = ctx.createBuffer(1, ctx.sampleRate * 2, ctx.sampleRate);
    (function () { var d = noise.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1; })();

    var hasPan = typeof ctx.createStereoPanner === 'function';
    function out(node, pan) {
      if (hasPan && pan) { var p = ctx.createStereoPanner(); p.pan.value = pan; node.connect(p); p.connect(bus); }
      else node.connect(bus);
    }

    function envGain(t, peak, attack, decay) {
      var g = ctx.createGain();
      g.gain.setValueAtTime(0.0001, t);
      g.gain.linearRampToValueAtTime(peak, t + attack);
      g.gain.exponentialRampToValueAtTime(0.0001, t + attack + decay);
      return g;
    }

    function osc(type, freq, t, dur, detune) {
      var o = ctx.createOscillator(); o.type = type; o.frequency.value = freq;
      if (detune) o.detune.value = detune;
      o.start(t); o.stop(t + dur + 0.1);
      return o;
    }

    // soft electric piano
    function ep(freq, t, vel, dur, pan) {
      var g = envGain(t, vel * 0.09, 0.012, dur);
      osc('sine', freq, t, dur).connect(g);
      osc('triangle', freq, t, dur, 3).connect(g);
      var gt = envGain(t, vel * 0.04, 0.006, 0.7);       // short "tine"
      osc('sine', freq * 2, t, 0.8).connect(gt);
      out(g, pan); out(gt, pan);
    }

    // bell-like chime for the sparse melody
    function chime(freq, t, vel, pan) {
      var g = envGain(t, vel * 0.09, 0.01, 2.2);
      osc('sine', freq, t, 2.3).connect(g);
      var g2 = envGain(t, vel * 0.02, 0.008, 1.1);
      osc('sine', freq * 2.005, t, 1.2).connect(g2);
      out(g, pan); out(g2, pan);
    }

    function bass(freq, t, vel) {
      var g = envGain(t, vel * 0.16, 0.025, 1.3);
      osc('sine', freq, t, 1.4).connect(g);
      var g2 = envGain(t, vel * 0.03, 0.025, 0.8);
      osc('triangle', freq, t, 0.9).connect(g2);
      g.connect(bus); g2.connect(bus);
    }

    function pad(freqs, t, len) {
      freqs.forEach(function (f, i) {
        var lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 750;
        var g = ctx.createGain();
        g.gain.setValueAtTime(0.0001, t);
        g.gain.linearRampToValueAtTime(0.014, t + 1.2);
        g.gain.setValueAtTime(0.014, t + len - 0.3);
        g.gain.exponentialRampToValueAtTime(0.0001, t + len + 1.4);
        osc('triangle', f, t, len + 1.5, -6).connect(lp);
        osc('triangle', f, t, len + 1.5, 6).connect(lp);
        lp.connect(g);
        out(g, i % 2 ? 0.35 : -0.35);
      });
    }

    function tick(t, vel, kind) {
      var src = ctx.createBufferSource(); src.buffer = noise;
      var f = ctx.createBiquadFilter();
      var g = ctx.createGain();
      if (kind === 'hat') { f.type = 'highpass'; f.frequency.value = 7000; }
      else { f.type = 'bandpass'; f.frequency.value = 1800; f.Q.value = 3; }
      var peak = (kind === 'hat' ? 0.03 : 0.045) * vel, dec = kind === 'hat' ? 0.05 : 0.04;
      g.gain.setValueAtTime(0.0001, t);
      g.gain.linearRampToValueAtTime(peak, t + 0.003);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dec);
      src.connect(f); f.connect(g); out(g, kind === 'hat' ? 0.2 : -0.15);
      src.start(t, Math.random() * 1.5, dec + 0.05);
    }

    // very quiet breeze layer
    var breeze = null;
    function startBreeze() {
      if (breeze) return;
      var src = ctx.createBufferSource(); src.buffer = noise; src.loop = true;
      var bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 520; bp.Q.value = 0.5;
      var g = ctx.createGain(); g.gain.value = 0.012;
      var lfo = ctx.createOscillator(); lfo.frequency.value = 0.07;
      var lg = ctx.createGain(); lg.gain.value = 0.008;
      lfo.connect(lg); lg.connect(g.gain);
      src.connect(bp); bp.connect(g); g.connect(tone);
      src.start(); lfo.start();
      breeze = { src: src, lfo: lfo };
    }
    function stopBreeze() {
      if (!breeze) return;
      try { breeze.src.stop(); breeze.lfo.stop(); } catch (e) {}
      breeze = null;
    }

    var stepIdx = 0, nextTime = 0, lastMel = -1, timer = null;

    function playStep(idx, t0) {
      var s = idx % 8, barIdx = Math.floor(idx / 8), cyc = barIdx % 8;
      var chord = (cyc < 4 ? PROG_A : PROG_B)[cyc % 4];
      var t = Math.max(0, t0 + (s % 2 ? step * 0.14 : 0) + (Math.random() - 0.5) * 0.012);   // lazy swing + human feel

      if (s === 0) {
        chord.notes.forEach(function (n, i) { ep(midi(n + 12), t + i * 0.055, 1 - i * 0.08, 3.2, (i - 2) * 0.12); });
        pad(chord.notes.slice(0, 4).map(function (n) { return midi(n - 12); }), t, step * 8);
        bass(midi(chord.bass), t, 1);
      } else if (s === 5) {
        chord.notes.slice(1, 4).forEach(function (n, i) { ep(midi(n + 12), t + i * 0.04, 0.5, 1.8, (i - 1) * 0.15); });
      } else if (s === 4) {
        bass(midi(chord.bass), t, 0.6);
      } else if (s === 7 && cyc % 2 === 1) {
        bass(midi(chord.bass + 7), t, 0.35);
      }

      if (s % 2 === 1) tick(t, 0.35 + Math.random() * 0.35, 'hat');
      if (s === 2 || s === 6) tick(t, 0.8, 'rim');

      if (barIdx % 3 !== 2 && s !== 0 && Math.random() < 0.3) {          // sparse chimes, breathing bars
        var k, tries = 0;
        do { k = MELODY[Math.floor(Math.random() * MELODY.length)]; tries++; } while (k === lastMel && tries < 4);
        lastMel = k;
        chime(midi(k), t, 0.7 + Math.random() * 0.3, (Math.random() - 0.5) * 0.7);
      }
    }

    function schedule(until) {
      while (nextTime < until) { playStep(stepIdx, nextTime); nextTime += step; stepIdx++; }
    }

    return {
      master: master,
      step: step,
      start: function (vol) {
        if (timer) { master.gain.setTargetAtTime(vol, ctx.currentTime, 0.3); return; }   // already running
        stepIdx = 0; nextTime = ctx.currentTime + 0.2; lastMel = -1;
        startBreeze();
        master.gain.cancelScheduledValues(ctx.currentTime);
        master.gain.setValueAtTime(master.gain.value, ctx.currentTime);
        master.gain.setTargetAtTime(vol, ctx.currentTime, 1.2);
        schedule(ctx.currentTime + 1.8);
        timer = setInterval(function () { schedule(ctx.currentTime + 1.8); }, 250);
      },
      setVolume: function (vol) { master.gain.setTargetAtTime(vol, ctx.currentTime, 0.15); },
      stop: function (cb) {
        clearInterval(timer); timer = null;
        master.gain.cancelScheduledValues(ctx.currentTime);
        master.gain.setValueAtTime(master.gain.value, ctx.currentTime);
        master.gain.setTargetAtTime(0, ctx.currentTime, 0.18);
        setTimeout(function () { stopBreeze(); if (cb) cb(); }, 900);
      },
      // offline rendering (used for testing)
      renderAll: function (seconds, vol) {
        master.gain.value = vol; nextTime = 0; stepIdx = 0; startBreeze(); schedule(seconds);
      }
    };
  }

  window.GE_MUSIC = { createEngine: createEngine };

  // ---------------------------------------------------------------- player + UI
  var state = { mode: null, ctx: null, engine: null, audio: null, playing: false, blocked: false, vol: DEFAULT_VOL };
  var ui = {};
  var gestureEvents = ['pointerdown', 'keydown', 'touchend', 'click'];

  function volume() {
    var v = parseFloat(store(KEY_VOL));
    return isFinite(v) ? Math.min(1, Math.max(0, v)) : DEFAULT_VOL;
  }
  function engineGain(v) { return 1.3 * v * v; }      // gentle curve, default 0.65 -> 0.55

  function injectStyle() {
    var css = '' +
      '#ge-music{position:fixed;right:16px;bottom:16px;z-index:60;display:flex;align-items:center;gap:10px;font-family:var(--sans,system-ui,sans-serif);}' +
      '#ge-music .ge-btn{width:44px;height:44px;border-radius:50%;border:1px solid var(--line,#3b4740);background:var(--paper,#222a26);color:var(--accent,#b4a3cf);cursor:pointer;display:grid;place-items:center;box-shadow:0 2px 12px rgba(0,0,0,.35);padding:0;transition:border-color .2s,background .2s;}' +
      '#ge-music .ge-btn:hover{border-color:var(--accent,#b4a3cf);}' +
      '#ge-music .ge-btn:focus-visible{outline:2px solid var(--accent,#b4a3cf);outline-offset:3px;}' +
      '#ge-music .ge-eq{display:flex;align-items:flex-end;gap:3px;height:16px;}' +
      '#ge-music .ge-eq i{display:block;width:3px;height:5px;background:currentColor;border-radius:1px;opacity:.9;}' +
      '#ge-music.on .ge-eq i{animation:ge-eq 1.6s ease-in-out infinite;}' +
      '#ge-music.on .ge-eq i:nth-child(2){animation-delay:-.5s;animation-duration:1.9s;}' +
      '#ge-music.on .ge-eq i:nth-child(3){animation-delay:-1s;animation-duration:1.3s;}' +
      '@keyframes ge-eq{0%,100%{height:4px}50%{height:15px}}' +
      '@media (prefers-reduced-motion:reduce){#ge-music.on .ge-eq i{animation:none;height:10px}}' +
      '#ge-music:not(.on) .ge-eq i{height:4px;opacity:.55}' +
      '#ge-music .ge-vol{width:92px;accent-color:var(--accent,#b4a3cf);cursor:pointer;opacity:0;pointer-events:none;transition:opacity .2s;}' +
      '#ge-music.on:hover .ge-vol,#ge-music.on:focus-within .ge-vol{opacity:1;pointer-events:auto;}' +
      '#ge-music .ge-hint{background:var(--paper,#222a26);border:1px solid var(--line,#3b4740);color:var(--ink-soft,#97a393);padding:8px 12px;border-radius:6px;font-size:13px;line-height:1.35;max-width:230px;box-shadow:0 2px 12px rgba(0,0,0,.3);}' +
      '@media (max-width:640px){#ge-music .ge-vol{display:none}#ge-music{right:12px;bottom:12px}}';
    var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  }

  function buildUI() {
    injectStyle();
    var box = document.createElement('div'); box.id = 'ge-music';
    box.innerHTML =
      '<span class="ge-hint" hidden>Нажмите в любом месте — включится тихая музыка</span>' +
      '<input class="ge-vol" type="range" min="0" max="1" step="0.01" aria-label="Громкость музыки">' +
      '<button class="ge-btn" type="button" aria-pressed="false" aria-label="Фоновая музыка"><span class="ge-eq"><i></i><i></i><i></i></span></button>';
    document.body.appendChild(box);
    ui.box = box;
    ui.btn = box.querySelector('.ge-btn');
    ui.vol = box.querySelector('.ge-vol');
    ui.hint = box.querySelector('.ge-hint');
    ui.vol.value = String(state.vol);
    ui.btn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (state.playing) { store(KEY_PREF, 'off'); pause(); }
      else { store(KEY_PREF, 'on'); play(); }
    });
    ui.vol.addEventListener('input', function () {
      state.vol = parseFloat(ui.vol.value); store(KEY_VOL, String(state.vol));
      applyVolume();
    });
    render();
  }

  function render() {
    if (!ui.box) return;
    ui.box.classList.toggle('on', state.playing);
    ui.btn.setAttribute('aria-pressed', state.playing ? 'true' : 'false');
    ui.btn.title = state.playing ? 'Выключить музыку' : 'Включить музыку';
    ui.hint.hidden = !(state.blocked && !state.playing);
  }

  function applyVolume() {
    if (state.mode === 'file' && state.audio) state.audio.volume = state.vol;
    if (state.mode === 'synth' && state.engine) state.engine.setVolume(engineGain(state.vol));
  }

  function detectFile() {
    return fetch(FILE, { method: 'HEAD' }).then(function (r) {
      var ct = r.headers.get('content-type') || '';
      return r.ok && /audio|mpeg|octet-stream/i.test(ct);
    }).catch(function () { return false; });
  }

  function savePos() {
    if (state.mode === 'file' && state.audio) store(KEY_POS, String(state.audio.currentTime), true);
  }

  function startFile() {
    if (!state.audio) {
      state.audio = new Audio(FILE); state.audio.loop = true; state.audio.preload = 'auto';
      var pos = parseFloat(store(KEY_POS, undefined, true));
      if (isFinite(pos)) { state.audio.addEventListener('loadedmetadata', function () { try { state.audio.currentTime = pos; } catch (e) {} }, { once: true }); }
      setInterval(savePos, 2000); window.addEventListener('pagehide', savePos);
    }
    state.audio.volume = state.vol;
    return state.audio.play().then(function () { return true; }, function () { return false; });
  }

  function startSynth() {
    if (!AC) return Promise.resolve(false);
    if (!state.ctx) { state.ctx = new AC(); state.engine = createEngine(state.ctx, state.ctx.destination); }
    var ctx = state.ctx;
    // resume() can stay pending while the browser blocks autoplay, so give it a short deadline
    var resumed = ctx.state === 'running' ? Promise.resolve() : Promise.race([
      ctx.resume(),
      new Promise(function (res) { setTimeout(res, 700); })
    ]);
    return resumed.then(function () {
      if (ctx.state !== 'running') return false;
      state.engine.start(engineGain(state.vol));
      return true;
    }, function () { return false; });
  }

  var AC = window.AudioContext || window.webkitAudioContext;

  function play() {
    if (state.playing) return Promise.resolve(true);
    var go = state.mode ? Promise.resolve(state.mode) : detectFile().then(function (ok) { state.mode = ok ? 'file' : 'synth'; return state.mode; });
    return go.then(function (mode) {
      return (mode === 'file' ? startFile() : startSynth());
    }).then(function (ok) {
      state.playing = !!ok; state.blocked = !ok; render();
      if (ok) detachGesture(); else attachGesture();
      return ok;
    });
  }

  function pause() {
    state.playing = false; state.blocked = false;
    if (state.mode === 'file' && state.audio) { savePos(); state.audio.pause(); }
    if (state.mode === 'synth' && state.engine) {
      var ctx = state.ctx;
      state.engine.stop(function () { if (!state.playing && ctx && ctx.state === 'running') ctx.suspend(); });
    }
    render(); detachGesture();
  }

  function onGesture() {
    if (store(KEY_PREF) === 'off' || state.playing) return;
    play();
  }
  var gestureOn = false;
  function attachGesture() {
    if (gestureOn || store(KEY_PREF) === 'off') return;
    gestureOn = true;
    gestureEvents.forEach(function (e) { document.addEventListener(e, onGesture, true); });
  }
  function detachGesture() {
    if (!gestureOn) return;
    gestureOn = false;
    gestureEvents.forEach(function (e) { document.removeEventListener(e, onGesture, true); });
  }

  function init() {
    state.vol = volume();
    buildUI();
    if (store(KEY_PREF) !== 'off') play();     // try to start on entry; falls back to first interaction
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
