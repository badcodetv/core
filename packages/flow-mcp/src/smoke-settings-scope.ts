/**
 * Manual DOM-mapping probe — how do we scope to the "Video generation default" section?
 * NOT part of CI.
 *
 * The Agent settings panel has TWO sections whose aspect and count tabs are named
 * identically ("16:9", "x1"…), Image first and Video second, so ensureVideoSettings' `.first()`
 * has been configuring the IMAGE defaults. This finds a container that holds one section and
 * not the other. Run with the Agent settings panel already open.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-settings-scope.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page

  const out = await page.evaluate(`(() => {
    const heads = [...document.querySelectorAll('*')].filter(
      el => !el.children.length && (el.textContent || '').trim() === 'Video generation default',
    )
    if (!heads.length) return { error: 'heading not found — is the Settings panel open?' }
    const head = heads[0]
    const rows = []
    let n = head.parentElement, depth = 1
    while (n && depth <= 6) {
      const tabs = [...n.querySelectorAll('[role="tab"], button')]
        .map(t => (t.textContent || '').trim())
        .filter(Boolean)
      rows.push({
        depth,
        tag: n.tagName,
        containsImageSection: (n.textContent || '').includes('Image generation default'),
        tabCount: tabs.length,
        tabs: tabs.slice(0, 14),
      })
      n = n.parentElement; depth++
    }
    return { rows }
  })()`)
  console.log(JSON.stringify(out, null, 2))
} finally {
  await client.close()
}
