/**
 * C1 spike, part 3: actually FILL the Start and End frame slots from local files.
 *
 * Clicking a slot opens Flow's media picker (project selector, Images/Uploads tabs, "Upload
 * media", a grid of role="option" rows, and an "Add to Prompt" button). This proves the whole
 * fill path end to end without submitting: upload into Start, upload into End, then read back
 * what each slot is holding.
 *
 * Credit-free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frame-fill.ts <projectId> <startImage> <endImage>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, startImage, endImage] = process.argv.slice(2)
if (!projectId || !startImage) throw new Error('usage: smoke-frame-fill.ts <projectId> <startImage> [endImage]')

/**
 * What each frame slot currently holds. Anchor on the SWAP BUTTON and take its parent: that
 * row is exactly [Start tile, swap button, End tile]. An earlier version looked for any div
 * containing the swap text with few children and matched a page-level container instead,
 * reporting the entire media browser as the slot contents.
 */
const SLOTS = `() => {
  const swap = [...document.querySelectorAll('button')].find(b => /Swap first and last frames/.test(b.textContent || ''))
  if (!swap || !swap.parentElement) return { error: 'swap button not found' }
  return [...swap.parentElement.children].map(c => ({
    text: (c.textContent || '').trim().slice(0, 30),
    imgs: [...c.querySelectorAll('img')].map(im => (im.currentSrc || im.src || '').slice(-28)),
  }))
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    pointerClick(l: Locator): Promise<void>
    tabClick(l: Locator): Promise<void>
    forceClick(l: Locator): Promise<void>
    uploadFiles(paths: string[], reveal?: () => Promise<void>): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  const crop = page.getByRole('button', { name: /crop_/ }).first()
  if (!(await crop.count())) {
    const agent = page.getByRole('button', { name: 'Agent', exact: true })
    if (await agent.count()) await inner.forceClick(agent)
  }
  await crop.waitFor({ state: 'visible', timeout: 30_000 })
  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  if ((await videoTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(videoTab)
  const framesTab = page.locator('button[role="tab"]').filter({ hasText: /Frames/ }).first()
  if ((await framesTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(framesTab)
  await page.keyboard.press('Escape')
  await page.waitForTimeout(600)

  console.log('slots before:', JSON.stringify(await page.evaluate(`(${SLOTS})()`)))

  const fill = async (label: 'Start' | 'End', file: string) => {
    const base = file.split('/').pop() ?? file
    const slot = page.getByText(label, { exact: true }).first()
    await inner.forceClick(slot)
    await page.waitForTimeout(1000)
    await inner.uploadFiles([file], async () => {
      const up = page.locator('button').filter({ hasText: /^upload\s*Upload media$/i }).first()
      await up.waitFor({ state: 'visible', timeout: 30_000 })
      await inner.forceClick(up)
    })
    // Clicking the row IS the confirm — the picker closes and the slot fills; "Add to Prompt"
    // belongs to a multi-select path and is gone by the time you could click it (same rule as
    // the character "Add from Project" picker). Needs pointerClick: forceClick's in-page
    // el.click() leaves the row merely highlighted.
    const row = page.locator('[role="option"]').filter({ hasText: base }).first()
    await row.waitFor({ state: 'visible', timeout: 60_000 })
    // A freshly-uploaded row appears IMMEDIATELY but shows a spinner until the asset resolves,
    // and clicking it while it spins does nothing at all — silently, which is how the first
    // attempt "succeeded" into two empty slots. Wait for its thumbnail.
    for (let i = 0; i < 60; i++) {
      const thumb = row.locator('img').first()
      const src = (await thumb.count()) ? await thumb.getAttribute('src') : null
      if (src && /http/.test(src)) break
      await page.waitForTimeout(1000)
    }
    console.log(`  [${label}] row ready:`, JSON.stringify(await row.locator('img').first().getAttribute('src').catch(() => null)).slice(0, 60))
    await inner.pointerClick(row)
    await page.waitForTimeout(2500)
    console.log(`slots after ${label}:`, JSON.stringify(await page.evaluate(`(${SLOTS})()`)))
  }

  await fill('Start', startImage)
  if (endImage) await fill('End', endImage)
} finally {
  await client.close()
}
