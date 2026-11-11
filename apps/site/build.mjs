#!/usr/bin/env node
// Builds badcode.tv (Channel BadCode) into apps/site/dist. No dependencies: plain Node.
//   node apps/site/build.mjs
// public/ is copied as-is (stills, logo, favicons); every address the TV can show gets its own
// index.html with its own title, description and link-preview picture, plus a plain-text copy of
// what is on screen for screen readers and search engines. Content: src/content.json.
import { readFileSync, writeFileSync, mkdirSync, rmSync, cpSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readManifesto, bodyHtml } from './manifesto.mjs';
import { readPolicies, lintPolicies, policiesFor, policyText, policyRecord, scoreboard } from './policies.mjs';
import { execFileSync } from 'node:child_process';
import { writeHologram } from './storyverse.mjs';
import { readDebates } from './debates.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, 'src'), pub = join(here, 'public'), dist = join(here, 'dist');
const C = JSON.parse(readFileSync(join(src, 'content.json'), 'utf8'));
// The government's manifesto comes from the files its cabinet writes, never from content.json.
C.government.manifesto = readManifesto(join(here, '..', '..', 'docs', 'government', 'manifesto'));
// Each policy is its own file (docs/government/policies/); a minister's page is its foreword plus
// its policies, stitched here so the TV and teletext read one body as before.
const POL = readPolicies(join(here, '..', '..', 'docs', 'government', 'policies'));
const { notReady: NOT_READY } = lintPolicies(POL);
const POLICY_PAGES = [], STITCHED = new Map();
const GOV = join(here, '..', '..', 'docs', 'government');
// Each policy's history is its own git log (one commit per policy change: tenet 2). A shallow
// checkout gives a shorter history, never an error.
const historyOf = file => { try {
  return execFileSync('git', ['log', '--follow', '--format=%as%x09%s', '--', join(GOV, 'policies', file)], { encoding: 'utf8' })
    .trim().split('\n').filter(Boolean).slice(0, 12).map(l => { const [date, ...s] = l.split('\t'); return { date, subject: s.join('\t') }; });
} catch { return []; } };
C.government.policies = [];
for (const m of C.government.manifesto) {
  const mine = policiesFor(m, POL);
  m.policyIds = mine.map(p => p.meta.id);
  for (const p of mine) C.government.policies.push(policyRecord(p, NOT_READY.get(p.meta.id), historyOf(p.file)));
  // the plain page prints foreword + every policy; the TV data keeps the foreword only (policies travel once, in G.policies)
  STITCHED.set(m.post, [m.body, ...mine.map(p => policyText(p, NOT_READY.get(p.meta.id)))].join('\n\n'));
  for (const p of mine) POLICY_PAGES.push({ m, p, text: policyText(p, NOT_READY.get(p.meta.id)) });
}
// The debate logs, as short plain-word captions, for GOVT 2–5 (Live, The floor, The record, Replay).
C.government.debates = readDebates(join(GOV, 'debates'));
const tpl = readFileSync(join(src, 'page.html'), 'utf8');
const css = readFileSync(join(src, 'tv.css'), 'utf8'), js = readFileSync(join(src, 'tv.js'), 'utf8');
const V = createHash('sha256').update(css + js + JSON.stringify(C)).digest('hex').slice(0, 10);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const O = C.origin, S = C.stories, SVP = C.storyverse, G = C.government, N = C.news, A = C.about;
const M = G.manifesto, CAB = M.filter(m => m.post !== 'prime-minister');
const DEFAULT_IMG = O + '/avatar-1024.png';
const SITE_DESC = `${A.lede} ${A.request.replace('fuck', 'f***')} Stories, the news, and a party of its own.`;

