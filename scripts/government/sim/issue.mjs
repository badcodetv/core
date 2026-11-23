// The Future Proof simulation: one issue, one day, one JSON file.
// This file IS the schema (SPEC below) plus the rules a shape can't express.
// Zero dependencies on purpose: Bob workers run it with plain `node`.
//
// Stages fill in order. A file may be valid at an earlier stage; `published` needs everything.

export const SCHEMA = 'fp-sim/1';
export const STAGES = ['clerk', 'citizens', 'bench', 'gate', 'jury', 'minister', 'published'];
export const SLOTS = ['parliament', 'longest-wait', 'alarm'];
export const POSTS = ['prime-minister', 'chancellor', 'foreign', 'home', 'education', 'defence', 'health', 'work-pensions', 'housing', 'energy-climate'];
export const RESULTS = ['pass', 'fail', 'unclear'];
export const STAMP = 'SIMULATED';

const DATE = /^\d{4}-\d{2}-\d{2}$/;
const ID = /^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$/;
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

/** "2026-11-17" -> "17 Nov 2026" */
export const longDate = (d) => { const [y, m, dd] = d.split('-').map(Number); return `${dd} ${MONTHS[m - 1]} ${y}`; };
/** The exact replay stamp every replayed issue must carry. */
export const replayStamp = (runDate, newsDate) => `Replayed on ${longDate(runDate)} from the news of ${longDate(newsDate)}`;

