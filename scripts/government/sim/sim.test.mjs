import { describe, it, expect } from 'vitest';
import { validateIssue, replayStamp, longDate } from './issue.mjs';
import { drawK, drawForIssue, rng, pick } from './lot.mjs';
import { buildFeed } from './feed.mjs';

const ids = (n, from = 0) => Array.from({ length: n }, (_, i) => `c${String(i + from).padStart(4, '0')}`);

/** A complete, valid published issue; override any top-level part. */
const good = (over = {}) => ({
  schema: 'fp-sim/1',
  id: '2026-11-17-thames-water',
  simulated: true,
  stamp: 'SIMULATED',
  stage: 'published',
  run: { mode: 'replay', run_date: '2026-11-23', news_date: '2026-11-17', replay_stamp: 'Replayed on 23 Nov 2026 from the news of 17 Nov 2026' },
  issue: {
    title: 'Who owns the water?', short: 'THAMES WATER', question: 'What should happen to a water company that cannot pay its debts?',
    summary: 'A water company owes far more than it can pay, and a court decides on a rescue.', summary_sources: ['s1'],
    field: 'water', owner: 'energy-climate', slot: 'parliament', slot_reason: 'a court date is set',
    news: [{ headline: 'Rescue deal delayed', sources: ['s1'] }],
  },
  poll: { pollster: 'YouGov', fieldwork: '7-8 Sep 2026', sample: '2,072 adults', finding: '74% want water in public ownership', real_share: 0.74, sources: ['s2'] },
  citizens: {
    pool: 'pool-2026-11-23', seed: '2026-11-17-thames-water/citizens', drawn: 100, ids: ids(100), model: 'claude-haiku-5-5',
    tests: [{ kind: 'test', text: 'Fewer sewage spills by 2029', backers: 81 }, { kind: 'limit', text: 'Bills do not rise further', backers: 66 }],
    split: { question: 'Water in public hands?', sim_share: 0.7 },
    voices: [{ citizen: 'c0001', who: '58, Swindon, retired', text: 'Fix the pipes first.' }, { citizen: 'c0002', who: '24, Leeds, student', text: 'I just want clean rivers.' }],
  },
  bench: [
    { id: 'A', title: 'Tougher referee', answer: 'Keep it private with a much tougher regulator and fines that bite.', engine: 'claude', model: 'mm', blind: true, sources: [] },
    { id: 'B', title: 'Public when bust', answer: 'A company that goes bust stays in public hands, tested against similar firms.', engine: 'claude', model: 'mm', blind: true, sources: [] },
    { id: 'C', title: 'Customer-owned', answer: 'Hand the company to a not-for-profit owned by its customers.', engine: 'codex', model: 'mm', blind: true, sources: [] },
  ],
  gate: {
    rows: [
      { answer: 'A', test: 'Fewer spills', result: 'fail', note: 'Most penalties deferred', sources: ['s1'] },
      { answer: 'B', test: 'Fewer spills', result: 'unclear', note: 'No evidence either way', sources: [] },
      { answer: 'C', test: 'Bills', result: 'fail', note: 'pure logic: a new owner still owes the debt, no source needed', sources: [] },
    ],
    verdict: 'No answer passes every test.', to_jury: true, rejected_claims: [],
  },
  jury: {
    seed: '2026-11-17-thames-water/jury', size: 12, ids: ids(12, 500), model: 'claude-haiku-5-5',
    question: 'Who takes the loss first?', options: ['Lenders', 'Bill payers', 'Taxpayers'], votes: [9, 1, 2],
    ruling: 'Lenders first.', reasons: [{ juror: 'c0500', text: 'They took the risk.' }, { juror: 'c0501', text: 'Not my bill.' }],
    review: '2027-11-23', real_jury: false,
  },
  minister: { post: 'energy-climate', decision: 'signed', trial: 'The next bust water company stays public for five years.', fail_number: 'Spills no lower than similar firms', stop: '2031-11-23', statement: 'Four prices. We printed who paid for each.' },
  predictions: [{ id: 'p1', answer: 'issue', claim: 'The court sanctions the rescue by 31 Jan 2027', prior: 0.6, due: '2027-01-31', rule: 'A court order published by the due date', sources: ['s1'], result: 'pending' }],
  sources: [
    { id: 's1', title: 'Rescue deal', publisher: 'City AM', date: '2026-11-09', url: 'https://www.cityam.com/x' },
    { id: 's2', title: 'Water poll', publisher: 'YouGov', url: 'https://yougov.com/x' },
  ],
  made_by: { workers: ['hand'] },
  ...over,
});
const errs = (doc, today = '2026-11-23') => validateIssue(doc, { today }).errors;

