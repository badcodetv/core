import { describe, it, expect } from 'vitest'
import { parseCharacters, type RawCharacterRow } from './character-list'

describe('parseCharacters', () => {
  it('parses a normal row, deriving id from the href', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc-123/character/71ef7331-65aa-4e13-84cc-6e3a3e37fa45', alt: 'Karen' },
    ]
    expect(parseCharacters(raw)).toEqual([
      { name: 'Karen', id: '71ef7331-65aa-4e13-84cc-6e3a3e37fa45' },
    ])
  })

  it('preserves card order across multiple characters', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000', alt: 'Karen' },
      { href: '/project/abc/character/bbbbbbbb-0000-0000-0000-000000000000', alt: 'Sean' },
    ]
    expect(parseCharacters(raw).map((c) => c.name)).toEqual(['Karen', 'Sean'])
  })

  it('drops a row with no href (id is unrecoverable)', () => {
    const raw: RawCharacterRow[] = [{ alt: 'Karen' }, { href: '', alt: 'Sean' }]
    expect(parseCharacters(raw)).toEqual([])
  })

  // Live 2026-08-12: a project showing THREE characters returned one, because the two without
  // a generated portrait render an avatar placeholder and carry no <img> at all. Requiring an
  // alt hid exactly the half-finished characters a caller most wants to find.
  it('keeps a portrait-less row, naming it from the visible caption', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000', label: 'Untitled Character' },
    ]
    expect(parseCharacters(raw)).toEqual([
      { name: 'Untitled Character', id: 'aaaaaaaa-0000-0000-0000-000000000000' },
    ])
  })

  it('prefers the visible caption over the img alt when both are present', () => {
    const raw: RawCharacterRow[] = [
      {
        href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000',
        alt: 'stale alt',
        label: 'Untitled Character',
      },
    ]
    expect(parseCharacters(raw)[0]!.name).toBe('Untitled Character')
  })

  it('falls back to the img alt when there is no caption', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000', alt: 'Karen', label: '' },
    ]
    expect(parseCharacters(raw)[0]!.name).toBe('Karen')
  })

  // The id is the only unambiguous handle, so a nameless row is still worth returning.
  it('keeps a row with an id but no recoverable name', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000' },
    ]
    expect(parseCharacters(raw)).toEqual([
      { name: '', id: 'aaaaaaaa-0000-0000-0000-000000000000' },
    ])
  })

  // Flow does not enforce unique character names; three "Untitled Character" cards in one
  // project is a real, observed state. Nothing here may collapse them.
  it('keeps every same-named character as its own row', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000', label: 'Untitled Character' },
      { href: '/project/abc/character/bbbbbbbb-0000-0000-0000-000000000000', label: 'Untitled Character' },
      { href: '/project/abc/character/cccccccc-0000-0000-0000-000000000000', label: 'Untitled Character' },
    ]
    const out = parseCharacters(raw)
    expect(out).toHaveLength(3)
    expect(new Set(out.map(c => c.id)).size).toBe(3)
  })

  it('drops a row whose href has no parseable /character/<id> segment', () => {
    const raw: RawCharacterRow[] = [{ href: '/project/abc/characters', alt: 'Karen' }]
    expect(parseCharacters(raw)).toEqual([])
  })

  it('returns an empty list for no rows', () => {
    expect(parseCharacters([])).toEqual([])
  })

  it('trims whitespace on href and name before parsing', () => {
    const raw: RawCharacterRow[] = [
      { href: '  /project/abc/character/aaaaaaaa-0000-0000-0000-000000000000  ', alt: '  Karen  ' },
    ]
    expect(parseCharacters(raw)).toEqual([
      { name: 'Karen', id: 'aaaaaaaa-0000-0000-0000-000000000000' },
    ])
  })
})
