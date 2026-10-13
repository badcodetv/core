// Money For Something: one still, Nano Banana 2, 16:9, x2, from a NEW prompt with project assets attached by name (a plate, a Flow Character).
// The client's own character picker fails on the Flow of 2026-10-14 (the @ picker stays open), so this uses the same attach() as mfs-clip.mts.
// usage: npx tsx mfs-still.mts <prompt.txt> <out.jpg> [--asset "mfst-plate-B.jpg" --asset "The Host"]
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
import { readFileSync } from 'node:fs'
const a = process.argv.slice(2)
const [promptFile, out] = a
const assets = a.flatMap((v, i) => (v === '--asset' ? [a[i + 1]] : []))
const prompt = readFileSync(promptFile, 'utf8').trim()
const uploads = a.flatMap((v, i) => (v === '--upload' ? [a[i + 1]] : []))
const c: any = await FlowClient.connect()
const page = c.page
const log = (...x: any[]) => console.log(new Date().toISOString().slice(11, 19), ...x)
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`
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
try {
  await page.keyboard.press('Escape').catch(() => {})
  await c.openProject({ id: 'cb27208c-4b16-426d-9144-c394f2735c15' })
  await c.reloadProject(); await c.ensureAgentOff()
  for (const u of uploads) { await c.uploadToProject(u); for (let i = 0; i < 8; i++) { await page.waitForTimeout(500); const ok = await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'I agree') as HTMLElement | undefined; b?.click(); return !!b }); if (ok) break } }
  await c.ensureImageMode(2, 'Nano Banana 2', '16:9')
  await c.setPrompt('')
  for (const n of assets) await attach(n)
  const box = page.locator('div[contenteditable="true"]').first()
  await box.evaluate((el: any) => el.focus()); await page.keyboard.press('Control+End'); await page.keyboard.insertText(' ' + prompt)
  await page.waitForTimeout(800)
  await page.screenshot({ path: out + '.bar.png' })
  const before = await c.snapshotMediaNames()
  await page.keyboard.press('Enter'); log('submitted')
  const canvases = await c.waitForNewCanvases(before, 2, 6 * 60_000)
  const cand = await c.harvestCandidates(canvases, out, 2)
  log('saved', JSON.stringify(cand.map((x: any) => x.path)))
} catch (e: any) { log('ERROR', String(e?.message ?? e).split('\n')[0]); await page.screenshot({ path: out + '.err.png' }).catch(() => {}); process.exitCode = 1 }
finally { await c.browser.close().catch(() => {}) }