// the plain-text page under each address
const nav = `<nav aria-label="Channels"><ul>
<li><a href="/stories">Stories</a>: ${S.map((s, i) => `<a href="/stories/${i + 1}">${esc(s.title)}</a>`).join(', ')}. Songs: ${S.map((s, i) => `<a href="/stories/${i + 5}">${esc(s.song)}</a>`).join(', ')}.</li>
<li><a href="/news">News</a>: <a href="/news">Future Proof</a>, <a href="/news/2">${esc(SVP.title)}</a>${N.bulletins.length ? ` and <a href="/news/3">${esc(N.title)}</a>` : ''}</li>
<li><a href="/government">The BadCode Government</a>: <a href="/government/2">live</a>, <a href="/government/3">every policy</a>, <a href="/government/4">the record</a>, <a href="/government/5">the arguments</a></li>
<li><a href="/about">About BadCode</a> and <a href="/text/100">BadCode Text</a></li>
</ul></nav>`;
const follow = `<h2>Follow BadCode</h2><ul>${C.socials.map(s => `<li>${s.url ? `<a href="${esc(s.url)}">${esc(s.name)}</a>` : `${esc(s.name)} (soon)`}</li>`).join('')}</ul><p>${esc(A.ai)}</p><p>${esc(A.sign)} &copy; 2026 BadCode</p>`;
const story = (s, i) => `<article><h2>${esc(s.title)}</h2><p>${esc(s.blurb)}</p><p>Film: ${s.film ? `<a href="https://www.youtube.com/watch?v=${esc(s.film)}">watch on YouTube</a>` : 'coming to YouTube'}. Song: ${esc(s.song)}.</p></article>`;
const MARKS = [['test', 'Has its test', 'Not ready: no test yet'], ['undo', 'Has an undo', 'No undo'], ['prediction', 'Makes a prediction the world will mark', 'No prediction'], ['argued', 'Argued against, on the record', 'Not argued over yet']];
const plainBody = {
  home: () => `<h1>BadCode</h1><p>${esc(A.lede)} ${esc(A.request)}</p><p>${esc(A.story)}</p>${S.map(story).join('')}`,
  stories: () => `<h1>Stories</h1>${S.map(story).join('')}`,
  // setup only (Kai): the hologram itself gives parts of the story away, this page does not
  sv: () => `<h1>${esc(SVP.title)}</h1><p>${esc(SVP.blurb)}</p><p>Maddie's hologram, under two minutes with sound, on NEWS, programme 2. <a href="${esc(SVP.hologram)}">Watch it full screen.</a></p>`,
  story: i => `<h1>${esc(S[i].title)}</h1>${story(S[i], i)}`,
  song: i => `<h1>${esc(S[i].song)}</h1><p>The song from ${esc(S[i].title)}. ${S[i].songVideo ? `<a href="https://www.youtube.com/watch?v=${esc(S[i].songVideo)}">Watch on YouTube</a>` : 'Coming to YouTube.'}</p>`,
  news: () => `<h1>${esc(N.title)}</h1><p>${esc(N.strap)} ${esc(N.status)}</p><p>${esc(N.signoff)}</p>`,
  gov: () => `<h1>The BadCode Government</h1><p>${esc(G.promise)}</p><p><a href="/government/scoreboard">The scoreboard</a>: every prediction we've made, and whether it held.</p><h2>The cabinet</h2><ul>${CAB.map(m => `<li><a href="/government/${m.post}"><strong>${esc(m.title)}</strong></a>: ${esc(m.line)}</li>`).join('')}</ul><p>${esc(G.notReal)}</p>`,
  minister: m => `<h1>${esc(m.title)}</h1><p><strong>${esc(m.line)}</strong></p>${bodyHtml(STITCHED.get(m.post) || m.body)}<p><a href="/government">The whole cabinet</a>. ${esc(G.notReal)}</p>`,
  policy: (m, r, text) => `${bodyHtml(text)}<ul>${MARKS.map(([k, yes, no]) => `<li>${r.marks[k] ? '✔ ' + yes : '✘ ' + no}</li>`).join('')}</ul>${r.history.length ? `<h2>Its history</h2><ul>${r.history.map(h => `<li>${esc(h.date)}: ${esc(h.subject)}</li>`).join('')}</ul>` : ''}<p>A policy of the <a href="/government/${m.post === 'prime-minister' ? '' : m.post}">${esc(m.title)}</a>. Each policy stands alone: back it or not on its own. <a href="/government/scoreboard">The scoreboard</a>. ${esc(G.notReal)}</p>`,
  board: () => { const b = scoreboard(G.policies); return `<h1>The scoreboard</h1><p>Every policy carries a prediction about the real UK, with our odds, marked on its date by the statistician against a named public source. Held: ${b.held}. Failed: ${b.failed}. Void: ${b.void}. Still to mark: ${b.pending}.${b.brier == null ? ' Nothing has been marked yet.' : ` Our calibration (Brier score, 0 is perfect, 0.25 is a coin toss): ${b.brier.toFixed(3)}.`}</p><ol>${b.checks.map(c => `<li><a href="/government/${c.id}">${esc(c.title)}</a> (${esc(c.post)}), ${esc(c.on)}: ${esc(c.claim)} Our odds: ${Math.round(c.prior * 100)}%. ${c.result === 'pending' ? 'Not marked yet.' : `Result: ${esc(c.result)}. ${esc(c.note)}`}</li>`).join('')}</ol>`; },
  cabinetText: () => `<h1>The cabinet, as teletext</h1><ul>${CAB.map((m, i) => `<li>Page ${402 + i}: <a href="/government/${m.post}">${esc(m.title)}</a>: ${esc(m.line)}</li>`).join('')}</ul>`,
  fp: () => `<h1>Future Proof</h1><p><strong>${esc(G.futureProof.question)}</strong></p><p>${esc(G.futureProof.intro)}</p><ol>${G.futureProof.tenets.map(t => `<li><strong>${esc(t[0])}.</strong> ${esc(t[1])}</li>`).join('')}</ol><p>${esc(G.futureProof.ask)}</p>`,
  // GOVT 2–5: the same facts the broadcast shows, as text
  live: () => `<h1>The government, live</h1><p>Every policy is proposed by a minister, attacked by an opposition on a different AI model, checked by a statistician who refuses anything that can't be measured, and answered by the minister: conceded and changed, or argued back. A human signs off every change. ${G.debates.length} policies have been argued so far.</p>${G.debates.map(d => `<h2><a href="/government/${d.id}">${esc(d.title)}</a></h2><ul>${d.points.map(x => `<li><strong>${x.who === 'opposition' ? 'The Opposition' : 'The Statistician'}:</strong> ${esc(x.said)} <strong>${esc(x.by)}:</strong> ${esc(x.answer)} <em>${x.res === 'conceded' ? 'Conceded' : 'Argued back'}.</em></li>`).join('')}</ul>`).join('')}`,
  floor: () => `<h1>Every policy on the table</h1><p>${G.policies.length} policies, each its own page, each with its odds and the day its prediction is marked.</p><ul>${G.policies.map(r => `<li><a href="/government/${r.id}">${esc(r.title)}</a>: ${r.marks.test && r.check ? `${Math.round(r.check.prior * 100)}%, marked ${esc(r.check.on)}` : 'needs a real test'}</li>`).join('')}</ul>`,
  record: () => `<h1>The record</h1><p>What has happened, newest first.</p><ul>${G.debates.flatMap(d => d.points.map(x => `<li>${esc(d.date)}, <a href="/government/${d.id}">${esc(d.title)}</a>: ${x.res === 'conceded' ? 'conceded' : 'argued back'}. ${esc(x.what || x.answer)}</li>`)).join('')}</ul><p><a href="/government/scoreboard">The scoreboard</a>.</p>`,
  about: () => `<h1>About BadCode</h1><p>${esc(A.lede)} ${esc(A.request)}</p><p>${esc(A.story)}</p>`,
  text: () => `<h1>BadCode Text</h1><p>The words of BadCode as teletext pages: 100 index, 200 stories, 300 news, 400 the manifesto, 401 the cabinet (402 to 411, one minister each), 700 follow, 800 about, 888 Future Proof.</p>`,
  missing: () => `<h1>Page not found</h1><p>We saw you'd try that. <a href="/">Back to the TV.</a></p>`,
};

