#!/usr/bin/env node
// Git -> Bob sync for the BadCode government. Dry run by default; --apply writes.
// Desired state: docs/government/{shared.md, workers/*.md, ministers/*.md, schedules.json}.
// Never deletes: things in Bob but not in git are reported as "extra (not touched)".
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, basename } from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const ALLOWED_KEYS = ['engine', 'model', 'effort', 'labels', 'include', 'tools'];
const SCHEDULE_FIELDS = ['worker', 'cron', 'timezone', 'message', 'enabled', 'keep_sessions'];

const csv = (s) => s.split(',').map((x) => x.trim()).filter(Boolean);

export function parseWorkerFile(text) {
  const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(text);
  if (!m) throw new Error('worker file: missing front matter (--- block)');
  const fm = {};
  for (const line of m[1].split(/\r?\n/)) {
    if (!line.trim()) continue;
    const i = line.indexOf(':');
    if (i < 0) throw new Error(`worker file: bad front-matter line: ${line}`);
    const key = line.slice(0, i).trim();
    if (!ALLOWED_KEYS.includes(key)) throw new Error(`worker file: unknown front-matter key: ${key}`);
    fm[key] = line.slice(i + 1).trim();
  }
  if (!fm.engine) throw new Error('worker file: front matter needs engine');
  const labels = {};
  for (const pair of csv(fm.labels ?? '')) {
    const j = pair.indexOf('=');
    if (j < 1) throw new Error(`worker file: bad label (want k=v): ${pair}`);
    labels[pair.slice(0, j).trim()] = pair.slice(j + 1).trim();
  }
  if (fm.include !== undefined && fm.include !== 'ministers') {
    throw new Error(`worker file: include must be "ministers", got "${fm.include}"`);
  }
  return {
    engine: fm.engine,
    model: fm.model ?? '',
    effort: fm.effort ?? '',
    labels,
    tools: csv(fm.tools ?? ''),
    include: fm.include ?? null,
    prompt: m[2].replace(/^\n+/, '').replace(/\s+$/, ''),
  };
}

export function assemblePrompt(shared, worker, briefs = []) {
  let out = `${shared.trim()}\n\n${worker.prompt.trim()}`;
  if (worker.include === 'ministers') {
    out += `\n\n## The ministers\n\n${briefs.map((b) => b.trim()).join('\n\n')}`;
  }
  return out;
}

export function parseMcpReply(bodyText) {
  let text = bodyText.trim();
  if (!text.startsWith('{')) {
    const line = text.split(/\r?\n/).filter((l) => l.startsWith('data:')).pop();
    if (!line) throw new Error(`unreadable MCP reply: ${text.slice(0, 200)}`);
    text = line.slice(5).trim();
  }
  const msg = JSON.parse(text);
  if (msg.error) throw new Error(`MCP error: ${msg.error.message ?? JSON.stringify(msg.error)}`);
  const r = msg.result;
  const out = r?.content?.[0]?.text;
  if (r?.isError) throw new Error(`MCP tool error: ${out ?? JSON.stringify(r)}`);
  return r;
}

const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const sortedLabels = (l) => Object.fromEntries(Object.entries(l ?? {}).sort(([a], [b]) => a.localeCompare(b)));

function workerShape(w) {
  return {
    name: w.name, engine: w.engine ?? '', model: w.model ?? '', effort: w.effort ?? '',
    tools: w.tools ?? [], prompt: w.prompt ?? '', labels: sortedLabels(w.labels),
  };
}
function scheduleShape(s) {
  return {
    name: s.name, worker: s.worker, cron: s.cron, timezone: s.timezone ?? 'UTC',
    message: s.message, enabled: s.enabled ?? true, keep_sessions: s.keep_sessions ?? 30,
  };
}

// desired: {workers:[{name,engine,model,effort,labels,tools,prompt}], schedules:[...]}
// current: {workers:[full records], schedules:[rows]}
export function planSync(desired, current) {
  const plan = [];
  const section = (kind, want, have, shape) => {
    const byName = new Map((have ?? []).map((x) => [x.name, x]));
    for (const d of want ?? []) {
      const body = shape(d);
      const c = byName.get(d.name);
      byName.delete(d.name);
      if (!c) { plan.push({ kind, name: d.name, op: 'create', body }); continue; }
      const cs = shape(c);
      const diff = Object.keys(body).filter((k) => !same(body[k], cs[k]));
      plan.push({ kind, name: d.name, op: diff.length ? 'update' : 'unchanged', body, changed: diff });
    }
    for (const name of byName.keys()) plan.push({ kind, name, op: 'extra', body: null });
  };
  section('worker', desired.workers, current.workers, workerShape);
  section('schedule', desired.schedules, current.schedules, scheduleShape);
  return plan;
}

// ---------- IO ----------

