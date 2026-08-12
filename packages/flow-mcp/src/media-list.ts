import { isMediaSrc, parseMediaName } from './media-url'

/**
 * One asset-picker tile (`role="option"`) as scraped from the page. Kept as plain data
 * (no DOM refs — those do not survive a `page.evaluate` round-trip), mirroring dom.ts's
 * RawImg / project.ts's ProjectTile pattern.
 */
export interface RawMediaOption {
  /**
   * The option's accessible name, as Flow renders it. Confirmed live: it DOUBLES the
   * title and appends a trailing kind word, e.g.
   * "Man in suit holding papers Man in suit holding papers Image".
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
 * Split Flow's doubled accessible name ("Man in suit holding papers Man in suit holding
 * papers Image") into { title, kind }. Root cause of the doubling is not confirmed (likely
 * a visually-hidden duplicate label node plus the visible caption, both folded into the
 * same accessible name), but it is consistent across every observed sample, including
 * ones truncated with a real "…" character baked into the text (not CSS ellipsis, which
 * would not appear in an accessible name at all).
 */
function splitDoubledName(accessibleName: string): { title: string; kind: string } {
  const trimmed = accessibleName.trim()
  if (!trimmed) return { title: '', kind: 'Unknown' }
  const lastSpace = trimmed.lastIndexOf(' ')
  const kind = lastSpace === -1 ? trimmed : trimmed.slice(lastSpace + 1)
  const rest = lastSpace === -1 ? '' : trimmed.slice(0, lastSpace)
  // Recover the title from "T T" WITHOUT assuming the two Ts are the same length split at
  // the midpoint (Math.floor(rest.length / 2)) — a regex backreference instead requires the
  // two captured halves be textually IDENTICAL and lets the engine find the split via
  // backtracking. That is strictly more robust: it works whether or not the halves happen
  // to be equal length by construction (they always are here, since "doubled" means two
  // copies of the same string), and it degrades gracefully — if `rest` is not actually of
  // the form "T T", the match simply fails and the caller falls back to `rest` untouched.
  const m = rest.match(/^(.+) \1$/)
  return { title: m ? m[1]! : rest, kind: kind || 'Unknown' }
}

/**
 * Turn scraped asset-picker option rows into a caller-facing media list. Pure — no page
 * access — so every rule here is unit-tested rather than verified by hand against a live
 * picker.
 *
 * - `alt` is the reliable source of the title where present (it is Flow's own, undoubled
 *   label for the tile's image) — the doubled-accessible-name split is only a FALLBACK for
 *   rows without one (e.g. video tiles, or a picker layout that omits alt).
 * - `kind` is classified from the trailing word of the accessible name ("Image", "Video",
 *   …); an unrecognised trailing word is still returned rather than dropped, so a caller
 *   sees Flow's raw label instead of a silently wrong guess.
 * - `mediaId` is recovered from `src` via the existing `media-url.ts` helpers (reused, not
 *   reimplemented) — undefined when `src` is absent or isn't a `getMediaUrlRedirect` URL.
 * - Gallery order is preserved and nothing is deduplicated away; see `MediaListItem.index`.
 */
export function parseMediaOptions(raw: RawMediaOption[]): MediaListItem[] {
  return raw.map((r, index) => {
    const { title: fallbackTitle, kind } = splitDoubledName(r.accessibleName)
    const alt = r.alt?.trim()
    const title = alt ? alt : fallbackTitle
    const mediaId = r.src && isMediaSrc(r.src) ? parseMediaName(r.src) ?? undefined : undefined
    return { title, kind, ...(mediaId ? { mediaId } : {}), index }
  })
}
