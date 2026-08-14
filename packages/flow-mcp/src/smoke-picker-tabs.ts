/**
 * Does the asset picker show CLIPS, and does that depend on the compose bar's mode?
 *
 * `flow_list_media` returned zero video rows in a project that demonstrably holds clips, while
 * the bar was in Video mode — and the picker there offers only All/Images/Characters/Uploads.
 * The suspicion: in a video source mode the picker is filtered to valid ingredients (stills),
 * so the one tool that can recover a clip's mediaId for `flow_refine_video` goes blind exactly
 * when you have just made a clip.
 *
 * Dumps the picker's tabs and its video-row count in the CURRENT mode, then in image mode.
 * Credit-free (ensureImageMode only moves compose-bar controls).
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-picker-tabs.ts <projectId>
 */
import type { Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-picker-tabs.ts <projectId>')

const TABS = `(() => [...document.querySelectorAll('[role="tab"]')].map(t => (t.textContent||'').trim()))()`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; ensureImageMode(c?: number, m?: string, a?: string): Promise<void> }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(2500)

  for (const phase of ['as-left', 'image-mode'] as const) {
    if (phase === 'image-mode') await inner.ensureImageMode()
    const bar = (await page.evaluate(`(() => [...document.querySelectorAll('button')].map(b => (b.textContent||'').trim()).filter(t => /Swap first and last|Video\\s*·|crop_/.test(t)))()`)) as string[]
    const items = await client.listMedia({ limit: 60 })
    const tabs = (await page.evaluate(TABS)) as string[]
    const vids = items.filter((i) => /video/i.test(String(i.kind)))
    console.log(`\n[${phase}] bar: ${JSON.stringify(bar)}`)
    console.log(`[${phase}] picker tabs: ${JSON.stringify(tabs)}`)
    console.log(`[${phase}] rows: ${items.length}, video rows: ${vids.length}`)
    for (const v of vids) console.log(`   ${v.mediaId ?? '(no mediaId)'}  ${v.title.slice(0, 40)}`)
  }
} finally {
  await client.close()
}
