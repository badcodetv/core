/**
 * L2, second surface · the clip's OWN page.
 *
 * The per-clip hover menu offers neither `Extend` nor `Edit` on ANY tier we have generated on —
 * Veo 3.1 Fast, Veo 3.1 Lite and Omni Flash all return the identical 11 items. Before calling
 * the matrix wrong, check the other place those controls could live: the clip tile is wrapped in
 * an `<a>`, so clicking it opens a detail view with its own controls.
 *
 * Credit-free: navigates and reads.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-clip-detail.ts <projectId> <clipMediaId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, clipId] = process.argv.slice(2)
if (!projectId || !clipId) throw new Error('usage: smoke-clip-detail.ts <projectId> <clipMediaId>')

const CONTROLS = `() => ({
  url: location.href,
  buttons: [...document.querySelectorAll('button, [role="menuitem"], [role="tab"], a')]
    .filter(el => el.getBoundingClientRect().width > 0)
    .map(el => (el.textContent || '').trim())
    .filter(t => t && t.length < 45),
})`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; forceClick(l: Locator): Promise<void>; hoverElement(l: Locator): Promise<void> }
  const page = inner.page
  await client.openProject({ id: projectId })

  const thumb = page.locator(`img[alt="Video thumbnail"][src*="${clipId}"]`).first()
  await thumb.waitFor({ state: 'visible', timeout: 60_000 })
  await thumb.scrollIntoViewIfNeeded().catch(() => {})
  await inner.hoverElement(thumb)
  await page.waitForTimeout(500)
  // The tile's own <a>/<button> wrapper — click the card, not the hover controls sitting on it.
  const link = page.locator(`video[src*="${clipId}"]`).first().locator('xpath=ancestor::a[1]')
  if (!(await link.count())) throw new Error('clip tile has no <a> wrapper — remap')
  await inner.forceClick(link)
  await page.waitForTimeout(3500)

  const state = (await page.evaluate(`(${CONTROLS})()`)) as { url: string; buttons: string[] }
  console.log(`url: ${state.url}`)
  console.log(`controls (${state.buttons.length}):\n  ${state.buttons.join('\n  ')}`)

  // Clicking a clip lands in Flow's SCENE EDITOR (/edit/<sceneId>), not a plain player — so the
  // page's own `more_vert` is a second menu worth dumping before concluding anything.
  const more = page.locator('button').filter({ hasText: /^more_vert\s*More$/ }).first()
  let menu: string[] | null = null
  if (await more.count()) {
    await inner.forceClick(more)
    await page.waitForTimeout(1000)
    menu = (await page.evaluate(`(() => {
      const roots = [...document.querySelectorAll('[role="menu"], [data-radix-popper-content-wrapper]')]
      const root = roots.length ? roots[roots.length - 1] : null
      if (!root) return null
      return [...root.querySelectorAll('[role="menuitem"], button')].map(el => (el.textContent || '').trim()).filter(Boolean)
    })()`)) as string[]
    console.log(`\nscene-editor more_vert menu: ${JSON.stringify(menu)}`)
    await page.keyboard.press('Escape')
  }

  // Third and last surface: the scene editor's TIMELINE. If "Extend" exists anywhere it is most
  // likely an action on the clip in the strip, not on the gallery tile.
  const strip: string[] = []
  const thumbs = page.locator('img[alt="Video thumbnail"], video')
  const n = Math.min(await thumbs.count(), 3)
  for (let i = 0; i < n; i++) {
    await inner.hoverElement(thumbs.nth(i)).catch(() => {})
    await page.waitForTimeout(600)
    const now = (await page.evaluate(`(${CONTROLS})()`)) as { buttons: string[] }
    for (const t of now.buttons) if (!state.buttons.includes(t) && !strip.includes(t)) strip.push(t)
  }
  console.log(`\ncontrols revealed by hovering the timeline: ${JSON.stringify(strip)}`)

  const all = [...state.buttons, ...(menu ?? []), ...strip]
  console.log(`\nExtend present: ${all.some((t) => /extend/i.test(t)) ? 'YES' : 'no'}`)
  console.log(`Edit present:   ${all.some((t) => /\bedit\b/i.test(t)) ? 'YES' : 'no'}`)
} finally {
  await client.close()
}
