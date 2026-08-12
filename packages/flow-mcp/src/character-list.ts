/**
 * One character card as scraped from the project root (evaluated as `(${SCRAPE_CHARACTERS})()`),
 * mirroring dom.ts's RawImg / project.ts's ProjectTile / media-list.ts's RawMediaOption pattern:
 * plain data, no DOM refs — those don't survive a `page.evaluate` round-trip.
 *
 * Confirmed live 2026-08-11 (see `openCharacterPage` in flow-client.ts): character cards on the
 * project root are `a[href*="/character/"]` anchors carrying the character's name as their
 * `<img alt>` — the same locator shape `openCharacterPage` uses to find ONE named character,
 * generalised here to enumerate all of them.
 */
export interface RawCharacterRow {
  href?: string
  /** The card's `<img alt>` — present only once the character has a generated portrait. */
  alt?: string
  /**
   * The visible caption, which lives in the anchor's PARENT, not inside the anchor (the
   * anchor's own text is nothing but material-symbols icon ligatures — "accessibility_new",
   * "faceaccessibility_new"). Recovered by subtracting the anchor's text from its parent's.
   */
  label?: string
}

export interface CharacterListItem {
  name: string
  id: string
}

/**
 * In-page scraper. Evaluating the bare function string returns the function itself, not its
 * result — a documented past bug (see media-list.ts, project.ts) — so callers MUST invoke it as
 * `(${SCRAPE_CHARACTERS})()`, never reference it bare.
 */
export const SCRAPE_CHARACTERS = `() => [...document.querySelectorAll('a[href*="/character/"]')].map(a => {
  const img = a.querySelector('img[alt]')
  const own = (a.textContent || '')
  const parent = a.parentElement ? (a.parentElement.textContent || '') : ''
  return {
    href: a.getAttribute('href') || '',
    alt: img ? (img.getAttribute('alt') || '') : '',
    label: parent.replace(own, '').trim(),
  }
})`

/**
 * Turn scraped character-card rows into a caller-facing list, deriving `id` from the href's
 * `/character/<id>` segment. Pure — no page access — so every rule here is unit-tested rather
 * than verified by hand against a live project root.
 *
 * The NAME is taken from the visible caption first and the `<img alt>` only as a fallback.
 * Requiring the alt (as this did originally) silently hid every character without a generated
 * portrait: live 2026-08-12 a project showing three characters returned one, because the two
 * un-portraited cards render an avatar placeholder rather than an `<img>`. Those are exactly
 * the characters a caller most needs to discover — a half-made character is the one you were
 * about to go and finish.
 *
 * Only `href` is genuinely required: without it there is no id, and an id is the sole
 * unambiguous handle (Flow lets several characters share the name "Untitled Character", so a
 * name is not a key). A row with an id but no recoverable name is still returned, named '',
 * rather than dropped — its id remains usable.
 */
export function parseCharacters(raw: RawCharacterRow[]): CharacterListItem[] {
  const out: CharacterListItem[] = []
  for (const r of raw) {
    const href = r.href?.trim()
    if (!href) continue
    const m = href.match(/\/character\/([0-9a-f-]+)/i)
    if (!m) continue
    const name = r.label?.trim() || r.alt?.trim() || ''
    out.push({ name, id: m[1]! })
  }
  return out
}
