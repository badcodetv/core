/**
 * `href` is optional: KNOWN ISSUE (automation-images.md:269-276) — the projects grid can render
 * a tile as a bare `<div>` with no `<a href>` at all. SCRAPE_PROJECTS can only discover tiles
 * that ARE anchors (that is the only evidenced selector we have — no locator for the div-only
 * variant is recorded anywhere, so recovering ITS name blind is out of scope here, same as any
 * other no-selector-knowledge gap). What this type change buys is that every consumer
 * (pickProject, toProjectSummaries) stays honest about a tile that has a name but nothing to
 * click or navigate to, instead of assuming href always exists.
 */
export interface ProjectTile { name: string; href?: string }

export interface ProjectSummary {
  name: string
  /** Present only when `href` was derivable — see `projectIdFromHref`. */
  id?: string
  href?: string
}

/** Returns the href of the first tile whose name matches (case-insensitive, trimmed), else null. */
export function pickProject(tiles: ProjectTile[], name: string): string | null {
  const want = name.trim().toLowerCase()
  const hit = tiles.find((t) => t.name.trim().toLowerCase() === want)
  return hit?.href ?? null
}

/**
 * Pull the project id out of a Flow project href
 * ("/fx/tools/flow/project/<id>" or "https://labs.google/fx/tools/flow/project/<id>?x=y" →
 * "<id>"). Returns undefined for a missing/malformed href rather than throwing — every caller
 * of this (flow_list_projects, flow_create_project's readback) needs to degrade gracefully on
 * the documented href-less-tile bug, not crash on it.
 */
export function projectIdFromHref(href: string | undefined): string | undefined {
  if (!href) return undefined
  const m = href.match(/\/project\/([^/?#]+)/)
  return m?.[1] || undefined
}

/**
 * Turn scraped project tiles into the caller-facing summary shape. Never throws: a tile with
 * no href (the href-less-grid bug) still contributes its name, just with `id`/`href` omitted —
 * a partial list is far more useful to a caller than an error, and this is the documented
 * failure mode this function exists to absorb.
 */
export function toProjectSummaries(tiles: ProjectTile[]): ProjectSummary[] {
  return tiles.map((t) => {
    const id = projectIdFromHref(t.href)
    return { name: t.name, ...(id ? { id } : {}), ...(t.href ? { href: t.href } : {}) }
  })
}

/**
 * In-page scraper (evaluated as `(${SCRAPE_PROJECTS})()`), mirroring dom.ts's SCRAPE_IMGS pattern.
 * Confirmed live 2026-06-30: project <a> anchors carry an empty text node — the visible name
 * lives in a sibling styled-components span with a HASHED class (so we cannot key on class).
 * For each project anchor we climb ancestors and take the first own-text node that is short and
 * is not an edit/delete affordance label. Untitled projects fall back to their date label.
 *
 * ⚠️ KNOWN GAP (automation-images.md:269-276): the projects grid can render a tile as a bare
 * `<div>` with NO `<a>` at all — this loop is rooted at `a[href*=…]`, so those tiles are
 * structurally invisible to it, not merely missing an href to read. No selector for that
 * div-only variant is recorded anywhere (blind Wave A work cannot invent one — same rule as
 * Wave C's Frames-to-Video gap), so this scrape still only returns anchor-backed tiles. What
 * IS fixed here: an anchor whose href attribute reads empty (a lesser, plausible variant of
 * the same bug) no longer gets silently dropped — the name still ships, `href` just comes back
 * falsy, matching the widened `ProjectTile.href?` type so `toProjectSummaries` can degrade
 * gracefully instead of every consumer needing its own guard.
 */
export const SCRAPE_PROJECTS = `() => {
  const ownText = (el) => Array.from(el.childNodes)
    .filter((n) => n.nodeType === 3)
    .map((n) => n.textContent.trim())
    .join('')
    .trim()
  const out = []
  for (const a of document.querySelectorAll('a[href*="/fx/tools/flow/project/"]')) {
    const href = a.getAttribute('href') || ''
    let name = ''
    let node = a
    for (let i = 0; i < 8 && node; i++) {
      for (const el of node.querySelectorAll('*')) {
        const t = ownText(el)
        if (t && t.length < 40 && !/^(edit|delete)/i.test(t)) { name = t; break }
      }
      if (name) break
      node = node.parentElement
    }
    out.push(href ? { name, href } : { name })
  }
  return out
}`
