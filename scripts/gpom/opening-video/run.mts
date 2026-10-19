/**
 * GPOM opening recut: animate every picked still (copy of second-half-video/run.mts), in WAVES — submit a few, collect, repeat.
 *
 * The pattern is scripts/gaze-board/run_waves.mts (submit-then-harvest, missing list recomputed
 * from disk every wave, so re-running never pays twice). What differs, and why:
 *   - Omni 1.1 Flash, Frames, 16:9, 720p, 8s, x1 (Jack's standing ruling; the options file).
 *   - The bot shots cast the West Country Bot Character after the Start slot is filled.
 *   - Completion and harvest go by tile KEY at the top of the grid (rebuild doc items 20–21,
 *     the br-videos.mts download menu), not videoTiles(), whose thumbnail selector went stale.
 *   - Harvested clips are named by matching their FIRST FRAME to the plates (match.py), because
 *     nothing in Flow says which clip came from which submit.
 *   - "Unusual activity" / an unfilled frame slot: a real reload, 10s, retry (Jack's rule).
 *
 * Plates are uniquely named copies in the WSL filesystem (law 20: never upload from /mnt).
 *
 *   npx tsx scripts/gpom/opening-video/run.mts [key …]     # WAVE=5 by default
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readdirSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../../..', import.meta.url).pathname
const HERE = join(REPO, 'scripts/gpom/opening-video')
const PROJECT = '80c32ec0-3564-415b-810b-9466492be788'
const STAGE = join(process.env.HOME!, '.cache/badcode-gpom-opening/plates')
const INBOX = '/mnt/d/badcode-videos/gitpush-origin-master/clips/opening-recut/video/inbox'
const LOG = join(HERE, 'run.log')
const WAVE = Number(process.env.WAVE ?? 5)
const RENDER_MS = Number(process.env.RENDER_MS ?? 12 * 60_000)

type Shot = { key: string; still: string | null; plate: string | null; src: string | null; out: string; motion: string; character: string | null }
const all: Shot[] = JSON.parse(execFileSync('python3', [join(HERE, 'shots.py')], { encoding: 'utf8' }))
const only = process.argv.slice(2)
const shots = all.filter(s => s.plate && (!only.length || only.includes(s.key)))
mkdirSync(STAGE, { recursive: true })
mkdirSync(INBOX, { recursive: true })

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}
const missing = () => shots.filter(s => !(existsSync(s.out) && statSync(s.out).size > 0))

const c: any = await FlowClient.connect(process.env.FLOW_CDP ?? `http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
const page = c.page
const sleep = (ms: number) => page.waitForTimeout(ms)

const keyAt = async (i: number): Promise<string> =>
  page.locator('flow-video-tile').nth(i).evaluate((e: any) => {
    const m = e.querySelector('video[src], img[src]')
    return m ? (m.getAttribute('src') || '').split('?')[0] : ''
  }).catch(() => '')
const topTiles = async (n: number) =>
  page.locator('flow-video-tile').evaluateAll((els: any[], n: number) => els.slice(0, n).map((e) => {
    const m = e.querySelector('video[src], img[src]')
    const t = e.textContent || ''
    return { key: m ? (m.getAttribute('src') || '').split('?')[0] : '', failed: /Failed/.test(t), pct: /\d+\s*%/.test(t), text: t.replace(/\s+/g, ' ').slice(0, 90) }
  }), n)
const allKeys = async (): Promise<Set<string>> => new Set((await topTiles(999)).map((t: any) => t.key).filter(Boolean))

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
  await (await dl).saveAs(out)
  await page.keyboard.press('Escape').catch(() => {})
}
const clickText = async (t: string) => page.evaluate((t: string) => {
  const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === t || b.getAttribute('aria-label') === t) as HTMLElement | undefined
  b?.click(); return !!b
}, t)
async function closeAgentPanel() {
  if (await page.locator('flow-agent-panel').count()) {
    await page.evaluate(() => { const p = document.querySelector('flow-agent-panel'); const b = p && [...p.querySelectorAll('button')].find((b) => b.getAttribute('aria-label') === 'Close') as HTMLElement | undefined; b?.click() })
    await sleep(800)
  }
}
async function hardReload() {
  await page.keyboard.press('Escape').catch(() => {})
  await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
  await sleep(4000)
}

async function atCast(name: string) {
  const box = c.promptBox()
  await c.setPrompt('')
  await box.click()
  // Typing the name after "@" filters the list: after a run of uploads the Character falls off
  // the unfiltered rows (rebuild doc item 49; frames 9 and 20, 2026-10-17).
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

const uploaded = new Set<string>()
/** One submit, confirmed by a new key at the top of the grid. Throws on anything else. */
async function submit(s: Shot) {
  const staged = join(STAGE, s.plate!)
  if (!existsSync(staged)) copyFileSync(s.src!, staged)
  await c.reloadProject(); await closeAgentPanel(); await c.ensureAgentOff()
  if (!uploaded.has(staged)) {
    await c.uploadToProject(staged)
    uploaded.add(staged)
    for (let i = 0; i < 10; i++) { await sleep(500); if (await clickText('I agree')) break }
  }
  // Item 15/57: the first Frames lookup of a process can race the popover; one retry clears it.
  try { await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: (s as any).duration ?? 8, count: 1, frames: true }) }
  catch { await sleep(1500); await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: (s as any).duration ?? 8, count: 1, frames: true }) }
  await c.fillFrameSlotRebuilt('Start', s.plate!)
  // Cast by "@" mention (rebuild doc items 30-33). The ingredients button the MCP's
  // addCharacterToPromptRebuilt clicks does not exist in Frames mode (probe 2026-10-17), but "@"
  // does, and the tag sits INLINE in the prompt box, so the prompt is typed after it, never set
  // with setPrompt (which select-all-deletes the tag).
  let cast = false
  await c.markTurnStart()
  if (s.character) {
    try { await atCast(s.character); cast = true }
    catch (err) { say({ event: 'cast-fail', key: s.key, why: (err as Error).message.split('\n')[0].slice(0, 160) }); await page.keyboard.press('Escape').catch(() => {}) }
  }
  await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {})
  const before = await allKeys()
  if (cast) await page.keyboard.insertText(' ' + s.motion)
  else await c.setPrompt(s.motion)
  await c.clickSubmit()
  const deadline = Date.now() + 45_000
  while (Date.now() < deadline) {
    const k0 = await keyAt(0)
    if (k0 && !before.has(k0)) return cast
    const n = await page.locator('flow-video-tile').count()
    // A pending tile has no media yet; it shows as a tile with a percentage and no key.
    const t = (await topTiles(1))[0]
    if (t && !t.key && (t.pct || /Generating|Queued/i.test(t.text))) return cast
    const card = await c.detectFailureCard().catch(() => null)
    if (card === 'blocked') throw new Error(`POLICY_BLOCKED ${s.key}`)
    if (n === 0) break
    await sleep(1000)
  }
  throw new Error(`SUBMIT_UNCONFIRMED ${s.key}`)
}

