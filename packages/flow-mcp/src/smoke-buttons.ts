/**
 * Manual probe — dump every visible button's accessible text on the current page. NOT part
 * of CI. The fastest way to answer "what state is the UI actually in right now?"
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-buttons.ts [/regex/ filter]
 */
import { FlowClient } from './flow-client'

const filter = process.argv[2] ? new RegExp(process.argv[2], 'i') : null

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page
  console.log('url:', page.url())
  const buttons = (await page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('button, [role="button"], [role="tab"]')) {
      const r = el.getBoundingClientRect()
      if (!r.width || !r.height) continue
      out.push({ text: (el.textContent || '').trim().slice(0, 60), x: Math.round(r.left), y: Math.round(r.top) })
    }
    return out
  })()`)) as { text: string; x: number; y: number }[]
  for (const b of buttons) {
    if (!filter || filter.test(b.text)) console.log(`  [${b.x},${b.y}] ${b.text}`)
  }
} finally {
  await client.close()
}
