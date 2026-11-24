// The Future Proof Demo: one demo day, one JSON file. A fresh start beside the simulation
// (scripts/government/sim/), sharing only the idea and the citizen pool (copied).
// This file IS the schema (SPEC) plus the rules a shape can't express, the rotation that picks each
// day's area and ending, and the rule that works out which ending a day actually reached.
// Zero dependencies on purpose: Bob workers run it with plain `node`.
//
// Like fixture data in a test: each day's case is made up (an invented town, proposal and numbers) on a
// topic that was really in the news. The ending is chosen up front; the checker still marks honestly,
// and the file is only valid when the honest marks reach the chosen ending.

export const SCHEMA = 'fp-demo/1';
export const STAGES = ['case', 'citizens', 'bench', 'gate', 'jury', 'minister', 'published'];
export const AREAS = ['housing', 'health', 'education', 'work', 'energy', 'transport', 'crime'];
export const ENDINGS = ['accepted', 'partly', 'rejected'];
export const RESULTS = ['pass', 'fail', 'unclear'];
// what the minister does for each ending
export const DECISION = { accepted: 'adopted', partly: 'trial', rejected: 'sent-back' };

const DATE = /^\d{4}-\d{2}-\d{2}$/;
const ID = /^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$/;
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
export const longDate = (d) => { const [y, m, dd] = d.split('-').map(Number); return `${dd} ${MONTHS[m - 1]} ${y}`; };

// ---------- the rotation ----------
// Day 0 is 10 Nov 2026, the first backfilled day. Areas go round in order, so each comes up once a week.
// Endings go round with them, one step later each week: area k in week w gets ENDINGS[(k + w) % 3].
// So over three weeks every area meets every ending once, and the first fortnight has 5 accepted,
// 5 partly and 4 rejected.
export const START = '2026-11-10';
const dayIndex = (d) => Math.round((Date.parse(`${d}T12:00:00Z`) - Date.parse(`${START}T12:00:00Z`)) / 864e5);
/** The area and ending a news date is given. */
export function plan(newsDate) {
  const i = dayIndex(newsDate);
  if (i < 0) throw new Error(`the demo starts on ${START}`);
  return { area: AREAS[i % 7], ending: ENDINGS[(i % 7 + Math.floor(i / 7)) % 3] };
}

// ---------- the ending a day reached ----------
// accepted: at least one answer passes every test and limit.
// rejected: every answer fails at least one of the citizens' limits (their red lines).
// partly:   anything in between (no clean pass, but at least one answer keeps within every limit).
export function scoreAnswers(doc) {
  const tests = doc.citizens?.tests ?? [];
  const kind = Object.fromEntries(tests.map((t) => [t.id, t.kind]));
  return ['A', 'B', 'C'].map((a) => {
    const rows = (doc.gate?.rows ?? []).filter((r) => r.answer === a);
    const n = (res) => rows.filter((r) => r.result === res).length;
    return {
      answer: a, pass: n('pass'), fail: n('fail'), unclear: n('unclear'), of: tests.length,
      clean: rows.length === tests.length && rows.every((r) => r.result === 'pass'),
      breaksLimit: rows.some((r) => r.result === 'fail' && kind[r.test] === 'limit'),
    };
  });
}
export function endingOf(doc) {
  const s = scoreAnswers(doc);
  if (s.some((x) => x.clean)) return 'accepted';
  if (s.every((x) => x.breaksLimit)) return 'rejected';
  return 'partly';
}
/** The answer the minister takes forward: a clean one, else the most passes among those within the limits. */
export function bestAnswer(doc) {
  const s = scoreAnswers(doc);
  const pool = s.some((x) => x.clean) ? s.filter((x) => x.clean) : s.filter((x) => !x.breaksLimit);
  return pool.sort((a, b) => b.pass - a.pass || a.fail - b.fail)[0]?.answer ?? null;
}

