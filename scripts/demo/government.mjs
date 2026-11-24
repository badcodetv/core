// The demo government: seven ministers whose manifestos are built only from demo days.
// One file per day on the data branch, docs/demo/government/<news date>.json, written after that day is
// published: the ministers' debate on the day, and the changes it makes to the manifestos.
// Folding the days in date order gives every manifesto line with its history. A line can only be born
// from a day that adopted or trialled something, in that minister's area.
import { AREAS } from './issue.mjs';

export const GOV_SCHEMA = 'fp-demo-gov/1';
const OPS = ['adopt', 'change', 'drop'];
const DATE = /^\d{4}-\d{2}-\d{2}$/;

export function checkGovShape(g) {
  const e = [];
  if (!g || typeof g !== 'object') return ['not an object'];
  const allowed = ['schema', 'date', 'day', 'debate', 'changes', 'made_by'];
  for (const k of Object.keys(g)) if (!allowed.includes(k)) e.push(`unknown field "${k}"`);
  if (g.schema !== GOV_SCHEMA) e.push(`schema must be ${GOV_SCHEMA}`);
  if (!DATE.test(g.date ?? '')) e.push('date: not a YYYY-MM-DD date');
  if (typeof g.day !== 'string' || !g.day.startsWith(g.date ?? '?')) e.push('day: the id of that date\'s demo day');
  if (!Array.isArray(g.debate) || g.debate.length < 2 || g.debate.length > 5) e.push('debate: 2 to 5 speeches');
  else g.debate.forEach((s, i) => {
    if (!AREAS.includes(s?.minister)) e.push(`debate[${i}].minister: unknown minister`);
    if (typeof s?.text !== 'string' || s.text.length < 10 || s.text.length > 400) e.push(`debate[${i}].text: 10 to 400 characters`);
  });
  if (!Array.isArray(g.changes)) e.push('changes: a list (may be empty)');
  else g.changes.forEach((c, i) => {
    if (!OPS.includes(c?.op)) e.push(`changes[${i}].op: adopt, change or drop`);
    if (!AREAS.includes(c?.minister)) e.push(`changes[${i}].minister: unknown minister`);
    if (typeof c?.line !== 'string' || !/^[a-z]+-\d+$/.test(c.line)) e.push(`changes[${i}].line: like housing-1`);
    if (c?.op !== 'drop' && (typeof c?.text !== 'string' || c.text.length < 10 || c.text.length > 240)) e.push(`changes[${i}].text: 10 to 240 characters`);
    if (typeof c?.why !== 'string' || c.why.length < 10 || c.why.length > 240) e.push(`changes[${i}].why: 10 to 240 characters`);
    for (const k of Object.keys(c ?? {})) if (!['op', 'line', 'minister', 'text', 'why'].includes(k)) e.push(`changes[${i}]: unknown field "${k}"`);
  });
  if (!g.made_by || !Array.isArray(g.made_by.workers)) e.push('made_by.workers: a list');
  return e;
}

/**
 * Fold the government days, in date order, over the published demo days.
 * days: Map id -> demo day (published, valid). govs: list of government day files.
 * Returns { lines: [{id, minister, status, text, from, live, history:[...]}], applied: [govs], skipped: [{date, errors}] }.
 */
export function foldGovernment(days, govs) {
  const lines = new Map();
  const applied = [], skipped = [];
  const sorted = [...govs].sort((a, b) => String(a?.date).localeCompare(String(b?.date)));
  const seen = new Set();
  for (const g of sorted) {
    const errs = checkGovShape(g);
    const day = days.get(g?.day);
    if (!errs.length) {
      if (seen.has(g.date)) errs.push('two government files for one date');
      if (!day) errs.push(`day ${g.day} is not a published demo day`);
      else if (day.run.news_date !== g.date) errs.push('date must be the day\'s news date');
    }
    if (!errs.length) {
      const area = day.plan.area, dec = day.minister.decision;
      if (g.debate[0].minister !== area) errs.push(`the ${area} minister opens the debate on a ${area} day`);
      const adopts = g.changes.filter((c) => c.op === 'adopt');
      if (dec === 'sent-back' && adopts.length) errs.push('a sent-back day adopts nothing');
      if (dec !== 'sent-back' && adopts.length !== 1) errs.push(`an ${dec} day adopts exactly one line`);
      // work on a copy so a bad file changes nothing
      const next = new Map([...lines].map(([k, v]) => [k, { ...v, history: [...v.history] }]));
      for (const c of g.changes) {
        const have = next.get(c.line);
        if (c.op === 'adopt') {
          if (c.minister !== area) errs.push(`only the ${area} minister adopts from a ${area} day`);
          if (have) { errs.push(`line ${c.line} already exists`); continue; }
          if (!c.line.startsWith(`${c.minister}-`)) errs.push(`a ${c.minister} line is called ${c.minister}-<n>`);
          next.set(c.line, { id: c.line, minister: c.minister, status: dec === 'adopted' ? 'policy' : 'trial', text: c.text, from: day.id, live: true,
            history: [{ date: g.date, op: 'adopt', day: day.id, text: c.text, why: c.why }] });
        } else {
          if (!have || !have.live) { errs.push(`${c.op} on ${c.line}, which isn't in the manifesto`); continue; }
          if (have.minister !== c.minister) errs.push(`only the ${have.minister} minister changes ${c.line}`);
          have.history.push({ date: g.date, op: c.op, day: day.id, text: c.text ?? null, why: c.why });
          if (c.op === 'change') have.text = c.text; else have.live = false;
        }
      }
      if (!errs.length) { lines.clear(); for (const [k, v] of next) lines.set(k, v); }
    }
    if (errs.length) skipped.push({ date: g?.date ?? '?', errors: errs });
    else { applied.push(g); seen.add(g.date); }
  }
  return { lines: [...lines.values()], applied, skipped };
}
