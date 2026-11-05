import { describe, it, expect } from 'vitest';
import { parseWorkerFile, assemblePrompt, planSync, parseMcpReply } from './sync-bob.mjs';

const FILE = `---
engine: claude
model: claude-opus-5-5
effort: high
labels: role=cabinet, tier=1
include: ministers
---
You are the cabinet.
`;

describe('parseWorkerFile', () => {
  it('parses a good file', () => {
    const w = parseWorkerFile(FILE);
    expect(w).toMatchObject({ engine: 'claude', model: 'claude-opus-5-5', effort: 'high', include: 'ministers', tools: [] });
    expect(w.prompt).toBe('You are the cabinet.');
  });
  it('parses labels', () => {
    expect(parseWorkerFile(FILE).labels).toEqual({ role: 'cabinet', tier: '1' });
  });
  it('parses include and tools', () => {
    const w = parseWorkerFile('---\nengine: claude\ntools: Read, Grep\n---\nx');
    expect(w.include).toBeNull();
    expect(w.tools).toEqual(['Read', 'Grep']);
  });
  it('rejects unknown keys', () => {
    expect(() => parseWorkerFile('---\nengine: claude\nflavour: x\n---\nx')).toThrow(/unknown/);
  });
  it('rejects missing engine', () => {
    expect(() => parseWorkerFile('---\nmodel: m\n---\nx')).toThrow(/engine/);
  });
});

describe('assemblePrompt', () => {
  it('joins shared and body', () => {
    expect(assemblePrompt('SHARED\n', { prompt: 'BODY', include: null })).toBe('SHARED\n\nBODY');
  });
  it('appends ministers in order', () => {
    const p = assemblePrompt('S', { prompt: 'B', include: 'ministers' }, ['### A (a)\nx\n', '### B (b)\ny']);
    expect(p).toBe('S\n\nB\n\n## The ministers\n\n### A (a)\nx\n\n### B (b)\ny');
  });
});

const dw = (o = {}) => ({ name: 'w', engine: 'claude', model: 'm', effort: 'high', labels: { a: 'b' }, tools: [], prompt: 'P', ...o });
const cw = (o = {}) => ({ id: 'x', created_at: 't', name: 'w', engine: 'claude', model: 'm', effort: 'high', labels: { a: 'b' }, prompt: 'P', ...o });
const op = (d, c) => planSync({ workers: d, schedules: [] }, { workers: c, schedules: [] });

describe('planSync', () => {
  it('creates', () => expect(op([dw()], [])[0].op).toBe('create'));
  it('unchanged, absent tools equals []', () => expect(op([dw()], [cw()])[0].op).toBe('unchanged'));
  it('updates on prompt change', () => expect(op([dw({ prompt: 'Q' })], [cw()])[0].op).toBe('update'));
  it('updates when only a minister brief changed', () => {
    const mk = (b) => dw({ prompt: assemblePrompt('S', { prompt: 'B', include: 'ministers' }, [b]) });
    const cur = cw({ prompt: assemblePrompt('S', { prompt: 'B', include: 'ministers' }, ['old']) });
    expect(op([mk('new')], [cur])[0].op).toBe('update');
  });
  it('updates on shared.md change', () => {
    const mk = (s) => dw({ prompt: assemblePrompt(s, { prompt: 'B', include: null }) });
    const cur = cw({ prompt: assemblePrompt('S1', { prompt: 'B', include: null }) });
    expect(op([mk('S2')], [cur])[0].op).toBe('update');
  });
  it('updates on label change', () => expect(op([dw({ labels: { a: 'c' } })], [cw()])[0].op).toBe('update'));
  it('update body has every field', () => {
    const p = op([dw({ prompt: 'Q' })], [cw()])[0];
    expect(Object.keys(p.body).sort()).toEqual(['effort', 'engine', 'labels', 'model', 'name', 'prompt', 'tools']);
  });
  it('reports extras, never deletes', () => {
    const plan = op([], [cw({ name: 'old' })]);
    expect(plan).toEqual([{ kind: 'worker', name: 'old', op: 'extra', body: null }]);
  });
  it('compares schedules, ignoring server fields', () => {
    const d = { name: 's', worker: 'w', cron: '0 5 * * *', timezone: 'Europe/London', keep_sessions: 14, enabled: false, message: 'm' };
    const c = { ...d, id: 'i', next_at: 'n', last_run: null, created_at: 't', changed_at: 't', worker_id: 'z', project: 'p' };
    const run = (cc) => planSync({ workers: [], schedules: [d] }, { workers: [], schedules: [cc] })[0].op;
    expect(run(c)).toBe('unchanged');
    expect(run({ ...c, cron: '0 6 * * *' })).toBe('update');
    expect(planSync({ workers: [], schedules: [d] }, { workers: [], schedules: [] })[0].op).toBe('create');
  });
});

const reply = (r) => JSON.stringify({ jsonrpc: '2.0', id: 1, ...r });
describe('parseMcpReply', () => {
  it('returns the result', () => {
    const r = parseMcpReply(reply({ result: { content: [{ type: 'text', text: '[]' }] } }));
    expect(r.content[0].text).toBe('[]');
  });
  it('throws on top-level error', () => {
    expect(() => parseMcpReply(reply({ error: { code: -1, message: 'nope' } }))).toThrow(/nope/);
  });
  it('throws on isError', () => {
    expect(() => parseMcpReply(reply({ result: { isError: true, content: [{ type: 'text', text: 'bad' }] } }))).toThrow(/bad/);
  });
  it('reads an SSE data line', () => {
    const r = parseMcpReply('event: message\ndata: ' + reply({ result: { content: [] } }) + '\n\n');
    expect(r.content).toEqual([]);
  });
});
