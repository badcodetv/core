import { describe, it, expect } from 'vitest';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { lintPolicies, policyText } from '../../apps/site/policies.mjs';
import { lintAll } from './policy-lint.mjs';

const good = (over = {}) => ({
  file: 'chancellor/the-slice.md', dirPost: 'chancellor', slug: 'the-slice', body: 'The wrong. A town.',
  needs: [], leavesOut: ['x'],
  meta: {
    id: 'chancellor/the-slice', title: 'The Slice', line: 'Public money, public slice.', owner: 'chancellor',
    status: 'draft', kind: 'trial', band: 'medium', stop: 'three years, then a vote',
    'test.where': 'next data centre', 'test.against': 'deals without', 'test.measure': 'investment per pound',
    'test.by': '2029', fails_if: 'a fifth less (provisional)', leaves_out: 'profit abroad', signs: 'the Chancellor',
    'check.claim': 'c', 'check.prior': '0.7', 'check.rule': 'r', 'check.source': 's', 'check.if_revised': 'first figure',
    'check.check_on': '2027-01-31', 'check.result': 'pending', ...over,
  },
});
const run = (ps, today = '2026-11-11') => lintPolicies(Array.isArray(ps) ? ps : [ps], { today });

describe('policy lint', () => {
  it('passes a complete policy', () => {
    const r = run(good());
    expect(r.errors).toEqual([]);
    expect(r.notReady.size).toBe(0);
  });
  it('marks an incomplete draft Not ready instead of failing', () => {
    const r = run(good({ fails_if: '' }));
    expect(r.errors).toEqual([]);
    expect(r.notReady.get('chancellor/the-slice')).toEqual(['fails_if']);
  });
  it('fails an incomplete policy that is not a draft', () => {
    expect(run(good({ status: 'kept', fails_if: '' })).errors[0]).toMatch(/not ready/);
  });
  it('refuses safe bets', () => {
    expect(run(good({ 'check.prior': '0.95' })).errors[0]).toMatch(/no safe bets/);
  });
  it('lets only a right have no stop date', () => {
    expect(run(good({ stop: 'never' })).errors[0]).toMatch(/only a right/);
    const right = good({ kind: 'right', stop: 'never', measure: 'appeals heard on time' });
    expect(run(right).errors).toEqual([]);
  });
  it('checks ownership, dependencies and jargon', () => {
    expect(run(good({ owner: 'home' })).errors.join()).toMatch(/owner/);
    expect(run({ ...good(), needs: ['home/nothing'] }).errors.join()).toMatch(/does not exist/);
    expect(run({ ...good(), body: 'Continuous integration for laws.' }).errors.join()).toMatch(/jargon/);
  });
  it('needs a note on a resolved check and warns on an overdue one', () => {
    expect(run(good({ 'check.result': 'held' })).errors.join()).toMatch(/check.note/);
    expect(run(good(), '2027-03-01').warnings.join()).toMatch(/still pending/);
  });
  it('warns when a post has nothing due within six months', () => {
    expect(run(good({ 'check.check_on': '2029-01-01' })).warnings.join()).toMatch(/six months/);
  });
});

describe('policy text', () => {
  it('prints the contract and the prediction in plain labelled lines', () => {
    const t = policyText(good());
    expect(t).toMatch(/^## The Slice/);
    expect(t).toMatch(/The test\. next data centre, against deals without/);
    expect(t).toMatch(/Our odds: 70%\. Checked on 2027-01-31: not checked yet\./);
    expect(t).toMatch(/Status: Draft\./);
    expect(policyText(good(), ['fails_if'])).toMatch(/Status: Draft, not ready\./);
    expect(policyText(good({ against: 'Too slow.', answer: 'Slow beats wrong.' }))).toMatch(/The best case against: Too slow\. Our answer: Slow beats wrong\./);
  });
});

describe('the repository', () => {
  it('has no policy errors', () => {
    const root = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
    expect(lintAll(root).errors).toEqual([]);
  });
});
