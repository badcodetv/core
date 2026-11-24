#!/usr/bin/env node
// The Future Proof Demo's command line. Plain node, no dependencies, so Bob workers can run it.
//
//   node scripts/demo/demo.mjs plan <news-date>                   (that day's area and ending)
//   node scripts/demo/demo.mjs validate <file|dir> [--today D]    (demo days and government days)
//   node scripts/demo/demo.mjs score <day.json>                   (each answer's marks, the ending reached)
//   node scripts/demo/demo.mjs draw <day-id> [--citizens 100] [--jury 12]
//   node scripts/demo/demo.mjs people <id> [<id>...]              (print those citizens from the pool)
//   node scripts/demo/demo.mjs find <days-dir> <news-date>        (that day's file and its stage)
//   node scripts/demo/demo.mjs government <root>                  (the manifestos as they stand)
//   node scripts/demo/demo.mjs feed <root> <out.json> [--today D] (root holds docs/demo/days and docs/demo/government)
//
// Exit code 1 on any validation error, so a worker can't publish a bad file.
import { readFileSync, readdirSync, statSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateDay, plan, scoreAnswers, endingOf, bestAnswer } from './issue.mjs';
import { checkGovShape, GOV_SCHEMA } from './government.mjs';
import { drawForIssue } from './lot.mjs';
import { buildDemoFeed } from './feed.mjs';

const here = dirname(fileURLToPath(import.meta.url));
export const POOL = join(here, '../../docs/demo/citizens/pool.json');
export const CABINET = join(here, '../../docs/demo/cabinet.json');

const args = process.argv.slice(2);
const flag = (name, dflt) => { const i = args.indexOf(`--${name}`); if (i < 0) return dflt; const v = args[i + 1]; args.splice(i, 2); return v; };
const today = flag('today', new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/London' }));
const nCit = Number(flag('citizens', 100)), nJury = Number(flag('jury', 12));
const [cmd, ...rest] = args;
const read = (f) => JSON.parse(readFileSync(f, 'utf8'));
const jsonFiles = (p) => !existsSync(p) ? [] : statSync(p).isDirectory()
  ? readdirSync(p, { recursive: true }).map(String).filter((f) => f.endsWith('.json') && !f.endsWith('feed.json') && !f.includes('.side.')).map((f) => join(p, f))
  : [p];
export function loadRoot(root) {
  return {
    days: jsonFiles(join(root, 'docs/demo/days')).map(read),
    govs: jsonFiles(join(root, 'docs/demo/government')).map(read),
  };
}

if (cmd === 'plan') {
  console.log(JSON.stringify(plan(rest[0])));
} else if (cmd === 'validate') {
  let bad = 0;
  for (const f of jsonFiles(rest[0])) {
    const doc = read(f);
    const errors = doc.schema === GOV_SCHEMA ? checkGovShape(doc) : validateDay(doc, { today }).errors;
    if (errors.length) { bad++; console.log(`✗ ${f}`); errors.forEach((e) => console.log(`  - ${e}`)); } else console.log(`✓ ${f}`);
  }
  process.exit(bad ? 1 : 0);
} else if (cmd === 'score') {
  const d = read(rest[0]);
  for (const s of scoreAnswers(d)) console.log(`${s.answer}: ${s.pass} pass, ${s.unclear} unclear, ${s.fail} fail of ${s.of}${s.clean ? '  (passes everything)' : ''}${s.breaksLimit ? '  (breaks a limit)' : ''}`);
  console.log(`reached: ${endingOf(d)}; plan wants: ${d.plan?.ending}; best answer: ${bestAnswer(d) ?? 'none'}`);
} else if (cmd === 'draw') {
  console.log(JSON.stringify(drawForIssue(read(POOL).people, rest[0], { citizens: nCit, jury: nJury }), null, 1));
} else if (cmd === 'people') {
  const want = new Set(rest);
  console.log(JSON.stringify(read(POOL).people.filter((p) => want.has(p.id)), null, 1));
} else if (cmd === 'find') {
  const dir = join(rest[0], rest[1]);
  for (const f of jsonFiles(dir)) console.log(`${f}\t${read(f).stage}`);
} else if (cmd === 'government' || cmd === 'feed') {
  const { days, govs } = loadRoot(rest[0]);
  const feed = buildDemoFeed(days, govs, read(CABINET), { today });
  if (cmd === 'government') {
    for (const m of feed.government.ministers) {
      console.log(`\n${m.title}, ${m.name}`);
      for (const l of feed.government.lines.filter((x) => x.minister === m.id && x.live)) console.log(`  ${l.id} [${l.status}] ${l.text}  (from ${l.from})`);
    }
  } else {
    writeFileSync(rest[1], JSON.stringify(feed, null, 1) + '\n');
    console.log(`feed: ${feed.days.length} days (${Object.entries(feed.endings).map(([k, v]) => `${v} ${k}`).join(', ')}), ${feed.government.lines.length} manifesto lines, ${feed.skipped.length} skipped`);
  }
  feed.skipped.forEach((s) => console.log(`  skipped ${s.id}: ${s.errors[0]}`));
} else {
  console.log('usage: demo.mjs plan|validate|score|draw|people|find|government|feed …  (see the top of this file)');
  process.exit(2);
}