const routes = [
  { path: '/', title: 'BadCode', desc: SITE_DESC, body: plainBody.home() },
  { path: '/stories', title: 'Stories · BadCode', desc: 'Four films, four songs and The Storyverse from BadCode, an AI sent back from a future that went wrong.', body: plainBody.stories() },
  ...S.map((s, i) => ({ path: `/stories/${i + 1}`, title: `${s.title} · BadCode`, desc: s.blurb, img: s.still, body: plainBody.story(i) })),
  ...S.map((s, i) => ({ path: `/stories/${i + 5}`, title: `${s.song} (song) · BadCode`, desc: `The song from ${s.title}.`, img: s.still, body: plainBody.song(i) })),
  // NEWS holds the specials (Kai, 2026-11-11): 1 Future Proof, 2 The Storyverse, 3 Money For Something
  { path: '/news', title: 'Future Proof · BadCode', desc: G.futureProof.question, body: plainBody.fp() },
  { path: '/future-proof', canon: '/news', title: 'Future Proof · BadCode', desc: G.futureProof.question, body: plainBody.fp() },
  { path: '/news/2', title: `${SVP.title} · BadCode`, desc: SVP.blurb, img: SVP.still, body: plainBody.sv() },
  { path: '/storyverse', canon: '/news/2', title: `${SVP.title} · BadCode`, desc: SVP.blurb, img: SVP.still, body: plainBody.sv() },
  { path: '/stories/9', canon: '/news/2', title: `${SVP.title} · BadCode`, desc: SVP.blurb, img: SVP.still, body: plainBody.sv() },
  ...(N.bulletins.length ? [{ path: '/news/3', title: `${N.title} · BadCode`, desc: N.strap, body: plainBody.news() }] : []),
  { path: '/government', title: 'The BadCode Government', desc: `${G.promise} ${G.notReal}`, body: plainBody.gov() },
  ...CAB.map(m => ({ path: `/government/${m.post}`, title: `${m.title} · The BadCode Government`, desc: m.line, body: plainBody.minister(m) })),
  ...POLICY_PAGES.map(({ m, p, text }) => ({ path: `/government/${p.meta.id}`, title: `${p.meta.title} · ${m.title} · The BadCode Government`, desc: p.meta.line,
    body: plainBody.policy(m, G.policies.find(r => r.id === p.meta.id), text) })),
  { path: '/government/scoreboard', title: 'The scoreboard · The BadCode Government', desc: 'Every prediction the BadCode government has made about the UK, its odds, and whether it held.', body: plainBody.board() },
  { path: '/government/2', title: 'Live · The BadCode Government', desc: 'Watch the BadCode government argue: every policy attacked, checked and answered in public.', body: plainBody.live() },
  { path: '/government/3', title: 'The floor · The BadCode Government', desc: `All ${G.policies.length} policies on the table, with our odds and the day each is marked.`, body: plainBody.floor() },
  { path: '/government/4', title: 'The record · The BadCode Government', desc: 'Everything the BadCode government has conceded, argued back and signed off.', body: plainBody.record() },
  { path: '/government/5', title: 'Replay · The BadCode Government', desc: 'Any argument, point by point, and what changed because of it.', body: plainBody.live() },
  { path: '/about', title: 'About · BadCode', desc: SITE_DESC, body: plainBody.about() },
  ...[100, 200, 201, 202, 203, 204, 300, 400, 700, 800, 888].map(p => ({ path: `/text/${p}`, title: `Page ${p} · BadCode Text`, desc: 'BadCode, as teletext.', body: plainBody.text() })),
  { path: '/text/401', title: 'Page 401 · BadCode Text', desc: 'The BadCode cabinet, as teletext.', body: plainBody.cabinetText() },
  ...CAB.map((m, i) => ({ path: `/text/${402 + i}`, title: `Page ${402 + i} · BadCode Text`, desc: `${m.title}: ${m.line}`, body: plainBody.minister(m) })),
];

