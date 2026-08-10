import { describe, it, expect } from 'vitest'
import { resolveComic } from './comics'

describe('resolveComic', () => {
  it('resolves a live comic to a component', () => {
    const r = resolveComic('camping')
    expect(r.kind).toBe('live')
    if (r.kind === 'live') expect(typeof r.Component).toBe('function')
  })

  it('resolves a known coming-soon comic to a stub with its title', () => {
    const r = resolveComic('optimistic-lens')
    expect(r.kind).toBe('stub')
    if (r.kind === 'stub') expect(r.title).toContain('Optimistic')
  })

  it('no longer treats emperors-coin as a comic — it is a coin at /coins/enc', () => {
    // Canon moved it from a comic to a cryptocurrency; the timeline node now
    // points at /coins/enc, so the comic resolver must not claim it.
    expect(resolveComic('emperors-coin').kind).toBe('not-found')
  })

  it('resolves an unknown slug to not-found', () => {
    expect(resolveComic('does-not-exist').kind).toBe('not-found')
  })

  it('resolves the second shipped comic (karen) to a live component', () => {
    const r = resolveComic('karen')
    expect(r.kind).toBe('live')
    if (r.kind === 'live') expect(typeof r.Component).toBe('function')
  })
})
