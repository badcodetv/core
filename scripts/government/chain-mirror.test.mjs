import { describe, it, expect } from 'vitest';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { buildPlan, planPolicy, sha256, canonicalRule, parseFlatFrontMatter } from './chain-mirror.mjs';

const policy = (extra = '') => `---
id: chancellor/the-slice
title: The Slice
check.claim: At least one new zone by mid-2027.
check.prior: 0.6
check.rule: Count zones. One or more: held.
check.source: The gov.uk AI Growth Zones page
check.source_url: https://www.gov.uk/ai-growth-zones
check.if_revised: First publication counts.
check.check_on: 2027-07-01
check.result: pending
${extra}---
Body.
`;
const uriFor = f => `https://raw.example/abc/${f}`;

describe('planPolicy', () => {
  it('posts a new policy and its gated prediction', () => {
    const [p, pred] = planPolicy({ id: 'chancellor/the-slice', file: 'x.md', text: policy() }, { uriFor });
    expect(p).toMatchObject({ op: 'post_policy', parent: null, content_hash: sha256(policy()), uri: 'https://raw.example/abc/x.md' });
    expect(pred).toMatchObject({ op: 'post_prediction', prior_bps: 6000, source_uri: 'https://www.gov.uk/ai-growth-zones',
      check_at: Date.parse('2027-07-01T00:00:00Z') / 1000 });
  });

  it('links a changed policy to the version it last posted, and skips an unchanged one', () => {
    const state = { 'chancellor/the-slice': { hash: 'old', account: 'Prev111' } };
    expect(planPolicy({ id: 'chancellor/the-slice', file: 'x.md', text: policy() }, { uriFor, state })[0])
      .toMatchObject({ op: 'post_policy', parent: 'Prev111' });
    const same = { 'chancellor/the-slice': { hash: sha256(policy()), account: 'Prev111' } };
    expect(planPolicy({ id: 'chancellor/the-slice', file: 'x.md', text: policy() }, { uriFor, state: same })[0].op).toBe('unchanged');
  });

  it('never posts a provisional check: a posted prediction cannot be withdrawn', () => {
    const [, pred] = planPolicy({ id: 'a/b', file: 'x.md', text: policy('check.provisional: yes\n') }, { uriFor });
    expect(pred.op).toBe('blocked');
    expect(pred.reason).toMatch(/provisional/);
  });

  it('blocks a check whose source is prose with no URL', () => {
    const text = policy().replace('check.source_url: https://www.gov.uk/ai-growth-zones\n', '');
    expect(planPolicy({ id: 'a/b', file: 'x.md', text }, { uriFor })[1]).toMatchObject({ op: 'blocked', reason: expect.stringMatching(/source URL/) });
  });

  it('freezes the rule without the result, so marking it in git does not change its hash', () => {
    const resolved = policy().replace('check.result: pending', 'check.result: held');
    expect(canonicalRule(parseFlatFrontMatter(resolved))).toBe(canonicalRule(parseFlatFrontMatter(policy())));
  });
});

describe('buildPlan', () => {
  it('walks policies and debates and sends nothing', () => {
    const root = mkdtempSync(join(tmpdir(), 'mirror-'));
    mkdirSync(join(root, 'docs/government/policies/chancellor'), { recursive: true });
    mkdirSync(join(root, 'docs/government/debates/chancellor'), { recursive: true });
    writeFileSync(join(root, 'docs/government/policies/chancellor/the-slice.md'), policy());
    writeFileSync(join(root, 'docs/government/policies/README.md'), '# not a policy');
    writeFileSync(join(root, 'docs/government/debates/chancellor/the-slice.md'), '# debate');
    const plan = buildPlan({ root, commit: 'abc', rawBase: 'https://raw.example', resolver: 'Stat111' });
    expect(plan.map(s => s.op)).toEqual(['post_policy', 'post_prediction', 'post_argument']);
    expect(plan[1].resolver).toBe('Stat111');
    expect(plan[2]).toMatchObject({ stance: 'neutral', id: 'chancellor/the-slice' });
  });

  it('has no send path in the source', () => {
    const src = readFileSync(new URL('./chain-mirror.mjs', import.meta.url), 'utf8');
    expect(src).not.toMatch(/@solana|@coral-xyz|sendTransaction|Keypair|\.rpc\(/);
  });
});
