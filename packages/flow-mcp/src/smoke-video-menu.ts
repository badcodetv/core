/**
 * What does Flow offer on an EXISTING clip?
 *
 * The question behind this: can we say "like that video, but slower" without re-uploading a
 * frame ourselves? platform-controls.md claims Omni Flash can edit an existing video (up to 3
 * conversational turns) and that Veo 3.1 Lite can Extend one — but those are the two matrix
 * rows still transcribed from Google's docs and never tested by us.
 *
 * Hovers each video tile and dumps its action menu. Credit-free: it opens menus, nothing else.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-menu.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-video-menu.ts <projectId>')

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
    forceClick(l: Locator): Promise<void>
    hoverElement(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(2500)

  const videos = page.locator('video')
  const count = await videos.count()
  console.log(`video tiles on the page: ${count}`)
  if (!count) throw new Error('no clips in this project — run one of the video smokes first')

  for (let i = 0; i < Math.min(count, 2); i++) {
    const tile = videos.nth(i)
    await tile.scrollIntoViewIfNeeded().catch(() => {})
    await inner.hoverElement(tile)
    await page.waitForTimeout(700)
    // The per-tile action button only mounts on hover; scope it to this tile's own card.
    // Dump every control the hover revealed anywhere near the tile, rather than guessing the
    // ancestor depth — the clip card's shape has never been mapped.
    const near = (await page.evaluate(`(() => [...document.querySelectorAll('button')]
      .map(b => (b.textContent || '').trim()).filter(t => t && t.length < 40))()`)) as string[]
    console.log(`[clip ${i}] buttons on page after hover:`, JSON.stringify(near.slice(0, 25)))
    // ⚠️ NOT .first(): the FIRST more_vert on the page is the top bar's project menu
    // (Rename / Trash / Delete). The per-clip one is the later of the two.
    const more = page.locator('button').filter({ hasText: /more_vert/ }).last()
    if (!(await more.count())) {
      console.log(`[clip ${i}] no more_vert anywhere`)
      continue
    }
    await inner.pointerClick(more)
    await page.waitForTimeout(1000)
    console.log(`[clip ${i}] menu:`, JSON.stringify(await page.evaluate(`(${MENU})()`)))
    await page.keyboard.press('Escape')
    await page.waitForTimeout(400)
  }
} finally {
  await client.close()
}
