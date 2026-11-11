import { test } from 'vitest';
import assert from 'node:assert/strict';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseDebate, plain, readDebates } from './debates.mjs';

const here = dirname(fileURLToPath(import.meta.url));

test('field names become plain words', () => {
  assert.equal(plain('test.where and fails_if now draw by lot'), 'where it is tried and the fail number now draw by lot');
  assert.equal(plain('Needs chancellor/windfall-act.'), 'Needs another policy.');
  assert.equal(plain('Fair. the body says so.'), 'Fair. The text says so.');
});

test('a debate log parses into points with outcomes', () => {
  const d = parseDebate(`# The Slice (chancellor/the-slice)

## 2026-11-11 · PR #dry-run

**Opposition:** The test can't test.
**Answer (Chancellor):** Fair.
**Outcome:** Conceded: test.where now draws by lot, this commit

**Statistician:** chancellor/the-slice: the window has no start.
**Answer (Chancellor):** No: it opens today.
**Outcome:** Rebutted
`);
  assert.equal(d.id, 'chancellor/the-slice');
  assert.equal(d.date, '2026-11-11');
  assert.deepEqual(d.points.map(p => [p.who, p.res]), [['opposition', 'conceded'], ['statistician', 'rebutted']]);
  assert.equal(d.points[0].what, 'Where it is tried now draws by lot');
  assert.equal(d.points[1].said, 'The window has no start.');
});

test('the real logs parse, with no field names left', () => {
  const ds = readDebates(join(here, '..', '..', 'docs', 'government', 'debates'));
  assert.ok(ds.length >= 5);
  const text = JSON.stringify(ds);
  assert.doesNotMatch(text, /\b(test|check|judgement)\.[a-z_]|fails_if|leaves_out|if_revised|check_on|\.mjs\b/);
});
