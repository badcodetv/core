/**
 * Manual DOM-mapping probe — find the container that holds ONE media tile together with its
 * own more_vert control. NOT part of CI.
 *
 * openAnimateMenu resolved the control with `:near(img[alt="Generated image"])`, which matches
 * a control near ANY tile, so `.first()` animated whichever tile happened to come first —
 * confirmed live 2026-08-12 by a clip that animated a completely different still.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-tile-card.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    hoverElement(l: unknown): Promise<void>
  }
  const page = inner.page
  await inner.ensureProjectRoot()
  await page.waitForTimeout(2000)

  const alts = await page.evaluate(`(() => {
    const counts = {}
    for (const im of document.querySelectorAll('img[alt]')) {
      const a = im.getAttribute('alt') || ''
      counts[a] = (counts[a] || 0) + 1
    }
    return counts
  })()`)
  console.log('=== img alt histogram ===')
  console.log(JSON.stringify(alts, null, 2))

  // Hover the SECOND tile, then ask: where does a more_vert appear relative to it?
  const tiles = page.locator('img[alt="Generated image"]')
  console.log('generated-image tiles:', await tiles.count())
  if (await tiles.count()) {
    const target = tiles.nth(1)
    await inner.hoverElement(target)
    await page.waitForTimeout(800)
    const info = await target.evaluate(el => {
      const out: unknown[] = []
      let n: Element | null = el
      for (let d = 0; d < 8 && n; d++) {
        const mv = [...n.querySelectorAll('button')].filter(b =>
          (b.textContent || '').includes('more_vert'),
        )
        const imgs = n.querySelectorAll('img[alt="Generated image"]').length
        out.push({ depth: d, tag: n.tagName, imgsInside: imgs, moreVertInside: mv.length })
        n = n.parentElement
      }
      return out
    })
    console.log('=== ancestor chain of tile[1] ===')
    console.log(JSON.stringify(info, null, 2))

    const visibleMv = await page.evaluate(`(() => {
      const out = []
      for (const b of document.querySelectorAll('button')) {
        if (!(b.textContent || '').includes('more_vert')) continue
        const r = b.getBoundingClientRect()
        if (!r.width || !r.height) continue
        out.push({ x: Math.round(r.left), y: Math.round(r.top), text: (b.textContent || '').trim().slice(0, 30) })
      }
      return out
    })()`)
    console.log('=== visible more_vert buttons while tile[1] hovered ===')
    console.log(JSON.stringify(visibleMv, null, 2))
  }
} finally {
  await client.close()
}
