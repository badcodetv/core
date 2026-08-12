/**
 * Manual probe — wait for a NEW video to finish rendering, then harvest it. NOT part of CI.
 * Spends nothing; it collects work already paid for, which is what you want after a
 * generation timed out with Flow still queueing it.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-watch-video.ts <known-id> <out.mp4> [minutes]
 */
import { FlowClient } from './flow-client'
import { contentTypeOf, harvestToFile } from './harvest'

const known = new Set((process.argv[2] ?? '').split(',').filter(Boolean))
const out = process.argv[3] ?? '/tmp/flow-latest.mp4'
const minutes = Number(process.argv[4] ?? 25)

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    scrapeMediaNames(): Promise<string[]>
  }
  const deadline = Date.now() + minutes * 60_000
  while (Date.now() < deadline) {
    await inner.ensureProjectRoot()
    await inner.page.waitForTimeout(2000)
    for (const n of await inner.scrapeMediaNames()) {
      if (known.has(n)) continue
      const ct = await contentTypeOf(inner.page.request, n).catch(() => '')
      if (!ct.startsWith('video/')) continue
      await harvestToFile(inner.page.request, n, out)
      console.log('NEW VIDEO', n, '->', out)
      process.exit(0)
    }
    console.log(`${new Date().toISOString().slice(11, 19)} still waiting`)
    await inner.page.waitForTimeout(60_000)
  }
  console.log('gave up waiting')
} finally {
  await client.close()
}
