import { describe, it, expect } from 'vitest'
import {
  classifyCoverState,
  songIdFromArt,
  durToSeconds,
  parseSongId,
  matchTakes,
  modelTag,
  exploreCells,
  narrowCells,
  mediaSlug,
  MAX_BASE_TITLE,
  type Take,
} from './take-row.mts'

const ID_A = '44f46458-d0c2-40f6-a14a-2c331b805fa8'
const ID_B = '9b1c2d3e-0000-4000-8000-000000000001'
const ID_C = '44f46458-ffff-4fff-8fff-ffffffffffff' // shares ID_A's first 8 chars

describe('parseSongId', () => {
  it('pulls the uuid out of an anchor', () => {
    expect(parseSongId('<a href="/song/44f46458-d0c2-40f6-a14a-2c331b805fa8">')).toBe(ID_A)
  })

  it('pulls the uuid out of a full URL', () => {
    expect(parseSongId(`https://suno.com/song/${ID_A}?sh=abc`)).toBe(ID_A)
  })

  it('returns the FIRST /song/<uuid> when there are several', () => {
    expect(parseSongId(`<a href="/song/${ID_B}"></a><a href="/song/${ID_A}"></a>`)).toBe(ID_B)
  })

  it('lower-cases an upper-case uuid', () => {
    expect(parseSongId(`/song/${ID_A.toUpperCase()}`)).toBe(ID_A)
  })

  it.each([
    [''],
    ['<a href="/create">'],
    [`<a href="/playlist/${ID_A}">`],                 // a uuid, but not a song
    ['<a href="/song/44f46458-d0c2-40f6-a14a">'],     // truncated uuid
    ['<a href="/song/zzzzzzzz-d0c2-40f6-a14a-2c331b805fa8">'],
  ])('returns null for %j', (s) => {
    expect(parseSongId(s)).toBeNull()
  })
})

describe('matchTakes', () => {
  const takes: Take[] = [
    { title: 'm3-A-r3-v6-w30', dur: '3:18', songId: ID_A },
    { title: 'm3-A-r3-v6-w30', dur: '3:02', songId: ID_B },
    { title: 'm3-A-r3-wild-w60', dur: '2:55', songId: ID_C },
    { title: 'still rendering', dur: null, songId: null },
    { title: 'deadbeef tribute', dur: '1:00', songId: null },
  ]

  it('a full uuid matches exactly that songId', () => {
    expect(matchTakes(takes, ID_B)).toEqual([takes[1]])
  })

  it('a full uuid is matched case-insensitively and never falls back to a title', () => {
    expect(matchTakes(takes, ID_A.toUpperCase())).toEqual([takes[0]])
    expect(matchTakes(takes, '00000000-0000-4000-8000-000000000000')).toEqual([])
  })

  it('an id8 returns only that take', () => {
    expect(matchTakes(takes, '9b1c2d3e')).toEqual([takes[1]])
  })

  it('an id8 shared by two songIds returns both (the caller reports TAKE_AMBIGUOUS)', () => {
    expect(matchTakes(takes, '44f46458')).toEqual([takes[0], takes[2]])
  })

  it('an id8 that matches no songId falls back to a title substring', () => {
    expect(matchTakes(takes, 'deadbeef')).toEqual([takes[4]])
  })

  it('a title shared by two takes returns both', () => {
    expect(matchTakes(takes, 'm3-A-r3-v6-w30')).toEqual([takes[0], takes[1]])
  })

  it('title matching is a case-insensitive substring', () => {
    expect(matchTakes(takes, 'WILD')).toEqual([takes[2]])
    expect(matchTakes(takes, 'r3')).toEqual([takes[0], takes[1], takes[2]])
  })

  it('no match → empty', () => {
    expect(matchTakes(takes, 'nope')).toEqual([])
  })
})

describe('modelTag (moved from suno.mts — behaviour unchanged)', () => {
  it.each([
    ['v6', 'v6'],
    ['v6-wild', 'wild'],
    ['V6-Wild', 'wild'],
    ['My Custom Model!', 'mycustommode'],       // punctuation/spaces stripped, capped at 12
    ['a-very-long-custom-model-name', 'averylongcus'],
    ['---', 'model'],                           // nothing left → 'model'
    ['v6-', 'model'],
  ])('%j → %j', (m, tag) => {
    expect(modelTag(m)).toBe(tag)
  })
})

describe('exploreCells', () => {
  it('is exactly the two cells of decision 6', () => {
    expect(exploreCells('m3-A', 3)).toStrictEqual([
      { model: 'v6', weirdness: 30, styleInfluence: 75, variety: 'off', maxMode: false, title: 'm3-A-r3-v6-w30' },
      { model: 'v6-wild', weirdness: 60, styleInfluence: 60, variety: 'off', maxMode: false, title: 'm3-A-r3-wild-w60' },
    ])
  })

  it('accepts a base title of exactly MAX_BASE_TITLE chars', () => {
    expect(MAX_BASE_TITLE).toBe(30)
    const base = 'x'.repeat(30)
    expect(exploreCells(base, 1)[0].title).toBe(`${base}-r1-v6-w30`)
  })

  it('throws on a 31-char base title', () => {
    expect(() => exploreCells('x'.repeat(31), 3)).toThrow(/30/)
  })

  it('throws on an empty base title or a round that is not a positive integer', () => {
    expect(() => exploreCells('', 3)).toThrow()
    expect(() => exploreCells('m3-A', 0)).toThrow()
    expect(() => exploreCells('m3-A', 1.5)).toThrow()
  })
})

