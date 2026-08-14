/**
 * What to keep out of a page-text dump taken when a generation times out.
 *
 * The point is L3 in `design/2026-08-12-flow-automation-coverage.md`: two failure states —
 * credit exhaustion and rate-limiting/recaptcha — have never been seen, so `classifyCard` cannot
 * name them and they surface as a bare `TIMEOUT`. The ruling was **do not invent the strings**.
 * So instead of guessing at patterns, a timeout writes down what was actually on screen, and the
 * next unmapped failure hands over its real wording instead of another unexplained timeout.
 *
 * Pure, because the judgement here — what counts as signal versus Flow's own chrome — is exactly
 * the kind of thing that rots silently inside a browser method.
 */

/**
 * Flow's UI text that carries no diagnostic information. Everything here is a control label or
 * navigation furniture present on every page, in every state.
 */
/**
 * Flow renders every control as its Material ligature glued straight onto the label —
 * `arrow_backGo Back`, `addAdd Media`, `more_vertMore options`. So the shape is the giveaway: a
 * lowercase run followed immediately by a capital. Matching the SHAPE rather than a list of
 * words is what keeps this from eating real messages that happen to begin "Image…" or "Delete…".
 */
const LIGATURE_LABEL_RE = /^[a-z][a-z0-9_]*(?=[A-Z])/
/**
 * A Material icon name on its own: one lowercase token, no spaces — `dashboard`, `swap_horiz`,
 * `crop_16_9`. Scraping LEAF nodes splits an icon away from its label, so these arrive alone and
 * the glued-together rule above never sees them. It costs us genuine one-word messages, which do
 * not exist in Flow's transcript.
 */
const ICON_NAME_RE = /^[a-z][a-z0-9_]*$/
/** The handful of controls whose text has no capital to key off. */
const BARE_CONTROLS = new Set(['Agent', 'Done', 'ULTRA', 'pausepause', 'playplay', 'skip_nextnext'])

/**
 * The lines worth writing down, in page order: visible, human-length, not chrome, deduped.
 *
 * `max` caps the file rather than the DOM walk — a wedged Flow page can hold thousands of
 * transcript nodes, and a dump nobody will read is as useless as no dump.
 */
export function dumpLines(texts: string[], max = 60): string[] {
  const out: string[] = []
  const seen = new Set<string>()
  for (const raw of texts) {
    const t = (raw ?? '').replace(/\s+/g, ' ').trim()
    // Under 3 chars is an icon ligature or a stray character; over 400 is a whole subtree's
    // textContent concatenated, which says nothing about where the message is.
    if (t.length < 3 || t.length > 400) continue
    if (LIGATURE_LABEL_RE.test(t) || ICON_NAME_RE.test(t) || BARE_CONTROLS.has(t)) continue
    if (seen.has(t)) continue
    seen.add(t)
    out.push(t)
    if (out.length >= max) break
  }
  return out
}
