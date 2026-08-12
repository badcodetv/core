import { describe, it, expect } from 'vitest'
import { parseMediaOptions, type RawMediaOption } from './media-list'

const IMG_SRC = (uuid: string) =>
  `https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=${uuid}`

describe('parseMediaOptions', () => {
  it('recovers the title from a doubled accessible name when there is no alt', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'Man in suit holding papers Man in suit holding papers Image' },
    ]
    expect(parseMediaOptions(raw)).toEqual([
      { title: 'Man in suit holding papers', kind: 'Image', index: 0 },
    ])
  })

  it('recovers a filename-style doubled title with no spaces to split on', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName:
          'keynes-portrait-pro-b.jpg keynes-portrait-pro-b.jpg Image',
      },
    ]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'keynes-portrait-pro-b.jpg',
      kind: 'Image',
    })
  })

  it('handles a truncated (ellipsis) doubled title without assuming equal-length halves via naive midpoint slicing', () => {
    // Both copies are truncated identically to the same shorter string — the regression
    // this guards is a Math.floor(length/2) split, which happens to work here too since the
    // halves ARE equal length, but the point is the algorithm never assumes that; it only
    // requires the two captured halves be textually identical.
    const raw: RawMediaOption[] = [
      {
        accessibleName:
          'Modifying facial features and ap… Modifying facial features and ap… Image',
      },
    ]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'Modifying facial features and ap…',
      kind: 'Image',
    })
  })

  it('prefers alt over the doubled-name split when alt is present', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man in suit holding papers Man in suit holding papers Image',
        alt: 'Man in suit holding papers',
      },
    ]
    expect(parseMediaOptions(raw)[0]!.title).toBe('Man in suit holding papers')
  })

  it('trusts alt even when it disagrees with the doubled-name text (alt is the reliable source)', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Untitled Untitled Image',
        alt: 'A more descriptive caption Flow filled in later',
      },
    ]
    expect(parseMediaOptions(raw)[0]!.title).toBe(
      'A more descriptive caption Flow filled in later',
    )
  })

  it('classifies kind from the trailing label', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'A quiet street at dusk A quiet street at dusk Video' },
    ]
    expect(parseMediaOptions(raw)[0]!.kind).toBe('Video')
  })

  it('defaults sensibly when the accessible name is empty', () => {
    const raw: RawMediaOption[] = [{ accessibleName: '' }]
    expect(parseMediaOptions(raw)[0]).toEqual({ title: '', kind: 'Unknown', index: 0 })
  })

  it('falls back to the raw (undoubled) rest when the halves are not textually identical', () => {
    // Malformed / unexpected input — the split simply fails closed rather than throwing or
    // guessing a wrong midpoint.
    const raw: RawMediaOption[] = [{ accessibleName: 'Alpha Bravo Image' }]
    expect(parseMediaOptions(raw)[0]!.title).toBe('Alpha Bravo')
  })

  it('extracts mediaId from a getMediaUrlRedirect src via the shared media-url helpers', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man in suit holding papers Man in suit holding papers Image',
        src: IMG_SRC('71ef7331-65aa-4e13-84cc-6e3a3e37fa45'),
      },
    ]
    expect(parseMediaOptions(raw)[0]!.mediaId).toBe('71ef7331-65aa-4e13-84cc-6e3a3e37fa45')
  })

  it('omits mediaId when src is absent or not a media redirect URL', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'A A Image' },
      { accessibleName: 'B B Image', src: 'https://example.com/thumb.png' },
    ]
    const items = parseMediaOptions(raw)
    expect(items[0]!.mediaId).toBeUndefined()
    expect(items[1]!.mediaId).toBeUndefined()
  })

  it('preserves gallery order and keeps duplicate titles as separate, indexed entries', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man in suit holding papers Man in suit holding papers Image',
        src: IMG_SRC('uuid-1'),
      },
      {
        accessibleName: 'Man in suit holding papers Man in suit holding papers Image',
        src: IMG_SRC('uuid-2'),
      },
      { accessibleName: 'A quiet street at dusk A quiet street at dusk Video' },
    ]
    const items = parseMediaOptions(raw)
    expect(items).toHaveLength(3)
    expect(items.map((i) => i.title)).toEqual([
      'Man in suit holding papers',
      'Man in suit holding papers',
      'A quiet street at dusk',
    ])
    expect(items.map((i) => i.index)).toEqual([0, 1, 2])
    expect(items[0]!.mediaId).toBe('uuid-1')
    expect(items[1]!.mediaId).toBe('uuid-2')
  })
})
