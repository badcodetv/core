// The Future Proof Demo on badcode.tv, at /demo/. A separate experiment from Future Proof Live
// (simulation.mjs): made-up cases on real news topics, a chosen ending each day, and a demo government
// built only from those days (design/2026-11-24-future-proof-demo/GOAL-3.md).
// The days and the government live on the branch demo/live, never on main. The build reads them straight
// from git, the same way simulation.mjs reads simulation/live:
//   git ls-tree origin/demo/live -- docs/demo/days docs/demo/government
// The page itself is docs/demo/page/index.html, wrapped here in a full document with its title, link
// preview and a plain-text list for screen readers, search engines and browsers without JavaScript.
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { buildDemoFeed } from '../../scripts/demo/feed.mjs';

export const DEMO_REF = 'origin/demo/live';
const git = (cwd, args) => execFileSync('git', args, { cwd, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });

// Every JSON file under one folder on the branch (working notes, ".side.", left out), parsed. null if the ref is missing.
export function readTree(repo, ref, dir) {
  try { git(repo, ['rev-parse', '--verify', '--quiet', ref]); } catch { return null; }
  return git(repo, ['ls-tree', '-r', '--name-only', ref, '--', dir]).split('\n')
    .filter((f) => f.endsWith('.json') && !f.includes('.side.'))
    .map((f) => JSON.parse(git(repo, ['show', `${ref}:${f}`])));
}

export const londonToday = () => new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/London' });

export function demoFeed(repo, { ref = DEMO_REF, today = londonToday() } = {}) {
  const days = readTree(repo, ref, 'docs/demo/days');
  if (!days) return null;
  const govs = readTree(repo, ref, 'docs/demo/government') ?? [];
  const cabinet = JSON.parse(readFileSync(join(repo, 'docs/demo/cabinet.json'), 'utf8'));
  return buildDemoFeed(days, govs, cabinet, { today });
}

const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const day = (d) => { const [y, m, dd] = d.split('-').map(Number); return `${dd} ${MON[m - 1]} ${y}`; };
const ENDING = { accepted: 'Accepted', partly: 'Partly: a trial', rejected: 'Rejected: sent back' };

export const TITLE = 'Future Proof Demo · BadCode';
export const DESC = 'A demo of how a future-proof government could decide things. Every day a made-up case on a real news topic goes round the loop: citizens drawn by lot set the tests, three answers are marked against them, and the day ends accepted, as a trial, or sent back. A demo government is built only from what passed.';

// The plain-text copy under the page: every day, newest first, then the manifestos.
export function plainList(feed) {
  if (!feed || !feed.days.length) return '<p>This is a demo. The first demo day hasn\'t been built yet.</p>';
  const mins = feed.government.ministers;
  const name = (id) => mins.find((m) => m.id === id);
  const days = feed.days.map((d) => `<li><h2>${esc(d.case.title)}</h2><p>${day(d.run.news_date)}. ${esc(ENDING[d.ending])}. ${esc(d.case.question)}</p><p>${esc(d.case.place)}: ${esc(d.case.story)}</p>${d.minister ? `<p>${esc(name(d.minister.minister)?.title)}: ${esc(d.minister.text)}</p>` : ''}</li>`).join('');
  const gov = mins.map((m) => {
    const lines = feed.government.lines.filter((l) => l.minister === m.id && l.live);
    return `<li><h3>${esc(m.title)}, ${esc(m.name)} (invented)</h3>${lines.length ? `<ul>${lines.map((l) => `<li>${l.status === 'trial' ? 'Trial: ' : ''}${esc(l.text)}</li>`).join('')}</ul>` : '<p>Nothing adopted yet.</p>'}</li>`;
  }).join('');
  return `<p><strong>This is a demo.</strong> ${feed.days.length} days: ${feed.endings.accepted} accepted, ${feed.endings.partly} partly, ${feed.endings.rejected} rejected.</p><ol>${days}</ol><h2>The demo government</h2><ul>${gov}</ul>`;
}

// Wrap the page fragment (head bits, <style>, then <main> and <script>) in a full document.
export function demoPage(fragment, feed, { origin, img }) {
  const at = fragment.indexOf('<main');
  if (at < 0) throw new Error('demo page: no <main> in docs/demo/page/index.html');
  const head = fragment.slice(0, at).replace(/<title>[\s\S]*?<\/title>\s*/, '').replace(/<meta name="claude:[^>]*>\s*/g, '');
  const url = `${origin}/demo/`;
  const back = `<p style="max-width:1080px;margin:1rem auto 0;padding:0 16px;font-size:.8rem"><a href="/" style="color:inherit">◀ badcode.tv</a></p>`;
  return `<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>${esc(TITLE)}</title>
<meta name="description" content="${esc(DESC)}">
<link rel="canonical" href="${url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BadCode">
<meta property="og:title" content="${esc(TITLE)}">
<meta property="og:description" content="${esc(DESC)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${origin}${img}">
<meta property="og:image:alt" content="Future Proof Demo, BadCode: this is a demo">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
${head.trim()}
</head>
<body>
${back}
${fragment.slice(at).trim()}
<noscript><section style="max-width:1080px;margin:0 auto;padding:0 16px">${plainList(feed)}</section></noscript>
</body>
</html>
`;
}
