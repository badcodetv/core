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

  it('drops a row with no alt (not a character card by openCharacterPage\'s own rule)', () => {
    const raw: RawCharacterRow[] = [
      { href: '/project/abc/character/aaaaaaaa-0000-0000-0000-000000000000' },
      { href: '/project/abc/character/bbbbbbbb-0000-0000-0000-000000000000', alt: '' },
    ]
    expect(parseCharacters(raw)).toEqual([])
  })

  it('drops a row whose href has no parseable /character/<id> segment', () => {
    const raw: RawCharacterRow[] = [{ href: '/project/abc/characters', alt: 'Karen' }]
    expect(parseCharacters(raw)).toEqual([])
  })

  it('returns an empty list for no rows', () => {
    expect(parseCharacters([])).toEqual([])
  })

  it('trims whitespace on href and alt before parsing', () => {
    const raw: RawCharacterRow[] = [
      { href: '  /project/abc/character/aaaaaaaa-0000-0000-0000-000000000000  ', alt: '  Karen  ' },
    ]
    expect(parseCharacters(raw)).toEqual([
      { name: 'Karen', id: 'aaaaaaaa-0000-0000-0000-000000000000' },
    ])
  })
})