// ---------- the shape ----------
const ids = { type: 'array', of: { type: 'string' } };
export const SPEC = {
  schema: { type: 'enum', values: [SCHEMA] },
  id: { type: 'string', re: ID },
  stage: { type: 'enum', values: STAGES },
  run: { type: 'object', fields: {
    mode: { type: 'enum', values: ['backfill', 'daily'] },
    run_date: { type: 'date' },
    news_date: { type: 'date' },
  } },
  plan: { type: 'object', fields: {
    area: { type: 'enum', values: AREAS },
    ending: { type: 'enum', values: ENDINGS },
  } },
  case: { type: 'object', fields: {
    title: { type: 'string', min: 3, max: 80 },
    short: { type: 'string', min: 2, max: 22 },
    question: { type: 'string', min: 10, max: 240 },
    place: { type: 'string', min: 2, max: 60 },
    story: { type: 'string', min: 40, max: 900 },
    in_the_news: { type: 'object', fields: {
      headline: { type: 'string', min: 5, max: 160 },
      why: { type: 'string', min: 10, max: 300 },
      memory_id: { type: 'string', opt: true },
      sources: ids,
    } },
    facts: { type: 'array', max: 4, of: { type: 'object', fields: {
      text: { type: 'string', min: 10, max: 240 },
      sources: { type: 'array', min: 1, of: { type: 'string' } },
    } } },
  } },
  citizens: { type: 'object', stage: 'citizens', fields: {
    pool: { type: 'string', min: 3 },
    seed: { type: 'string', min: 3 },
    drawn: { type: 'int', minv: 50, maxv: 300 },
    ids: { type: 'array', min: 50, of: { type: 'string' } },
    model: { type: 'string', min: 3 },
    tests: { type: 'array', min: 3, max: 6, of: { type: 'object', fields: {
      id: { type: 'string', re: /^t\d$/ },
      kind: { type: 'enum', values: ['test', 'limit'] },
      text: { type: 'string', min: 8, max: 160 },
      backers: { type: 'int', minv: 0 },
    } } },
    voices: { type: 'array', min: 2, max: 6, of: { type: 'object', fields: {
      citizen: { type: 'string', min: 2 },
      who: { type: 'string', min: 3, max: 80 },
      text: { type: 'string', min: 5, max: 280 },
    } } },
  } },
  bench: { type: 'array', stage: 'bench', min: 3, max: 3, of: { type: 'object', fields: {
    id: { type: 'enum', values: ['A', 'B', 'C'] },
    angle: { type: 'string', min: 3, max: 60 },
    title: { type: 'string', min: 3, max: 70 },
    answer: { type: 'string', min: 20, max: 900 },
    engine: { type: 'enum', values: ['claude', 'codex'] },
    model: { type: 'string', min: 2 },
  } } },
  gate: { type: 'object', stage: 'gate', fields: {
    rows: { type: 'array', min: 9, of: { type: 'object', fields: {
      answer: { type: 'enum', values: ['A', 'B', 'C'] },
      test: { type: 'string', re: /^t\d$/ },
      result: { type: 'enum', values: RESULTS },
      note: { type: 'string', min: 3, max: 300 },
    } } },
    verdict: { type: 'string', min: 10, max: 400 },
    rounds: { type: 'int', minv: 1, maxv: 3 },
  } },
  ending: { type: 'enum', values: ENDINGS, stage: 'gate' },
  jury: { type: 'object', stage: 'jury', fields: {
    seed: { type: 'string', min: 3 },
    size: { type: 'int', minv: 12, maxv: 99 },
    ids: { type: 'array', min: 12, of: { type: 'string' } },
    model: { type: 'string', min: 3 },
    question: { type: 'string', min: 10, max: 300 },
    options: { type: 'array', min: 2, max: 4, of: { type: 'string', min: 2, max: 120 } },
    votes: { type: 'array', min: 2, max: 4, of: { type: 'int', minv: 0 } },
    ruling: { type: 'string', min: 5, max: 400 },
    reasons: { type: 'array', min: 2, max: 4, of: { type: 'object', fields: {
      juror: { type: 'string', min: 2 },
      text: { type: 'string', min: 5, max: 280 },
    } } },
  } },
  minister: { type: 'object', stage: 'minister', fields: {
    minister: { type: 'enum', values: AREAS },
    decision: { type: 'enum', values: Object.values(DECISION) },
    answer: { type: 'enum', values: ['A', 'B', 'C'], opt: true },
    text: { type: 'string', min: 10, max: 400 },
    statement: { type: 'string', min: 20, max: 700 },
    stop: { type: 'date', opt: true },
  } },
  predictions: { type: 'array', stage: 'minister', max: 3, of: { type: 'object', fields: {
    id: { type: 'string', re: /^p\d$/ },
    claim: { type: 'string', min: 10, max: 300 },
    due: { type: 'date' },
    rule: { type: 'string', min: 10, max: 300 },
    result: { type: 'enum', values: ['pending', 'hit', 'miss', 'void'] },
    marked_on: { type: 'date', opt: true },
    mark_note: { type: 'string', opt: true, max: 400 },
  } } },
  sources: { type: 'array', min: 1, of: { type: 'object', fields: {
    id: { type: 'string', re: /^s\d+$/ },
    title: { type: 'string', min: 3 },
    publisher: { type: 'string', min: 2 },
    date: { type: 'date', opt: true },
    url: { type: 'url' },
  } } },
  made_by: { type: 'object', fields: {
    workers: { type: 'array', of: { type: 'string' } },
    note: { type: 'string', opt: true, max: 400 },
  } },
};

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
      if (typeof v !== 'boolean') bad('not true/false');
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

