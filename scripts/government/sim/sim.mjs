#!/usr/bin/env node
// The simulation's command line. Plain node, no dependencies, so Bob workers can run it.
//
//   node scripts/government/sim/sim.mjs validate <issue.json|dir> [--today YYYY-MM-DD]
//   node scripts/government/sim/sim.mjs draw <issue-id> [--pool path] [--citizens 100] [--jury 12]
//   node scripts/government/sim/sim.mjs people <pool-path> <id> [<id>...]   (print those citizens)
//   node scripts/government/sim/sim.mjs find <issues-dir> <news-date>     (that day's issue and its stage)
//   node scripts/government/sim/sim.mjs fields <issues-dir>               (each field's last day, oldest first)
//   node scripts/government/sim/sim.mjs feed <issues-dir> <out.json> [--today YYYY-MM-DD]
//
// Exit code 1 on any validation error, so a worker can't publish a bad file.
import { readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateIssue } from './issue.mjs';
import { drawForIssue } from './lot.mjs';
import { buildFeed } from './feed.mjs';

const here = dirname(fileURLToPath(import.meta.url));
export const DEFAULT_POOL = join(here, '../../../docs/government/simulation/citizens/pool.json');

const args = process.argv.slice(2);
const flag = (name, dflt) => { const i = args.indexOf(`--${name}`); if (i < 0) return dflt; const v = args[i + 1]; args.splice(i, 2); return v; };
const today = flag('today', new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/London' }));
const poolPath = flag('pool', DEFAULT_POOL);
const nCit = Number(flag('citizens', 100)), nJury = Number(flag('jury', 12));
const [cmd, ...rest] = args;

const issueFiles = (p) => statSync(p).isDirectory()
  ? readdirSync(p, { recursive: true }).filter((f) => String(f).endsWith('.json') && !String(f).endsWith('feed.json') && !String(f).includes('.side.')).map((f) => join(p, String(f)))
  : [p];

if (cmd === 'validate') {
  let bad = 0;
  for (const f of issueFiles(rest[0])) {
    const { errors } = validateIssue(JSON.parse(readFileSync(f, 'utf8')), { today });
    if (errors.length) { bad++; console.log(`✗ ${f}`); errors.forEach((e) => console.log(`  - ${e}`)); } else console.log(`✓ ${f}`);
  }
  process.exit(bad ? 1 : 0);
} else if (cmd === 'draw') {
  const pool = JSON.parse(readFileSync(poolPath, 'utf8')).people;
  console.log(JSON.stringify(drawForIssue(pool, rest[0], { citizens: nCit, jury: nJury }), null, 1));
} else if (cmd === 'people') {
  const pool = JSON.parse(readFileSync(rest[0], 'utf8')).people;
  const want = new Set(rest.slice(1));
  console.log(JSON.stringify(pool.filter((p) => want.has(p.id)), null, 1));
} else if (cmd === 'find') {
  // find <issues-dir> <news-date>: print "<path>\t<stage>" for that day's issue(s), or nothing
  const dir = join(rest[0], rest[1]);
  let files = [];
  try { files = readdirSync(dir).filter((f) => f.endsWith('.json') && !f.includes('.side.')); } catch { /* no day yet */ }
  for (const f of files) console.log(`${join(dir, f)}\t${JSON.parse(readFileSync(join(dir, f), 'utf8')).stage}`);
} else if (cmd === 'fields') {
  // fields <issues-dir>: each field's last news date, oldest first (the "longest wait" slot)
  const last = {};
  for (const f of issueFiles(rest[0])) { const d = JSON.parse(readFileSync(f, 'utf8')); const k = d.issue?.field; if (k && (!last[k] || last[k] < d.run.news_date)) last[k] = d.run.news_date; }
  Object.entries(last).sort((a, b) => a[1].localeCompare(b[1])).forEach(([k, v]) => console.log(`${v}\t${k}`));
} else if (cmd === 'feed') {
  const docs = issueFiles(rest[0]).map((f) => JSON.parse(readFileSync(f, 'utf8')));
  const feed = buildFeed(docs, { today });
  writeFileSync(rest[1], JSON.stringify(feed, null, 1) + '\n');
  console.log(`feed: ${feed.issues.length} issues, ${feed.scoreboard.pending} predictions pending, ${feed.skipped.length} skipped`);
  if (feed.skipped.length) feed.skipped.forEach((s) => console.log(`  skipped ${s.id}: ${s.errors[0]}`));
} else {
  console.log('usage: sim.mjs validate|draw|people|feed …  (see the top of this file)');
  process.exit(2);
}
