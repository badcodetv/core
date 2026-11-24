import { test } from 'vitest';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateDay, plan, endingOf, bestAnswer, START } from './issue.mjs';
import { foldGovernment } from './government.mjs';
import { buildDemoFeed } from './feed.mjs';
import { drawForIssue } from './lot.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const pool = JSON.parse(readFileSync(join(here, '../../docs/demo/citizens/pool.json'), 'utf8')).people;
const cabinet = JSON.parse(readFileSync(join(here, '../../docs/demo/cabinet.json'), 'utf8'));

// marks: {A: 'ppfp', ...} one letter per test t1..tN (p pass, f fail, u unclear)
function day(date, marks, { kinds = 'ttll', run = '2026-11-24', mode = 'backfill' } = {}) {
  const p = plan(date);
  const id = `${date}-demo-case`;
  const draw = drawForIssue(pool, id);
  const tests = [...kinds].map((k, i) => ({ id: `t${i + 1}`, kind: k === 't' ? 'test' : 'limit', text: `Test number ${i + 1} for the case`, backers: 40 }));
  const d = {
    schema: 'fp-demo/1', id, stage: 'published',
    run: { mode, run_date: run, news_date: date },
    plan: p,
    case: { title: 'A made-up case', short: 'CASE', question: 'What should the town do about it?', place: 'Fernbridge (made up)',
      story: 'Fernbridge, a made-up town of 40,000, has a problem that was really in the news this week, with invented numbers.',
      in_the_news: { headline: 'A real headline', why: 'The topic was in the news on this day.', sources: ['s1'] }, facts: [] },
    citizens: { pool: 'pool-2026-11-23', seed: draw.citizenSeed, drawn: 100, ids: draw.citizens, model: 'claude-haiku-5-5', tests,
      voices: [{ citizen: draw.citizens[0], who: 'a carer, 40s', text: 'Make it work for us.' }, { citizen: draw.citizens[1], who: 'a builder, 30s', text: 'Keep it simple.' }] },
    bench: ['A', 'B', 'C'].map((a) => ({ id: a, angle: 'an angle', title: `Answer ${a}`, answer: `What answer ${a} would do, in plain words.`, engine: 'claude', model: 'claude-sonnet-5-5' })),
    gate: { rows: Object.entries(marks).flatMap(([a, m]) => [...m].map((r, i) => ({ answer: a, test: `t${i + 1}`, result: { p: 'pass', f: 'fail', u: 'unclear' }[r], note: 'Because the answer says so.' }))),
      verdict: 'What the marks show, in a sentence.', rounds: 1 },
    jury: { seed: draw.jurySeed, size: 12, ids: draw.jury, model: 'claude-haiku-5-5', question: 'Who should pay for it, in the end?', options: ['the town', 'the users'], votes: [7, 5], ruling: 'The town pays, 7 to 5.',
      reasons: [{ juror: draw.jury[0], text: 'Everyone gains.' }, { juror: draw.jury[1], text: 'Users gain most.' }] },
    sources: [{ id: 's1', title: 'A real story', publisher: 'BBC News', date: date, url: 'https://www.bbc.co.uk/news/x' }],
    made_by: { workers: ['test'] },
  };
  d.ending = endingOf(d);
  const best = bestAnswer(d);
  const decision = { accepted: 'adopted', partly: 'trial', rejected: 'sent-back' }[d.ending];
  d.minister = { minister: p.area, decision, answer: decision === 'sent-back' ? undefined : best, text: 'What is signed, or why it goes back.', statement: 'The minister explains the decision in plain words.', stop: decision === 'trial' ? '2027-06-01' : undefined };
  d.predictions = decision === 'sent-back' ? [] : [{ id: 'p1', claim: 'Something will happen by then.', due: '2027-03-01', rule: 'Marked hit if it happened.', result: 'pending' }];
  return d;
}
const ok = (d) => assert.deepEqual(validateDay(d).errors, []);
const bad = (d, re) => assert.ok(validateDay(d).errors.some((e) => re.test(e)), validateDay(d).errors.join('\n'));

test('the rotation: areas weekly, every area meets every ending in three weeks, 5/5/4 in the first fortnight', () => {
  assert.deepEqual(plan(START), { area: 'housing', ending: 'accepted' });
  const first = Array.from({ length: 14 }, (_, i) => plan(new Date(Date.parse(START) + i * 864e5).toISOString().slice(0, 10)));
  const n = (e) => first.filter((p) => p.ending === e).length;
  assert.deepEqual([n('accepted'), n('partly'), n('rejected')], [5, 5, 4]);
  for (const a of ['housing', 'crime']) {
    const got = Array.from({ length: 21 }, (_, i) => plan(new Date(Date.parse(START) + i * 864e5).toISOString().slice(0, 10))).filter((p) => p.area === a).map((p) => p.ending).sort();
    assert.deepEqual(got, ['accepted', 'partly', 'rejected']);
  }
  assert.throws(() => plan('2026-11-09'));
});

