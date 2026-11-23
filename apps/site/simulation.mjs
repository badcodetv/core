// Future Proof Live (SIMULATED) on badcode.tv, at /future-proof/live/.
// The issues live on the branch simulation/live, never on main (design/2026-11-23-future-proof-rework,
// build log D3). The build reads them straight from git, so the site needs no copy on main:
//   git ls-tree origin/simulation/live -- docs/government/simulation/issues
// The page itself is docs/government/simulation/page/index.html (the same file the private mirror
// publishes); here it is wrapped in a full document with its own title, link preview and a plain-text
// list for screen readers, search engines and browsers without JavaScript.
import { execFileSync } from 'node:child_process';
import { buildFeed } from '../../scripts/government/sim/feed.mjs';

export const SIM_REF = 'origin/simulation/live';
const DIR = 'docs/government/simulation/issues';
const git = (cwd, args) => execFileSync('git', args, { cwd, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });

// Every issue file on the branch (working notes, ".side.", are left out), parsed. null if the ref is missing.
export function readIssues(repo, ref = SIM_REF) {
  try { git(repo, ['rev-parse', '--verify', '--quiet', ref]); } catch { return null; }
  const files = git(repo, ['ls-tree', '-r', '--name-only', ref, '--', DIR]).split('\n')
    .filter(f => f.endsWith('.json') && !f.includes('.side.'));
  return files.map(f => JSON.parse(git(repo, ['show', `${ref}:${f}`])));
}

export const londonToday = () => new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/London' });

export function simulationFeed(repo, { ref = SIM_REF, today = londonToday() } = {}) {
  const docs = readIssues(repo, ref);
  return docs ? buildFeed(docs, { today }) : null;
}

const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const day = d => { const [y, m, dd] = d.split('-').map(Number); return `${dd} ${MON[m - 1]} ${y}`; };

export const TITLE = 'SIMULATED · Future Proof Live · BadCode';
export const DESC = 'SIMULATED. Every day one real UK news story goes round the Future Proof loop: AI stand-ins for citizens, drawn by lot, set the test; three answers are written blind and checked; a simulated minister signs one small trial with predictions marked on their date. Not real people. Not a real party.';

// The plain-text copy under the page: every issue, newest first, with what was decided.
export function plainList(feed) {
  if (!feed || !feed.issues.length) return '<p>SIMULATED. The feed has not been built yet.</p>';
  const s = feed.scoreboard;
  return `<p><strong>SIMULATED.</strong> ${feed.issues.length} issues. Predictions: ${s.total}, of which ${s.pending} still to mark, ${s.hit} came true, ${s.miss} did not.</p><ol>${feed.issues.map(d => `<li><h2>${esc(d.issue.title)}</h2><p>SIMULATED. News of ${day(d.run.news_date)}${d.run.mode === 'replay' ? ` (${esc(d.run.replay_stamp)})` : ''}. ${esc(d.issue.question)}</p>${d.minister ? `<p>The simulated minister: ${esc(d.minister.statement || '')}</p>` : ''}</li>`).join('')}</ol>`;
}

// Wrap the page fragment (head bits, <style>, then <main> and <script>) in a full document.
export function simulationPage(fragment, feed, { origin, img }) {
  const at = fragment.indexOf('<main');
  if (at < 0) throw new Error('simulation page: no <main> in docs/government/simulation/page/index.html');
  const head = fragment.slice(0, at).replace(/<title>[\s\S]*?<\/title>\s*/, '').replace(/<meta name="claude:[^>]*>\s*/g, '');
  const body = fragment.slice(at);
  const url = `${origin}/future-proof/live/`;
  const back = `<p class="eyebrow" style="max-width:1080px;margin:1rem auto 0"><a href="/" style="color:inherit">◀ badcode.tv</a> · <a href="/government/" style="color:inherit">The BadCode Government</a></p>`;
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
<meta property="og:image:alt" content="SIMULATED: Future Proof Live, BadCode">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
${head.trim()}
</head>
<body>
${back}
${body.trim()}
<noscript><section style="max-width:1080px;margin:0 auto">${plainList(feed)}</section></noscript>
</body>
</html>
`;
}
