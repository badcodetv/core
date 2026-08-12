/**
 * Map the DOM of a finished CLIP's card (as opposed to a still's, which `openAnimateMenu`
 * already knows). The still's control is a `more_vert` inside the img's grandparent; that
 * ancestor xpath finds nothing on a clip, so this dumps where the control actually lives.
 *
 * Credit-free: hovers and reads. Usage: npx tsx packages/flow-mcp/src/smoke-clip-card.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-clip-card.ts <projectId>')

const PROBE = `() => {
  // Hover SWAPS the thumbnail out for the live <video> preview, so anchor on whichever is
  // present — a probe anchored only on the thumbnail goes blind exactly when it matters.
  const thumb = document.querySelector('img[alt="Video thumbnail"]') || document.querySelector('video')
  if (!thumb) return { error: 'no clip tile (neither thumbnail nor video)' }
  const tb = thumb.getBoundingClientRect()
  const path = (el) => {
    const out = []
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      out.unshift(n.tagName.toLowerCase() + (n.className && typeof n.className === 'string' ? '.' + n.className.trim().split(/\\s+/).join('.') : ''))
    }
    return out.slice(-6).join(' > ')
  }
  // How far up from the thumbnail do you have to walk to find a more_vert?
  let depth = -1
  for (let n = thumb, i = 0; n && i < 12; n = n.parentElement, i++) {
    if (n.querySelector && [...n.querySelectorAll('button')].some(b => (b.textContent||'').includes('more_vert'))) { depth = i; break }
  }
  const buttons = [...document.querySelectorAll('button')]
    .map(b => ({ text: (b.textContent||'').trim().slice(0, 30), r: b.getBoundingClientRect(), path: path(b) }))
    .filter(b => b.r.width > 0)
    .map(b => ({
      text: b.text,
      overThumb: b.r.left >= tb.left - 20 && b.r.right <= tb.right + 20 && b.r.top >= tb.top - 20 && b.r.bottom <= tb.bottom + 20,
      box: [Math.round(b.r.left), Math.round(b.r.top), Math.round(b.r.width), Math.round(b.r.height)],
      path: b.path,
    }))
  return {
    thumbBox: [Math.round(tb.left), Math.round(tb.top), Math.round(tb.width), Math.round(tb.height)],
    ancestorDepthWithMoreVert: depth,
    thumbPath: path(thumb),
    overThumb: buttons.filter(b => b.overThumb),
    moreVerts: buttons.filter(b => b.text.includes('more_vert')),
  }
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; hoverElement(l: Locator): Promise<void> }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(3000)

  console.log('BEFORE HOVER:', JSON.stringify(await page.evaluate(`(${PROBE})()`), null, 1))
  const tile = page.locator('img[alt="Video thumbnail"]').first()
  await tile.scrollIntoViewIfNeeded().catch(() => {})
  await inner.hoverElement(tile)
  await page.waitForTimeout(1200)
  console.log('AFTER HOVER:', JSON.stringify(await page.evaluate(`(${PROBE})()`), null, 1))
} finally {
  await client.close()
}
