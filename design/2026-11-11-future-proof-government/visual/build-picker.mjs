// Builds picker.html from picker.src.html with the real policy table (docs/government/policies).
import { readFileSync, writeFileSync } from 'node:fs';
import { readPolicies, lintPolicies } from '../../../apps/site/policies.mjs';
const here = new URL('.', import.meta.url).pathname;
const ps = readPolicies(here + '../../../docs/government/policies');
const L = lintPolicies(ps);
const rows = ps.map(p => { const x = p.meta; return [x.id, x.title, x.owner, x.status, x.kind, x['check.check_on'], x['check.prior'], x['check.result'], L.notReady.has(x.id) ? 1 : 0]; });
writeFileSync(here + 'picker.html', readFileSync(here + 'picker.src.html', 'utf8').replace('/*POLS*/[]', JSON.stringify(rows)));
console.log('picker.html', rows.length, 'policies');
