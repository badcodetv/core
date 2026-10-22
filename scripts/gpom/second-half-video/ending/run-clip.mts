/**
 * GPOM second half, the ENDING run (scenes C/D/E, 2026-10-21): ONE Flow video job per invocation, priced and
 * logged before it spends. A copy of run-cut3.mts with its own Flow project (FLOW_PROJECT), ledger
 * (ending/ledger.json, the run total against CAP=1500), log (ending/run.log) and md5 pool (clips/second-half/ending).
 *
 *   FLOW_CDP_PORT=<port> FLOW_PROJECT=<uuid> npx tsx scripts/gpom/second-half-video/ending/run-clip.mts <job.json>
 *   job.json: { key, scene?, src, motion, out, count?: 1|2, duration?: 4|6|8|10, character?: string }
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, unlinkSync, writeFileSync } from 'node:fs'
import { basename, dirname, join } from 'node:path'
import { FlowClient } from '../../../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../../../..', import.meta.url).pathname
const HERE = join(REPO, 'scripts/gpom/second-half-video/ending')
const PROJECT = process.env.FLOW_PROJECT ?? (() => { throw new Error('FLOW_PROJECT unset') })()
const STAGE = join(process.env.HOME!, '.cache/badcode-gpom-ending/plates')
const VIDEO = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending'
const LOG = join(HERE, 'run.log')
const LEDGER = join(HERE, 'ledger.json')
const CAP = Number(process.env.CAP ?? 1500)
const MAX_PER_CLIP = Number(process.env.MAX_PER_CLIP ?? 20)
const RENDER_MS = Number(process.env.RENDER_MS ?? 12 * 60_000)

type Job = { key: string; scene?: string; src: string; motion: string; out: string; count?: number; duration?: number; character?: string }
const job: Job = JSON.parse(readFileSync(process.argv[2]!, 'utf8'))
const count = job.count ?? 1
const duration = job.duration ?? 8
const ledger: { spent: number; jobs: unknown[] } = existsSync(LEDGER) ? JSON.parse(readFileSync(LEDGER, 'utf8')) : { spent: 0, jobs: [] }
mkdirSync(STAGE, { recursive: true })
mkdirSync(dirname(job.out), { recursive: true })

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), key: job.key, ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

const c: any = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT}`)
const page = c.page
const sleep = (ms: number) => page.waitForTimeout(ms)

const topTiles = async (n: number) =>
  page.locator('flow-video-tile').evaluateAll((els: any[], n: number) => els.slice(0, n).map((e) => {
    const m = e.querySelector('video[src], img[src]')
    const t = e.textContent || ''
    return { key: m ? (m.getAttribute('src') || '').split('?')[0] : '', failed: /Failed/.test(t), pct: /\d+\s*%/.test(t), text: t.replace(/\s+/g, ' ').slice(0, 90) }
  }), n)
const allKeys = async (): Promise<Set<string>> => new Set((await topTiles(999)).map((t: any) => t.key).filter(Boolean))
const clickText = async (t: string) => page.evaluate((t: string) => {
  const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === t || b.getAttribute('aria-label') === t) as HTMLElement | undefined
  b?.click(); return !!b
}, t)

async function balance(): Promise<number | null> {
  try {
    await page.evaluate(() => { const b = [...document.querySelectorAll('button, a')].find((b) => (b.getAttribute('aria-label') || '').startsWith('Google Account')) as HTMLElement; b?.click() })
    let n: number | null = null
    for (let i = 0; i < 10 && n === null; i++) {
      await sleep(500)
      const m = await page.evaluate(() => document.body.innerText.match(/([\d,]+)\s+Google Flow credits/))
      if (m) n = Number(m[1].replace(/,/g, ''))
    }
    await page.keyboard.press('Escape').catch(() => {})
    await sleep(500)
    return n
  } catch { return null }
}

async function price(): Promise<number | null> {
  await c.openSettings()
  await sleep(800)
  const txt: string[] = await page.evaluate(() => [...document.querySelectorAll('flow-credit-cost-label, .credit-cost-label')].map((e) => (e as HTMLElement).innerText))
  await c.closeSettings()
  const m = txt.join(' ').match(/use\s+([\d,]+)\s+credits/)
  return m ? Number(m[1].replace(/,/g, '')) : null
}

async function download(i: number, out: string) {
  const tile = page.locator('flow-video-tile').nth(i)
  await tile.scrollIntoViewIfNeeded().catch(() => {})
  const dl = page.waitForEvent('download', { timeout: 60_000 }); dl.catch(() => {})
  await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
  const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
  await item.waitFor({ state: 'visible', timeout: 15_000 })
  await item.click()
  const orig = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /Original size/i }).first()
  await orig.waitFor({ state: 'visible', timeout: 15_000 })
  await orig.click()
  const d = await dl
  try { await d.saveAs(out) }
  catch (err) {
    // 2026-10-21: with the shared Chrome's download behaviour set to its own folder (another tab's
    // session), Playwright's artifact copy is gone (ENOENT) but Chrome still writes the file to
    // ~/Downloads under its suggested name. Take it from there.
    const f = join(process.env.HOME!, 'Downloads', d.suggestedFilename())
    for (let k = 0; k < 240 && !existsSync(f); k++) await sleep(500)
    if (!existsSync(f)) throw err
    await sleep(1500)
    copyFileSync(f, out); unlinkSync(f)
  }
  await page.keyboard.press('Escape').catch(() => {})
}

async function atCast(name: string) {
  const box = c.promptBox()
  await c.setPrompt('')
  await box.click()
  await page.keyboard.type('@')
  await sleep(800)
  await page.keyboard.type(name.split(' ').slice(0, 2).join(' '))
  const row = () => page.evaluate((name: string) => {
    const el = [...document.querySelectorAll('.cdk-overlay-container [role=option]')].find((r) => (r as HTMLElement).innerText.trim().replace(/\s+/g, ' ') === `${name} Character`)
    if (!el) return false
    for (const type of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
      el.dispatchEvent(new (type.startsWith('pointer') ? PointerEvent : MouseEvent)(type, { bubbles: true, cancelable: true, view: window }))
    return true
  }, name)
  let ok = false
  for (let i = 0; i < 20 && !(ok = await row()); i++) await sleep(500)
  if (!ok) throw new Error(`CHARACTER_NOT_FOUND: no "${name} Character" row after @`)
  await sleep(1500)
  if (await page.locator('.cdk-overlay-container [role=option]').count()) { await clickText('Add to prompt'); await sleep(1500) }
  const text = await box.innerText().catch(() => '')
  if (!text.includes(name)) throw new Error(`CHARACTER_TAG_MISSING: box reads "${text.slice(0, 60)}"`)
  await page.keyboard.press('End')
}

const md5 = (f: string) => execFileSync('md5sum', [f], { encoding: 'utf8' }).split(' ')[0]
function knownMd5s(): Map<string, string> {
  const m = new Map<string, string>()
  const walk = (d: string) => { for (const f of readdirSync(d, { withFileTypes: true })) { const p = join(d, f.name); if (f.isDirectory()) walk(p); else if (f.name.endsWith('.mp4')) m.set(md5(p), p) } }
  walk(VIDEO)
  return m
}
function firstFrameDist(clip: string, still: string): number {
  const py = `
import subprocess,sys
def sig(p,v):
    cmd=['ffmpeg','-v','error','-i',p]+(['-frames:v','1'] if v else [])+['-vf','scale=32:32','-f','rawvideo','-pix_fmt','gray','-']
    return subprocess.run(cmd,capture_output=True,check=True).stdout[:1024]
a=sig(sys.argv[1],True);b=sig(sys.argv[2],False)
print(sum((x-y)**2 for x,y in zip(a,b))/len(a))`
  return Number(execFileSync('python3', ['-c', py, clip, still], { encoding: 'utf8' }).trim())
}

try {
  if (!page.url().includes(PROJECT)) { await page.goto(`https://flow.google.com/project/${PROJECT}`, { waitUntil: 'domcontentloaded' }); await sleep(5000) }
  const before0 = await balance()
  if (process.env.HARVEST_ONLY !== '1') {
    // A unique staged name per job: the frame picker matches by BASENAME (flow-client submitVideo note).
    const staged = join(STAGE, `gpom-end-${job.key}-${basename(job.src)}`)
    copyFileSync(job.src, staged)
    await c.reloadProject()
    await c.ensureAgentOff()
    await c.uploadToProject(staged)
    for (let i = 0; i < 10; i++) { await sleep(500); if (await clickText('I agree')) break }
    const cfg = { model: 'Omni 1.1 Flash', aspect: '16:9', duration, count, frames: true }
    try { await c.ensureVideoConfigRebuilt(cfg) } catch { await sleep(1500); await c.ensureVideoConfigRebuilt(cfg) }
    try { await c.fillFrameSlotRebuilt('Start', basename(staged)) }
    catch (err) {
      say({ event: 'fill-retry', why: (err as Error).message.split('\n')[0].slice(0, 120) })
      await page.reload({ waitUntil: 'domcontentloaded' }); await sleep(10_000)
      await c.ensureAgentOff()
      try { await c.ensureVideoConfigRebuilt(cfg) } catch { await sleep(1500); await c.ensureVideoConfigRebuilt(cfg) }
      await c.fillFrameSlotRebuilt('Start', basename(staged))
    }
    const cost = await price()
    const perClip = cost === null ? null : cost / count
    say({ event: 'priced', cost, perClip, count, duration, balance: before0, spentSoFar: ledger.spent, cap: CAP })
    if (cost === null) throw new Error('PRICE_UNREAD: no credit-cost label, not submitting')
    if (perClip! > MAX_PER_CLIP) throw new Error(`PRICE_OVER: ${perClip} per clip > ${MAX_PER_CLIP}, not submitting`)
    if (ledger.spent + cost > CAP) throw new Error(`CAP: ${ledger.spent} + ${cost} > ${CAP}, not submitting`)

    let cast = false
    await c.markTurnStart()
    if (job.character) { await atCast(job.character); cast = true }
    await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {})
    const baseline = await allKeys()
    if (cast) await page.keyboard.insertText(' ' + job.motion)
    else await c.setPrompt(job.motion)
    await c.clickSubmit()
    // Confirm Flow took it: a pending tile (no media key yet) or a new key at the top.
    let taken = false
    for (const deadline = Date.now() + 45_000; Date.now() < deadline;) {
      const t = (await topTiles(1))[0]
      if (t && ((t.key && !baseline.has(t.key)) || (!t.key && (t.pct || /Generating|Queued/i.test(t.text))))) { taken = true; break }
      const card = await c.detectFailureCard().catch(() => null)
      if (card === 'blocked') throw new Error('POLICY_BLOCKED')
      await sleep(1000)
    }
    if (!taken) throw new Error('SUBMIT_UNCONFIRMED')
    ledger.spent += cost
    ledger.jobs.push({ key: job.key, scene: job.scene ?? null, cost, src: job.src, out: job.out, at: new Date().toISOString() })
    writeFileSync(LEDGER, JSON.stringify(ledger, null, 1))
    say({ event: 'submitted', cast, cost, spentTotal: ledger.spent })
  }

  // Wait until NOTHING at the top of the grid is still rendering (a percentage or a key-less tile).
  // 2026-10-20: "a new key at the top" fired on the previous job's tile (its key had not loaded into the
  // baseline), so completion is "no pending tiles", after a 30 s floor, and the harvest skips any tile
  // already harvested (ledger.keys) or whose file md5 matches a clip already on disk.
  await sleep(30_000)
  const deadline = Date.now() + RENDER_MS
  while (Date.now() < deadline) {
    const top = await topTiles(count + 4)
    const pending = top.filter((t: any) => t.pct || !t.key)
    if (!pending.length) break
    const card = await c.detectFailureCard().catch(() => null)
    if (card === 'blocked') throw new Error('POLICY_BLOCKED (after submit)')
    await sleep(15_000)
  }
  await page.keyboard.press('Escape').catch(() => {})
  await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {}); await sleep(6000)
  const list = await topTiles(count + 6)
  say({ event: 'rendered', top: list.map((t: any) => ({ key: t.key.slice(-20), failed: t.failed, pct: t.pct })) })
  const known = knownMd5s()
  const seen = new Set<string>((ledger as any).keys ?? [])
  const got: string[] = []
  for (const [i, t] of list.entries()) {
    if (got.length >= count) break
    if (!t.key || seen.has(t.key) || t.pct) continue
    if (t.failed) { say({ event: 'tile-failed', i, text: t.text }); continue }
    const out = count > 1 ? job.out.replace(/\.mp4$/, `-${'abcd'[got.length]}.mp4`) : job.out
    for (let d = 1; d <= 3; d++) {
      try { await download(i, out); break }
      catch (err) { say({ event: 'download-retry', i, d, why: (err as Error).message.split('\n')[0].slice(0, 120) }); await page.reload({ waitUntil: 'domcontentloaded' }); await sleep(5000) }
    }
    if (!existsSync(out)) continue
    const h = md5(out)
    const dupe = known.get(h)
    const dist = firstFrameDist(out, job.src)
    say({ event: dupe ? 'dupe-skipped' : 'harvested', i, file: out, md5: h, dupeOf: dupe ?? null, firstFrameDist: Math.round(dist), match: dist < 400 })
    ;(ledger as any).keys = [...seen.add(t.key)]
    writeFileSync(LEDGER, JSON.stringify(ledger, null, 1))
    if (dupe) { unlinkSync(out); continue }
    known.set(h, out)
    got.push(out)
  }
  const after = await balance()
  say({ event: 'done', files: got, balanceBefore: before0, balanceAfter: after, charged: before0 !== null && after !== null ? before0 - after : null })
} catch (err) {
  say({ event: 'error', why: (err as Error).message.split('\n')[0].slice(0, 200) })
  process.exitCode = 1
} finally {
  await c.close?.().catch(() => {})
}