describe('narrowCells', () => {
  it('covers the pick at Audio Influence 75 then 40, Weirdness 30, Style Influence 75, on the given model', () => {
    expect(narrowCells('m3-B', 4, 'v6-wild')).toStrictEqual([
      { model: 'v6-wild', weirdness: 30, styleInfluence: 75, audioInfluence: 75, variety: 'off', maxMode: false, title: 'm3-B-r4-wild-ai75-w30' },
      { model: 'v6-wild', weirdness: 30, styleInfluence: 75, audioInfluence: 40, variety: 'off', maxMode: false, title: 'm3-B-r4-wild-ai40-w30' },
    ])
  })

  it('tags the title with modelTag of the pick\'s model', () => {
    expect(narrowCells('m3-B', 4, 'v6').map((c) => c.title)).toEqual(['m3-B-r4-v6-ai75-w30', 'm3-B-r4-v6-ai40-w30'])
  })

  it('enforces the same base-title cap as exploreCells', () => {
    expect(() => narrowCells('x'.repeat(31), 4, 'v6')).toThrow(/30/)
  })
})

describe('mediaSlug', () => {
  it('slugs the title and appends the first 8 chars of the song id', () => {
    expect(mediaSlug('M3 Lane: take 2', ID_A)).toBe('m3-lane-take-2-44f46458')
  })

  it('keeps an already-slugged title as is', () => {
    expect(mediaSlug('m3-A-r3-v6-w30', ID_A)).toBe('m3-a-r3-v6-w30-44f46458')
  })

  it('never produces a leading/trailing/double dash, and survives an all-punctuation title', () => {
    expect(mediaSlug('  --Hello,, World!!  ', ID_B)).toBe('hello-world-9b1c2d3e')
    expect(mediaSlug('!!!', ID_B)).toBe('take-9b1c2d3e')
  })
})

describe('durToSeconds', () => {
  it('parses M:SS', () => {
    expect(durToSeconds('3:20')).toBe(200)
    expect(durToSeconds('0:07')).toBe(7)
    expect(durToSeconds('0:00')).toBe(0)
  })

  it('parses MM:SS with more than one minute digit', () => {
    expect(durToSeconds('12:05')).toBe(725)
  })

  it('parses H:MM:SS', () => {
    expect(durToSeconds('1:02:03')).toBe(3723)
  })

  it('tolerates surrounding whitespace', () => {
    expect(durToSeconds(' 3:20\n')).toBe(200)
  })

  it.each([
    [''],
    ['abc'],
    ['200'],       // bare seconds: ambiguous, not a Suno duration
    ['3:2'],       // seconds must be two digits
    ['3:60'],      // seconds out of range
    ['1:60:00'],   // minutes out of range when hours are present
    ['-1:20'],
    ['3:20.5'],
    ['1:2:3:4'],
    [':20'],
  ])('throws on %j', (bad) => {
    expect(() => durToSeconds(bad)).toThrow(/durToSeconds/)
  })
})


describe('songIdFromArt', () => {
  it('reads the uuid from both artwork sizes', () => {
    expect(songIdFromArt('https://cdn2.suno.ai/image_870fbab1-78fd-42e8-b52e-2bc44c901fa2.jpeg?width=360')).toBe('870fbab1-78fd-42e8-b52e-2bc44c901fa2')
    expect(songIdFromArt('https://cdn2.suno.ai/image_large_870FBAB1-78fd-42e8-b52e-2bc44c901fa2.jpeg')).toBe('870fbab1-78fd-42e8-b52e-2bc44c901fa2')
  })
  it('is null without one', () => {
    expect(songIdFromArt(null)).toBeNull()
    expect(songIdFromArt('https://cdn-o.suno.com/sil-100.mp3')).toBeNull()
  })
})

describe('classifyCoverState', () => {
  const empty = { clearButton: false, typeLabel: null, cardText: null, cardArt: null, styleLen: 0, lyricParas: 1, title: '' }
  it('custom-empty: nothing attached, empty boxes (as read live 2026-09-11)', () => {
    expect(classifyCoverState(empty)).toEqual({ state: 'custom-empty' })
  })
  it('custom-leftover: a detached source leaves its words behind (live: 994 / 18 / title)', () => {
    expect(classifyCoverState({ ...empty, styleLen: 994, lyricParas: 18, title: 'gpom-cut1F-haunting-dark-si50-ai20-w45' })).toEqual({
      state: 'custom-leftover', styleLen: 994, lyricParas: 18, title: 'gpom-cut1F-haunting-dark-si50-ai20-w45',
    })
    expect(classifyCoverState({ ...empty, title: 'x' }).state).toBe('custom-leftover')
  })
  it('attached: reads mode, title, duration and song id from the live card', () => {
    expect(classifyCoverState({
      ...empty,
      clearButton: true,
      typeLabel: 'Change condition type from Cover',
      cardText: 'Audio Cover gpom-cut1F-haunting-dark-si50-ai20-w45 00:05/01:05',
      cardArt: 'https://cdn2.suno.ai/image_870fbab1-78fd-42e8-b52e-2bc44c901fa2.jpeg?width=360',
      styleLen: 994, lyricParas: 18,
    })).toEqual({
      state: 'attached',
      mode: 'Cover',
      source: { title: 'gpom-cut1F-haunting-dark-si50-ai20-w45', dur: '1:05', songId: '870fbab1-78fd-42e8-b52e-2bc44c901fa2' },
    })
  })
  it('attached wins over leftover text, and survives an unreadable card', () => {
    const s = classifyCoverState({ ...empty, clearButton: true, typeLabel: null, styleLen: 5 })
    expect(s).toEqual({ state: 'attached', mode: 'unknown', source: { title: null, dur: null, songId: null } })
  })
})
