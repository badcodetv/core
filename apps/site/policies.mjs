// The BadCode government's policies: one file per policy, docs/government/policies/<post>/<slug>.md.
// Format and rules: docs/government/policies/README.md. Used by the site build and by
// scripts/government/policy-lint.mjs (design/2026-11-11-future-proof-government/README.md §4.1).
import { readdirSync, readFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { parseFrontMatter } from './manifesto.mjs';

export const POSTS = ['prime-minister', 'chancellor', 'foreign', 'home', 'education', 'defence',
  'health', 'work-pensions', 'housing', 'energy-climate'];
export const STATUSES = ['draft', 'in-trial', 'kept', 'changed', 'dropped'];
export const KINDS = ['trial', 'judgement-call', 'right'];
export const BANDS = ['none', 'small', 'medium', 'large'];
export const RESULTS = ['pending', 'held', 'failed', 'void'];
export const MAX_RIGHTS = 3; // shared.md: "What never has a stop date: rights, and only rights" (three)
export const MAX_PRIOR = 0.9; // no safe bets (design §4.3)
export const MAX_LINE = 100;
export const MAX_WORDS = 300;

// ids are split on commas or semicolons; prose lists (leaves_out) on semicolons only, since an item may hold a comma
const list = v => (!v || v === 'none' ? [] : String(v).split(/\s*[;,]\s*/).filter(Boolean));
const prose = v => (!v || v === 'none' ? [] : String(v).split(/\s*;\s*/).filter(Boolean));
const isDate = v => /^\d{4}-\d{2}-\d{2}$/.test(v || '') && !Number.isNaN(Date.parse(v));

// What each kind must carry before it counts as ready (the policy contract's green tick).
const NEEDS_BY_KIND = {
  trial: ['test.where', 'test.against', 'test.measure', 'test.by', 'fails_if', 'stop'],
  'judgement-call': ['judgement.principle', 'judgement.review', 'judgement.change_mind', 'stop'],
  right: ['measure'],
};
const ALWAYS = ['leaves_out', 'signs', 'check.claim', 'check.prior', 'check.rule', 'check.source',
  'check.if_revised', 'check.check_on', 'check.result'];

export function readPolicies(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const post of readdirSync(dir).sort()) {
    const pdir = join(dir, post);
    if (!statSync(pdir).isDirectory()) continue;
    for (const f of readdirSync(pdir).filter(f => /^[a-z0-9-]+\.md$/.test(f)).sort()) {
      const { meta, body } = parseFrontMatter(readFileSync(join(pdir, f), 'utf8'));
      out.push({ file: `${post}/${f}`, dirPost: post, slug: f.slice(0, -3), meta, body,
        needs: list(meta.needs), leavesOut: prose(meta.leaves_out) });
    }
  }
  return out;
}

