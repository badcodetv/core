/**
 * Manual probe — screenshot the current Flow page. NOT part of CI.
 *
 * Exists so a DOM-derived claim (a name read out of an `alt`, say) can be checked against
 * what the UI actually shows, rather than trusting one attribute twice.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-shot.ts <out.png> [url]
 */
import { FlowClient } from './flow-client'

const out = process.argv[2] ?? '/tmp/flow-shot.png'
const url = process.argv[3]

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page
  if (url) {
    await page.goto(url, { waitUntil: 'domcontentloaded' })
    await page.waitForTimeout(3000)
  }
  await page.screenshot({ path: out, fullPage: false })
  console.log('url:', page.url())
  console.log('shot:', out)
} finally {
  await client.close()
}
