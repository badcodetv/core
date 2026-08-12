import { isMediaSrc, parseMediaName } from './media-url'

/**
 * One asset-picker tile (`role="option"`) as scraped from the page. Kept as plain data
 * (no DOM refs — those do not survive a `page.evaluate` round-trip), mirroring dom.ts's
 * RawImg / project.ts's ProjectTile pattern.
 */
export interface RawMediaOption {
  /**
   * The option's accessible name, as Flow renders it: the title with its kind CONCATENATED
   * onto the end, no separator — "Man in suit holding papersImage", "Untitled
   * CharacterCharacter". Mapped live 2026-08-12 from a real picker.
   *
   * Some tiles additionally carry a leading material-symbols icon ligature, likewise with no
   * separator ("personUntitled CharacterCharacter"); the icon's own name leaks into the
   * accessible name because the ligature is rendered as ordinary text.
   */
  accessibleName: string
  /** The tile's `<img alt>` — Flow's own, non-doubled title, when the tile carries one. */
  alt?: string
  /** The tile's media `src` (thumbnail or full), used to recover the media id. */
  src?: string
}

export interface MediaListItem {
  title: string
  kind: string
  mediaId?: string
  /**
   * Position of this item in the returned list (0-based, gallery order preserved). The
   * gallery legitimately shows several items sharing the same auto-caption title (e.g. two
   * separate "Man in suit holding papers" generations), so titles are never collapsed or
   * suffixed here — an invented suffix would corrupt the exact accessible-name string a
   * caller needs for a follow-up exact-ish match (flow_create_character_from_media matches
   * mediaTitle against this same text). `index` lets a caller disambiguate ("the second one
   * titled X") out of band, without touching the title text itself.
   */
  index: number
}

/**
 * In-page scraper (evaluated as `(${SCRAPE_MEDIA_OPTIONS})()`), mirroring dom.ts's
 * SCRAPE_IMGS / project.ts's SCRAPE_PROJECTS pattern: return plain data from the page
 * context, not element handles — evaluating the bare function string returns the function
 * itself, not its result, so callers MUST invoke it as `(${SCRAPE_MEDIA_OPTIONS})()`.
 */
export const SCRAPE_MEDIA_OPTIONS = `() => [...document.querySelectorAll('[role="option"]')].map(el => {
  const media = el.querySelector('img, video')
  const alt = media && media.tagName === 'IMG' ? (media.getAttribute('alt') || undefined) : undefined
  const src = media ? (media.currentSrc || media.src || media.getAttribute('src') || media.poster || '') : ''
  return {
    accessibleName: (el.getAttribute('aria-label') || el.textContent || '').trim(),
    alt,
    src,
  }
})`

/**
 * The kind labels Flow appends to a tile's accessible name. Matched as an exact suffix, so
 * an unrecognised label is never mistaken for part of the title — see parseAccessibleName.
 * "Image" and "Character" are observed live; "Video" and "Audio" follow the same pattern and
 * are included because a project with clips in it will hit them immediately.
 */
const KIND_SUFFIXES = ['Image', 'Video', 'Character', 'Audio'] as const

/**
 * Leading material-symbols ligature names seen leaking into accessible names. Stripped only
 * when butted directly against a capital letter, so a genuine title that merely starts with
 * one of these words ("person walking away") is left alone.
 */
const ICON_LIGATURE_RE = /^(?:person|face|movie|videocam|image|mic|accessibility_new)+(?=[A-Z])/

/**
 * Split a picker tile's accessible name into { title, kind }.
 *
 * The shape is `<title><Kind>` with NO separator, optionally prefixed by an icon ligature:
 * "Man in suit holding papersImage" → { title: "Man in suit holding papers", kind: "Image" },
 * "personUntitled CharacterCharacter" → { title: "Untitled Character", kind: "Character" }.
 *
 * An earlier version of this function assumed the name DOUBLED the title
 * ("T T Image") and split on the last space. That was inferred, never observed, and it put
 * the wrong value in `kind` for every single row — "papersImage", "bookImage",
 * "CharacterCharacter" — while quietly corrupting the fallback title too. Mapped against a
 * live picker 2026-08-12.
 *
 * Titles arrive already truncated by Flow with a real "…" character baked into the text (not
 * CSS ellipsis, which would not reach an accessible name at all), so a title may legitimately
 * end mid-word. Nothing here tries to repair that.
 */
function parseAccessibleName(accessibleName: string): { title: string; kind: string } {
  const trimmed = accessibleName.trim()
  if (!trimmed) return { title: '', kind: 'Unknown' }
  const kind = KIND_SUFFIXES.find(k => trimmed.endsWith(k) && trimmed.length > k.length)
  // No recognised suffix: return the name untouched rather than guessing where a title ends.
  // Trimming a suffix we cannot identify would silently corrupt the exact string a caller
  // needs for the flow_create_character_from_media round-trip.
  if (!kind) return { title: trimmed.replace(ICON_LIGATURE_RE, ''), kind: 'Unknown' }
  const title = trimmed.slice(0, -kind.length).replace(ICON_LIGATURE_RE, '').trim()
  return { title, kind }
}

/**
 * Turn scraped asset-picker option rows into a caller-facing media list. Pure — no page
 * access — so every rule here is unit-tested rather than verified by hand against a live
 * picker.
 *
 * - `alt` is the reliable source of the title where present (it is Flow's own clean label for
 *   the tile's image, free of both the kind suffix and any icon ligature) — parsing the
 *   accessible name is only a FALLBACK for rows without one (observed: character tiles that
 *   have no portrait generated yet, which carry no <img> at all).
 * - `kind` is classified from the trailing word of the accessible name ("Image", "Video",
 *   …); an unrecognised trailing word is still returned rather than dropped, so a caller
 *   sees Flow's raw label instead of a silently wrong guess.
 * - `mediaId` is recovered from `src` via the existing `media-url.ts` helpers (reused, not
 *   reimplemented) — undefined when `src` is absent or isn't a `getMediaUrlRedirect` URL.
 * - Gallery order is preserved and nothing is deduplicated away; see `MediaListItem.index`.
 */
export function parseMediaOptions(raw: RawMediaOption[]): MediaListItem[] {
  return raw.map((r, index) => {
    const { title: fallbackTitle, kind } = parseAccessibleName(r.accessibleName)
    const alt = r.alt?.trim()
    const title = alt ? alt : fallbackTitle
    const mediaId = r.src && isMediaSrc(r.src) ? parseMediaName(r.src) ?? undefined : undefined
    return { title, kind, ...(mediaId ? { mediaId } : {}), index }
  })
}