test('the three endings come from the marks', () => {
  ok(day('2026-11-10', { A: 'pppp', B: 'ppuf', C: 'pfpp' })); // accepted: A passes everything
  ok(day('2026-11-11', { A: 'ppup', B: 'pfpf', C: 'ufpp' })); // partly: no clean pass, A within the limits
  ok(day('2026-11-12', { A: 'ppfp', B: 'pppf', C: 'uupf' })); // rejected: every answer breaks a limit (t3/t4)
});

test('a day whose honest marks miss the chosen ending is not valid', () => {
  bad(day('2026-11-10', { A: 'ppup', B: 'ppup', C: 'ppup' }), /the plan wants accepted/);
  bad(day('2026-11-12', { A: 'pppp', B: 'ffff', C: 'ffff' }), /the plan wants rejected/);
});

test('the minister follows the ending, and a trial takes the best answer within the limits', () => {
  const d = day('2026-11-11', { A: 'pfpp', B: 'pppf', C: 'uupp' });
  assert.equal(d.minister.answer, 'A');
  ok(d);
  d.minister.answer = 'B'; bad(d, /best answer within the limits \(A\)/);
  const e = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pfpp' });
  e.minister.decision = 'trial'; bad(e, /is adopted, not trial/);
});

test('every answer is marked on every test exactly once, and predictions fall due after the run', () => {
  const d = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pppp' });
  d.gate.rows.pop(); bad(d, /exactly one mark for answer C on t4/);
  const e = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pppp' });
  e.predictions[0].due = '2026-11-24'; bad(e, /not after the run date/);
});

test('the topic must really be in the news: a source is required', () => {
  const d = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pppp' });
  d.case.in_the_news.sources = []; d.sources = [{ ...d.sources[0] }];
  bad(d, /needs a source/);
});

test('the government grows only from adopted and trialled days', () => {
  const a = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pppp' }); // housing, accepted
  const r = day('2026-11-12', { A: 'ppfp', B: 'pppf', C: 'uupf' }); // education, rejected
  const days = new Map([[a.id, a], [r.id, r]]);
  const g1 = { schema: 'fp-demo-gov/1', date: '2026-11-10', day: a.id, made_by: { workers: ['t'] },
    debate: [{ minister: 'housing', text: 'We adopt this, here is why.' }, { minister: 'energy', text: 'And what will it cost?' }],
    changes: [{ op: 'adopt', line: 'housing-1', minister: 'housing', text: 'Every new home gets a repair line.', why: 'Passed every test on 10 Nov.' }] };
  const g2 = { schema: 'fp-demo-gov/1', date: '2026-11-12', day: r.id, made_by: { workers: ['t'] },
    debate: [{ minister: 'education', text: 'Nothing passed, so we try again.' }, { minister: 'housing', text: 'Our line still stands.' }],
    changes: [{ op: 'change', line: 'housing-1', minister: 'housing', text: 'Every new home gets a repair line answered in a day.', why: 'The 12 Nov debate showed waits matter.' }] };
  const out = foldGovernment(days, [g2, g1]);
  assert.deepEqual(out.skipped, []);
  assert.equal(out.lines.length, 1);
  assert.equal(out.lines[0].status, 'policy');
  assert.match(out.lines[0].text, /in a day/);
  assert.equal(out.lines[0].history.length, 2);
  // a rejected day can't adopt; a day nobody published can't either
  const g3 = { ...g2, changes: [{ op: 'adopt', line: 'education-1', minister: 'education', text: 'Something nobody passed.', why: 'No reason at all.' }] };
  assert.match(foldGovernment(days, [g1, g3]).skipped[0].errors.join(), /adopts nothing/);
  assert.match(foldGovernment(new Map(), [g1]).skipped[0].errors.join(), /not a published demo day/);
  // the wrong minister can't adopt
  const g4 = { ...g1, changes: [{ ...g1.changes[0], minister: 'energy', line: 'energy-1' }] };
  assert.match(foldGovernment(days, [g4]).skipped[0].errors.join(), /only the housing minister/);
});

test('the feed: newest first, endings counted, bad files left out', () => {
  const a = day('2026-11-10', { A: 'pppp', B: 'pppp', C: 'pppp' });
  const p = day('2026-11-11', { A: 'ppup', B: 'pfpf', C: 'ufpp' });
  const broken = { ...day('2026-11-12', { A: 'ppfp', B: 'pppf', C: 'uupf' }), ending: 'accepted' };
  const f = buildDemoFeed([a, p, broken], [], cabinet, { today: '2026-11-24' });
  assert.deepEqual(f.days.map((d) => d.id), [p.id, a.id]);
  assert.deepEqual(f.endings, { accepted: 1, partly: 1, rejected: 0 });
  assert.equal(f.skipped.length, 1);
  assert.equal(f.government.ministers.length, 7);
  assert.equal(f.scoreboard.total, 2);
});

test('the cabinet: seven invented ministers, one per area', () => {
  assert.deepEqual(cabinet.ministers.map((m) => m.area), ['housing', 'health', 'education', 'work', 'energy', 'transport', 'crime']);
});
