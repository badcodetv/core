// take-row.mts — pure helpers for suno.mts (no browser, no I/O), unit-tested in take-row.test.mts.
// This module must import NOTHING from suno.mts: suno.mts imports from here, and pulling it in would
// drag Playwright into every test (and the two-way import is a verified init-order cycle).
// `modelTag` lives here and suno.mts re-exports it.

/** A Suno duration string → seconds. Accepts 'M:SS' / 'MM:SS' and 'H:MM:SS'; throws on anything else. */
export function durToSeconds(dur: string): number {
  const s = dur.trim()
  const m = /^(?:(\d+):([0-5]\d)|(\d+)):([0-5]\d)$/.exec(s)
  if (!m) throw new Error(`durToSeconds: not a M:SS or H:MM:SS duration: ${JSON.stringify(dur)}`)
  const [, h, mm, mOnly, ss] = m
  return h !== undefined
    ? Number(h) * 3600 + Number(mm) * 60 + Number(ss)
    : Number(mOnly) * 60 + Number(ss)
}

/** One row of the create page's take list. `songId` is the uuid in `suno.com/song/<uuid>`. */
export interface Take {
  title: string
  dur: string | null
  songId: string | null
}

const UUID = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
const SONG_ID_IN = new RegExp(`/song/(${UUID})(?![0-9a-f-])`, 'i')
const IS_UUID = new RegExp(`^${UUID}$`, 'i')
const IS_ID8 = /^[0-9a-f]{8}$/i

/** The first `/song/<uuid>` in an href or a chunk of HTML, lower-cased; null when there is none. */
export function parseSongId(hrefOrHtml: string): string | null {
  const m = SONG_ID_IN.exec(hrefOrHtml)
  return m ? m[1].toLowerCase() : null
}

/**
 * Resolve a user's key to takes. Order (decision 4 — a take is its song ID, titles are ambiguous
 * across a pair): a full uuid → exact songId, never a title; an 8-hex id8 → songId prefix, falling
 * back to a title substring only if no id matches; anything else → case-insensitive title substring.
 * More than one result is the caller's TAKE_AMBIGUOUS, not an error here.
 */
export function matchTakes(takes: Take[], key: string): Take[] {
  const k = key.trim().toLowerCase()
  if (IS_UUID.test(k)) return takes.filter((t) => t.songId?.toLowerCase() === k)
  const byTitle = () => takes.filter((t) => t.title.toLowerCase().includes(k))
  if (IS_ID8.test(k)) {
    const byId = takes.filter((t) => t.songId?.toLowerCase().startsWith(k))
    return byId.length ? byId : byTitle()
  }
  return byTitle()
}

/** The model as it appears in a title: v6 → `v6`, v6-wild → `wild`, a custom model → its name. */
export const modelTag = (m: string) =>
  m.toLowerCase().replace(/^v6-/, '').replace(/[^a-z0-9]+/g, '').slice(0, 12) || 'model'

/** One Create's settings. Variety is always Off and Max Mode always off in the listening loop. */
export interface Cell {
  model: string
  weirdness: number
  styleInfluence: number
  variety: 'off'
  maxMode: false
  audioInfluence?: number
  title: string
}

/** `listTakes` truncates titles at 48 chars (suno.mts), so the base must leave room for the suffix. */
export const MAX_BASE_TITLE = 30

function checkRound(fn: string, baseTitle: string, round: number): void {
  if (!baseTitle) throw new Error(`${fn}: empty base title`)
  if (baseTitle.length > MAX_BASE_TITLE)
    throw new Error(
      `${fn}: base title ${JSON.stringify(baseTitle)} is ${baseTitle.length} chars; max ${MAX_BASE_TITLE} (listTakes truncates titles at 48)`,
    )
  if (!Number.isInteger(round) || round < 1) throw new Error(`${fn}: round must be a positive integer, got ${round}`)
}

/**
 * Decision 6 — explore spread, safe end + wild end, prompt boxes unchanged within the round.
 * The `-r<N>-` in every title stops a later round matching an earlier round's takes.
 */
export function exploreCells(baseTitle: string, round: number): Cell[] {
  checkRound('exploreCells', baseTitle, round)
  const cell = (model: string, weirdness: number, styleInfluence: number): Cell => ({
    model,
    weirdness,
    styleInfluence,
    variety: 'off',
    maxMode: false,
    title: `${baseTitle}-r${round}-${modelTag(model)}-w${weirdness}`,
  })
  return [cell('v6', 30, 75), cell('v6-wild', 60, 60)]
}

/** Decision 7 — narrow = cover the pick with the refined boxes, on the pick's model. */
export function narrowCells(baseTitle: string, round: number, model: string): Cell[] {
  checkRound('narrowCells', baseTitle, round)
  const cell = (audioInfluence: number): Cell => ({
    model,
    weirdness: 30,
    styleInfluence: 75,
    audioInfluence,
    variety: 'off',
    maxMode: false,
    title: `${baseTitle}-r${round}-${modelTag(model)}-ai${audioInfluence}-w30`,
  })
  return [cell(75), cell(40)]
}

/** File-name stem for a recording: `<slug(title)>-<first 8 of songId>`. */
export function mediaSlug(title: string, songId: string): string {
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'take'
  return `${slug}-${songId.toLowerCase().slice(0, 8)}`
}
