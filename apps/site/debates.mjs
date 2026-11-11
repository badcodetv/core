// The government's debate logs (docs/government/debates/<post>/<slug>.md) as short broadcast captions
// for the GOVT channel (Live, The record, Replay). Plain words only: field names never reach the screen
// (docs/marketing/the-reader.md). Format of a log: docs/government/debates/README.md.
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';

const PLAIN = [
  [/\btest\.where\b/g, 'where it is tried'], [/\btest\.against\b/g, 'what it is compared with'],
  [/\btest\.measure\b/g, 'what is measured'], [/\btest\.by\b/g, 'the deadline'], [/\bfails_if\b/g, 'the fail number'],
  [/\bcheck\.claim\b/g, 'the prediction'], [/\bcheck\.rule\b/g, 'the marking rule'], [/\bcheck\.source\b/g, 'the source'],
  [/\bcheck\.if_revised\b/g, 'the correction rule'], [/\bcheck\.check_on\b/g, 'the marking date'], [/\bcheck\.prior\b/g, 'our odds'],
  [/\bcheck\.\w+/g, 'the prediction'], [/\bif_revised\b/g, 'the correction rule'], [/\bcheck_on\b/g, 'the marking date'], [/\bleaves_out\b/g, 'who it leaves out'], [/\bprior\b/g, 'odds'],
  [/\bjudgement\.\w+/g, 'the judgement'], [/\bpolicy-lint\.mjs\b/g, 'the format check'], [/\bthe lint\b/g, 'the format check'], [/\blint\b/g, 'format check'], [/\bREADME\b/g, 'rules'], [/\bBody\b/g, 'The text'], [/,? this commit\b/g, ''], [/\bthe body\b/gi, 'the text'], [/\bband size\b/g, 'size'], [/\bband\b/g, 'size'],
  [/\([^)]*(evidence|Policy file|en-\d|PR #)[^)]*\)/g, ''], [/\b[a-z-]+\/[a-z0-9-]+\b/g, 'another policy'],
];
const upper = s => s.charAt(0).toUpperCase() + s.slice(1);
export function plain(s) {
  return PLAIN.reduce((t, [re, to]) => t.replace(re, to), String(s))
    .replace(/\s+([.,;])/g, '$1').replace(/\s{2,}/g, ' ').replace(/\s*\(see [^)]*\)?/g, '')
    .replace(/([.!?] )([a-z])(?![a-z]*\.)/g, (m, a, c) => a + c.toUpperCase()).trim();
}
// The first sentences up to about `max` characters: a caption, never the whole speech.
export function caption(s, max = 240) {
  // a sentence ends at . ! or ? followed by a space and a capital, a digit, a quote or a pound sign,
  // so 54.83p, 0.35 and e.g. stay whole
  const sent = plain(s).split(/(?<=[.!?]["”]?)\s+(?=[A-Z0-9"“£])/);
  let out = '';
  for (const x of sent) { if (out.length >= 110 && (out + ' ' + x).length > max) break; out += (out ? ' ' : '') + x; }
  out = upper(out.trim());
  return out.length > max + 60 ? out.slice(0, max).replace(/\s\S*$/, '') + '…' : out;
}

export function parseDebate(src) {
  const head = src.match(/^# (.+) \(([^)]+)\)/m);
  if (!head) return null;
  const date = (src.match(/^## (\d{4}-\d{2}-\d{2})/m) || [])[1] || '';
  const points = [];
  for (const block of src.split(/\n(?=\*\*(?:Opposition|Statistician):\*\*)/).slice(1)) {
    const who = block.match(/^\*\*(Opposition|Statistician):\*\*\s*(.+)/);
    const ans = block.match(/^\*\*Answer \(([^)]+)\):\*\*\s*(.+)/m);
    const out = block.match(/^\*\*Outcome:\*\*\s*(.+)/m);
    if (!who || !ans || !out) continue;
    const res = /^Conceded/i.test(out[1]) ? 'conceded' : 'rebutted';
    const what = out[1].replace(/^(Conceded|Rebutted):?\s*/i, '').replace(/,? this commit\.?$/, '').replace(/^\(|\)$/g, '');
    points.push({ who: who[1].toLowerCase(), said: caption(who[2].replace(/^[a-z-]+\/[a-z0-9-]+:\s*/, '')),
      by: ans[1], answer: caption(ans[2]), res, what: what ? upper(caption(what, 160)) : '' });
  }
  return { id: head[2], title: head[1], date, points };
}

export function readDebates(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const post of readdirSync(dir).sort()) {
    const pdir = join(dir, post);
    if (!statSync(pdir).isDirectory()) continue;
    for (const f of readdirSync(pdir).filter(f => f.endsWith('.md')).sort()) {
      const d = parseDebate(readFileSync(join(pdir, f), 'utf8'));
      if (d && d.points.length) out.push(d);
    }
  }
  return out.sort((a, b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
}