// ---------- the shape ----------
// type: 'string' | 'date' | 'number' | 'int' | 'bool' | 'url' | 'enum' | 'object' | 'array'
// opt: may be missing or null. min: min length (strings/arrays) or min value (numbers).
const src = { type: 'array', min: 1, of: { type: 'string' } }; // source ids
export const SPEC = {
  schema: { type: 'enum', values: [SCHEMA] },
  id: { type: 'string', re: ID },
  simulated: { type: 'bool', is: true },
  stamp: { type: 'enum', values: [STAMP] },
  stage: { type: 'enum', values: STAGES },
  run: { type: 'object', fields: {
    mode: { type: 'enum', values: ['live', 'replay'] },
    run_date: { type: 'date' },
    news_date: { type: 'date' },
    replay_stamp: { type: 'string', opt: true },
  } },
  issue: { type: 'object', fields: {
    title: { type: 'string', min: 3, max: 80 },
    short: { type: 'string', min: 2, max: 22 }, // the label that travels round the loop
    question: { type: 'string', min: 10, max: 240 },
    summary: { type: 'string', min: 20, max: 900 },
    summary_sources: src,
    field: { type: 'string', min: 2 },
    owner: { type: 'enum', values: POSTS },
    slot: { type: 'enum', values: SLOTS },
    slot_reason: { type: 'string', min: 5 },
    news: { type: 'array', min: 1, of: { type: 'object', fields: {
      headline: { type: 'string', min: 5 },
      memory_id: { type: 'string', opt: true },
      sources: src,
    } } },
  } },
  poll: { type: 'object', opt: true, fields: {
    pollster: { type: 'string', min: 2 },
    fieldwork: { type: 'string', min: 4 },
    sample: { type: 'string', min: 2 },
    finding: { type: 'string', min: 10 },
    real_share: { type: 'number', opt: true, minv: 0, maxv: 1 },
    sources: src,
  } },
  citizens: { type: 'object', stage: 'citizens', fields: {
    pool: { type: 'string', min: 3 },
    seed: { type: 'string', min: 3 },
    drawn: { type: 'int', minv: 50, maxv: 300 },
    ids: { type: 'array', min: 50, of: { type: 'string' } },
    model: { type: 'string', min: 3 },
    tests: { type: 'array', min: 2, max: 8, of: { type: 'object', fields: {
      kind: { type: 'enum', values: ['test', 'limit'] },
      text: { type: 'string', min: 8, max: 160 },
      backers: { type: 'int', minv: 0 },
    } } },
    split: { type: 'object', opt: true, fields: {
      question: { type: 'string', min: 5 },
      sim_share: { type: 'number', minv: 0, maxv: 1 },
    } },
    voices: { type: 'array', min: 2, max: 8, of: { type: 'object', fields: {
      citizen: { type: 'string', min: 2 },
      who: { type: 'string', min: 3 },
      text: { type: 'string', min: 5, max: 280 },
    } } },
  } },
  bench: { type: 'array', stage: 'bench', min: 3, max: 3, of: { type: 'object', fields: {
    id: { type: 'enum', values: ['A', 'B', 'C'] },
    title: { type: 'string', min: 3, max: 70 },
    answer: { type: 'string', min: 20, max: 900 },
    engine: { type: 'enum', values: ['claude', 'codex'] },
    model: { type: 'string', min: 2 },
    blind: { type: 'bool', is: true },
    sources: { type: 'array', of: { type: 'string' } },
  } } },
  gate: { type: 'object', stage: 'gate', fields: {
    rows: { type: 'array', min: 3, of: { type: 'object', fields: {
      answer: { type: 'enum', values: ['A', 'B', 'C'] },
      test: { type: 'string', min: 3 },
      result: { type: 'enum', values: RESULTS },
      note: { type: 'string', min: 3, max: 300 },
      sources: { type: 'array', of: { type: 'string' } },
    } } },
    verdict: { type: 'string', min: 10, max: 400 },
    to_jury: { type: 'bool' },
    rejected_claims: { type: 'array', of: { type: 'string' } },
  } },
  jury: { type: 'object', stage: 'jury', fields: {
    seed: { type: 'string', min: 3 },
    size: { type: 'int', minv: 12, maxv: 99 },
    ids: { type: 'array', min: 12, of: { type: 'string' } },
    model: { type: 'string', min: 3 },
    question: { type: 'string', min: 10, max: 300 },
    options: { type: 'array', min: 2, max: 5, of: { type: 'string', min: 2 } },
    votes: { type: 'array', min: 2, max: 5, of: { type: 'int', minv: 0 } },
    ruling: { type: 'string', min: 5, max: 400 },
    reasons: { type: 'array', min: 2, max: 6, of: { type: 'object', fields: {
      juror: { type: 'string', min: 2 },
      text: { type: 'string', min: 5, max: 280 },
    } } },
    review: { type: 'date' },
    real_jury: { type: 'bool' },
  } },
  minister: { type: 'object', stage: 'minister', fields: {
    post: { type: 'enum', values: POSTS },
    decision: { type: 'enum', values: ['signed', 'refused'] },
    trial: { type: 'string', min: 10, max: 400 },
    fail_number: { type: 'string', min: 5, max: 240 },
    stop: { type: 'date' },
    statement: { type: 'string', min: 20, max: 700 },
  } },
  predictions: { type: 'array', stage: 'minister', min: 1, max: 4, of: { type: 'object', fields: {
    id: { type: 'string', min: 2 },
    answer: { type: 'enum', values: ['A', 'B', 'C', 'issue'] },
    claim: { type: 'string', min: 10, max: 300 },
    prior: { type: 'number', minv: 0.05, maxv: 0.9 },
    due: { type: 'date' },
    rule: { type: 'string', min: 10, max: 300 },
    sources: { type: 'array', of: { type: 'string' } },
    result: { type: 'enum', values: ['pending', 'hit', 'miss', 'void'] },
    marked_on: { type: 'date', opt: true },
    mark_note: { type: 'string', opt: true, max: 400 },
  } } },
  sources: { type: 'array', min: 1, of: { type: 'object', fields: {
    id: { type: 'string', min: 1, re: /^s\d+$/ },
    title: { type: 'string', min: 3 },
    publisher: { type: 'string', min: 2 },
    date: { type: 'date', opt: true },
    url: { type: 'url' },
  } } },
  made_by: { type: 'object', fields: {
    workers: { type: 'array', of: { type: 'string' } },
    note: { type: 'string', opt: true },
  } },
};