describe('issue validator', () => {
  it('passes a complete published replay', () => expect(errs(good())).toEqual([]));

  it('requires the SIMULATED stamp and simulated: true', () => {
    expect(errs(good({ stamp: 'REAL' })).join()).toMatch(/stamp/);
    expect(errs(good({ simulated: false })).join()).toMatch(/simulated/);
  });

  it('needs the exact replay stamp', () => {
    const d = good(); d.run.replay_stamp = 'Replayed today';
    expect(errs(d).join()).toMatch(/replay_stamp must be exactly/);
    expect(replayStamp('2026-11-23', '2026-11-17')).toBe('Replayed on 23 Nov 2026 from the news of 17 Nov 2026');
    expect(longDate('2027-01-05')).toBe('5 Jan 2027');
  });

  it('refuses hindsight: predictions must fall due after the run date', () => {
    const d = good(); d.predictions[0].due = '2026-11-20';
    expect(errs(d).join()).toMatch(/no hindsight/);
    d.predictions[0].due = '2026-11-23';
    expect(errs(d).join()).toMatch(/no hindsight/);
  });

  it('refuses a mark made before the due date or in the future', () => {
    const d = good(); Object.assign(d.predictions[0], { result: 'hit', marked_on: '2027-01-01' });
    expect(errs(d, '2027-02-01').join()).toMatch(/marked before it was due/);
    d.predictions[0].marked_on = '2027-02-05';
    expect(errs(d, '2027-02-01').join()).toMatch(/marked in the future/);
  });

  it('rejects unknown and uncited sources', () => {
    const d = good(); d.issue.summary_sources = ['s9'];
    expect(errs(d).join()).toMatch(/unknown source "s9"/);
    const e = good(); e.sources.push({ id: 's3', title: 'Extra', publisher: 'XX', url: 'https://x.org/a' });
    expect(errs(e).join()).toMatch(/s3 is never cited/);
  });

  it('makes a gate pass or fail on a fact cite a source', () => {
    const d = good(); d.gate.rows[0].sources = [];
    expect(errs(d).join()).toMatch(/needs a source/);
  });

  it('needs three blind answers from two engines', () => {
    const d = good(); d.bench[2].engine = 'claude';
    expect(errs(d).join()).toMatch(/two different engines/);
    const e = good(); e.bench[1].blind = false;
    expect(errs(e).join()).toMatch(/must be true/);
  });

  it('checks the jury adds up and only jurors give reasons', () => {
    const d = good(); d.jury.votes = [9, 1, 1];
    expect(errs(d).join()).toMatch(/add up/);
    const e = good(); e.jury.reasons[0].juror = 'c0001';
    expect(errs(e).join()).toMatch(/wasn't on the jury/);
  });

  it('refuses a citizens split with no real poll share beside it', () => {
    const d = good(); delete d.poll.real_share;
    expect(errs(d).join()).toMatch(/real_share/);
  });

  it('never lets simulated citizens be called the public', () => {
    const d = good(); d.minister.statement = 'The public decided, and we listened to them.';
    expect(errs(d).join()).toMatch(/the public/);
  });

  it('accepts an unfinished issue at its own stage, but not as published', () => {
    const d = good({ stage: 'bench' }); delete d.gate; delete d.jury; delete d.minister; delete d.predictions;
    d.sources = d.sources; d.issue.summary_sources = ['s1', 's2']; delete d.poll.real_share; delete d.citizens.split;
    expect(errs(d)).toEqual([]);
    expect(errs({ ...d, stage: 'published' }).join()).toMatch(/missing/);
  });

  it('a live run uses its own day and carries no replay stamp', () => {
    const d = good({ id: '2026-11-23-thames-water' }); d.run = { mode: 'live', run_date: '2026-11-23', news_date: '2026-11-23' };
    expect(errs(d)).toEqual([]);
    d.run.replay_stamp = 'Replayed on 23 Nov 2026 from the news of 23 Nov 2026';
    expect(errs(d).join()).toMatch(/no replay stamp/);
  });
});

describe('drawing by lot', () => {
  it('is the same every time for the same seed, and different for another', () => {
    const pool = ids(1000);
    expect(drawK(pool, 12, 'x')).toEqual(drawK(pool, 12, 'x'));
    expect(drawK(pool, 12, 'x')).not.toEqual(drawK(pool, 12, 'y'));
    expect(new Set(drawK(pool, 100, 'x')).size).toBe(100);
  });
  it('never puts a citizen who set the tests on the jury', () => {
    const pool = ids(1000).map((id) => ({ id }));
    const d = drawForIssue(pool, '2026-11-17-thames-water');
    expect(d.citizens).toHaveLength(100);
    expect(d.jury).toHaveLength(12);
    expect(d.jury.some((j) => d.citizens.includes(j))).toBe(false);
  });
  it('picks by share', () => {
    const r = rng('shares'); const n = { a: 0, b: 0 };
    for (let i = 0; i < 5000; i++) n[pick({ a: 0.8, b: 0.2 }, r())]++;
    expect(n.a / 5000).toBeGreaterThan(0.75); expect(n.a / 5000).toBeLessThan(0.85);
  });
});

describe('feed', () => {
  it('lists valid published issues newest first and skips the rest', () => {
    const older = good({ id: '2026-11-16-thames-water' }); older.run = { ...older.run, news_date: '2026-11-16', replay_stamp: replayStamp('2026-11-23', '2026-11-16') };
    const half = good({ id: '2026-11-18-half', stage: 'gate' });
    const broken = good({ id: '2026-11-19-bad', stamp: 'NOPE' });
    const f = buildFeed([older, good(), half, broken], { today: '2026-11-23' });
    expect(f.issues.map((d) => d.id)).toEqual(['2026-11-17-thames-water', '2026-11-16-thames-water']);
    expect(f.skipped.map((s) => s.id).sort()).toEqual(['2026-11-18-half', '2026-11-19-bad']);
    expect(f.scoreboard).toMatchObject({ total: 2, pending: 2, hit: 0, miss: 0, hit_rate: null });
    expect(f.stamp).toBe('SIMULATED');
  });
});
