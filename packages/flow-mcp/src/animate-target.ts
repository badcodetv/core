import { isMediaSrc, parseMediaName } from './media-url'

/**
 * A raw "Generated image" tile as scraped from the page (see flow-client.ts's
 * SCRAPE_ANIMATE_TILES) — just enough to resolve a media name, mirroring dom.ts's RawImg /
 * media-list.ts's RawMediaOption pattern (plain data, no DOM refs — those don't survive a
 * page.evaluate round-trip).
 */
export interface RawAnimateTile {
  src: string
}

/**
 * A tile reduced to its DOM position (the index openAnimateMenu will target via `.nth()`) and
 * its resolved media name. `name` is null when the src hasn't resolved to a
 * `getMediaUrlRedirect` URL yet — normal for the first tick or two right after an upload lands
 * (a loading/placeholder src briefly precedes the real one).
 */
export interface AnimateTile {
  index: number
  name: string | null
}

/** Parse raw scraped tiles into AnimateTiles, preserving DOM order as `index`. */
export function toAnimateTiles(raw: RawAnimateTile[]): AnimateTile[] {
  return raw.map((t, index) => ({ index, name: isMediaSrc(t.src) ? parseMediaName(t.src) : null }))
}

/**
 * Identify which "Generated image" tile is the just-uploaded still, by diffing against a
 * pre-upload snapshot of the same tile list (the same before/after-snapshot idea `generateVideo`
 * already uses for detecting the finished clip, applied one step earlier).
 *
 * Returns the DOM index of the ONE tile whose media name is new; `null` when that isn't
 * unambiguous — zero matches (nothing has landed yet, or the src hasn't resolved) or more than
 * one (an unrelated tile changed at the same moment, e.g. another upload mid-flight). A wrong
 * guess here means silently animating a DIFFERENT still than the one the caller just supplied,
 * with no visible sign anything went wrong — so ambiguity is never resolved by picking anyway.
 */
export function pickNewTileIndex(before: AnimateTile[], after: AnimateTile[]): number | null {
  const beforeNames = new Set(before.map((t) => t.name).filter((n): n is string => n !== null))
  const candidates = after.filter((t) => t.name !== null && !beforeNames.has(t.name))
  return candidates.length === 1 ? candidates[0]!.index : null
}

/**
 * Full target selection, including the one safe fallback: if the name-diff can't disambiguate
 * (most likely because the new tile's src hasn't resolved to a parseable media name on this
 * tick, so it never entered `candidates`) but the project holds exactly ONE "Generated image"
 * tile in total, there is no other still it could be — target it even though the diff alone
 * couldn't confirm it name-for-name. This is what keeps the common case (a fresh/near-empty
 * project — the normal state for a project this tool just uploaded into) working even when
 * identification-by-name is momentarily imperfect, without ever guessing among genuine
 * candidates: any OTHER ambiguity (zero tiles, or 2+ with no clean diff) still returns null, and
 * the caller (`waitForNewAnimateTile`) keeps polling and eventually fails closed rather than
 * animating a tile it isn't sure about.
 */
export function chooseAnimateTarget(before: AnimateTile[], after: AnimateTile[]): number | null {
  const byDiff = pickNewTileIndex(before, after)
  if (byDiff !== null) return byDiff
  return after.length === 1 ? 0 : null
}

/**
 * Did attaching a source frame produce a reference chip for something OTHER than the tile we
 * targeted? Compares chip media ids before and after the attach, so only the chip THIS turn
 * created is judged.
 *
 * Reading "the first reference chip on the page" instead is wrong, and wrong in exactly the way
 * the animate bug itself was: Flow leaves earlier turns' chips in the DOM (two were live at
 * once, one scrolled far off-screen at y=-464), so the first match is routinely a stale one
 * from a previous generation. That produced a false ANIMATE_WRONG_SOURCE on a correct attach.
 *
 * Returns false — no complaint — when no new chip appeared, since that means we cannot tell.
 * This guards a known bug; it must not become a tripwire that blocks work on a UI tweak.
 */
export function attachedWrongSource(
  beforeChips: string[],
  afterChips: string[],
  expected: string,
): boolean {
  const remaining = new Map<string, number>()
  for (const c of beforeChips) remaining.set(c, (remaining.get(c) ?? 0) + 1)
  const fresh: string[] = []
  for (const c of afterChips) {
    const n = remaining.get(c) ?? 0
    if (n > 0) remaining.set(c, n - 1)
    else fresh.push(c)
  }
  if (!fresh.length) return false
  return !fresh.includes(expected)
}
