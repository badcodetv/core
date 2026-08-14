/**
 * L2 · Are `Extend` and `Edit existing video` real, and are they really tier-locked?
 *
 * `platform-controls.md` claims Extend is Veo 3.1 Lite only and video Edit is Omni Flash only.
 * Both are transcribed from Google's docs and never tested — and BOTH columns we have tested
 * turned out wrong, which is the whole argument for not trusting these two. A Veo 3.1 Fast clip
 * showed neither action, which is consistent with the claim but proves nothing on its own.
 *
 * ⚠️ Spends credits: one 4s clip per tier named on the command line (Veo 3.1 Lite ≈ 10,
 * Omni Flash ≈ 15). Text-to-video, so nothing is uploaded. The menu dump afterwards is free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-tier-menus.ts <projectId> <outDir> [model...]
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, outDir, ...models] = process.argv.slice(2)
if (!projectId || !outDir) throw new Error('usage: smoke-tier-menus.ts <projectId> <outDir> [model...]')
const TIERS = models.length ? models : ['Veo 3.1 Lite', 'Omni Flash']

const MOTION = 'A single plain metal disc resting on a dark wooden table, one thin light from above. The light dims slightly. No cuts.'

const MENU = `() => {
  const roots = [...document.querySelectorAll('[role="menu"], [data-radix-popper-content-wrapper]')]
  const root = roots.length ? roots[roots.length - 1] : null
  if (!root) return null
  return [...root.querySelectorAll('[role="menuitem"], button')].map(el => (el.textContent || '').trim()).filter(Boolean)
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    pointerClick(l: Locator): Promise<void>
    hoverElement(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  for (const model of TIERS) {
    const slug = model.toLowerCase().replace(/[^a-z0-9]+/g, '-')
    const started = Date.now()
    const clip = await client.generateVideo({
      motion: MOTION,
      outPath: `${outDir}/${slug}.mp4`,
      model,
      durationSeconds: 4,
    })
    console.log(`\n=== ${model} — ${clip.mediaId} in ${((Date.now() - started) / 1000).toFixed(1)}s`)

    // Hover the thumbnail (which the hover swaps out for the <video>), then anchor the card on
    // the video — see openClipMenu for why these cannot be the same element.
    const thumb = page.locator(`img[alt="Video thumbnail"][src*="${clip.mediaId}"]`).first()
    await thumb.waitFor({ state: 'visible', timeout: 60_000 })
    await thumb.scrollIntoViewIfNeeded().catch(() => {})
    await inner.hoverElement(thumb)
    const card = page
      .locator(`video[src*="${clip.mediaId}"]`)
      .first()
      .locator('xpath=ancestor::div[.//button[contains(., "more_vert")]][1]')
    const more = card.locator('button:has-text("more_vert")').first()
    await more.waitFor({ state: 'visible', timeout: 15_000 })
    await inner.pointerClick(more)
    await page.waitForTimeout(1000)
    const items = (await page.evaluate(`(${MENU})()`)) as string[] | null
    console.log(`menu: ${JSON.stringify(items)}`)
    console.log(`  Extend present: ${items?.some((t) => /extend/i.test(t)) ? 'YES' : 'no'}`)
    console.log(`  Edit present:   ${items?.some((t) => /\bedit\b/i.test(t)) ? 'YES' : 'no'}`)
    await page.keyboard.press('Escape')
    await page.waitForTimeout(500)
  }
} finally {
  await client.close()
}