// Returns { errors: [..], notReady: Map<id, [missing..]>, warnings: [..] }.
// errors fail the lint whatever the status; a missing contract field fails it unless the policy
// is a draft, where it marks the policy "Not ready" instead.
export function lintPolicies(policies, { today = new Date().toISOString().slice(0, 10) } = {}) {
  const errors = [], warnings = [], notReady = new Map();
  const ids = new Set();
  const err = (p, m) => errors.push(`${p.file}: ${m}`);
  for (const p of policies) {
    const m = p.meta, id = m.id;
    if (!id) { err(p, 'no id'); continue; }
    if (ids.has(id)) err(p, `duplicate id ${id}`);
    ids.add(id);
    const [post] = String(id).split('/');
    if (!POSTS.includes(post)) err(p, `id ${id} does not start with a cabinet post`);
    if (m.owner !== post) err(p, `owner "${m.owner}" must be the post in its id (${post})`);
    if (p.dirPost !== post) err(p, `filed under ${p.dirPost}/ but its id says ${post}`);
    for (const k of ['title', 'line', 'status', 'kind']) if (!m[k]) err(p, `no ${k}`);
    if (m.line && m.line.length > MAX_LINE) err(p, `line is ${m.line.length} characters (max ${MAX_LINE})`);
    if (m.status && !STATUSES.includes(m.status)) err(p, `status "${m.status}" is not one of ${STATUSES.join(', ')}`);
    if (m.kind && !KINDS.includes(m.kind)) err(p, `kind "${m.kind}" is not one of ${KINDS.join(', ')}`);
    if (m.band && !BANDS.includes(m.band)) err(p, `band "${m.band}" is not one of ${BANDS.join(', ')}`);
    if (m.kind === 'right' && m.stop && m.stop !== 'never') err(p, 'a right has stop: never');
    if (m.kind !== 'right' && m.stop === 'never') err(p, 'only a right may have stop: never');
    if ((m.status === 'changed' || m.status === 'dropped') && !m.write_up) err(p, `a ${m.status} policy needs write_up`);
    const words = String(p.body).split(/\s+/).filter(Boolean).length;
    if (words > MAX_WORDS) err(p, `body is ${words} words (max ${MAX_WORDS})`);
    if (/composition over inheritance|continuous integration|data-driven/i.test(p.body + (m.line || '')))
      err(p, 'software jargon on a public page (shared.md, Plain words)');

    const missing = [...(NEEDS_BY_KIND[m.kind] || []), ...ALWAYS].filter(k => !m[k] || m[k] === 'none');
    if (m['check.prior']) {
      const pr = Number(m['check.prior']);
      if (!(pr > 0 && pr <= MAX_PRIOR)) err(p, `check.prior ${m['check.prior']} must be above 0 and at most ${MAX_PRIOR} (no safe bets)`);
    }
    if (m['check.check_on'] && !isDate(m['check.check_on'])) err(p, `check.check_on "${m['check.check_on']}" is not YYYY-MM-DD`);
    if (m['check.result'] && !RESULTS.includes(m['check.result'])) err(p, `check.result "${m['check.result']}" is not one of ${RESULTS.join(', ')}`);
    if (m['check.result'] && m['check.result'] !== 'pending' && !m['check.note']) err(p, 'a resolved check needs check.note');
    if (m['check.result'] === 'pending' && isDate(m['check.check_on']) && m['check.check_on'] < today)
      warnings.push(`${p.file}: world check was due ${m['check.check_on']} and is still pending`);

    if (missing.length) {
      if (m.status === 'draft') notReady.set(id, missing);
      else err(p, `not ready (missing ${missing.join(', ')}) but status is ${m.status}`);
    }
  }
  for (const p of policies) for (const n of p.needs) if (!ids.has(n)) err(p, `needs ${n}, which does not exist`);
  const rights = policies.filter(p => p.meta.kind === 'right').length;
  if (rights > MAX_RIGHTS) errors.push(`${rights} rights; shared.md allows ${MAX_RIGHTS}, and a new right comes by human PR`);
  // Each post keeps one check due within six months, so the scoreboard isn't empty for years.
  const soon = new Date(Date.parse(today) + 183 * 864e5).toISOString().slice(0, 10);
  for (const post of POSTS) {
    const mine = policies.filter(p => p.meta.owner === post && p.meta.status !== 'dropped');
    if (mine.length && !mine.some(p => p.meta['check.result'] !== 'pending' || (isDate(p.meta['check.check_on']) && p.meta['check.check_on'] <= soon)))
      warnings.push(`${post}: no world check due within six months`);
  }
  return { errors, warnings, notReady };
}

// The manifesto page's `policies:` list, in its order; ids not found are reported by the lint.
export function policiesFor(page, policies) {
  const byId = new Map(policies.map(p => [p.meta.id, p]));
  return list(page.policies).map(id => byId.get(id)).filter(Boolean);
}

const pct = p => `${Math.round(Number(p) * 100)}%`;
const RESULT_WORDS = { pending: 'not checked yet', held: 'it held', failed: 'it failed', void: 'void' };
const STATUS_WORDS = { draft: 'Draft', 'in-trial': 'In trial', kept: 'Kept', changed: 'Changed', dropped: 'Dropped' };

// A policy as plain manifesto text ("## Title" then paragraphs), the form the site and teletext print.
// notReady: the list of missing fields from the lint, if any.
export function policyText(p, notReady) {
  const m = p.meta, out = [`## ${m.title}`, m.line, String(p.body).trim()];
  if (m.kind === 'trial') {
    out.push(`The test. ${m['test.where']}, against ${m['test.against']}, measured by ${m['test.measure']}, by ${m['test.by']}.`.replace(/\.\./g, '.'));
    if (m.fails_if) out.push(`Fails if: ${m.fails_if}`);
  } else if (m.kind === 'judgement-call') {
    out.push(`Judgement call. ${m['judgement.principle']} Reviewed ${m['judgement.review']}. What would change our mind: ${m['judgement.change_mind']}`);
  } else if (m.kind === 'right') {
    out.push(`A right: it never stops. Measured by ${m.measure}`);
  }
  if (m.kind !== 'right' && m.stop) out.push(`The undo. ${m.stop}`);
  if (m.leaves_out) out.push(`Who it leaves out: ${p.leavesOut.join('; ')}.`);
  if (m.signs) out.push(`Who signs: ${m.signs}.`);
  if (m['check.claim']) {
    const r = m['check.result'] || 'pending';
    out.push(`Our prediction: ${m['check.claim']} Our odds: ${pct(m['check.prior'])}. Checked on ${m['check.check_on']}: ${RESULT_WORDS[r] || r}.${m['check.note'] ? ` ${m['check.note']}` : ''}`);
  }
  const status = STATUS_WORDS[m.status] || m.status;
  out.push(`Status: ${status}${notReady ? ', not ready' : ''}.${m.write_up ? ` ${m.write_up}` : ''}`);
  return out.filter(Boolean).map(s => s.replace(/\.\.$/, '.')).join('\n\n');
}
