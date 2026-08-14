import { describe, it, expect } from 'vitest'
import {
  attachedWrongSource,
  toAnimateTiles,
  pickNewTileIndex,
  chooseAnimateTarget,
  type AnimateTile,
  type RawAnimateTile,
} from './animate-target'

const SRC = (uuid: string) =>
  `https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=${uuid}`

describe('toAnimateTiles', () => {
  it('resolves media names from getMediaUrlRedirect srcs, preserving DOM order', () => {
    const raw: RawAnimateTile[] = [{ src: SRC('uuid-a') }, { src: SRC('uuid-b') }]
    expect(toAnimateTiles(raw)).toEqual([
      { index: 0, name: 'uuid-a' },
      { index: 1, name: 'uuid-b' },
    ])
  })

  it('leaves name null for a src that has not resolved yet', () => {
    const raw: RawAnimateTile[] = [{ src: '' }, { src: 'data:image/png;base64,abc' }]
    expect(toAnimateTiles(raw)).toEqual([
      { index: 0, name: null },
      { index: 1, name: null },
    ])
  })
})

describe('pickNewTileIndex', () => {
  it('identifies the single tile whose name is new', () => {
    const before: AnimateTile[] = [{ index: 0, name: 'old-1' }]
    const after: AnimateTile[] = [
      { index: 0, name: 'old-1' },
      { index: 1, name: 'new-upload' },
    ]
    expect(pickNewTileIndex(before, after)).toBe(1)
  })

  it('is null when nothing new has landed yet (upload still in flight)', () => {
    const before: AnimateTile[] = [{ index: 0, name: 'old-1' }]
    const after: AnimateTile[] = [{ index: 0, name: 'old-1' }]
    expect(pickNewTileIndex(before, after)).toBeNull()
  })

  it('is null (never guesses) when two tiles are new at once', () => {
    // e.g. a race: something else landed in the project at the same moment as our upload.
    const before: AnimateTile[] = []
    const after: AnimateTile[] = [
      { index: 0, name: 'new-1' },
      { index: 1, name: 'new-2' },
    ]
    expect(pickNewTileIndex(before, after)).toBeNull()
  })

  it('ignores tiles whose name has not resolved (null) on either side', () => {
    const before: AnimateTile[] = [{ index: 0, name: null }]
    const after: AnimateTile[] = [
      { index: 0, name: null },
      { index: 1, name: 'resolved-upload' },
    ]
    expect(pickNewTileIndex(before, after)).toBe(1)
  })

  it('does not treat an unresolved (null) tile itself as a new candidate', () => {
    const before: AnimateTile[] = []
    const after: AnimateTile[] = [{ index: 0, name: null }]
    expect(pickNewTileIndex(before, after)).toBeNull()
  })

  it('handles an empty before snapshot (first upload into a fresh project)', () => {
    const before: AnimateTile[] = []
    const after: AnimateTile[] = [{ index: 0, name: 'only-upload' }]
    expect(pickNewTileIndex(before, after)).toBe(0)
  })
})

describe('chooseAnimateTarget', () => {
  it('prefers the name-diff result when it is unambiguous', () => {
    const before: AnimateTile[] = [{ index: 0, name: 'old-1' }]
    const after: AnimateTile[] = [
      { index: 0, name: 'old-1' },
      { index: 1, name: 'new-upload' },
    ]
    expect(chooseAnimateTarget(before, after)).toBe(1)
  })

  it('falls back to the sole tile when the diff cannot confirm it by name (fresh/near-empty project)', () => {
    // The uploaded still's src has not resolved to a getMediaUrlRedirect URL on this tick, so
    // pickNewTileIndex sees no new NAME — but it is the only tile on the page at all, so there
    // is no other candidate it could be.
    const before: AnimateTile[] = []
    const after: AnimateTile[] = [{ index: 0, name: null }]
    expect(chooseAnimateTarget(before, after)).toBe(0)
  })

  it('does NOT fall back when the project holds more than one tile and the diff is ambiguous', () => {
    // A cluttered project: two tiles present, name-diff inconclusive (e.g. neither resolved
    // yet) — picking either would risk animating the wrong still, so this must fail closed,
    // not guess index 0.
    const before: AnimateTile[] = [{ index: 0, name: 'old-1' }]
    const after: AnimateTile[] = [
      { index: 0, name: 'old-1' },
      { index: 1, name: null },
    ]
    expect(chooseAnimateTarget(before, after)).toBeNull()
  })

  it('is null when there are zero tiles at all', () => {
    expect(chooseAnimateTarget([], [])).toBeNull()
  })
})

describe('attachedWrongSource', () => {
  const TARGET = 'aaaa-1111'
  const STALE = 'ffff-9999'

  it('ignores a stale chip left over from an earlier turn', () => {
    // Live 2026-08-12: two chips were attached at once, the older scrolled off-screen at
    // y=-464. Reading "the first chip" flagged a CORRECT attach as wrong.
    expect(attachedWrongSource([STALE], [STALE, TARGET], TARGET)).toBe(false)
  })

  it('flags a genuinely wrong attach', () => {
    expect(attachedWrongSource([STALE], [STALE, 'bbbb-2222'], TARGET)).toBe(true)
  })

  it('says nothing when no new chip appeared — it cannot tell, so it must not block', () => {
    expect(attachedWrongSource([STALE], [STALE], TARGET)).toBe(false)
    expect(attachedWrongSource([], [], TARGET)).toBe(false)
  })

  it('handles a first-ever attach with no prior chips', () => {
    expect(attachedWrongSource([], [TARGET], TARGET)).toBe(false)
    expect(attachedWrongSource([], ['bbbb-2222'], TARGET)).toBe(true)
  })

  it('counts by multiset, so re-attaching the same media reads as new', () => {
    expect(attachedWrongSource([TARGET], [TARGET, TARGET], TARGET)).toBe(false)
    expect(attachedWrongSource([TARGET], [TARGET, 'bbbb-2222'], TARGET)).toBe(true)
  })
})
