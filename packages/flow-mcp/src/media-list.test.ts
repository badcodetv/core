import { describe, it, expect } from 'vitest'
import { parseMediaOptions, type RawMediaOption } from './media-list'

const IMG_SRC = (uuid: string) =>
  `https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=${uuid}`

// Every accessible-name string below was captured from a live Flow asset picker on
// 2026-08-12 (magic-money-tree-story). The suite this replaced was written against an
// INVENTED "doubled title" shape ("T T Image") that Flow has never produced; it passed
// completely while the real parser put "papersImage" and "CharacterCharacter" in `kind` for
// every single row. Prefer adding observed strings here over plausible ones.
describe('parseMediaOptions', () => {
  it('splits title from the kind suffix concatenated onto it, with no alt to fall back on', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'Man in suit holding papersImage' }]
    expect(parseMediaOptions(raw)).toEqual([
      { title: 'Man in suit holding papers', kind: 'Image', index: 0 },
    ])
  })

  it('splits a filename-style title', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'keynes-portrait-pro-b.jpgImage' }]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'keynes-portrait-pro-b.jpg',
      kind: 'Image',
    })
  })

  it('handles a title Flow has already truncated with a real ellipsis character', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'Modifying facial features and ap…Image' },
    ]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'Modifying facial features and ap…',
      kind: 'Image',
    })
  })

  // "Untitled Character" + kind "Character" — the suffix repeats a word that is genuinely
  // part of the title, so only an exact-suffix strip gets this right.
  it('strips only the kind suffix when the title itself ends in that same word', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'Untitled CharacterCharacter' }]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'Untitled Character',
      kind: 'Character',
    })
  })

  // Un-portraited character tiles render a material-symbols icon whose ligature text leaks
  // into the accessible name.
  it('strips a leading icon ligature butted against the title', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'personUntitled CharacterCharacter' }]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'Untitled Character',
      kind: 'Character',
    })
  })

  it('leaves a title alone that merely starts with a ligature word followed by a space', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'person walking away at duskImage' }]
    expect(parseMediaOptions(raw)[0]!.title).toBe('person walking away at dusk')
  })

  it('prefers alt over the parsed accessible name when alt is present', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man in suit holding papersImage',
        alt: 'Man in suit holding papers',
      },
    ]
    expect(parseMediaOptions(raw)[0]!.title).toBe('Man in suit holding papers')
  })

  it('trusts alt even when it disagrees with the accessible name (alt is the reliable source)', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'UntitledImage',
        alt: 'A more descriptive caption Flow filled in later',
      },
    ]
    expect(parseMediaOptions(raw)[0]!.title).toBe(
      'A more descriptive caption Flow filled in later',
    )
  })

  it('classifies Video and Audio kinds by the same suffix rule', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'A quiet street at duskVideo' },
      { accessibleName: 'Rain on a tin roofAudio' },
    ]
    expect(parseMediaOptions(raw).map(i => i.kind)).toEqual(['Video', 'Audio'])
  })

  it('defaults sensibly when the accessible name is empty', () => {
    const raw: RawMediaOption[] = [{ accessibleName: '' }]
    expect(parseMediaOptions(raw)[0]).toEqual({ title: '', kind: 'Unknown', index: 0 })
  })

  // Fail closed: trimming a suffix we cannot identify would corrupt the exact string a
  // caller needs for the flow_create_character_from_media round-trip.
  it('returns an unrecognised kind label untouched rather than guessing where the title ends', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'Some new tile shapeSticker' }]
    expect(parseMediaOptions(raw)[0]).toMatchObject({
      title: 'Some new tile shapeSticker',
      kind: 'Unknown',
    })
  })

  it('does not treat a name that is nothing but the kind label as a suffix to strip', () => {
    const raw: RawMediaOption[] = [{ accessibleName: 'Image' }]
    expect(parseMediaOptions(raw)[0]).toMatchObject({ title: 'Image', kind: 'Unknown' })
  })

  it('extracts mediaId from a getMediaUrlRedirect src via the shared media-url helpers', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man in suit holding papersImage',
        src: IMG_SRC('71ef7331-65aa-4e13-84cc-6e3a3e37fa45'),
      },
    ]
    expect(parseMediaOptions(raw)[0]!.mediaId).toBe('71ef7331-65aa-4e13-84cc-6e3a3e37fa45')
  })

  it('recovers mediaId from a thumbnail URL carrying extra query params', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Untitled CharacterCharacter',
        src: `${IMG_SRC('fe570f52-44d5-484d-85e4-f64620c70c17')}&mediaUrlType=MEDIA_URL_TYPE_THUMBNAIL`,
      },
    ]
    expect(parseMediaOptions(raw)[0]!.mediaId).toBe('fe570f52-44d5-484d-85e4-f64620c70c17')
  })

  it('omits mediaId when src is absent, empty, or not a media redirect URL', () => {
    const raw: RawMediaOption[] = [
      { accessibleName: 'AImage' },
      { accessibleName: 'BImage', src: 'https://example.com/thumb.png' },
      { accessibleName: 'personUntitled CharacterCharacter', src: '' },
    ]
    for (const item of parseMediaOptions(raw)) expect(item.mediaId).toBeUndefined()
  })

  it('preserves gallery order and keeps duplicate titles as separate, indexed entries', () => {
    const raw: RawMediaOption[] = [
      {
        accessibleName: 'Man wearing suit portraitImage',
        alt: 'Man wearing suit portrait',
        src: IMG_SRC('2b5957c4-373e-4dd3-b33e-1a9c16afbe67'),
      },
      {
        accessibleName: 'Man wearing suit portraitImage',
        alt: 'Man wearing suit portrait',
        src: IMG_SRC('c17ff97b-89a2-41aa-90eb-6a96f22eedea'),
      },
      { accessibleName: 'A quiet street at duskVideo' },
    ]
    const items = parseMediaOptions(raw)
    expect(items).toHaveLength(3)
    expect(items.map(i => i.title)).toEqual([
      'Man wearing suit portrait',
      'Man wearing suit portrait',
      'A quiet street at dusk',
    ])
    expect(items.map(i => i.index)).toEqual([0, 1, 2])
    expect(items[0]!.mediaId).toBe('2b5957c4-373e-4dd3-b33e-1a9c16afbe67')
    expect(items[1]!.mediaId).toBe('c17ff97b-89a2-41aa-90eb-6a96f22eedea')
  })
})