/** Validate one demo day. Returns { errors: string[] }. `today` guards marks made in the future. */
export function validateDay(doc, { today } = {}) {
  const errs = [];
  if (!doc || typeof doc !== 'object') return { errors: ['not an object'] };
  const stage = STAGES.includes(doc.stage) ? doc.stage : 'published';
  const at = (s) => STAGES.indexOf(s);
  for (const [k, s] of Object.entries(SPEC)) {
    if (s.stage && at(stage) < at(s.stage) && (doc[k] === undefined || doc[k] === null)) continue;
    checkValue(doc[k], s, k, errs);
  }
  for (const k of Object.keys(doc)) if (!(k in SPEC)) errs.push(`unknown top-level field "${k}"`);
  if (errs.length) return { errors: errs };

  const r = doc.run;
  if (!doc.id.startsWith(r.news_date)) errs.push(`id must start with the news date ${r.news_date}`);
  if (r.news_date > r.run_date) errs.push('news_date is after run_date');
  if (r.mode === 'daily' && r.news_date !== r.run_date) errs.push('a daily run uses the same day\'s news');
  let want;
  try { want = plan(r.news_date); } catch (e) { errs.push(e.message); }
  if (want && (doc.plan.area !== want.area || doc.plan.ending !== want.ending)) {
    errs.push(`plan must be the rotation's: area ${want.area}, ending ${want.ending}`);
  }

  // sources: every id cited exists, every source is cited
  const sid = new Set(doc.sources.map((s) => s.id));
  if (sid.size !== doc.sources.length) errs.push('duplicate source ids');
  const cited = new Set();
  const cite = (list, where) => (list || []).forEach((id) => { cited.add(id); if (!sid.has(id)) errs.push(`${where}: unknown source "${id}"`); });
  cite(doc.case.in_the_news.sources, 'case.in_the_news.sources');
  if (!doc.case.in_the_news.sources.length) errs.push('case.in_the_news needs a source: the topic must really be in the news');
  doc.case.facts.forEach((f, i) => cite(f.sources, `case.facts[${i}].sources`));
  for (const s of doc.sources) if (!cited.has(s.id)) errs.push(`source ${s.id} is never cited`);

  const c = doc.citizens;
  if (c) {
    if (c.ids.length !== c.drawn) errs.push(`citizens.ids has ${c.ids.length}, drawn says ${c.drawn}`);
    if (new Set(c.ids).size !== c.ids.length) errs.push('citizens.ids repeats a citizen');
    const tids = c.tests.map((t) => t.id);
    if (new Set(tids).size !== tids.length) errs.push('two tests share an id');
    if (!c.tests.some((t) => t.kind === 'test')) errs.push('citizens set no test');
    if (!c.tests.some((t) => t.kind === 'limit')) errs.push('citizens set no limit');
    for (const t of c.tests) if (t.backers > c.drawn) errs.push(`${t.id} has more backers than citizens drawn`);
    for (const v of c.voices) if (!c.ids.includes(v.citizen)) errs.push(`voice from ${v.citizen}, who wasn't drawn`);
  }
  if (doc.bench) {
    if (doc.bench.map((b) => b.id).sort().join('') !== 'ABC') errs.push('bench needs exactly A, B and C');
    for (const b of doc.bench) { const w = b.answer.trim().split(/\s+/).length; if (w > 130) errs.push(`answer ${b.id} has ${w} words (at most 120, 130 with grace)`); }
  }
  if (doc.gate) {
    const tids = (c?.tests ?? []).map((t) => t.id);
    for (const a of ['A', 'B', 'C']) for (const t of tids) {
      const n = doc.gate.rows.filter((g) => g.answer === a && g.test === t).length;
      if (n !== 1) errs.push(`gate needs exactly one mark for answer ${a} on ${t} (has ${n})`);
    }
    for (const g of doc.gate.rows) if (!tids.includes(g.test)) errs.push(`gate marks unknown test ${g.test}`);
    const reached = endingOf(doc);
    if (doc.ending !== reached) errs.push(`ending says ${doc.ending} but the marks reach ${reached}`);
    if (stage !== 'gate' && reached !== doc.plan.ending) errs.push(`the marks reach ${reached}, the plan wants ${doc.plan.ending}: rewrite the case or the answers and check again; never edit a mark`);
  }
  if (doc.jury) {
    const j = doc.jury;
    if (j.ids.length !== j.size) errs.push(`jury.ids has ${j.ids.length}, size says ${j.size}`);
    if (j.votes.length !== j.options.length) errs.push('jury.votes must line up with jury.options');
    else if (j.votes.reduce((a, b) => a + b, 0) !== j.size) errs.push('jury votes must add up to the jury size');
    for (const x of j.reasons) if (!j.ids.includes(x.juror)) errs.push(`reason from ${x.juror}, who wasn't on the jury`);
    if (c && j.ids.some((id) => c.ids.includes(id))) errs.push('a juror also set the tests');
  }
  if (doc.minister) {
    const m = doc.minister;
    if (m.minister !== doc.plan.area) errs.push(`the ${doc.plan.area} minister decides a ${doc.plan.area} day`);
    if (m.decision !== DECISION[doc.ending]) errs.push(`a day ending ${doc.ending} is ${DECISION[doc.ending]}, not ${m.decision}`);
    const best = bestAnswer(doc);
    if (m.decision === 'sent-back') { if (m.answer) errs.push('a sent-back day takes no answer forward'); }
    else if (m.decision === 'adopted') { if (!scoreAnswers(doc).find((x) => x.answer === m.answer)?.clean) errs.push('an adopted answer must pass every test'); }
    else if (m.answer !== best) errs.push(`a trial takes forward the best answer within the limits (${best})`);
    if (m.decision === 'trial' && !m.stop) errs.push('a trial needs a stop date');
    if (m.stop && m.stop <= r.run_date) errs.push('minister.stop must be after the run date');
  }
  if (doc.predictions) {
    const need = doc.minister?.decision === 'sent-back' ? 0 : 1;
    if (doc.predictions.length < need) errs.push('an adopted or trialled day makes at least one prediction');
    const pids = new Set();
    for (const [i, p] of doc.predictions.entries()) {
      if (pids.has(p.id)) errs.push(`duplicate prediction id ${p.id}`); pids.add(p.id);
      if (p.due <= r.run_date) errs.push(`predictions[${i}]: due ${p.due} is not after the run date ${r.run_date}`);
      if (p.result !== 'pending') {
        if (!p.marked_on) errs.push(`predictions[${i}]: a marked prediction needs marked_on`);
        else if (p.marked_on < p.due) errs.push(`predictions[${i}]: marked before it was due`);
        if (today && p.marked_on && p.marked_on > today) errs.push(`predictions[${i}]: marked in the future`);
      }
    }
  }
  if (stage === 'published') {
    for (const k of ['citizens', 'bench', 'gate', 'ending', 'jury', 'minister', 'predictions']) if (doc[k] === undefined) errs.push(`published day is missing ${k}`);
  }
  if (/\bthe public (decided|voted|chose|wants|said)\b/i.test(JSON.stringify(doc))) errs.push('the citizens are made up: never "the public decided/voted/wants"');
  return { errors: errs };
}
