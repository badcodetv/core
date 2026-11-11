#!/usr/bin/env node
// The git → chain mirror, DRY RUN ONLY. Design: design/2026-11-11-future-proof-government/m5-open-record.md §9.
//
// Reads the government's policy files (docs/government/policies/<post>/<slug>.md, the M2 format) and
// debate logs (docs/government/debates/<id>.md, M3), and prints the plan of what one mirror key WOULD post
// to the deliberation program: a policy record per new or changed file, a prediction per gated world
// check, a neutral argument per debate log version.
//
// There is no send path in this file. It opens no RPC connection, reads no key and signs nothing. Making
// it post is a separate, reviewed change that needs Kai's yes (no devnet, no mainnet until then).
//
//   node scripts/government/chain-mirror.mjs [--state mirror-state.json] [--commit <sha>] [--raw-base <url>]
//
// --state is the mirror's memory of what it last posted per id ({ "<id>": { "hash": "<hex>",
// "account": "<pubkey>" } }); with none, everything is new. On a live mirror it would be rebuilt from the
// chain itself (every Policy whose author is the mirror key), never trusted from git alone.
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

export const RESOLVER_PLACEHOLDER = '<statistician resolver key>';
const URL_RE = /https?:\/\/[^\s)<>"']+/;

export const sha256 = data => createHash('sha256').update(data).digest('hex');

// Flat `key: value` front matter, the M2 policy format (no nesting; `check.claim` is one key).
export function parseFlatFrontMatter(text) {
  const m = /^---\n([\s\S]*?)\n---\n?/.exec(text);
  if (!m) return {};
  const meta = {};
  for (const line of m[1].split('\n')) {
    const i = line.indexOf(':');
    if (i <= 0 || /^\s/.test(line)) continue;
    meta[line.slice(0, i).trim()] = line.slice(i + 1).trim();
  }
  return meta;
}

// The frozen rule of a world check, canonical so anyone can recompute its hash from the file at the
// pinned commit. The result and the provisional flag are not part of the rule.
export function canonicalRule(meta) {
  const keys = ['check.claim', 'check.rule', 'check.source', 'check.source_url', 'check.if_revised', 'check.check_on', 'check.prior'];
  const rule = {};
  for (const k of keys) if (meta[k] !== undefined) rule[k] = meta[k];
  return JSON.stringify(rule, Object.keys(rule).sort());
}

export function planPolicy({ id, file, text }, { state = {}, uriFor, resolver = RESOLVER_PLACEHOLDER }) {
  const meta = parseFlatFrontMatter(text);
  const hash = sha256(text);
  const prev = state[id];
  const steps = [];
  if (prev && prev.hash === hash) {
    steps.push({ op: 'unchanged', id });
  } else {
    steps.push({
      op: 'post_policy', id, content_hash: hash, uri: uriFor(file),
      parent: prev ? prev.account : null,
      note: prev ? 'revision: parent is the last version the mirror posted' : 'new policy',
    });
  }
  if (meta['check.claim']) steps.push(planCheck(id, file, meta, { state, uriFor, resolver }));
  return steps;
}

function planCheck(id, file, meta, { state, uriFor, resolver }) {
  const rule = canonicalRule(meta);
  const rule_hash = sha256(rule);
  const base = { op: 'post_prediction', id, rule_hash };
  const blocked = reason => ({ ...base, op: 'blocked', reason });
  if ((state[id]?.predictions ?? []).includes(rule_hash)) return { ...base, op: 'unchanged' };
  if (/^(yes|true)$/i.test(meta['check.provisional'] ?? '')) {
    return blocked('provisional: not yet fact-gated, and a posted prediction can never be withdrawn');
  }
  if ((meta['check.result'] ?? 'pending') !== 'pending') return blocked(`already resolved in git (${meta['check.result']}); a prediction is posted before its check date, never after`);
  const checkOn = meta['check.check_on'];
  if (!/^\d{4}-\d{2}-\d{2}$/.test(checkOn ?? '')) return blocked('no check_on date');
  const check_at = Math.floor(Date.parse(`${checkOn}T00:00:00Z`) / 1000);
  const prior = Number(meta['check.prior']);
  if (!(prior > 0 && prior < 1)) return blocked('prior missing or not strictly between 0 and 1');
  const source = meta['check.source_url'] ?? (URL_RE.exec(meta['check.source'] ?? '') ?? [])[0];
  if (!source) return blocked('no source URL: check.source is prose; the program freezes a URI (add check.source_url)');
  return {
    ...base, policy: `<the account of ${id}'s latest version>`, resolver,
    check_at, check_on: checkOn, prior_bps: Math.round(prior * 10_000),
    rule_uri: `${uriFor(file)}#check`, source_uri: source,
  };
}

export function planDebate({ id, file, text }, { state = {}, uriFor }) {
  const hash = sha256(text);
  if ((state[id]?.debates ?? []).includes(hash)) return { op: 'unchanged', id, kind: 'debate' };
  return { op: 'post_argument', id, stance: 'neutral', target: `<the account of ${id}'s latest version>`, content_hash: hash, uri: uriFor(file), note: 'the debate log as it stands, both sides' };
}

function walk(dir, prefix = '') {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const name of readdirSync(dir).sort()) {
    const full = join(dir, name);
    if (statSync(full).isDirectory()) out.push(...walk(full, `${prefix}${name}/`));
    else if (name.endsWith('.md') && name !== 'README.md') out.push(`${prefix}${name}`);
  }
  return out;
}

export function buildPlan({ root, state = {}, commit, rawBase, resolver }) {
  const uriFor = file => `${rawBase}/${commit}/${file}`;
  const plan = [];
  for (const rel of walk(join(root, 'docs/government/policies'))) {
    const file = `docs/government/policies/${rel}`;
    const text = readFileSync(join(root, file), 'utf8');
    const id = parseFlatFrontMatter(text).id ?? rel.replace(/\.md$/, '');
    plan.push(...planPolicy({ id, file, text }, { state, uriFor, resolver }));
  }
  for (const rel of walk(join(root, 'docs/government/debates'))) {
    const file = `docs/government/debates/${rel}`;
    plan.push(planDebate({ id: rel.replace(/\.md$/, ''), file, text: readFileSync(join(root, file), 'utf8') }, { state, uriFor }));
  }
  return plan;
}

function main(argv) {
  const arg = name => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : undefined; };
  const root = process.cwd();
  const commit = arg('--commit') ?? execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
  const rawBase = arg('--raw-base') ?? 'https://raw.githubusercontent.com/<owner>/<repo>';
  const state = arg('--state') ? JSON.parse(readFileSync(arg('--state'), 'utf8')) : {};
  const plan = buildPlan({ root, state, commit, rawBase, resolver: arg('--resolver') ?? RESOLVER_PLACEHOLDER });
  const count = op => plan.filter(s => s.op === op).length;
  console.log(JSON.stringify({ dry_run: true, commit, plan }, null, 2));
  console.error(`DRY RUN — nothing sent. ${count('post_policy')} policies, ${count('post_prediction')} predictions, ` +
    `${count('post_argument')} debate logs would post; ${count('blocked')} checks blocked; ${count('unchanged')} unchanged.`);
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) main(process.argv.slice(2));
