import { describe, it, expect } from 'vitest'
import { pickProject, projectIdFromHref, toProjectSummaries, type ProjectTile } from './project'

const tiles: ProjectTile[] = [
  { name: 'camping-v2', href: '/fx/tools/flow/project/aaa' },
  { name: 'Magic Money Tree', href: '/fx/tools/flow/project/bbb' },
  { name: 'camping-v2', href: '/fx/tools/flow/project/ccc' }, // older dup
]

describe('pickProject', () => {
  it('returns the href of the first exact name match', () => {
    expect(pickProject(tiles, 'camping-v2')).toBe('/fx/tools/flow/project/aaa')
  })
  it('is case-insensitive and trims', () => {
    expect(pickProject(tiles, '  CAMPING-V2 ')).toBe('/fx/tools/flow/project/aaa')
  })
  it('returns null when no tile matches', () => {
    expect(pickProject(tiles, 'nope')).toBeNull()
  })
  it('returns null for an empty list', () => {
    expect(pickProject([], 'camping-v2')).toBeNull()
  })
  it('does not throw on an href-less tile (returns null if no other tile matches)', () => {
    const hrefless: ProjectTile[] = [{ name: 'ghost-project' }]
    expect(pickProject(hrefless, 'ghost-project')).toBeNull()
  })
})

describe('projectIdFromHref', () => {
  it('extracts the id from a relative href', () => {
    expect(projectIdFromHref('/fx/tools/flow/project/aaa')).toBe('aaa')
  })
  it('extracts the id from an absolute href with a trailing slash', () => {
    expect(projectIdFromHref('https://labs.google/fx/tools/flow/project/bbb/')).toBe('bbb')
  })
  it('extracts the id from a href with a trailing query string', () => {
    expect(projectIdFromHref('/fx/tools/flow/project/ccc?tab=media')).toBe('ccc')
  })
  it('returns undefined for undefined', () => {
    expect(projectIdFromHref(undefined)).toBeUndefined()
  })
  it('returns undefined for an empty string', () => {
    expect(projectIdFromHref('')).toBeUndefined()
  })
  it('returns undefined for a href with no /project/ segment', () => {
    expect(projectIdFromHref('/fx/tools/flow')).toBeUndefined()
  })
})

describe('toProjectSummaries', () => {
  it('maps an anchor-backed tile to name + id + href', () => {
    expect(toProjectSummaries([{ name: 'camping-v2', href: '/fx/tools/flow/project/aaa' }])).toEqual([
      { name: 'camping-v2', id: 'aaa', href: '/fx/tools/flow/project/aaa' },
    ])
  })
  it('handles the documented href-less tile case: name only, id and href omitted, no throw', () => {
    expect(() => toProjectSummaries([{ name: 'ghost-project' }])).not.toThrow()
    expect(toProjectSummaries([{ name: 'ghost-project' }])).toEqual([{ name: 'ghost-project' }])
  })
  it('handles a mixed list without losing the href-less entry', () => {
    const mixed: ProjectTile[] = [
      { name: 'camping-v2', href: '/fx/tools/flow/project/aaa' },
      { name: 'ghost-project' },
    ]
    expect(toProjectSummaries(mixed)).toEqual([
      { name: 'camping-v2', id: 'aaa', href: '/fx/tools/flow/project/aaa' },
      { name: 'ghost-project' },
    ])
  })
  it('omits id for a malformed href but keeps the href and name', () => {
    expect(toProjectSummaries([{ name: 'weird', href: '/fx/tools/flow' }])).toEqual([
      { name: 'weird', href: '/fx/tools/flow' },
    ])
  })
})
