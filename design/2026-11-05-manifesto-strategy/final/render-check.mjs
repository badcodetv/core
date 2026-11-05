// Renders the staged manifesto pages with the live site renderer (apps/site/manifesto.mjs),
// unchanged, and compares their shape with the live pages in docs/government/manifesto/.
// Run: node design/2026-11-05-manifesto-strategy/final/render-check.mjs
import { readManifesto, bodyHtml } from '../../../apps/site/manifesto.mjs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const staged = readManifesto(join(here, 'manifesto'));
const live = readManifesto(join(here, '../../../docs/government/manifesto'));
const shape = p => {
  const html = bodyHtml(p.body);
  return { h2: (html.match(/<h2>/g) || []).length, p: (html.match(/<p>/g) || []).length,
    words: p.body.split(/\s+/).filter(Boolean).length, lineChars: p.line.length,
    joined: p.body.split(/\n\s*\n/).filter(b => !b.trim().startsWith('## ') && /\n/.test(b.trim())).length,
    markdown: /(\*\*|^- |^\d+\. |\[.*\]\(|`)/m.test(p.body) };
};
let bad = 0;
for (const s of staged) {
  const l = live.find(x => x.post === s.post);
  const a = shape(s), b = l ? shape(l) : null;
  const flags = [];
  if (!l) flags.push('NO LIVE PAGE OF THIS NAME');
  if (a.h2 !== 1) flags.push(`h2=${a.h2}`);
  if (a.joined) flags.push(`${a.joined} block(s) with single newlines joined into one <p>`);
  if (a.markdown) flags.push('markdown syntax renders literally');
  if (a.lineChars >= 100) flags.push(`line ${a.lineChars} chars (>=100)`);
  if (flags.length) bad++;
  console.log(`${s.post.padEnd(16)} staged h2=${a.h2} p=${a.p} words=${a.words} line=${a.lineChars}ch | live h2=${b?.h2} p=${b?.p} words=${b?.words}${flags.length ? '  !! ' + flags.join('; ') : '  ok'}`);
}
console.log(`${staged.length} staged pages parsed; ${bad} flagged.`);