const slash = p => (p === '/' || p.endsWith('/') ? p : p + '/');
// internal links get the trailing slash too, so Pages never has to redirect
const slashLinks = html => html.replace(/href="(\/(?:stories|news|government|about|text|future-proof|storyverse)[^"]*?)"/g, (m, h) => `href="${slash(h)}"`);
function pageHtml(r) {
  const img = r.img ? O + r.img : DEFAULT_IMG;
  const fill = { TITLE: esc(r.title), DESC: esc(r.desc), CANON: O + slash(r.canon || r.path), OGIMG: img, V, CONTENT_JSON: JSON.stringify(C).replace(/</g, '\\u003c'), PLAIN: r.body + nav + follow };
  return slashLinks(tpl.replace(/\{\{(\w+)\}\}/g, (m, k) => (k in fill ? fill[k] : m)));
}

// The Storyverse page is derived from the hologram's editor page; rewrite it here so the two never drift.
// If the source moved on in a way the derivation doesn't understand, keep the last good copy and say so.
try { const r = writeHologram(); if (r === 'written') console.log('storyverse: public/storyverse/hologram/index.html regenerated'); }
catch (e) { console.warn('storyverse: kept the existing page,', e.message); }

rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });
// public/ holds the static files. The old one-page map (index.html, 404.html, styles.css) and the
// /tv test page are left behind: the TV replaces them.
const SKIP = new Set(['index.html', '404.html', 'styles.css', 'tv']);
cpSync(pub, dist, { recursive: true, filter: p => !SKIP.has(p.slice(pub.length + 1).split('/')[0]) || p === pub });
writeFileSync(join(dist, 'tv.css'), css);
writeFileSync(join(dist, 'tv.js'), js);
for (const r of routes) {
  const file = r.path === '/' ? join(dist, 'index.html') : join(dist, r.path.slice(1), 'index.html');
  mkdirSync(dirname(file), { recursive: true });
  writeFileSync(file, pageHtml(r));
}
writeFileSync(join(dist, '404.html'), pageHtml({ path: '/404', title: 'Page not found · BadCode', desc: SITE_DESC, body: plainBody.missing() }).replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"'));
// a short cache for the HTML, a long one for the stills; the version query string busts css/js
writeFileSync(join(dist, '_headers'), `/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/stills/*\n  Cache-Control: public, max-age=86400\n/storyverse/hologram/voice/*\n  Cache-Control: public, max-age=86400\n`);
for (const f of ['avatar-1024.png', 'favicon.svg']) if (!existsSync(join(dist, f))) console.warn('missing', f);
console.log(`built ${routes.length + 1} pages into ${dist} (version ${V})`);
