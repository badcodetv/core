import { test } from 'vitest';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { simulationPage, plainList, readIssues, TITLE, DESC } from './simulation.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const frag = readFileSync(join(here, '..', '..', 'docs', 'government', 'simulation', 'page', 'index.html'), 'utf8');
const issue = {
  id: '2026-11-10-x', run: { news_date: '2026-11-10', mode: 'replay', replay_stamp: 'Replayed on 23 Nov 2026 from the news of 10 Nov 2026' },
  issue: { title: 'A <title>', question: 'Who pays?' }, minister: { statement: 'We sign one small trial.' },
};
const feed = { issues: [issue], scoreboard: { total: 3, pending: 3, hit: 0, miss: 0 } };

test('every title, description and preview says SIMULATED', () => {
  assert.match(TITLE, /^SIMULATED/);
  assert.match(DESC, /^SIMULATED\./);
  const html = simulationPage(frag, feed, { origin: 'https://www.badcode.tv', img: '/future-proof/live/preview.png' });
  assert.match(html, /^<!doctype html>/);
  assert.match(html, /<title>SIMULATED · Future Proof Live · BadCode<\/title>/);
  assert.match(html, /og:image" content="https:\/\/www\.badcode\.tv\/future-proof\/live\/preview\.png"/);
  assert.match(html, /<span class="stamp">SIMULATED<\/span>/);
  assert.doesNotMatch(html, /claude:viewport/);
  assert.equal((html.match(/<title>/g) || []).length, 1);
});

test('the plain list escapes and stamps every issue', () => {
  const p = plainList(feed);
  assert.match(p, /A &lt;title&gt;/);
  assert.match(p, /SIMULATED\. News of 10 Nov 2026 \(Replayed on 23 Nov 2026/);
  assert.match(plainList(null), /SIMULATED/);
});

test('the simulation never calls its citizens "the public"', () => {
  const html = simulationPage(frag, feed, { origin: 'o', img: '/i.png' });
  assert.doesNotMatch(html.replace(/public sector/gi, ''), /\bthe public\b/i);
});

test('a missing branch gives null, not an error', () => {
  assert.equal(readIssues(here, 'refs/heads/no-such-branch-here'), null);
});

test('every panel header and the scoreboard carry the SIMULATED stamp', () => {
  const heads = frag.match(/<div class="ph">[\s\S]*?<\/div>/g) || [];
  assert.ok(heads.length >= 7);
  for (const h of heads) assert.match(h, /SIMULATED/, h.slice(0, 80));
  assert.match(frag, /SIMULATED<\/span><span class="eyebrow">The calendar's scoreboard/);
  assert.match(frag, /'Simulated '\+/);
});
