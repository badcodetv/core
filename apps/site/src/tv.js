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
  // a manifesto body, escaped: "## x" becomes <h2>, other blank-line blocks <p> (same rule as build.mjs)
  const bodyHtml = b => String(b).split(/\n\s*\n/).map(x => x.trim()).filter(Boolean).map(x => x.startsWith('## ') ? `<h2>${esc(x.slice(3))}</h2>` : `<p>${esc(x.replace(/\s*\n\s*/g, ' '))}</p>`).join('');

  const MARK_TRI = 'M13.38 -12.51A2.97 2.97 0 0 1 16.33 -8.29L12.77 -0.66A2.97 2.97 0 0 1 7.64 -0.21L2.82 -7.11A2.97 2.97 0 0 1 4.99 -11.77Z';
  const HOST = '<svg class="host" viewBox="0 0 100 120" role="img" aria-label="The BadCode host: a white balaclava with a red triangle eyepatch"><path d="M18 120 C18 80 22 62 50 62 C78 62 82 80 82 120Z" fill="#1d1c1b"/><ellipse cx="50" cy="40" rx="24" ry="30" fill="#f2f0ea"/><rect x="33" y="34" width="34" height="11" rx="5" fill="#2a2522"/><path d="M57 33 L68 36 L62 46 Z" fill="#cc2b37" stroke="#cc2b37" stroke-linejoin="round" stroke-width="2"/><circle cx="41" cy="39.5" r="2" fill="#ddd"/></svg>';
  const RING = (stroke, w = 4.5) => `<svg viewBox="-34 -34 68 68" aria-hidden="true"><circle class="r" r="27.75" fill="none" stroke="${stroke}" stroke-width="${w}" transform="rotate(-90)"/><path class="t" d="${MARK_TRI}" fill="#cc2b37"/></svg>`;

  const CH = ['stories', 'news', 'government', 'testcard'];
  const S = C.stories, SVP = C.storyverse;
  // NEWS is the catch-all for specials (Kai, 2026-11-11): 1 Future Proof, 2 The Storyverse, then Money For
  // Something (its bulletins when there are some, its title card until then). Shorts go here too.
  const NP = [{ k: 'fp' }, { k: 'sv' }, ...(C.news.bulletins.length ? C.news.bulletins.map((b, i) => ({ k: 'mfs', i })) : [{ k: 'mfs', i: 0 }])];
  const NEWS_FP = 1, NEWS_SV = 2;
  const newsProg = p => NP[p - 1] || NP[NP.length - 1];
  // GOVT: 1 the manifesto (where it stands), then the government in action, as a broadcast
  // (design/2026-11-11-future-proof-government/visual/, round 2): 2 Live, 3 The floor, 4 The record, 5 Replay
  const GOV_TABS = [[1, 'Manifesto'], [2, 'Live'], [3, 'The floor'], [4, 'The record'], [5, 'Replay']];
  const DEB = C.government.debates || [];
  // the cabinet: every minister but the PM, whose line is the promise heading (docs/government/manifesto/)
  const CAB = (C.government.manifesto || []).filter(m => m.post !== 'prime-minister');
  // one record per policy (docs/government/policies/), built by build.mjs: text, marks, history, world check
  const POLS = C.government.policies || [];
  const MARKS = [['test', 'Has its test', 'Not ready'], ['undo', 'Has an undo', 'No undo'], ['prediction', 'Makes a prediction', 'No prediction'], ['argued', 'Argued against', 'Not argued yet']];
  const marksHtml = r => `<ul class="marks">${MARKS.map(([k, y, n]) => `<li class="${r.marks[k] ? 'on' : 'off'}">${r.marks[k] ? '✔' : '✘'} ${esc(r.marks[k] ? y : n)}</li>`).join('')}</ul>`;
  const odds = p => Math.round(p * 100) + '%';
  const count = { stories: S.length * 2, news: NP.length, government: GOV_TABS.length, testcard: 1 };

  // ---------- state + addresses ----------
  let state = { ch: 'stories', p: 1, text: null };
  function fromPath(path) {
    path = path.replace(/\/+$/, '') || '/';
    let m;
    if (path === '/') return null;
    if ((m = path.match(/^\/text\/(\d{3})$/))) return { ch: 'stories', p: 1, text: +m[1] };
    if (path === '/future-proof') return { ch: 'news', p: NEWS_FP, text: null };
    if (path === '/storyverse' || path === '/stories/9') return { ch: 'news', p: NEWS_SV, text: null }; // /stories/9 was its old home
    if (path === '/about') return { ch: 'testcard', p: 1, text: null };
    if (path === '/government/scoreboard') return { ch: 'government', p: 1, text: null, board: true };
    if ((m = path.match(/^\/government\/([a-z-]+\/[a-z0-9-]+)$/)) && POLS.some(x => x.id === m[1])) return { ch: 'government', p: 1, text: null, policy: m[1] };
    if ((m = path.match(/^\/government\/([a-z-]+)$/)) && CAB.some(x => x.post === m[1])) return { ch: 'government', p: 1, text: null, minister: m[1] };
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
    if (s.ch === 'government' && s.p === 1 && s.board) return '/government/scoreboard/';
    if (s.ch === 'government' && s.p === 1 && s.policy) return '/government/' + s.policy + '/';
    if (s.ch === 'government' && s.p === 1 && s.minister) return '/government/' + s.minister + '/';
    return C.channels[s.ch].path + (s.p > 1 ? '/' + s.p : '') + '/';
  }
  function titleFor(s) {
    if (s.text) return `Page ${s.text} · BadCode Text`;
    if (s.ch === 'stories') { const st = S[(s.p - 1) % S.length]; return (s.p > S.length ? `${st.song} (song)` : st.title) + ' · BadCode'; }
    if (s.ch === 'news') { const k = newsProg(s.p).k; return (k === 'fp' ? 'Future Proof' : k === 'sv' ? SVP.title : 'Money For Something') + ' · BadCode'; }
    if (s.ch === 'government' && s.board) return 'The scoreboard · The BadCode Government';
    if (s.ch === 'government' && s.policy) { const r = POLS.find(x => x.id === s.policy); if (r) return r.title + ' · The BadCode Government'; }
    if (s.ch === 'government') { const mm = s.p === 1 && s.minister && CAB.find(x => x.post === s.minister); return (s.p > 1 ? GOV_TABS[s.p - 1][1] + ' · The BadCode Government' : mm ? mm.title + ' · The BadCode Government' : 'The BadCode Government') + (mm ? '' : ' · BadCode'); }
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
  function videoFor(s) { if (s.ch === 'stories') { const st = S[(s.p - 1) % S.length]; return s.p > S.length ? st.songVideo : st.film; } if (s.ch === 'news') { const np = newsProg(s.p), b = np.k === 'mfs' && C.news.bulletins[np.i]; return b && b.youtube; } return null; }
  function stopVideo() { video.innerHTML = ''; video.classList.remove('on'); tv.classList.remove('playing'); }
  function play(id) {
    video.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&playsinline=1" title="${esc(titleFor(state))}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`;
    video.classList.add('on'); tv.classList.add('playing');
  }

  // ---------- programmes ----------
  let govTimer;
  // ---------- the government in action (GOVT 2–5) ----------
  // One broadcast in four views over the same data: the policies (C.government.policies) and the debate logs
  // (C.government.debates, captions made by apps/site/debates.mjs). Role colours are the same everywhere:
  // minister green, opposition red, statistician blue, human amber. Design: design/2026-11-11-future-proof-government/visual/.
  const MINN = { 'prime-minister': 'Prime Minister', chancellor: 'Chancellor', foreign: 'Foreign Secretary', home: 'Home Secretary', education: 'Education Secretary', defence: 'Defence Secretary', health: 'Health Secretary', housing: 'Housing Secretary', 'energy-climate': 'Energy Secretary', 'work-pensions': 'Work and Pensions' };
  const ROLE = { opposition: ['The Opposition', 'var(--opp)', 'attacks', 'Finds the strongest case against the policy'], statistician: ['The Statistician', 'var(--stat)', 'checks', "Refuses anything that can't be measured"] };
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const dshort = d => { const [y, m, dd] = String(d).split('-'); return `${+dd} ${MON[+m - 1]} ${y.slice(2)}`; };
  const dlong = d => { const [y, m, dd] = String(d).split('-'); return `${+dd} ${MON[+m - 1]} ${y}`; };
  const tenths = p => `${Math.round(p * 10)} in 10`;
  const daysTo = d => Math.max(0, Math.ceil((new Date(d + 'T12:00:00') - Date.now()) / 864e5));
  const DBY = Object.fromEntries(DEB.map(d => [d.id, d]));
  const polOf = id => POLS.find(r => r.id === id);
  const checked = () => POLS.filter(r => r.check && r.marks.test).sort((a, b) => a.check.on.localeCompare(b.check.on));
  const notReady = () => POLS.filter(r => !r.marks.test);
  const tally = res => DEB.reduce((n, d) => n + d.points.filter(x => x.res === res).length, 0);
  const BEATS = [];
  DEB.forEach((d, di) => d.points.forEach((x, pi) => { BEATS.push({ di, pi, half: 0 }); BEATS.push({ di, pi, half: 1 }); }));
  let gv = { bi: 0, playing: !RM, filter: 'all', drawer: null, rd: 0, rp: 0 };

  function statusHtml() {
    const next = checked()[0];
    return `<ul class="gstat"><li><b>${POLS.length}</b> policies, each on its own</li><li><b>${DEB.length}</b> argued in public</li><li><b>${notReady().length}</b> still need a real test</li>${next ? `<li>First prediction marked in <b>${daysTo(next.check.on)} days</b></li>` : ''}</ul>
      <p class="tolive"><a href="/government/2/" data-gp="2">● Watch the government work, live</a></p>`;
  }
  function govShell(p, inner) {
    const next = checked()[0];
    const tick = [DEB.length ? `${tally('conceded')} points conceded and ${tally('rebutted')} argued back so far` : '', next ? `First prediction marked in ${daysTo(next.check.on)} days: ${next.title}` : '', `${POLS.length} policies on the table, ${notReady().length} still need a real test`, 'The opposition sits at 07:30 and the statistician at 08:00', 'Every change is signed off by a human before it goes live'].filter(Boolean);
    prog.innerHTML = `<div class="p-live"><div class="lnav"><span class="brand">The BadCode Government</span>
      <nav class="tabs" aria-label="The government">${GOV_TABS.map(([n, l]) => `<a href="/government/${n > 1 ? n + '/' : ''}" data-gp="${n}"${n === p ? ' aria-current="page"' : ''}>${n === 2 ? '<i class="dot"></i>' : ''}${l}</a>`).join('')}</nav>
      <span class="clock">${new Date().toTimeString().slice(0, 5)}</span></div>
      <div class="lview">${inner}</div>
      <div class="ticker" aria-hidden="true"><b>Latest</b><div><div class="run">${tick.map(t => `<span>${esc(t)}</span>`).join('')}</div></div></div></div>`;
  }
  const verdict = res => `<span class="verdict v-${res}">${res === 'conceded' ? 'Conceded' : 'Argued back'}</span>`;
  const goGov = (p, extra = {}) => { Object.assign(gv, extra); state = { ch: 'government', p, text: null }; render(false); commit(true); };

  function govLive() {
    if (!BEATS.length) { govShell(2, `<div class="lempty"><p>The first sitting hasn't been argued yet. The opposition sits at 07:30.</p></div>`); return; }
    const b = BEATS[gv.bi % BEATS.length], d = DEB[b.di], x = d.points[b.pi], pol = polOf(d.id) || { title: d.title, line: '', post: '' };
    const role = ROLE[x.who] || ROLE.opposition;
    const stage = b.half === 0 ? (x.who === 'opposition' ? 1 : 2) : 3;
    const RAIL = [['Written', '06:00'], ['Attacked', '07:30'], ['Checked', '08:00'], ['Answered', 'next 06:00'], ['Signed off', 'by a human'], ['Marked', pol.check ? dshort(pol.check.on) : 'on its date']];
    const lower = b.half === 0
      ? `<div class="who" style="background:${role[1]}">${role[0]}<small>${role[2]}, point ${b.pi + 1} of ${d.points.length}</small></div><div class="said"><p>${role[3]}</p></div>`
      : `<div class="who" style="background:var(--cab)">${esc(x.by)}<small>answers point ${b.pi + 1}</small></div><div class="said"><p>${x.res === 'conceded' && x.what ? '<b>Changed:</b> ' + esc(x.what) : 'Stands by it. The point stays on the record.'}</p>${verdict(x.res)}</div>`;
    govShell(2, `<div class="live">
      <div class="head"><span class="kick">On the table · ${esc(MINN[pol.post] || '')}</span><h2>${esc(d.title)}</h2><p class="pline">${esc(pol.line)}</p>
        <div class="lctl"><button data-lv="-1" aria-label="Back">◀</button><button data-lv="p" aria-pressed="${gv.playing}">${gv.playing ? 'Pause' : 'Play'}</button><button data-lv="1" aria-label="Next">▶</button><button data-lv="r">Watch from the start</button></div></div>
      <blockquote class="quote fade" style="--qc:${b.half ? 'var(--cab)' : role[1]}">${esc(b.half ? x.answer : x.said)}</blockquote>
      <div class="side">${pol.check ? `<div class="odds"><b>${tenths(pol.check.prior)}</b><span>our odds: ${esc(pol.check.claim.length > 120 ? pol.check.claim.slice(0, 118).replace(/\s\S*$/, '') + '…' : pol.check.claim)} Marked ${dlong(pol.check.on)}.</span></div>` : ''}
        <div class="score"><div><b style="color:var(--cab)">${d.points.filter(y => y.res === 'conceded').length}</b><span>conceded</span></div><div><b style="color:var(--opp)">${d.points.filter(y => y.res === 'rebutted').length}</b><span>argued back</span></div></div></div>
      <div class="lower fade">${lower}</div>
      <ol class="rail">${RAIL.map(([r, t], i) => `<li class="${i < stage ? 'done' : i === stage ? 'now' : ''}">${r}<small>${t}</small></li>`).join('')}</ol></div>`);
    $$('[data-lv]', prog).forEach(btn => btn.onclick = () => {
      const k = btn.dataset.lv;
      if (k === 'r') { goGov(5, { rd: b.di, rp: 0 }); return; }
      if (k === 'p') gv.playing = !gv.playing; else gv.bi = (gv.bi + +k + BEATS.length) % BEATS.length;
      govLive(); const again = $(`[data-lv="${k}"]`, prog); if (again) again.focus();
    });
    clearTimeout(govTimer);
    if (gv.playing && !clean()) govTimer = setTimeout(() => { if (state.ch === 'government' && state.p === 2 && !state.text) { gv.bi = (gv.bi + 1) % BEATS.length; govLive(); } }, 6500);
  }

  function govFloor() {
    const F = { all: () => true, argued: r => DBY[r.id], soon: r => r.marks.test && r.check && daysTo(r.check.on) < 150, nr: r => !r.marks.test };
    const onAir = BEATS.length ? DEB[BEATS[gv.bi % BEATS.length].di].id : '';
    const pips = r => DBY[r.id] ? 5 : r.marks.test ? 2 : 1; // argued: through "signed off"; the rest written and signed off, not yet attacked
    const tile = r => `<button class="tile${DBY[r.id] ? ' argued' : ''}${r.marks.test ? '' : ' nr'}${F[gv.filter](r) ? '' : ' dimmed'}" data-tp="${esc(r.id)}">${r.id === onAir ? '<i class="tally" title="On air now"></i>' : ''}<b>${esc(r.title)}</b>
      <span class="pips">${[0, 1, 2, 3, 4, 5].map(i => `<i class="${i <= pips(r) ? 'on' : ''}"></i>`).join('')}</span>
      <span class="meta"><span>${r.marks.test && r.check ? tenths(r.check.prior) : 'Needs a test'}</span><span>${r.marks.test && r.check ? dshort(r.check.on) : ''}</span></span></button>`;
    const posts = Object.keys(MINN).filter(p => POLS.some(r => r.post === p));
    const dr = gv.drawer && polOf(gv.drawer);
    govShell(3, `<div class="floor">
      <div class="fbar"><span class="sum">${POLS.length} on the table <span>· ${DEB.length} argued · ${notReady().length} need a test</span></span>
        ${[['all', 'All'], ['argued', 'Argued'], ['soon', 'Marked within 5 months'], ['nr', 'Needs a test']].map(([k, l]) => `<button class="chip" data-ff="${k}" aria-pressed="${gv.filter === k}">${l}</button>`).join('')}</div>
      <p class="key"><span><i class="k-arg"></i>argued: see the replay</span><span><i class="k-nr"></i>no real test yet</span><span><i class="k-air"></i>on air now</span><span>bars: how far through the day's steps</span></p>
      ${posts.map(p => `<div class="desk"><h3>${esc(MINN[p])}</h3><div class="tiles">${POLS.filter(r => r.post === p).map(tile).join('')}</div></div>`).join('')}</div>
      ${dr ? `<div class="drawer" role="dialog" aria-label="${esc(dr.title)}"><button class="chip x" data-fx>Close</button><span class="dmin">${esc(MINN[dr.post] || '')}</span><h3>${esc(dr.title)}</h3><p>${esc(dr.line)}</p>
        <p>${!dr.marks.test ? "<b>No real test yet.</b> It says so on its page rather than invent a number to look complete." : dr.check ? `<b>Our prediction, ${tenths(dr.check.prior)}:</b> ${esc(dr.check.claim)} Marked ${dlong(dr.check.on)}.` : ''}</p>
        <p class="dnote">The opposition hasn't reached this one yet. It takes up to six a day. <a href="/government/${esc(dr.id)}/" data-policy="${esc(dr.id)}">Read the policy</a></p></div>` : ''}`);
    const fl = $('.floor', prog);
    $$('[data-ff]', prog).forEach(b => b.onclick = () => { gv.filter = b.dataset.ff; govFloor(); $(`[data-ff="${gv.filter}"]`, prog).focus(); });
    $$('[data-tp]', prog).forEach(b => b.onclick = () => {
      const id = b.dataset.tp;
      if (DBY[id]) { goGov(5, { rd: DEB.indexOf(DBY[id]), rp: 0 }); return; }
      const top = fl.scrollTop; gv.drawer = id; govFloor(); $('.floor', prog).scrollTop = top; $('[data-fx]', prog).focus();
    });
    const fx = $('[data-fx]', prog); if (fx) fx.onclick = () => { gv.drawer = null; govFloor(); };
    $$('[data-policy]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, policy: a.dataset.policy }; render(false); commit(true); }; });
  }

  function govRecord() {
    const ev = [];
    DEB.forEach((d, di) => d.points.forEach((x, pi) => ev.push({ cls: x.res, tag: x.res === 'conceded' ? 'Conceded' : 'Argued back', when: dshort(d.date), di, pi, html: `<b>${esc(d.title)}.</b> ${esc(x.what || x.answer)}` })));
    const nr = notReady(), ch = checked(), held = POLS.filter(r => r.check && r.check.result === 'held').length, missed = POLS.filter(r => r.check && r.check.result === 'failed').length;
    if (nr.length) ev.unshift({ cls: 'flag', tag: 'Flagged', when: 'standing', html: `<b>${nr.length} policies say "Needs a test".</b> ${esc(nr.slice(0, 3).map(r => r.title).join(', '))}${nr.length > 3 ? ' and others' : ''}.` });
    const c = tally('conceded'), r = tally('rebutted');
    govShell(4, `<div class="record">
      <section><h3>What's happened · ${ev.length} events</h3><div class="feed">${ev.map(e => `<button class="ev ${e.cls}"${e.di != null ? ` data-ed="${e.di}" data-ep="${e.pi}"` : ''}><span class="tag">${e.tag}<small>${esc(e.when)}</small></span><span class="evp">${e.html}</span></button>`).join('')}</div></section>
      <section class="right">
        ${ch[0] ? `<div class="due"><h3>First prediction marked in</h3><p class="big"><b>${daysTo(ch[0].check.on)} days</b><span>${esc(ch[0].title)}, ${dlong(ch[0].check.on)}</span></p></div>` : ''}
        <div class="tally4"><div><b>${held}</b><span>held</span></div><div><b>${missed}</b><span>missed</span></div><div><b>${ch.filter(x => x.check.result === 'pending').length}</b><span>to mark</span></div><div><b>${nr.length}</b><span>need a test</span></div></div>
        ${c + r ? `<p class="watch">${c} of ${c + r} points conceded. A cabinet that agrees with everything isn't debating, so we count it every week.</p>` : ''}
        <h3 class="cu">Coming up</h3><div class="guide">
          ${[['05:00', '<b>News</b>: the headlines gathered for the cabinet'], ['06:00', "<b>The cabinet sits</b>: ministers answer yesterday's points and propose changes"], ['07:30', '<b>The opposition</b>: attacks every change'], ['08:00', "<b>The statistician</b>: refuses anything that can't be measured"], ['Sunday', '<b>The week in review</b>: concessions counted, misses printed']].map(([t, s]) => `<div class="slot"><time>${t}</time><span>${s}</span></div>`).join('')}
          ${ch.slice(0, 4).map(x => `<div class="slot"><time>${dshort(x.check.on)}</time><span><b>Marked</b>: ${esc(x.title)}, at ${tenths(x.check.prior)}</span></div>`).join('')}
        </div><p class="tobrd"><a href="/government/scoreboard/" data-board>The full scoreboard ▶</a></p></section></div>`);
    $$('[data-ed]', prog).forEach(b => b.onclick = () => goGov(5, { rd: +b.dataset.ed, rp: +b.dataset.ep }));
    const bb = $('[data-board]', prog); if (bb) bb.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, board: true }; render(false); commit(true); };
  }

  function govReplay() {
    if (!DEB.length) { govShell(5, `<div class="lempty"><p>Nothing to replay yet.</p></div>`); return; }
    gv.rd = Math.min(gv.rd, DEB.length - 1);
    const d = DEB[gv.rd]; gv.rp = Math.min(gv.rp, d.points.length - 1);
    const x = d.points[gv.rp], pol = polOf(d.id) || { post: '', check: null }, role = ROLE[x.who] || ROLE.opposition;
    govShell(5, `<div class="replay">
      <div class="picks">${DEB.map((y, i) => `<button class="chip" data-rd="${i}" aria-pressed="${i === gv.rd}">${esc(y.title)}</button>`).join('')}</div>
      <div class="rtitle"><h2>${esc(d.title)}</h2><span>${esc(MINN[pol.post] || '')}${pol.check ? ` · ${tenths(pol.check.prior)} · marked ${dlong(pol.check.on)}` : ''} · <a href="/government/${esc(d.id)}/" data-policy="${esc(d.id)}">read the policy</a></span></div>
      <div class="exch fade">
        <div class="card"><div class="who" style="background:${role[1]}">${role[0]}<small>point ${gv.rp + 1} of ${d.points.length}</small></div><p>${esc(x.said)}</p></div>
        <div class="card"><div class="who" style="background:var(--cab)">${esc(x.by)}<small>answers</small></div><p>${esc(x.answer)}</p></div>
        <div class="changed">${verdict(x.res)}<span>${x.res === 'conceded' ? '<b>What changed:</b> ' + esc(x.what || 'the policy, in the same sitting.') : '<b>Nothing changed:</b> the minister stood by it, and the point stays on the record.'}</span></div></div>
      <div class="track"><div class="marks">${d.points.map((y, i) => `<button class="${y.who} ${y.res}" data-rp="${i}"${i === gv.rp ? ' aria-current="true"' : ''} aria-label="Point ${i + 1}: ${y.who}, ${y.res === 'conceded' ? 'conceded' : 'argued back'}">${i + 1}</button>`).join('')}</div>
        <div class="tctl"><button class="chip" data-rs="-1">◀ Back</button><span>Top edge: who raised it (red opposition, blue statistician). Fill: green conceded, red argued back.</span><button class="chip" data-rs="1">Next ▶</button></div></div></div>`);
    $$('[data-rd]', prog).forEach(b => b.onclick = () => { gv.rd = +b.dataset.rd; gv.rp = 0; govReplay(); $(`[data-rd="${gv.rd}"]`, prog).focus(); });
    $$('[data-rp]', prog).forEach(b => b.onclick = () => { gv.rp = +b.dataset.rp; govReplay(); $(`[data-rp="${gv.rp}"]`, prog).focus(); });
    $$('[data-rs]', prog).forEach(b => b.onclick = () => {
      const k = +b.dataset.rs, n = DEB[gv.rd].points.length;
      if (k > 0) { if (gv.rp < n - 1) gv.rp++; else { gv.rd = (gv.rd + 1) % DEB.length; gv.rp = 0; } }
      else if (gv.rp > 0) gv.rp--; else { gv.rd = (gv.rd + DEB.length - 1) % DEB.length; gv.rp = DEB[gv.rd].points.length - 1; }
      govReplay(); $(`[data-rs="${k}"]`, prog).focus();
    });
    $$('[data-policy]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, policy: a.dataset.policy }; render(false); commit(true); }; });
  }
  function govBroadcast(p) {
    ({ 2: govLive, 3: govFloor, 4: govRecord, 5: govReplay })[p]();
    $$('.tabs [data-gp]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); goGov(+a.dataset.gp); flashOsd(); }; });
  }

  function renderProg(gesture) {
    clearTimeout(govTimer); stopVideo();
    const nk = state.ch === 'news' && newsProg(state.p).k;
    tv.classList.toggle('daylight', state.ch === 'government' && state.p === 1);
    tv.classList.toggle('fp-on', nk === 'fp'); // Future Proof: broadcast, so scanlines back on
    tv.classList.toggle('sv-on', nk === 'sv'); // the hologram brings its own CRT: the TV's scanlines step aside
    const s = state;
    if (nk === 'fp') {
      // Future Proof: three questions, each with a how-it-is / how-it-could-be 3D scene, playing inside the screen
      // (built by scripts/future-proof/build-questions.py from design/2026-11-11-future-proof-simple/).
      const f = C.government.futureProof;
      prog.innerHTML = `<div class="p-fp"><iframe src="${esc(f.questions)}" title="Future Proof: three questions" allow="fullscreen" allowfullscreen></iframe>
        <a class="fp-full" href="${esc(f.questions)}">Full screen</a></div>`;
    } else if (nk === 'sv') {
      // The Storyverse: Maddie's hologram plays inside the screen. A static page derived from the editor page by
      // apps/site/storyverse.mjs (source design/2026-11-05-gpom-meeting/lookdev/index.html); it asks for a tap, for the sound.
      prog.innerHTML = `<div class="p-sv"><iframe src="${esc(SVP.hologram)}" title="${esc(SVP.title)}: Maddie's hologram" allow="autoplay; fullscreen"></iframe>
        <a class="fp-full" href="${esc(SVP.hologram)}">Full screen</a></div>`;
    } else if (s.ch === 'stories') {
      const i = (s.p - 1) % S.length, st = S[i], song = s.p > S.length, vid = song ? st.songVideo : st.film;
      const pic = st.still ? `<img class="still" src="${esc(st.still)}" alt="">` : `<div class="blank"><span>PICTURE COMING</span></div>`;
      const sleeve = song ? `<div class="sleeve">${st.still ? `<img src="${esc(st.still)}" alt="">` : ''}</div>` : '';
      const status = vid ? `<button class="pill" data-play>▶ Play</button>` : `<span class="pill">Coming to YouTube</span>`;
      prog.innerHTML = `<div class="p-story${song ? ' song' : ''}">${pic}${sleeve}<span class="bug">BadCode One · ${s.p} of ${count.stories}</span>
        <div class="cap"><span class="kind">${song ? 'Song from ' + esc(st.title) : 'Film ' + (i + 1) + ' of ' + S.length}</span><h1>${esc(song ? st.song : st.title)}</h1>
        ${song ? '' : `<p>${esc(st.blurb)}</p>`}${status}</div></div>`;
      if (vid && gesture) play(vid);
    } else if (s.ch === 'news') {
      const n = C.news, b = n.bulletins[newsProg(s.p).i];
      prog.innerHTML = `<div class="p-news"><span class="bug">Money For Something</span>${HOST}
        <div class="txt"><h1>${esc(b ? b.title : n.title)}</h1><p class="strap">${esc(n.strap)}</p>${b && b.youtube ? '<button class="pill" data-play>▶ Play</button>' : `<span class="pill">${esc(n.status)}</span>`}</div>
        <div class="lower">${esc(n.signoff)}<small>BadCode news · working name</small></div>
        <div class="tick"><span>${n.ticker.map(esc).join('  ◂  ')}</span></div></div>`;
      if (b && b.youtube && gesture) play(b.youtube);
    } else if (s.ch === 'government') {
      const g = C.government;
      const bar = `<div class="bar"><svg viewBox="-34 -34 68 68" aria-hidden="true"><circle r="27.75" fill="none" stroke="#fff" stroke-width="4.5"/><path d="${MARK_TRI}" fill="#cc2b37"/></svg>The BadCode Government</div>`;
      if (s.p > 1) {
        govBroadcast(s.p);
      } else {
        const seen = store.get('bc-ppb');
        const mm = s.minister && CAB.find(x => x.post === s.minister);
        const pol = s.policy && POLS.find(x => x.id === s.policy);
        const owner = pol && (C.government.manifesto || []).find(x => x.post === pol.post);
        const listOf = post => POLS.filter(r => r.post === post);
        const cards = rs => `<ul class="pols">${rs.map(r => `<li><a href="/government/${r.id}/" data-policy="${r.id}"><b>${esc(r.title)}</b><span>${esc(r.line)}</span>${marksHtml(r)}</a></li>`).join('')}</ul>`;
        let inner;
        if (s.board) {
          const ch = POLS.filter(r => r.check).map(r => ({ r, c: r.check })).sort((a, b) => a.c.on.localeCompare(b.c.on));
          const done = ch.filter(x => x.c.result === 'held' || x.c.result === 'failed');
          const brier = done.length ? done.reduce((t, x) => t + (x.c.prior - (x.c.result === 'held' ? 1 : 0)) ** 2, 0) / done.length : null;
          inner = `<p class="q"><a class="back" href="/government/" data-cabinet>◀ The cabinet</a></p><h1>The scoreboard</h1>
            <p class="lead">Every policy makes a prediction about the real UK, with our odds. The statistician marks it on its date against a public source, whether it flatters us or not.</p>
            <p class="tally"><b>${done.filter(x => x.c.result === 'held').length}</b> held · <b>${done.filter(x => x.c.result === 'failed').length}</b> failed · <b>${ch.filter(x => x.c.result === 'pending').length}</b> still to mark${brier == null ? '' : ` · calibration ${brier.toFixed(3)} (0 is perfect, 0.25 a coin toss)`}</p>
            <table class="board"><thead><tr><th>Marked on</th><th>Prediction</th><th>Odds</th><th>Result</th></tr></thead><tbody>${ch.map(({ r, c }) => `<tr class="r-${c.result}"><td>${esc(c.on)}</td><td><a href="/government/${r.id}/" data-policy="${r.id}">${esc(r.title)}</a>: ${esc(c.claim)}</td><td>${odds(c.prior)}</td><td>${c.result === 'pending' ? 'to mark' : esc(c.result)}</td></tr>`).join('')}</tbody></table>`;
        } else if (pol) {
          inner = `<p class="q"><a class="back" href="/government/${pol.post === 'prime-minister' ? '' : pol.post + '/'}" ${pol.post === 'prime-minister' ? 'data-cabinet' : `data-minister="${pol.post}"`}>◀ ${esc(owner ? owner.title : 'The cabinet')}</a></p>${marksHtml(pol)}<div class="mbody">${bodyHtml(pol.text)}</div>
            ${pol.history.length ? `<h2>Its history</h2><ul class="hist">${pol.history.map(h => `<li><time>${esc(h.date)}</time> ${esc(h.subject)}</li>`).join('')}</ul>` : ''}`;
        } else if (mm) {
          inner = `<p class="q"><a class="back" href="/government/" data-cabinet>◀ The cabinet</a></p><h1>${esc(mm.title)}</h1><p class="lead"><b>${esc(mm.line)}</b></p><div class="mbody">${bodyHtml(mm.body)}</div><h2>Policies, one at a time</h2>${cards(listOf(mm.post))}`;
        } else {
          const pm = (C.government.manifesto || []).find(x => x.post === 'prime-minister');
          inner = `<p class="q">The manifesto</p><h1>${esc(g.promise)}</h1>${statusHtml()}
          <ul class="cab">${CAB.map(x => `<li><a href="/government/${x.post}/" data-minister="${x.post}"><b>${esc(x.title)}</b><span>${esc(x.line)}</span></a></li>`).join('')}</ul>
          <p class="tobrd"><a href="/government/scoreboard/" data-board>The scoreboard: every prediction we've made, and whether it held ▶</a></p>
          ${pm ? `<h2>The Prime Minister's policies</h2>${cards(listOf('prime-minister'))}` : ''}`;
        }
        prog.innerHTML = `<div class="p-gov">${bar}<div class="body">${inner}<p class="notreal">${esc(g.notReal)} Press 2 to watch it live. Future Proof is on NEWS.</p></div><div class="haz"></div>
          <div class="ppb${seen || clean() ? ' gone' : ''}"><p>There now follows a party political broadcast on behalf of</p><b>The BadCode Government</b></div></div>`;
        if (!seen && !clean()) { store.set('bc-ppb', '1'); govTimer = setTimeout(() => { const p = $('.ppb', prog); if (p) p.classList.add('gone'); }, 2600); }
      }
    } else {
      prog.innerHTML = `<div class="p-test"><div class="bars"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="disc">${HOST}</div><div class="cap">TEST CARD B · BADCODE · press TEXT for page 800, about BadCode</div></div>`;
    }
    const pb = $('[data-play]', prog); if (pb) pb.onclick = () => { const v = videoFor(state); if (v) play(v); };
    $$('[data-minister]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, minister: a.dataset.minister }; render(false); commit(true); }; });
    $$('[data-policy]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, policy: a.dataset.policy }; render(false); commit(true); }; });
    const bb = $('[data-board]', prog); if (bb) bb.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null, board: true }; render(false); commit(true); };
    $$('[data-gp]', prog).forEach(a => { a.onclick = e => { e.preventDefault(); state = { ch: 'government', p: +a.dataset.gp, text: null }; render(false); commit(true); flashOsd(); }; });
    const cb = $('[data-cabinet]', prog); if (cb) cb.onclick = e => { e.preventDefault(); state = { ch: 'government', p: 1, text: null }; render(false); commit(true); };
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
        dots('Stories: films and songs', 200), dots('News: Future Proof and more', 300), dots('The BadCode Government', 400), dots('Future Proof', 888), dots('Follow BadCode', 700), dots('About BadCode', 800), '',
        L('m', ' We have seen how this ends. We came'), L('m', ' back to change it. Type a page, or'), L('m', ' press a colour below.')],
      200: () => [head(p), '', title('br w', 'STORIES'), '', ...S.flatMap((st, i) => [`<span class="w"> ${i + 1} </span>${link(201 + i, st.title.toUpperCase().slice(0, 34))}`, L('c', `   song ${i + 5}: ${st.song.slice(0, 30)}`)]),
        L('w', ' Each film works on its own. They also'), L('w', ' share one universe.'), '', L('g', ' Channel 1 for pictures: press STORIES')],
      300: () => [head(p), '', title('br w', 'MONEY FOR SOMETHING'), '', ...wrap(n.strap), '', L('y', ' ' + n.status), '', ...wrap(n.ticker[2]), '', L('m', ' "' + n.signoff.slice(0, 35)), L('m', '  ' + n.signoff.slice(35) + '"'), '', L('b', ' Working name.')],
      400: () => [head(p), '', title('by', 'THE BADCODE GOVERNMENT'), '', L('w', ' THE MANIFESTO'), '', ...g.pledges.flatMap((pl, i) => [L('y', ` PLEDGE ${i + 1}`) + L('w', ' ' + pl[0].slice(0, 28)), ...wrap(pl[1], 34, '   ').map(x => L('c', x)), '']),
        `<span class="g"> ${esc(g.promise.slice(0, 33))} </span>${link(888, '888', 'g')}`, dots('The cabinet', 401)],
      401: () => [head(p), '', title('by', 'THE CABINET'), '', ...CAB.map((x, i) => dots(x.title.slice(0, 30), 402 + i)), '', L('c', ' Each minister reads the news daily.'), L('c', ' The manifesto moves with it.'), `<span class="w"> Manifesto </span>${link(400, '400')}`],
      700: () => [head(p), '', title('bb y', 'FOLLOW BADCODE'), '', ...C.socials.map(s => s.url ? `<span class="w"> </span><a class="y" href="${esc(s.url)}" target="_blank" rel="noopener">${esc(pad(s.name, 12))}</a><span class="g">open</span>` : `<span class="w"> ${esc(pad(s.name, 12))}</span><span class="b">soon</span>`)],
      800: () => [head(p), '', title('bb y', 'ABOUT BADCODE'), '', ...wrap(a.lede), L('r', ' ' + a.request), '', ...wrap(a.story), '', ...wrap(a.ai).map(x => L('c', x)), '', ...wrap(a.sign).map(x => L('m', x))],
      888: () => [`P888 SUBTITLES: WHAT WE MEANT ${stamp().slice(0, 10)}`, '', `<span class="dh">${esc(pad(' FUTURE PROOF', W))}</span>`, '', ...wrap(g.futureProof.question), '', ...g.futureProof.tenets.map((t, i) => ` ${i + 1} ${t[0]}`), '', ...wrap(g.futureProof.ask), '', ' Channel 3, programme 2, has the rest.', ' ' + '100 back to the index'],
    };
    CAB.forEach((x, i) => { P[402 + i] = () => { const body = wrap(x.body.replace(/^## .*$/gm, '').replace(/\s+/g, ' '), 37).slice(0, 11); return [head(402 + i), '', title('by', x.title.toUpperCase().slice(0, 38)), '', ...wrap(x.line).map(l => L('y', l)), '', ...body.map(l => L('w', l)), '', L('c', ' MORE: badcode.tv/government'), `<span class="w"> The cabinet </span>${link(401, '401')}`]; }; });
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
    if (state.text) { const order = [100, 200, ...S.map((_, i) => 201 + i), 300, 400, 401, ...CAB.map((_, i) => 402 + i), 700, 800, 888]; const i = order.indexOf(state.text); goText(order[(i + d + order.length) % order.length]); return; }
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
    const sc = e.target.closest && e.target.closest('.p-gov, .p-live .floor, .p-live .feed, .p-live .record, .p-live .replay');
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
