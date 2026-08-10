import { describe, expect, it } from 'vitest'
import { resolveCoin } from './coins'
import { homeSteps } from '../home/timeline'

describe('resolveCoin', () => {
  it('resolves enc to a live component', () => {
    const r = resolveCoin('enc')
    expect(r.kind).toBe('live')
    // Lazy components are objects, not functions — asserting `typeof === function`
    // here would pass for the eager comics registry and fail for this one.
    if (r.kind === 'live') expect(r.Component).toBeTruthy()
  })

  it('takes its title from the timeline, so titles live in one place', () => {
    const r = resolveCoin('enc')
    if (r.kind === 'live') expect(r.title).toContain('Emperor')
  })

  it('resolves an unknown slug to not-found', () => {
    expect(resolveCoin('does-not-exist').kind).toBe('not-found')
  })
})

describe('the timeline node for enc', () => {
  it('points at the coin route, not the old comic one', () => {
    const node = homeSteps.find((n) => n.id === 'emperors-coin')
    expect(node?.route).toBe('/coins/enc')
  })

  it('is reachable even while the node is still coming-soon', () => {
    // Status governs how the homepage presents it, not whether the route works —
    // otherwise the page would be unreachable for the weeks it is being built.
    const node = homeSteps.find((n) => n.id === 'emperors-coin')
    expect(node?.status).toBe('coming-soon')
    expect(resolveCoin('enc').kind).toBe('live')
  })
})