// ---------- shape checking ----------
function checkValue(v, spec, path, errs) {
  if (v === undefined || v === null) { if (!spec.opt) errs.push(`${path}: missing`); return; }
  const bad = (m) => errs.push(`${path}: ${m}`);
  switch (spec.type) {
    case 'string':
      if (typeof v !== 'string') return bad('not a string');
      if (spec.min && v.trim().length < spec.min) bad(`too short (min ${spec.min})`);
      if (spec.max && v.length > spec.max) bad(`too long (${v.length} > ${spec.max})`);
      if (spec.re && !spec.re.test(v)) bad(`doesn't match ${spec.re}`);
      return;
    case 'date':
      if (typeof v !== 'string' || !DATE.test(v) || Number.isNaN(Date.parse(v))) bad('not a YYYY-MM-DD date');
      return;
    case 'url':
      if (typeof v !== 'string' || !/^https?:\/\/[^\s/]+\.[^\s]+/.test(v)) bad('not an http(s) URL');
      return;
    case 'number': case 'int':
      if (typeof v !== 'number' || Number.isNaN(v)) return bad('not a number');
      if (spec.type === 'int' && !Number.isInteger(v)) bad('not a whole number');
      if (spec.minv !== undefined && v < spec.minv) bad(`below ${spec.minv}`);
      if (spec.maxv !== undefined && v > spec.maxv) bad(`above ${spec.maxv}`);
      return;
    case 'bool':
      if (typeof v !== 'boolean') return bad('not true/false');
      if (spec.is !== undefined && v !== spec.is) bad(`must be ${spec.is}`);
      return;
    case 'enum':
      if (!spec.values.includes(v)) bad(`must be one of ${spec.values.join(', ')}`);
      return;
    case 'array':
      if (!Array.isArray(v)) return bad('not a list');
      if (spec.min && v.length < spec.min) bad(`needs at least ${spec.min}`);
      if (spec.max && v.length > spec.max) bad(`at most ${spec.max}`);
      v.forEach((x, i) => checkValue(x, spec.of, `${path}[${i}]`, errs));
      return;
    case 'object':
      if (typeof v !== 'object' || Array.isArray(v)) return bad('not an object');
      for (const [k, s] of Object.entries(spec.fields)) checkValue(v[k], s, `${path}.${k}`, errs);
      for (const k of Object.keys(v)) if (!(k in spec.fields)) bad(`unknown field "${k}"`);
      return;
  }
}

/** Fields required at or after a stage. */
const neededAt = (stage) => STAGES.indexOf(stage);

/**
 * Validate one issue. `today` (YYYY-MM-DD) is the date the check runs; it guards hindsight.
 * Returns { errors: string[] }.
 */
