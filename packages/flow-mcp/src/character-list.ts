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
  alt?: string
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
  return { href: a.getAttribute('href') || '', alt: img ? (img.getAttribute('alt') || '') : '' }
})`

/**
 * Turn scraped character-card rows into a caller-facing list, deriving `id` from the href's
 * `/character/<id>` segment. Pure — no page access — so every rule here is unit-tested rather
 * than verified by hand against a live project root.
 *
 * A row missing either half is dropped rather than guessed at: no href means no id is
 * recoverable at all, and no alt means the row isn't a character card in the first place (it's
 * what `openCharacterPage`'s `:has(img[alt="<name>"])` locator already assumes — a card with no
 * alt simply never matches a name lookup, so it shouldn't surface here either).
 */
export function parseCharacters(raw: RawCharacterRow[]): CharacterListItem[] {
  const out: CharacterListItem[] = []
  for (const r of raw) {
    const href = r.href?.trim()
    const name = r.alt?.trim()
    if (!href || !name) continue
    const m = href.match(/\/character\/([0-9a-f-]+)/i)
    if (!m) continue
    out.push({ name, id: m[1]! })
  }
  return out
}
