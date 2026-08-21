/**
 * "Did you mean…" for match names.
 *
 * Effect and transition match names are strings like `AE.ADBE Gaussian Blur` that nobody can
 * recall and no vendor publishes. When one does not resolve, the useful answer is not
 * "not found" but *"not found — the closest three are these"*, so a caller can fix it in one
 * more step instead of listing the whole catalogue.
 *
 * Lives in `src/` rather than the panel because it is pure string work and deserves unit tests,
 * but it is imported BY the panel (esbuild bundles it in) — it must therefore stay free of any
 * Node or ppro dependency.
 */

/** Lowercase, and drop everything that is not a letter or digit: `AE.ADBE Gaussian Blur` and
 * `gaussian blur` should look alike, because to a person they are. */
function fold(s: string): string {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '')
}

/** Ordinary Levenshtein, two-row. The lists are ~100 short strings, so this is free. */
export function editDistance(a: string, b: string): number {
  if (a === b) return 0
  if (a.length === 0) return b.length
  if (b.length === 0) return a.length

  let prev = Array.from({ length: b.length + 1 }, (_, i) => i)
  let curr = new Array<number>(b.length + 1)

  for (let i = 1; i <= a.length; i += 1) {
    curr[0] = i
    for (let j = 1; j <= b.length; j += 1) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1
      curr[j] = Math.min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost)
    }
    const swap = prev
    prev = curr
    curr = swap
  }
  return prev[b.length]
}

/**
 * The `count` candidates closest to `wanted`, best first.
 *
 * Ranked in bands rather than by raw distance, because distance alone ranks badly on names of
 * very different lengths: `blur` is 15 edits from `AE.ADBE Gaussian Blur` even though it is
 * obviously what was meant. Containment therefore wins outright, and distance only orders
 * within a band.
 */
export function nearestNames(wanted: string, candidates: readonly string[], count = 3): string[] {
  const w = fold(wanted)
  if (!w) return candidates.slice(0, count)

  const scored = candidates.map((name) => {
    const c = fold(name)
    let band = 3
    if (c === w) band = 0
    else if (c.startsWith(w) || w.startsWith(c)) band = 1
    else if (c.includes(w) || w.includes(c)) band = 2
    return { name, band, distance: editDistance(w, c) }
  })

  scored.sort((a, b) => a.band - b.band || a.distance - b.distance || a.name.localeCompare(b.name))
  return scored.slice(0, count).map((s) => s.name)
}

/** The tail of a `*_NOT_FOUND` message: ` The closest are: a, b, c.` — or the count when we
 * have nothing close enough to be worth naming. */
export function didYouMean(wanted: string, candidates: readonly string[], count = 3): string {
  if (candidates.length === 0) return ' Premiere reported none at all.'
  const near = nearestNames(wanted, candidates, count)
  return ` The closest of the ${candidates.length} available are: ${near.join(', ')}.`
}