export function validateIssue(doc, { today } = {}) {
  const errs = [];
  if (!doc || typeof doc !== 'object') return { errors: ['not an object'] };
  const stage = STAGES.includes(doc.stage) ? doc.stage : 'published';
  for (const [k, s] of Object.entries(SPEC)) {
    const later = s.stage && neededAt(stage) < neededAt(s.stage);
    if (later && (doc[k] === undefined || doc[k] === null)) continue; // not reached yet
    checkValue(doc[k], s, k, errs);
  }
  for (const k of Object.keys(doc)) if (!(k in SPEC)) errs.push(`unknown top-level field "${k}"`);
  if (errs.length) return { errors: errs };

  // ---------- rules beyond shape ----------
  const r = doc.run;
  if (!doc.id.startsWith(r.news_date)) errs.push(`id must start with the news date ${r.news_date}`);
  if (r.news_date > r.run_date) errs.push('news_date is after run_date');
  if (r.mode === 'replay') {
    const want = replayStamp(r.run_date, r.news_date);
    if (r.replay_stamp !== want) errs.push(`run.replay_stamp must be exactly "${want}"`);
    if (r.news_date >= r.run_date) errs.push('a replay must come from news before its run date');
  } else {
    if (r.replay_stamp) errs.push('a live run carries no replay stamp');
    if (r.news_date !== r.run_date) errs.push('a live run uses the same day\'s news');
  }

  // every source id cited must exist; every source must be cited
  const ids = new Set(doc.sources.map((s) => s.id));
  if (ids.size !== doc.sources.length) errs.push('duplicate source ids');
  const cited = new Set();
  const cite = (list, where) => (list || []).forEach((id) => { cited.add(id); if (!ids.has(id)) errs.push(`${where}: unknown source "${id}"`); });
  cite(doc.issue.summary_sources, 'issue.summary_sources');
  doc.issue.news.forEach((n, i) => cite(n.sources, `issue.news[${i}].sources`));
  if (doc.poll) cite(doc.poll.sources, 'poll.sources');
  (doc.bench || []).forEach((b, i) => cite(b.sources, `bench[${i}].sources`));
  (doc.gate?.rows || []).forEach((g, i) => cite(g.sources, `gate.rows[${i}].sources`));
  (doc.predictions || []).forEach((p, i) => cite(p.sources, `predictions[${i}].sources`));
  for (const s of doc.sources) if (!cited.has(s.id)) errs.push(`source ${s.id} is never cited`);

  if (doc.citizens) {
    const c = doc.citizens;
    if (c.ids.length !== c.drawn) errs.push(`citizens.ids has ${c.ids.length}, drawn says ${c.drawn}`);
    if (new Set(c.ids).size !== c.ids.length) errs.push('citizens.ids repeats a citizen');
    for (const t of c.tests) if (t.backers > c.drawn) errs.push('a test has more backers than citizens drawn');
    if (!c.tests.some((t) => t.kind === 'test')) errs.push('citizens set no test');
    for (const v of c.voices) if (!c.ids.includes(v.citizen)) errs.push(`voice from ${v.citizen}, who wasn't drawn`);
    if (c.split && doc.poll && doc.poll.real_share === undefined) errs.push('a citizens split needs poll.real_share beside it');
  }
  if (doc.bench) {
    const got = doc.bench.map((b) => b.id).sort().join('');
    if (got !== 'ABC') errs.push('bench needs exactly A, B and C');
    const engines = new Set(doc.bench.map((b) => b.engine));
    if (engines.size < 2) errs.push('bench answers must come from two different engines');
  }
  if (doc.gate) {
    for (const id of ['A', 'B', 'C']) if (!doc.gate.rows.some((g) => g.answer === id)) errs.push(`gate has no row for answer ${id}`);
    for (const [i, g] of doc.gate.rows.entries()) if (g.result !== 'unclear' && !(g.sources || []).length && !/no source|unsourced/i.test(g.note)) {
      // a pass/fail on a fact must point at a source; a pure logic check may say "no source needed" in the note
      if (!/logic|by definition|no source needed/i.test(g.note)) errs.push(`gate.rows[${i}]: a ${g.result} needs a source (or say "no source needed" when it is pure logic)`);
    }
  }
  if (doc.jury) {
    const j = doc.jury;
    if (j.ids.length !== j.size) errs.push(`jury.ids has ${j.ids.length}, size says ${j.size}`);
    if (j.votes.length !== j.options.length) errs.push('jury.votes must line up with jury.options');
    else if (j.votes.reduce((a, b) => a + b, 0) !== j.size) errs.push('jury votes must add up to the jury size');
    for (const x of j.reasons) if (!j.ids.includes(x.juror)) errs.push(`reason from ${x.juror}, who wasn't on the jury`);
    if (j.review <= r.run_date) errs.push('jury.review must be after the run date');
    if (doc.citizens && j.ids.some((id) => !/^c\d{4}$/.test(id))) errs.push('jurors must be pool citizens (c0000 form)');
  }
  if (doc.minister) {
    if (doc.minister.stop <= r.run_date) errs.push('minister.stop must be after the run date');
  }
  if (doc.predictions) {
    const pids = new Set();
    for (const [i, p] of doc.predictions.entries()) {
      if (pids.has(p.id)) errs.push(`duplicate prediction id ${p.id}`); pids.add(p.id);
      // NO HINDSIGHT: a prediction must fall due after the day it was made.
      if (p.due <= r.run_date) errs.push(`predictions[${i}]: due ${p.due} is not after the run date ${r.run_date} (no hindsight)`);
      if (p.result !== 'pending') {
        if (!p.marked_on) errs.push(`predictions[${i}]: a marked prediction needs marked_on`);
        else if (p.marked_on < p.due) errs.push(`predictions[${i}]: marked before it was due`);
        if (today && p.marked_on && p.marked_on > today) errs.push(`predictions[${i}]: marked in the future`);
      }
    }
  }
  if (stage === 'published') {
    for (const k of ['citizens', 'bench', 'gate', 'jury', 'minister', 'predictions']) if (!doc[k]) errs.push(`published issue is missing ${k}`);
  }
  // never call simulated citizens "the public"
  const text = JSON.stringify(doc);
  if (/\bthe public (decided|voted|chose|wants|said)\b/i.test(text)) errs.push('never say "the public" decided/voted/wants: they are simulated citizens');
  return { errors: errs };
}
