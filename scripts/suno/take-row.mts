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

// ─────────────────────────────────────────────────────────────────────────────
// The create page's player — mapped live 2026-09-11 (docs/suno-gpt/automation.md §10).
// Selectors only; the browser code that uses them lives in suno.mts.

/** One per take row. The row itself has only a hashed CSS class, so rows are found from this. */
export const SEL_SELECT_CLIP = '[aria-label="Select clip"]'
/** The row's song link, `/song/<uuid>` — the take's identity (decision 4). */
export const SEL_SONG_LINK = 'a[href*="/song/"]'
/** The row's Play control is its artwork: `aria-label="Play <title>"`. A native click works. */
export const SEL_ROW_PLAY = '[role="button"][aria-label^="Play "]'
/** The one element that plays takes. Its src becomes a `blob:` URL ~1 s after Play. */
export const SEL_PLAYER_AUDIO = 'audio#active-audio-play'
/** A 0.096 s silent clip Suno keeps around — never the take. */
export const SEL_SILENT_AUDIO = 'audio#silent-audio'
/** The playbar's toggle: its label reads `Playbar: Pause button` while playing. */
export const SEL_PLAYBAR_PAUSE = 'button[aria-label="Playbar: Pause button"]'
export const SEL_PLAYBAR_PLAY = 'button[aria-label="Playbar: Play button"]'
/** 🔴 Suno plays the next row ~1 s after `ended`. A recorder must pause on `ended` and on any later `play`. */
export const AUTO_ADVANCES = true

// ─────────────────────────────────────────────────────────────────────────────
// v6 Cover — attach, detach and mode detection, mapped live 2026-09-11 (automation.md §10).

/** Present only while a source is attached. Its click detaches (a REAL mouse click — see detachCover). */
export const SEL_CLEAR_CONDITION = 'button[aria-label="Clear audio condition"]'
/** `aria-label="Change condition type from Cover"` — the suffix is the attachment's mode. */
export const SEL_CONDITION_TYPE = 'button[aria-label^="Change condition type from "]'
/** The attachment card's artwork: `image_<songId>.jpeg`. The Remix picker's rows carry the same img. */
export const SEL_CONDITION_ART = 'img[alt^="Cover art for "]'
/** Mounted only with audio (or a Voice) attached — never proof of Cover on its own. */
export const SEL_AUDIO_INFLUENCE = '[role="slider"][aria-label="Audio Influence"]'

/** The song ID inside a Suno artwork URL (`…/image_<uuid>.jpeg`, `image_large_<uuid>`). */
export function songIdFromArt(src: string | null | undefined): string | null {
  const m = /image_(?:large_)?([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/i.exec(src ?? '')
  return m ? m[1].toLowerCase() : null
}

/** What the page shows, scraped by suno.mts — kept as plain data so the judgement is testable. */
export interface CoverScrape {
  /** `SEL_CLEAR_CONDITION` is on the page. */
  clearButton: boolean
  /** `aria-label` of `SEL_CONDITION_TYPE`, or null. */
  typeLabel: string | null
  /** The card's text, e.g. `Audio Cover <title> 00:05/01:05`, or null. */
  cardText: string | null
  /** The card artwork's `src`, or null. */
  cardArt: string | null
  styleLen: number
  lyricParas: number
  title: string
}

export type CoverState =
  | { state: 'custom-empty' }
  | { state: 'custom-leftover'; styleLen: number; lyricParas: number; title: string }
  | { state: 'attached'; mode: string; source: { title: string | null; dur: string | null; songId: string | null } }

/**
 * The three states narrow needs to tell apart:
 *   custom-empty    — nothing attached, boxes empty (an empty Lexical editor reads 1 paragraph)
 *   custom-leftover — nothing attached, but boxes hold text (e.g. a detached source's words)
 *   attached        — a source is attached; `mode` is the condition type (Cover, Extend, …)
 * The attachment signal is the Clear button, not the mode tabs: v6's tabs read Simple · Advanced ·
 * Sounds in every state, so the old v5.5 "Cover tab" check has nothing to look at.
 */
export function classifyCoverState(s: CoverScrape): CoverState {
  if (s.clearButton) {
    const mode = /^Change condition type from (.+)$/.exec(s.typeLabel ?? '')?.[1]?.trim() ?? 'unknown'
    const m = /^Audio\s+\S+\s+(.*?)\s+\d{1,2}:\d{2}\/(\d{1,2}):(\d{2})$/.exec((s.cardText ?? '').replace(/\s+/g, ' ').trim())
    const dur = m ? `${Number(m[2])}:${m[3]}` : null
    return { state: 'attached', mode, source: { title: m ? m[1] : null, dur, songId: songIdFromArt(s.cardArt) } }
  }
  if (s.styleLen > 0 || s.lyricParas > 1 || s.title.trim() !== '') {
    return { state: 'custom-leftover', styleLen: s.styleLen, lyricParas: s.lyricParas, title: s.title }
  }
  return { state: 'custom-empty' }
}
