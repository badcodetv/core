import { describe, it, expect } from 'vitest'
import {
  batchOutPath,
  planBatch,
  emptyBatchAccumulator,
  finalizeBatch,
  foldBatchOutcome,
  shouldContinueAfterFailure,
} from './batch'

describe('batchOutPath', () => {
  it('zero-pads the index to 2 digits and uses .jpg', () => {
    expect(batchOutPath('/out', 0)).toBe('/out/00.jpg')
    expect(batchOutPath('/out', 7)).toBe('/out/07.jpg')
    expect(batchOutPath('/out', 12)).toBe('/out/12.jpg')
  })
  it('does not double a trailing slash', () => {
    expect(batchOutPath('/out/', 1)).toBe('/out/01.jpg')
  })
})

describe('shouldContinueAfterFailure', () => {
  it('continues past a policy block — prompt-specific, not a session problem', () => {
    expect(shouldContinueAfterFailure('POLICY_BLOCKED')).toBe(true)
  })
  it('stops on a timeout — likely a wedged session', () => {
    expect(shouldContinueAfterFailure('TIMEOUT')).toBe(false)
  })
  it('stops on any other error code (SUBMIT_FAILED, an unmapped message, …)', () => {
    expect(shouldContinueAfterFailure('SUBMIT_FAILED')).toBe(false)
    expect(shouldContinueAfterFailure('Target closed')).toBe(false)
  })
})

const item = (n: number) => ({ path: `/out/0${n}.jpg`, mediaId: `m${n}`, width: 1024, height: 1024 })

describe('foldBatchOutcome', () => {
  it('appends a success to items and signals continue', () => {
    const { acc, continue: cont } = foldBatchOutcome(emptyBatchAccumulator(), 0, 'p0', {
      ok: true,
      item: item(0),
    })
    expect(acc.items).toEqual([{ index: 0, prompt: 'p0', ...item(0) }])
    expect(acc.failed).toEqual([])
    expect(cont).toBe(true)
  })

  it('appends a POLICY_BLOCKED failure and signals continue', () => {
    const { acc, continue: cont } = foldBatchOutcome(emptyBatchAccumulator(), 3, 'p3 (names a real person)', {
      ok: false,
      code: 'POLICY_BLOCKED',
    })
    expect(acc.items).toEqual([])
    expect(acc.failed).toEqual([
      { index: 3, prompt: 'p3 (names a real person)', code: 'POLICY_BLOCKED', error: 'POLICY_BLOCKED' },
    ])
    expect(cont).toBe(true)
  })

  it('appends a non-blocked failure and signals stop', () => {
    const { acc, continue: cont } = foldBatchOutcome(emptyBatchAccumulator(), 4, 'p4', {
      ok: false,
      code: 'TIMEOUT',
    })
    expect(acc.failed).toEqual([{ index: 4, prompt: 'p4', code: 'TIMEOUT', error: 'TIMEOUT' }])
    expect(cont).toBe(false)
  })

  it('threads the accumulator across multiple folds, preserving order', () => {
    let acc = emptyBatchAccumulator()
    ;({ acc } = foldBatchOutcome(acc, 0, 'p0', { ok: true, item: item(0) }))
    ;({ acc } = foldBatchOutcome(acc, 1, 'p1', { ok: false, code: 'POLICY_BLOCKED' }))
    ;({ acc } = foldBatchOutcome(acc, 2, 'p2', { ok: true, item: item(2) }))
    expect(acc.items.map((i) => i.index)).toEqual([0, 2])
    expect(acc.failed.map((f) => f.index)).toEqual([1])
    // Invariant generateBatch relies on to compute a resume index: every attempted prompt
    // lands in exactly one of the two arrays, so their combined length is the count attempted.
    expect(acc.items.length + acc.failed.length).toBe(3)
  })
})

describe('finalizeBatch', () => {
  it('partial is false when nothing failed', () => {
    const acc = emptyBatchAccumulator()
    const { acc: withItem } = foldBatchOutcome(acc, 0, 'p0', { ok: true, item: item(0) })
    expect(finalizeBatch(withItem)).toEqual({ items: withItem.items, failed: [], partial: false })
  })

  it('partial is true whenever failed is non-empty, even if items is too', () => {
    let acc = emptyBatchAccumulator()
    ;({ acc } = foldBatchOutcome(acc, 0, 'p0', { ok: true, item: item(0) }))
    ;({ acc } = foldBatchOutcome(acc, 1, 'p1', { ok: false, code: 'POLICY_BLOCKED' }))
    const result = finalizeBatch(acc)
    expect(result.partial).toBe(true)
    expect(result.items).toHaveLength(1)
    expect(result.failed).toHaveLength(1)
  })
})

describe('planBatch', () => {
  const prompts = ['a', 'b', 'c']

  it('plans every prompt when nothing exists yet', () => {
    const plan = planBatch(prompts, '/out', () => false)
    expect(plan.map((p) => p.skip)).toEqual([false, false, false])
    expect(plan.map((p) => p.path)).toEqual(['/out/00.jpg', '/out/01.jpg', '/out/02.jpg'])
  })

  it('skips exactly the prompts whose file is already on disk', () => {
    // The resume case: a run that died after two images picks up at the third.
    const done = new Set(['/out/00.jpg', '/out/01.jpg'])
    const plan = planBatch(prompts, '/out', (p) => done.has(p))
    expect(plan.map((p) => p.skip)).toEqual([true, true, false])
  })

  it('regenerates a hole in the middle, not just the tail', () => {
    // Deleting one bad image and re-running must regenerate that one and leave the rest.
    const done = new Set(['/out/00.jpg', '/out/02.jpg'])
    const plan = planBatch(prompts, '/out', (p) => done.has(p))
    expect(plan.map((p) => p.skip)).toEqual([true, false, true])
  })

  it('keeps index aligned with the prompt list even when skipping', () => {
    // Index is what maps an image back to its prompt; a resumed run that renumbered would
    // silently pair prompts with the wrong pictures.
    const plan = planBatch(prompts, '/out', (p) => p.endsWith('00.jpg'))
    expect(plan.map((p) => [p.index, p.prompt])).toEqual([[0, 'a'], [1, 'b'], [2, 'c']])
  })
})
