/**
 * Probe Flow's video download menu (2026-11-27, Kai: "we should always generate at 1080p").
 * Opens a project in its own tab, opens tile N's Download submenu, prints every row, and (with ROW=<regex>)
 * clicks that row and saves the file. Usage:
 *   npx tsx scripts/scene/probe-upscale.mts <projectId> <tileIndex> [outPath]   (ROW='1080p' to download)
 */
import { copyFileSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'
import { DOWNLOAD_LOCK, withLock } from '../../packages/flow-mcp/src/lock'

const [PROJECT, IDX = '0', OUT] = process.argv.slice(2)
const ROW = process.env.ROW
const ENDPOINT = process.env.FLOW_CDP ?? `http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`
const c: any = await FlowClient.openTab(ENDPOINT, `https://flow.google.com/project/${PROJECT}`, 'probe')
const page = c.page
await page.waitForTimeout(6000)
const tiles = page.locator('flow-video-tile')
console.log(JSON.stringify({ tiles: await tiles.count() }))
const tile = tiles.nth(Number(IDX))
await tile.scrollIntoViewIfNeeded().catch(() => {})
await withLock(DOWNLOAD_LOCK, async () => {
  const ps = await page.context().newCDPSession(page)
  const { targetInfo } = await ps.send('Target.getTargetInfo')
  await ps.detach().catch(() => {})
  const cdp = await c.browser.newBrowserCDPSession()
  const dir = mkdtempSync(join(process.env.TMPDIR ?? tmpdir(), 'flowdl-'))
  try {
    const dl = { behavior: 'allowAndName', downloadPath: dir, eventsEnabled: true }
    try { await cdp.send('Browser.setDownloadBehavior', { ...dl, browserContextId: targetInfo.browserContextId } as any) }
    catch { await cdp.send('Browser.setDownloadBehavior', dl as any) }
    const done = new Promise<string>((ok, bad) => {
      const t = setTimeout(() => bad(new Error('DOWNLOAD_TIMEOUT')), 300_000)
      cdp.on('Browser.downloadProgress', (e: any) => {
        if (e.state === 'completed') { clearTimeout(t); ok(e.guid) }
        else if (e.state === 'canceled') { clearTimeout(t); bad(new Error('DOWNLOAD_CANCELED')) }
      })
    })
    done.catch(() => {})
    await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
    const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
    await item.waitFor({ state: 'visible', timeout: 15_000 })
    await item.click()
    await page.waitForTimeout(1500)
    const rows = await page.locator('.cdk-overlay-container [role="menuitem"]').allInnerTexts()
    console.log(JSON.stringify({ rows: rows.map((r: string) => r.replace(/\s+/g, ' ').trim()) }))
    if (ROW && OUT) {
      const t0 = Date.now()
      await page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: new RegExp(ROW, 'i') }).first().click()
      const guid = await done
      copyFileSync(join(dir, guid), OUT)
      console.log(JSON.stringify({ saved: OUT, seconds: (Date.now() - t0) / 1000 }))
    }
    await page.keyboard.press('Escape').catch(() => {})
  } finally {
    await cdp.detach().catch(() => {})
    rmSync(dir, { recursive: true, force: true })
  }
})
await page.close().catch(() => {})
process.exit(0)
