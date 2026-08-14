/**
 * Manual probe — find the newest video in the open project and harvest it. NOT part of CI.
 * Spends NOTHING: it collects a clip that has already been generated (and paid for), which
 * is exactly what you want after a generation timed out while Flow was still queueing it.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-harvest-video.ts <out.mp4>
 */
import { FlowClient } from './flow-client'

const out = process.argv[2] ?? '/tmp/flow-harvested.mp4'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    scrapeMediaNames(): Promise<string[]>
  }
  await inner.ensureProjectRoot()
  await inner.page.waitForTimeout(2500)

  const { contentTypeOf, harvestToFile } = await import('./harvest')
  const names = await inner.scrapeMediaNames()
  console.log(`${names.length} media ids on the page`)

  const videos: string[] = []
  for (const n of names) {
    const ct = await contentTypeOf(inner.page.request, n).catch(() => '')
    if (ct.startsWith('video/')) videos.push(n)
  }
  console.log('video media ids:', videos)
  if (!videos.length) {
    console.log('no video yet — still rendering or queued')
  } else {
    const newest = videos[videos.length - 1]!
    await harvestToFile(inner.page.request, newest, out)
    console.log('harvested', newest, '->', out)
  }
} finally {
  await client.close()
}
