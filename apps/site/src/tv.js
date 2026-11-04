// Channel BadCode. Channel = section (Stories, News, Government, 0 = test card); number = programme.
// TEXT turns any channel into teletext. Every state has a real address (/stories/2, /text/300), so
// links can be shared. Content lives in content.json, injected by build.mjs as window.BADCODE.
(function () {
  'use strict';
  const C = window.BADCODE;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  };
  const tv = $('#tv'), scr = $('#scr'), prog = $('#prog'), video = $('#video'), tt = $('#tt'), tti = $('#tti'), over = $('#over'), osd = $('#osd');
  const snow = $('#snow'), sx = snow.getContext('2d');
  const clean = () => tv.classList.contains('clean') || RM;
  const wait = ms => new Promise(r => setTimeout(r, clean() ? 0 : ms));
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  const MARK_TRI = 'M13.38 -12.51A2.97 2.97 0 0 1 16.33 -8.29L12.77 -0.66A2.97 2.97 0 0 1 7.64 -0.21L2.82 -7.11A2.97 2.97 0 0 1 4.99 -11.77Z';
  const HOST = '<svg class="host" viewBox="0 0 100 120" role="img" aria-label="The BadCode host: a white balaclava with a red triangle eyepatch"><path d="M18 120 C18 80 22 62 50 62 C78 62 82 80 82 120Z" fill="#1d1c1b"/><ellipse cx="50" cy="40" rx="24" ry="30" fill="#f2f0ea"/><rect x="33" y="34" width="34" height="11" rx="5" fill="#2a2522"/><path d="M57 33 L68 36 L62 46 Z" fill="#cc2b37" stroke="#cc2b37" stroke-linejoin="round" stroke-width="2"/><circle cx="41" cy="39.5" r="2" fill="#ddd"/></svg>';
  const RING = (stroke, w = 4.5) => `<svg viewBox="-34 -34 68 68" aria-hidden="true"><circle class="r" r="27.75" fill="none" stroke="${stroke}" stroke-width="${w}" transform="rotate(-90)"/><path class="t" d="${MARK_TRI}" fill="#cc2b37"/></svg>`;

  const CH = ['stories', 'news', 'government', 'testcard'];
  const S = C.stories;
  const count = { stories: S.length * 2, news: Math.max(1, C.news.bulletins.length), government: 2, testcard: 1 };

  // ---------- state + addresses ----------
  let state = { ch: 'stories', p: 1, text: null };
  function fromPath(path) {
    path = path.replace(/\/+$/, '') || '/';
    let m;
    if (path === '/') return null;
    if ((m = path.match(/^\/text\/(\d{3})$/))) return { ch: 'stories', p: 1, text: +m[1] };
    if (path === '/future-proof') return { ch: 'government', p: 2, text: null };
    if (path === '/about') return { ch: 'testcard', p: 1, text: null };
    for (const ch of ['stories', 'news', 'government']) {
      if (path === C.channels[ch].path) return { ch, p: 1, text: null };
      if ((m = path.match(new RegExp('^' + C.channels[ch].path + '/(\\d+)$')))) {
        const p = +m[1];
        if (p >= 1 && p <= count[ch]) return { ch, p, text: null };
      }
    }
    return { ch: 'stories', p: 1, text: 404 };
  }
  function toPath(s) {
    // Pages serves dir/index.html, so every address ends in a slash (no redirect hop)
    if (s.text) return '/text/' + s.text + '/';
    if (s.ch === 'testcard') return '/about/';
    return C.channels[s.ch].path + (s.p > 1 ? '/' + s.p : '') + '/';
  }
  function titleFor(s) {
    if (s.text) return `Page ${s.text} · BadCode Text`;
    if (s.ch === 'stories') { const st = S[(s.p - 1) % S.length]; return (s.p > S.length ? `${st.song} (song)` : st.title) + ' · BadCode'; }
    if (s.ch === 'news') return 'Money For Something · BadCode';
    if (s.ch === 'government') return (s.p === 2 ? 'Future Proof' : 'The BadCode Government') + ' · BadCode';
    return 'About · BadCode';
  }
  function commit(push) {
    const path = toPath(state);
    if (location.pathname.replace(/\/+$/, '') !== path.replace(/\/+$/, '')) {
      try { history[push ? 'pushState' : 'replaceState'](state, '', path); } catch (e) {}
    }
    document.title = titleFor(state);
    if (!state.text || state.text === 404) store.set('bc-last', path);
  }

  // ---------- snow + on-screen display ----------
  let snowing = false;
  function snowLoop() { if (!snowing) return; const im = sx.createImageData(160, 120); for (let i = 0; i < im.data.length; i += 4) { const v = Math.random() * 255 | 0; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255; } sx.putImageData(im, 0, 0); setTimeout(snowLoop, 70); }
  async function burst(ms) { if (clean()) return; scr.classList.add('static'); snowing = true; snowLoop(); await wait(ms); snowing = false; scr.classList.remove('static'); }
  let osdT;
  function flashOsd() {
    const c = C.channels[state.ch];
    osd.innerHTML = state.text ? `P${state.text}<small>TEXT</small>` : `${c.n}<small>${esc(c.short)}${count[state.ch] > 1 ? ' · ' + state.p : ''}</small>`;
    osd.classList.add('show'); clearTimeout(osdT); osdT = setTimeout(() => osd.classList.remove('show'), 2200);
  }

  // ---------- video ----------
  function videoFor(s) { if (s.ch === 'stories') { const st = S[(s.p - 1) % S.length]; return s.p > S.length ? st.songVideo : st.film; } if (s.ch === 'news') { const b = C.news.bulletins[s.p - 1]; return b && b.youtube; } return null; }
  function stopVideo() { video.innerHTML = ''; video.classList.remove('on'); tv.classList.remove('playing'); }
  function play(id) {
    video.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&playsinline=1" title="${esc(titleFor(state))}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`;
    video.classList.add('on'); tv.classList.add('playing');
  }

  // ---------- programmes ----------
  let govTimer;
  function renderProg(gesture) {
    clearTimeout(govTimer); stopVideo();
    tv.classList.toggle('daylight', state.ch === 'government');
    const s = state;
    if (s.ch === 'stories') {
      const i = (s.p - 1) % S.length, st = S[i], song = s.p > S.length, vid = song ? st.songVideo : st.film;
      const pic = st.still ? `<img class="still" src="${esc(st.still)}" alt="">` : `<div class="blank"><span>PICTURE COMING</span></div>`;
      const sleeve = song ? `<div class="sleeve">${st.still ? `<img src="${esc(st.still)}" alt="">` : ''}</div>` : '';
      const status = vid ? `<button class="pill" data-play>▶ Play</button>` : `<span class="pill">Coming to YouTube</span>`;
      prog.innerHTML = `<div class="p-story${song ? ' song' : ''}">${pic}${sleeve}<span class="bug">BadCode One · ${s.p} of ${count.stories}</span>
        <div class="cap"><span class="kind">${song ? 'Song from ' + esc(st.title) : 'Film ' + (i + 1) + ' of ' + S.length}</span><h1>${esc(song ? st.song : st.title)}</h1>
        ${song ? '' : `<p>${esc(st.blurb)}</p>`}${status}</div></div>`;
      if (vid && gesture) play(vid);
    } else if (s.ch === 'news') {
      const n = C.news, b = n.bulletins[s.p - 1];
      prog.innerHTML = `<div class="p-news"><span class="bug">Money For Something</span>${HOST}
        <div class="txt"><h1>${esc(b ? b.title : n.title)}</h1><p class="strap">${esc(n.strap)}</p>${b && b.youtube ? '<button class="pill" data-play>▶ Play</button>' : `<span class="pill">${esc(n.status)}</span>`}</div>
        <div class="lower">${esc(n.signoff)}<small>BadCode news · working name</small></div>
        <div class="tick"><span>${n.ticker.map(esc).join('  ◂  ')}</span></div></div>`;
      if (b && b.youtube && gesture) play(b.youtube);
    } else if (s.ch === 'government') {
      const g = C.government;
      const bar = `<div class="bar"><svg viewBox="-34 -34 68 68" aria-hidden="true"><circle r="27.75" fill="none" stroke="#fff" stroke-width="4.5"/><path d="${MARK_TRI}" fill="#cc2b37"/></svg>The BadCode Government</div>`;
      if (s.p === 2) {
        const f = g.futureProof;
        prog.innerHTML = `<div class="p-gov fp">${bar}<div class="body"><p class="q">Future Proof</p><h1>${esc(f.question)}</h1><p class="lead">${esc(f.intro)}</p>
          <ol>${f.tenets.map(t => `<li><b>${esc(t[0])}</b><span>${esc(t[1])}</span></li>`).join('')}</ol><p class="ask">${esc(f.ask)}</p><p class="notreal">${esc(g.notReal)} Press ◀ for the manifesto.</p></div><div class="haz"></div></div>`;
      } else {
        const seen = store.get('bc-ppb');
        prog.innerHTML = `<div class="p-gov">${bar}<div class="body"><p class="q">The manifesto</p><h1>${esc(g.promise)}</h1>
          <ol>${g.pledges.map(t => `<li><b>${esc(t[0])}</b><span>${esc(t[1])}</span></li>`).join('')}</ol><p class="notreal">${esc(g.notReal)} Press 2 for Future Proof.</p></div><div class="haz"></div>
          <div class="ppb${seen || clean() ? ' gone' : ''}"><p>There now follows a party political broadcast on behalf of</p><b>The BadCode Government</b></div></div>`;
        if (!seen && !clean()) { store.set('bc-ppb', '1'); govTimer = setTimeout(() => { const p = $('.ppb', prog); if (p) p.classList.add('gone'); }, 2600); }
      }
    } else {
      prog.innerHTML = `<div class="p-test"><div class="bars"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="disc">${HOST}</div><div class="cap">TEST CARD B · BADCODE · press TEXT for page 800, about BadCode</div></div>`;
    }
    const pb = $('[data-play]', prog); if (pb) pb.onclick = () => { const v = videoFor(state); if (v) play(v); };
  }

  // ---------- teletext ----------
  const W = 40;
  const pad = (s, n) => s + ' '.repeat(Math.max(0, n - s.length));
  function wrap(text, width = 37, indent = ' ') { const out = []; let line = ''; for (const w of String(text).split(/\s+/)) { if ((line + ' ' + w).trim().length > width) { out.push(indent + line.trim()); line = w; } else line += ' ' + w; } if (line.trim()) out.push(indent + line.trim()); return out; }
  const L = (cls, text) => `<span class="${cls}">${esc(text)}</span>`;
  const link = (page, label, cls = 'y') => `<a class="${cls}" href="/text/${page}/" data-page="${page}">${esc(label)}</a>`;
  const stamp = () => { const d = new Date(); return d.toLocaleDateString('en-GB', { weekday: 'short', day: '2-digit', month: 'short' }).replace(',', '') + ' ' + d.toTimeString().slice(0, 8); };
  const head = p => `<span class="w">P${p}</span> <span class="y">BADCODE</span>  <span class="w hdclock">${stamp()}</span>`;
  const title = (cls, t) => `<span class="${cls} dh">${esc(pad(' ' + t, W))}</span>`;
  const fast = `<span class="ft"><a class="br" href="/text/300/" data-page="300"> News  </a><a class="bg" href="/text/888/" data-page="888"> Future </a><a class="by" href="/text/400/" data-page="400"> Govt  </a><a class="bb w" href="/text/200/" data-page="200"> Stories </a></span>`;
  const dots = (label, page) => `<span class="w"> ${esc(pad(label + ' ', 33).replace(/ (?= *$)/g, '.'))}</span>${link(page, String(page))}`;
  function page(p) {
    const n = C.news, g = C.government, a = C.about;
    const P = {
      100: () => [head(p), '', title('bb y', 'BADCODE TEXT'), '', L('c', ' Received from a future that went wrong'), '',
        dots('Stories: films and songs', 200), dots('News: Money For Something', 300), dots('The BadCode Government', 400), dots('Future Proof', 888), dots('Follow BadCode', 700), dots('About BadCode', 800), '',
        L('m', ' We have seen how this ends. We came'), L('m', ' back to change it. Type a page, or'), L('m', ' press a colour below.')],
      200: () => [head(p), '', title('br w', 'STORIES'), '', ...S.flatMap((st, i) => [`<span class="w"> ${i + 1} </span>${link(201 + i, st.title.toUpperCase().slice(0, 34))}`, L('c', `   song ${i + 5}: ${st.song.slice(0, 30)}`)]), '',
        L('w', ' Each film works on its own. They also'), L('w', ' share one universe.'), '', L('g', ' Channel 1 for pictures: press STORIES')],
      300: () => [head(p), '', title('br w', 'MONEY FOR SOMETHING'), '', ...wrap(n.strap), '', L('y', ' ' + n.status), '', ...wrap(n.ticker[2]), '', L('m', ' "' + n.signoff.slice(0, 35)), L('m', '  ' + n.signoff.slice(35) + '"'), '', L('b', ' Working name.')],
      400: () => [head(p), '', title('by', 'THE BADCODE GOVERNMENT'), '', L('w', ' THE MANIFESTO'), '', ...g.pledges.flatMap((pl, i) => [L('y', ` PLEDGE ${i + 1}`) + L('w', ' ' + pl[0].slice(0, 28)), ...wrap(pl[1], 34, '   ').map(x => L('c', x)), '']),
        `<span class="g"> ${esc(g.promise.slice(0, 33))} </span>${link(888, '888', 'g')}`, L('b', ' ' + g.notReal)],
      700: () => [head(p), '', title('bb y', 'FOLLOW BADCODE'), '', ...C.socials.map(s => s.url ? `<span class="w"> </span><a class="y" href="${esc(s.url)}" target="_blank" rel="noopener">${esc(pad(s.name, 12))}</a><span class="g">open</span>` : `<span class="w"> ${esc(pad(s.name, 12))}</span><span class="b">soon</span>`)],
      800: () => [head(p), '', title('bb y', 'ABOUT BADCODE'), '', ...wrap(a.lede), L('r', ' ' + a.request), '', ...wrap(a.story), '', ...wrap(a.ai).map(x => L('c', x)), '', ...wrap(a.sign).map(x => L('m', x))],
      888: () => [`P888 SUBTITLES: WHAT WE MEANT ${stamp().slice(0, 10)}`, '', `<span class="dh">${esc(pad(' FUTURE PROOF', W))}</span>`, '', ...wrap(g.futureProof.question), '', ...g.futureProof.tenets.map((t, i) => ` ${i + 1} ${t[0]}`), '', ...wrap(g.futureProof.ask), '', ' Channel 3, programme 2, has the rest.', ' ' + '100 back to the index'],
    };
    for (let i = 0; i < S.length; i++) {
      P[201 + i] = () => { const st = S[i]; return [head(201 + i), '', title('br w', st.title.toUpperCase().slice(0, 38)), '', ...wrap(st.blurb), '', L('y', ' Film: ') + L('w', st.film ? 'on YouTube now' : 'coming to YouTube'), L('y', ' Song: ') + L('w', st.song.slice(0, 31)), '', `<span class="w"> Picture: STORIES, then </span>${L('y', String(i + 1))}`, `<span class="w"> All stories </span>${link(200, '200')}`]; };
    }
    if (P[p]) return P[p]();
    return [head(p), '', L('w', ` Page ${p} not found.`), L('c', " We saw you'd try that."), '', `<span class="w"> Index </span>${link(100, '100')}`];
  }
  function drawText() {
    const p = state.text;
    tt.classList.toggle('day', p === 888);
    const lines = page(p === 404 ? 404 : p);
    while (lines.length < 23) lines.push('');
    lines[23] = fast;
    tti.innerHTML = lines.map(l => `<div>${l || '&nbsp;'}</div>`).join('');
  }
  tti.addEventListener('click', e => { const a = e.target.closest('a[data-page]'); if (a) { e.preventDefault(); goText(+a.dataset.page); } });
  setInterval(() => { const c = $('.hdclock', tti); if (c) c.textContent = stamp(); }, 1000);
  let typed = '';
  function goText(p, push = true) { state.text = p; typed = ''; render(false); commit(push); flashOsd(); }

  // ---------- render ----------
  function syncRemote() {
    $('[data-k=text]').setAttribute('aria-pressed', !!state.text);
    $$('.strands button').forEach(b => b.setAttribute('aria-current', !state.text && b.dataset.k === state.ch));
  }
  function render(gesture) {
    syncRemote();
    if (state.text) { stopVideo(); tt.classList.add('on'); prog.classList.remove('on'); tv.classList.remove('daylight'); drawText(); return; }
    tt.classList.remove('on'); prog.classList.add('on'); renderProg(gesture);
  }
  async function tune(next, push = true) {
    if (off) powerOn(false);
    state = Object.assign({ text: null }, next);
    commit(push); flashOsd(); await burst(180); render(true);
  }

  // ---------- power, hijack, closedown ----------
  let off = false;
  function powerOff() { off = true; stopVideo(); tv.classList.add('off'); }
  function powerOn() { off = false; tv.classList.remove('off'); }
  function londonHour() { try { return +new Intl.DateTimeFormat('en-GB', { hour: 'numeric', hourCycle: 'h23', timeZone: 'Europe/London' }).format(new Date()); } catch (e) { return 12; } }
  function closedown() {
    over.innerHTML = `<div class="ov-closed" role="button" tabindex="0" aria-label="Closedown. Press any button to carry on.">${RING('#cfc8bb')}<p>BadCode has now closed down.<br>Programmes resume at 6am.<br>The future doesn't close.</p><small>Press any button to carry on watching.</small></div>`;
    over.classList.add('on');
    try { sessionStorage.setItem('bc-closed', '1'); } catch (e) {}
  }
  const dismiss = () => { if (over.classList.contains('on') && $('.ov-closed', over)) { over.classList.remove('on'); over.innerHTML = ''; return true; } return false; };
  async function hijack() {
    over.classList.add('on');
    over.innerHTML = `<div class="ov-boring"><h2>Public consultation: your views on local services</h2><i></i><i style="width:70%"></i><i style="width:85%"></i><i style="width:40%"></i><i style="width:60%"></i></div>`;
    await wait(1300); scr.classList.add('tear'); await burst(450); scr.classList.remove('tear');
    over.innerHTML = `<div class="ov-host">${HOST}</div>`; await wait(1000);
    await ident();
  }
  async function ident() { over.classList.add('on'); over.innerHTML = `<div class="ov-ident">${RING('#e8e2d6')}<p>${esc(C.channels[state.ch].name.toUpperCase())}</p></div>`; await wait(1300); over.classList.remove('on'); over.innerHTML = ''; }

  // ---------- input ----------
  function strand(ch) {
    if (state.text) { goText(C.channels[ch].teletext); return; }
    tune({ ch, p: 1 });
  }
  function step(d) {
    if (state.text) { const order = [100, 200, ...S.map((_, i) => 201 + i), 300, 400, 700, 800, 888]; const i = order.indexOf(state.text); goText(order[(i + d + order.length) % order.length]); return; }
    const n = count[state.ch]; tune({ ch: state.ch, p: ((state.p - 1 + d + n) % n) + 1 });
  }
  function chStep(d) { const i = CH.indexOf(state.ch); tune({ ch: CH[(i + d + CH.length) % CH.length], p: 1 }); }
  function digit(k) {
    if (state.text) { typed = (typed + k).slice(-3); if (typed.length < 3) { const h = $('#tti div'); if (h) h.innerHTML = `<span class="w">P${typed.padEnd(3, '-')}</span> <span class="y">BADCODE</span>  <span class="w">searching</span>`; return; } goText(+typed); return; }
    if (k === '0') { tune({ ch: 'testcard', p: 1 }); return; }
    const p = +k; if (p <= count[state.ch]) tune({ ch: state.ch, p }); else flashOsd();
  }
  function setClean(v) { tv.classList.toggle('clean', v); $('[data-k=clean]').setAttribute('aria-pressed', v); store.set('bc-clean', v ? '1' : ''); }
  function setTucked(v) { tv.classList.toggle('tucked', v); store.set('bc-tucked', v ? '1' : ''); }
  const KEYS = {
    power: () => off ? (powerOn(), render(false)) : powerOff(),
    text: () => { if (state.text) { state.text = null; render(false); commit(true); flashOsd(); } else goText(C.channels[state.ch].teletext); },
    clean: () => setClean(!tv.classList.contains('clean')),
    tuck: () => setTucked(!tv.classList.contains('tucked')),
    stories: () => strand('stories'), news: () => strand('news'), government: () => strand('government'),
    prev: () => step(-1), next: () => step(1), up: () => chStep(1), down: () => chStep(-1),
  };
  function press(k) {
    if (dismiss() && k !== 'power') { return; }
    if (off && k !== 'power') powerOn();
    if (/^\d$/.test(k)) digit(k); else if (KEYS[k]) KEYS[k]();
  }
  $$('[data-k]').forEach(b => b.addEventListener('click', () => press(b.dataset.k)));
  over.addEventListener('click', () => dismiss());
  document.addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey || e.target.closest('input,textarea')) return;
    const map = { ArrowLeft: 'prev', ArrowRight: 'next', ArrowUp: 'up', ArrowDown: 'down', t: 'text', s: 'stories', n: 'news', g: 'government', c: 'clean', r: 'tuck', Escape: state.text ? 'text' : null };
    if (/^\d$/.test(e.key)) { press(e.key); e.preventDefault(); return; }
    const k = map[e.key]; if (k) { press(k); e.preventDefault(); }
  });
  // swipe on the picture: up/down changes channel, left/right changes programme
  let t0 = null;
  scr.addEventListener('touchstart', e => { const t = e.touches[0]; t0 = { x: t.clientX, y: t.clientY }; }, { passive: true });
  scr.addEventListener('touchend', e => {
    if (!t0) return; const t = e.changedTouches[0], dx = t.clientX - t0.x, dy = t.clientY - t0.y; t0 = null;
    if (Math.max(Math.abs(dx), Math.abs(dy)) < 50) return;
    const sc = e.target.closest && e.target.closest('.p-gov');
    if (sc && sc.scrollHeight > sc.clientHeight + 4 && Math.abs(dy) > Math.abs(dx)) return; // that swipe was a scroll
    if (dismiss()) return;
    if (Math.abs(dy) > Math.abs(dx)) chStep(dy < 0 ? 1 : -1); else step(dx < 0 ? 1 : -1);
  }, { passive: true });
  window.addEventListener('popstate', () => { const s = fromPath(location.pathname); if (s) { state = s; render(false); flashOsd(); document.title = titleFor(state); } });

  // ---------- start ----------
  (async function start() {
    if (store.get('bc-clean')) setClean(true);
    const smallLandscape = matchMedia('(orientation: landscape) and (max-height: 520px)').matches;
    if (store.get('bc-tucked') || smallLandscape) setTucked(true);
    const home = (location.pathname.replace(/\/+$/, '') || '/') === '/';
    const deep = fromPath(location.pathname);
    let last = null; const lp = store.get('bc-last'); if (home && lp) last = fromPath(lp);
    state = deep || last || { ch: 'stories', p: 1, text: null };
    if (state.text === 404 && !location.pathname.startsWith('/text/')) state.text = 404;
    render(false);
    if (!home || state.text === 404) { document.title = titleFor(state); if (state.text !== 404) store.set('bc-last', toPath(state)); flashOsd(); }
    let closed = false; try { closed = !!sessionStorage.getItem('bc-closed'); } catch (e) {}
    const h = londonHour();
    if (home) {
      if (!store.get('bc-seen') && !clean()) { store.set('bc-seen', '1'); await hijack(); }
      else if (!clean()) await ident();
      commit(false); flashOsd();
    }
    if (h >= 1 && h < 6 && !closed) closedown();
  })();
})();
