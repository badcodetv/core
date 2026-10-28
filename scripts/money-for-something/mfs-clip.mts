// Money For Something: one Omni 1.1 Flash clip from a plate, with an optional Flow Character attached for its Voice.
// Adapted from scripts/camping-mv2/mv2run.mts (same tile detection and download path).
// usage: npx tsx mfs-clip.mts <plate.jpg> <prompt.txt> <out.mp4> [--char "The Host"] [--mode frames|ingredients] [--probe]
//   --probe stops before submit and saves a screenshot next to <out>, so a new layout can be checked for free.
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
import { readFileSync, existsSync, mkdirSync } from 'node:fs'
import { basename, dirname } from 'node:path'
const a = process.argv.slice(2)
const [plate, promptFile, out] = a
const opt = (k: string) => { const i = a.indexOf(k); return i > 0 ? a[i + 1] : undefined }
const chars = a.flatMap((v, i) => (v === '--char' ? [a[i + 1]] : []))
const mode = opt('--mode') ?? 'frames'
const probe = a.includes('--probe')
const prompt = readFileSync(promptFile, 'utf8').trim()
mkdirSync(dirname(out), { recursive: true })
if (existsSync(out) && !probe) { console.log('exists, skip', out); process.exit(0) }
const c: any = await FlowClient.connect()
const page = c.page
const log = (...x: any[]) => console.log(new Date().toISOString().slice(11, 19), ...x)
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`
const tileKey = async (i: number): Promise<string> => page.locator('flow-video-tile').nth(i).evaluate((e: any) => { const m = e.querySelector('video[src], img[src]'); return m ? (m.getAttribute('src') || '').split('?')[0] : 'pending:' + (e.textContent || '').slice(0, 40) }).catch(() => '')
const keys = async (): Promise<Set<string>> => new Set(await page.locator('flow-video-tile').evaluateAll((els: any[]) => els.map((e) => { const m = e.querySelector('video[src], img[src]'); return m ? (m.getAttribute('src') || '').split('?')[0] : '' }).filter(Boolean)))
const tileDone = async (i: number): Promise<boolean> => page.locator('flow-video-tile').nth(i).evaluate((e: any) => !!(e.querySelector('video[src], img[src]')) && !/\d+\s*%/.test(e.textContent || ''))
const clickText = async (t: string) => page.evaluate((t: string) => { const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === t || b.getAttribute('aria-label') === t) as HTMLElement | undefined; b?.click(); return !!b }, t)
const rows = () => page.evaluate(() => document.querySelectorAll('[role=option]').length)
async function attach(name: string) {
  const box = page.locator('div[contenteditable="true"]').first()
  await box.evaluate((el: any) => el.focus())
  await page.keyboard.press('Control+End')
  await page.keyboard.type('@')
  await page.waitForSelector('[role=option]', { timeout: 15000 })
  await page.locator('input[aria-label="Search assets"]').fill(name)
  await page.waitForTimeout(6000)
  const ok = await page.evaluate(([name, fire]: string[]) => { const el = [...document.querySelectorAll('[role=option]')].find((r: any) => r.innerText.trim().startsWith(name)); if (el) eval(fire)(el); return !!el }, [name, fire])
  if (!ok) throw new Error('ASSET_NOT_FOUND ' + name)
  await page.waitForTimeout(1500)
  if ((await rows()) > 0) { await page.evaluate((fire: string) => { const b = [...document.querySelectorAll('button')].find((x: any) => x.innerText.trim() === 'Add to prompt'); if (b) eval(fire)(b) }, fire); await page.waitForTimeout(1500) }
  if ((await rows()) > 0) throw new Error('PICKER_STILL_OPEN ' + name)
  log('attached', name)
}
async function download(i: number, to: string) {
  const tile = page.locator('flow-video-tile').nth(i)
  const dl = page.waitForEvent('download', { timeout: 60_000 }); dl.catch(() => {})
  await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
  const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
  await item.waitFor({ state: 'visible', timeout: 15_000 }); await item.click()
  const orig = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /Original size/i }).first()
  await orig.waitFor({ state: 'visible', timeout: 15_000 }); await orig.click()
  const d = await dl; await d.saveAs(to)
  await page.keyboard.press('Escape').catch(() => {})
}
try {
  await c.reloadProject(); await c.ensureAgentOff()
  if (!process.env.MFS_SKIP_UPLOAD) { await c.uploadToProject(plate); for (let i = 0; i < 8; i++) { await page.waitForTimeout(500); if (await clickText('I agree')) break } }
  await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: Number(process.env.MFS_DURATION ?? 8), count: 1, frames: mode === 'frames' })
  if (mode === 'frames') await c.fillFrameSlotRebuilt('Start', basename(plate))
  await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {})
  const before = await keys()
  await c.setPrompt('')
  if (mode !== 'frames') await attach(basename(plate))
  for (const ch of chars) await attach(ch)
  const box = page.locator('div[contenteditable="true"]').first()
  await box.evaluate((el: any) => el.focus()); await page.keyboard.press('Control+End'); await page.keyboard.insertText(' ' + prompt)
  await page.waitForTimeout(800)
  await page.screenshot({ path: out + '.bar.png' })
  log('box:', (await box.innerText()).replace(/\s+/g, ' ').slice(0, 160))
  if (probe) { log('probe only, not submitted'); process.exit(0) }
  await page.keyboard.press('Enter')
  log('submitted')
  const deadline = Date.now() + 12 * 60_000; let ok = false
  while (Date.now() < deadline) {
    const k0 = await tileKey(0)
    if (k0 && !before.has(k0)) {
      const txt: string = await page.locator('flow-video-tile').nth(0).evaluate((e: any) => e.textContent || '')
      if (/Failed/.test(txt)) throw new Error('FLOW_FAILED: ' + txt.replace(/\s+/g, ' ').slice(0, 120))
      if (await tileDone(0)) { ok = true; break }
    }
    await page.waitForTimeout(5000)
  }
  if (!ok) { await page.screenshot({ path: out + '.timeout.png' }); throw new Error('TIMEOUT') }
  await page.waitForTimeout(2000)
  for (let d = 1; ; d++) {
    try { await download(0, out); break } catch (e: any) {
      if (d >= 4) throw new Error('DOWNLOAD_FAILED (clip is rendered in Flow; harvest it, do not regenerate)')
      await page.keyboard.press('Escape').catch(() => {}); await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {}); await page.waitForTimeout(4000)
    }
  }
  log('saved', out)
} catch (e: any) { log('ERROR', String(e?.message ?? e).split('\n')[0]); await page.screenshot({ path: out + '.err.png' }).catch(() => {}); process.exitCode = 1 }
finally { await c.browser.close().catch(() => {}) }
