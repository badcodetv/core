// Round 2 (Kai, 2026-11-11: A's look, B's overview, C's replays). Builds studio.html from studio.src.html
// with the real policy table (docs/government/policies) and every debate log (docs/government/debates).
import { readFileSync, writeFileSync, readdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { readPolicies, lintPolicies } from '../../../apps/site/policies.mjs';

const here = new URL('.', import.meta.url).pathname;
const root = join(here, '../../..');
const ps = readPolicies(join(root, 'docs/government/policies'));
const L = lintPolicies(ps);
const pols = ps.map(p => { const x = p.meta; return { id: x.id, t: x.title, line: x.line, o: x.owner, s: x.status, k: x.kind, on: x['check.check_on'], pr: +x['check.prior'], r: x['check.result'], claim: x['check.claim'], nr: L.notReady.has(x.id) ? 1 : 0, against: x.against || '' }; });

// The first one or two sentences, up to about `max` characters: a caption, never the whole speech.
// Field names never reach the screen (the reader rule: no software words on the page).
const PLAIN = [[/\btest\.where\b/g, 'where it is tried'], [/\btest\.against\b/g, 'what it is compared with'], [/\btest\.measure\b/g, 'what is measured'], [/\btest\.by\b/g, 'the deadline'],
  [/\bfails_if\b/g, 'the fail number'], [/\bcheck\.claim\b/g, 'the prediction'], [/\bcheck\.rule\b/g, 'the marking rule'], [/\bcheck\.source\b/g, 'the source'], [/\bcheck\.if_revised\b/g, 'the correction rule'],
  [/\bcheck\.check_on\b/g, 'the marking date'], [/\bcheck\.prior\b/g, 'our odds'], [/\bcheck\.\w+/g, 'the prediction'], [/\bleaves_out\b/g, 'who it leaves out'], [/\bprior\b/g, 'odds'],
  [/\bjudgement\.\w+/g, 'the judgement'], [/\bthe body\b/gi, 'the text'], [/\bband\b/g, 'size'], [/\bstop\b(?= )/g, 'the stop date'], [/\([^)]*(evidence|Policy file|en-\d|PR #)[^)]*\)/g, ''],
  [/\b[a-z-]+\/[a-z0-9-]+\b/g, m => m.includes('-') || m.includes('/') ? 'another policy' : m]];
const plain = s => PLAIN.reduce((t, [re, to]) => t.replace(re, to), s).replace(/\s+([.,;])/g, '$1').replace(/\s{2,}/g, ' ').replace(/\s*\(see [^)]*\)?/g, '').replace(/([.!?] )([a-z])/g, (m, a, c) => a + c.toUpperCase()).trim();
function cap(s, max = 240) {
  const sent = plain(s).match(/[^.!?]+[.!?]+(\s|$)/g) || [plain(s)];
  let out = '';
  for (const x of sent) { if (out.length >= 110 && (out + x).length > max) break; out += x; }
  return out.trim().length > max + 60 ? out.slice(0, max).replace(/\s\S*$/, '') + '…' : out.trim();
}

const debates = [];
const ddir = join(root, 'docs/government/debates');
for (const post of readdirSync(ddir).filter(f => !f.endsWith('.md'))) {
  for (const f of readdirSync(join(ddir, post)).filter(f => f.endsWith('.md'))) {
    const src = readFileSync(join(ddir, post, f), 'utf8');
    const [, title, id] = src.match(/^# (.+) \(([^)]+)\)/m);
    const date = (src.match(/^## (\d{4}-\d{2}-\d{2})/m) || [])[1];
    const points = [];
    for (const block of src.split(/\n(?=\*\*(?:Opposition|Statistician):\*\*)/).slice(1)) {
      const who = block.match(/^\*\*(Opposition|Statistician):\*\*\s*(.+)/);
      const ans = block.match(/^\*\*Answer \(([^)]+)\):\*\*\s*(.+)/m);
      const out = block.match(/^\*\*Outcome:\*\*\s*(.+)/m);
      if (!who || !ans || !out) continue;
      const res = /^Conceded/.test(out[1]) ? 'conceded' : 'rebutted';
      const what = out[1].replace(/^(Conceded|Rebutted):?\s*/, '').replace(/,? this commit\.?$/, '').replace(/^\(|\)$/g, '');
      points.push({ who: who[1].toLowerCase(), said: cap(who[2].replace(/^[a-z-]+\/[a-z0-9-]+:\s*/, '')), by: ans[1], answer: cap(ans[2]), res, what: (w => w.charAt(0).toUpperCase() + w.slice(1))(cap(what, 160)) });
    }
    debates.push({ id, title, date, points });
  }
}

const out = readFileSync(join(here, 'studio.src.html'), 'utf8')
  .replace('/*POLS*/[]', JSON.stringify(pols))
  .replace('/*DEBATES*/[]', JSON.stringify(debates));
writeFileSync(join(here, 'studio.html'), out);
console.log('studio.html', pols.length, 'policies', debates.length, 'debates', debates.reduce((n, d) => n + d.points.length, 0), 'points');