/** Wait for the wave's tiles to finish, then download every new finished tile to the inbox. */
async function collect(baseline: Set<string>, want: number) {
  const deadline = Date.now() + RENDER_MS
  let tiles: any[] = []
  while (Date.now() < deadline) {
    tiles = (await topTiles(want + 4)).filter((t: any) => !baseline.has(t.key))
    const done = tiles.filter((t: any) => t.failed || (t.key && !t.pct))
    say({ event: 'poll', fresh: tiles.length, done: done.length, want })
    if (tiles.length >= want && done.length >= tiles.length) break
    await sleep(15_000)
  }
  await hardReload()
  const list = await topTiles(want + 4)
  let order = readdirSync(INBOX).filter(f => f.endsWith('.mp4')).length
  for (const [i, t] of list.entries()) {
    if (!t.key || baseline.has(t.key) || t.failed || t.pct) {
      if (t.failed) say({ event: 'tile-failed', i, text: t.text })
      continue
    }
    const dst = join(INBOX, `raw-${String(order++).padStart(3, '0')}.mp4`)
    for (let d = 1; d <= 3; d++) {
      try { await download(i, dst); say({ event: 'harvested', i, file: dst }); break }
      catch (err) { say({ event: 'download-retry', i, d, why: (err as Error).message.split('\n')[0].slice(0, 120) }); await hardReload() }
    }
  }
  try { execFileSync('python3', [join(HERE, 'match.py'), '--apply'], { stdio: 'inherit' }) }
  catch (err) { say({ event: 'match-fail', why: (err as Error).message.slice(0, 160) }) }
}

try {
  await page.goto(`https://flow.google.com/project/${PROJECT}`, { waitUntil: 'domcontentloaded' })
  await sleep(5000)
  let stuck = 0
  const blocked = new Set<string>()
  for (let wave = 1; wave <= 8; wave++) {
    const todo = missing().filter(s => !blocked.has(s.key))
    if (!todo.length) { say({ event: 'all-present', wave }); break }
    const batch = todo.slice(0, WAVE)
    say({ event: 'wave', wave, missing: todo.length, submitting: batch.map(s => s.key) })
    await c.reloadProject()
    const baseline = await allKeys()
    let submitted = 0
    for (const s of batch) {
      for (let attempt = 1; attempt <= 4; attempt++) {
        try {
          const cast = await submit(s)
          submitted++
          say({ event: 'submitted', key: s.key, wave, cast, attempt })
          break
        } catch (err) {
          const m = (err as Error).message.split('\n')[0].slice(0, 160)
          if (/POLICY_BLOCKED|UPLOAD_REFUSED/.test(m)) { blocked.add(s.key); say({ event: 'skip', key: s.key, why: m }); break }
          say({ event: 'submit-retry', key: s.key, attempt, why: m })
          await sleep(10_000)
          await hardReload()
        }
      }
    }
    if (!submitted) { if (++stuck >= 2) { say({ event: 'stalled', wave }); break } continue }
    await collect(baseline, submitted)
    const left = missing().filter(s => !blocked.has(s.key)).length
    say({ event: 'wave-done', wave, remaining: left })
    stuck = left === todo.length ? stuck + 1 : 0
    if (stuck >= 2) { say({ event: 'stalled', wave, remaining: left }); break }
  }
  say({ event: 'done', remaining: missing().map(s => s.key), blocked: [...blocked] })
} finally {
  await c.close?.().catch(() => {})
}