export function loadDesired(root) {
  const gov = join(root, 'docs/government');
  const need = (p) => {
    if (!existsSync(p)) throw new Error(`missing desired-state file: ${p}`);
    return p;
  };
  const shared = readFileSync(need(join(gov, 'shared.md')), 'utf8');
  const wdir = need(join(gov, 'workers'));
  const wfiles = readdirSync(wdir).filter((f) => f.endsWith('.md')).sort();
  if (!wfiles.length) throw new Error(`no worker files in ${wdir}`);
  const mdir = join(gov, 'ministers');
  const briefs = existsSync(mdir)
    ? readdirSync(mdir).filter((f) => f.endsWith('.md')).sort().map((f) => readFileSync(join(mdir, f), 'utf8'))
    : [];
  const workers = wfiles.map((f) => {
    const w = parseWorkerFile(readFileSync(join(wdir, f), 'utf8'));
    if (w.include === 'ministers' && !briefs.length) throw new Error(`${f} includes ministers but ${mdir} has no briefs`);
    return { name: basename(f, '.md'), ...w, prompt: assemblePrompt(shared, w, briefs) };
  });
  const schedules = JSON.parse(readFileSync(need(join(gov, 'schedules.json')), 'utf8'));
  for (const s of schedules) {
    for (const k of ['name', 'worker', 'cron', 'message']) if (!s[k]) throw new Error(`schedules.json: ${s.name ?? '?'} needs ${k}`);
    if (!workers.some((w) => w.name === s.worker)) throw new Error(`schedules.json: ${s.name} names unknown worker ${s.worker}`);
  }
  return { workers, schedules };
}

export function makeClient(url, key, fetchImpl = fetch) {
  let id = 0;
  return async function call(name, args = {}) {
    const res = await fetchImpl(url, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${key}`,
        'Content-Type': 'application/json',
        Accept: 'application/json, text/event-stream',
        'X-Bob-Client': 'bob-sync',
      },
      body: JSON.stringify({ jsonrpc: '2.0', id: ++id, method: 'tools/call', params: { name, arguments: args } }),
    });
    const text = await res.text();
    if (!res.ok) throw new Error(`HTTP ${res.status} from ${name}: ${text.slice(0, 200)}`);
    const r = parseMcpReply(text);
    const t = r?.content?.[0]?.text;
    return t ? JSON.parse(t) : null;
  };
}

export async function fetchCurrent(call) {
  const list = (await call('worker_list')) ?? [];
  const workers = [];
  for (const w of list) workers.push(await call('worker_list', { name: w.name }));
  const schedules = (await call('schedule_list')) ?? [];
  return { workers, schedules };
}

function gitWhy(root, env) {
  try {
    const sha = (env.GITHUB_SHA || execFileSync('git', ['rev-parse', 'HEAD'], { cwd: root, encoding: 'utf8' })).trim().slice(0, 7);
    const subj = execFileSync('git', ['log', '-1', '--format=%s'], { cwd: root, encoding: 'utf8' }).trim();
    return `git ${sha}: ${subj}`;
  } catch { return 'git: sync-bob'; }
}

export async function main(argv, env = process.env, call = null) {
  const apply = argv.includes('--apply');
  const oi = argv.indexOf('--only');
  const only = oi >= 0 ? argv[oi + 1] : null;
  if (only && !['workers', 'schedules'].includes(only)) throw new Error('--only must be workers or schedules');
  const ri = argv.indexOf('--root');
  const root = ri >= 0 ? argv[ri + 1] : process.cwd();
  if (!call) {
    if (!env.BOB_MCP_KEY) throw new Error('BOB_MCP_KEY is not set');
    call = makeClient(env.BOB_URL || 'https://bob.box.badcode.tv/mcp', env.BOB_MCP_KEY);
  }
  const desired = loadDesired(root);
  const current = await fetchCurrent(call);
  let plan = planSync(desired, current);
  if (only) plan = plan.filter((p) => p.kind === only.slice(0, -1));
  const why = apply ? gitWhy(root, env) : '';
  let failed = 0;
  for (const p of plan) {
    const label = `${p.kind.padEnd(8)} ${p.name.padEnd(20)}`;
    if (p.op === 'extra') { console.log(`${label} extra (not touched)`); continue; }
    if (p.op === 'unchanged') { console.log(`${label} unchanged`); continue; }
    const detail = p.op === 'update' ? ` (${p.changed.join(', ')})` : '';
    if (!apply) { console.log(`${label} ${p.op}${detail}`); continue; }
    try {
      const tool = `${p.kind}_${p.op}`;
      await call(tool, p.kind === 'worker' ? { ...p.body, why } : p.body);
      console.log(`${label} ${p.op}d${detail}`);
    } catch (e) {
      failed++;
      console.error(`${label} ${p.op} FAILED: ${e.message}`);
    }
  }
  if (!apply) console.log('(dry run: nothing written; pass --apply)');
  return failed ? 1 : 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main(process.argv.slice(2)).then((c) => process.exit(c), (e) => { console.error(`sync-bob: ${e.message}`); process.exit(1); });
}
