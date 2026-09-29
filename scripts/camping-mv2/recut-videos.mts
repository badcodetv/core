// Camping mv2 RE-CUT clips (2026-09-29): Omni 1.1 Flash · Frames · 16:9 · 720p · 8s · x1, one per accepted still.
// Derived from mv2run.mts. Plates: $RECUT_WORK/plates/recut-<id>.jpg (copies of clips/recut-stills/picks/).
// Usage: npx tsx scripts/camping-mv2/recut-videos.mts [id …]   (existing takes are skipped)
// Reuses FlowClient's private primitives; replaces tile detection (tiles now carry <video src>).
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
import { readFileSync, writeFileSync, existsSync, copyFileSync, mkdirSync } from 'node:fs'
const S = process.env.RECUT_WORK ?? `${process.env.HOME}/.cache/badcode-recut`  // work dir: plates/, takes/
const OUT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Camping Comic/music video/videos-recut'
const prompts: { id: string; prompt: string }[] = JSON.parse(readFileSync(new URL('./recut-videos.json', import.meta.url), 'utf8'))
const only = process.argv.slice(2)
const c: any = await FlowClient.connect()
const page = c.page
mkdirSync(OUT, { recursive: true }); mkdirSync(`${S}/takes`, { recursive: true })
await page.goto('https://flow.google.com/project/b93409d1-c1b9-4330-ae71-a07f65e2f780'); await page.waitForTimeout(5000)
const log = (...a: any[]) => console.log(new Date().toISOString().slice(11, 19), ...a)
const tileCount = async (): Promise<number> => page.locator('flow-video-tile').count()
const tileKey = async (i: number): Promise<string> => page.locator('flow-video-tile').nth(i).evaluate((e: any) => { const m = e.querySelector('video[src], img[src]'); return m ? (m.getAttribute('src') || '').split('?')[0] : 'pending:' + (e.textContent || '').slice(0, 40) }).catch(() => '')
const keys = async (): Promise<Set<string>> => new Set(await page.locator('flow-video-tile').evaluateAll((els: any[]) => els.map((e) => { const m = e.querySelector('video[src], img[src]'); return m ? (m.getAttribute('src') || '').split('?')[0] : '' }).filter(Boolean)))
const tileDone = async (i: number): Promise<boolean> => page.locator('flow-video-tile').nth(i).evaluate((e: any) => !!(e.querySelector('video[src], img[src]')) && !/\d+\s*%/.test(e.textContent || ''))
async function download(i: number, out: string) {
  const tile = page.locator('flow-video-tile').nth(i)
  const dl = page.waitForEvent('download', { timeout: 60_000 }); dl.catch(() => {})
  await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
  const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
  await item.waitFor({ state: 'visible', timeout: 15_000 })
  await item.click()
  const orig = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /Original size/i }).first()
  await orig.waitFor({ state: 'visible', timeout: 15_000 })
  await orig.click()
  const d = await dl
  await d.saveAs(out)
  await page.keyboard.press('Escape').catch(() => {})
}
const clickText = async (t: string) => page.evaluate((t: string) => { const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === t || b.getAttribute('aria-label') === t) as HTMLElement | undefined; b?.click(); return !!b }, t)
async function closeAgentPanel() {
  if (await page.locator('flow-agent-panel').count()) { await page.evaluate(() => { const p = document.querySelector('flow-agent-panel'); const b = p && [...p.querySelectorAll('button')].find((b) => b.getAttribute('aria-label') === 'Close') as HTMLElement | undefined; b?.click() }); await page.waitForTimeout(800) }
}
const uploaded = new Set<string>()
async function upload(path: string) {
  if (uploaded.has(path)) { log('  plate already uploaded, reusing'); return }
  await c.uploadToProject(path)
  uploaded.add(path)
  for (let i = 0; i < 20; i++) { await page.waitForTimeout(500); if (await clickText('I agree')) { log('  agreed rights dialog'); break } }
}
async function one(p: { id: string; prompt: string }) {
  const nn = p.id
  const take = `${S}/takes/${nn}.mp4`
  if (existsSync(take)) { log(nn, 'exists, skip'); return }
  if (process.env.HARVEST_ONLY) { await download(Number(process.env.HARVEST_INDEX ?? 0), take); copyFileSync(take, `${OUT}/${nn}.mp4`); log(nn, 'harvested'); return }
  const plate = `${S}/plates/recut-${nn}.jpg`
  await c.reloadProject(); await closeAgentPanel(); await c.ensureAgentOff()
  await upload(plate)
  await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: 8, count: 1, frames: true })
  await c.fillFrameSlotRebuilt('Start', `recut-${nn}.jpg`)
  await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {})
  const before = await keys()
  await c.setPrompt(p.prompt)
  await c.clickSubmit()
  log(nn, 'submitted')
  const deadline = Date.now() + 12 * 60_000
  let ok = false
  while (Date.now() < deadline) {
    const card = await c.detectFailureCard().catch(() => null)
    if (card === 'blocked') throw new Error(`POLICY_BLOCKED ${nn}`)
    const k0 = await tileKey(0)
    if (k0 && !before.has(k0)) {
      const txt: string = await page.locator('flow-video-tile').nth(0).evaluate((e: any) => e.textContent || '')
      if (/Failed/.test(txt)) throw new Error(`FLOW_FAILED ${nn}: ${txt.replace(/\s+/g, ' ').slice(0, 90)}`)
      if (await tileDone(0)) { ok = true; break }
    }
    await page.waitForTimeout(5000)
  }
  if (!ok) throw new Error(`TIMEOUT ${nn}`)
  await page.waitForTimeout(2000)
  for (let d = 1; ; d++) {
    try { await download(0, take); break } catch (e: any) {
      if (d >= 4) throw new Error(`DOWNLOAD_FAILED ${nn} (clip is rendered in Flow; harvest it, do not regenerate)`)
      log('  download retry', d, String(e?.message ?? e).split('\n')[0])
      await page.keyboard.press('Escape').catch(() => {})
      await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
      await page.waitForTimeout(4000)
    }
  }
  copyFileSync(take, `${OUT}/${nn}.mp4`)
  log(nn, 'saved')
}
try {
  const queue = prompts.filter((p) => !only.length || only.includes(p.id))
  const deferred: typeof queue = []
  for (const [qi, p] of [...queue, ...queue].entries()) {
    if (qi >= queue.length && !deferred.includes(p)) continue
    for (let attempt = 1; ; attempt++) {
      try { await one(p); break } catch (e: any) {
        const m = String(e?.message ?? e).split('\n')[0]
        if (/POLICY_BLOCKED|DOWNLOAD_FAILED/.test(m)) { log('SKIP', p.id, m); break }
        if (attempt >= 4) { if (qi < queue.length) { deferred.push(p); log('DEFER', p.id, m) } else log('GAVE UP', p.id, m); break }
        const wait = 10_000
        log('RETRY', p.id, 'attempt', attempt, m, 'waiting', wait / 1000, 's')
        await page.waitForTimeout(wait)
        await page.keyboard.press('Escape').catch(() => {})
        await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
        log('  refreshed page')
      }
    }
  }
} catch (e: any) { log('ERROR', e?.message?.split('\n')[0]); process.exitCode = 1 }
finally { await c.browser.close().catch(() => {}) }
