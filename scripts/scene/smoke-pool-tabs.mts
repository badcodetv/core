/**
 * Live check (no generation, no credits): a pool tab is tagged, `connect` skips it, and a sweep closes it.
 *   FLOW_CDP_PORT=<port> npx tsx scripts/scene/smoke-pool-tabs.mts
 */
import { chromium } from 'playwright'
import { FlowClient, isPoolTab } from '../../packages/flow-mcp/src/flow-client'

const EP = `http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`
const count = async () => {
  const b = await chromium.connectOverCDP(EP)
  const pages = b.contexts()[0]!.pages()
  const pool = [] as typeof pages
  for (const p of pages) if (await isPoolTab(p)) pool.push(p)
  return { b, all: pages.length, pool }
}
const before = await count(); await before.b.close()
const t = await FlowClient.openTab(EP, 'https://flow.google.com', 'smoke')
const mid = await count()
const attached: any = await FlowClient.connect(EP)
const skipped = !(await isPoolTab(attached.page))
await attached.close()
for (const p of mid.pool) await p.close()
await mid.b.close()
const after = await count(); await after.b.close()
await (t as any).browser.close().catch(() => {})
const ok = mid.all === before.all + 1 && mid.pool.length === before.pool.length + 1 && skipped && after.all === before.all && after.pool.length === 0
console.log(JSON.stringify({ before: before.all, opened: mid.all, poolTabs: mid.pool.length, connectSkippedPoolTab: skipped, after: after.all, ok }))
process.exit(ok ? 0 : 1)
