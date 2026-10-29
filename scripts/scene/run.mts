/**
 * new-scene stage 3: animate every picked still of a scene, in WAVES — submit a few, collect, repeat.
 * Generalised from scripts/gpom/opening-video/run.mts (GPOM opening recut, 2026-10-17/19).
 *
 * The pattern is scripts/gaze-board/run_waves.mts (submit-then-harvest, missing list recomputed
 * from disk every wave, so re-running never pays twice). What differs, and why:
 *   - Model, aspect, mode and length come from the scene: scene.json "video" (from the story's
 *     look.md), overridden by video-jobs.json — see scripts/scene/scene.py video_settings. There is
 *     NO default (2026-10-29, design/2026-10-29-style-leak-audit.md §1: this runner used to force
 *     one story's Omni 1.1 Flash / 16:9 / Frames on every scene). 720p and x1 are runner mechanics
 *     (x1 because clips are named by first frame). What each submit used goes to video/inbox/
 *     settings.json, and match.py writes that onto the recipe card.
 *   - A job with a `character` casts that Flow Character with "@" after the Start slot is filled.
 *   - Completion and harvest go by tile KEY at the top of the grid (rebuild doc items 20–21,
 *     the br-videos.mts download menu), not videoTiles(), whose thumbnail selector went stale.
 *   - Harvested clips are named by matching their FIRST FRAME to the plates (match.py), because
 *     nothing in Flow says which clip came from which submit.
 *   - "Unusual activity" / an unfilled frame slot: a real reload, 10s, retry (Jack's rule).
 *
 * Plates are uniquely named copies in the WSL filesystem (law 20: never upload from /mnt).
 *
 *   FLOW_CDP_PORT=<port> npx tsx scripts/scene/run.mts <scene-dir> [key …]     # WAVE=5 by default
 *
 * Run it with run_in_background and never alongside another Flow runner or MCP call: one browser.
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const HERE = join(REPO, 'scripts/scene')
const SCENE = process.argv[2]
if (!SCENE || !existsSync(join(SCENE, 'scene.json'))) throw new Error('usage: run.mts <scene-dir> [key …]')
const CFG = JSON.parse(readFileSync(join(SCENE, 'scene.json'), 'utf8'))
const PROJECT: string = CFG.flow_project
if (!PROJECT) throw new Error('scene.json has no flow_project')
const STAGE = join(process.env.HOME!, '.cache/badcode-scenes', CFG.scene, 'plates')
const INBOX = join(CFG.media, 'video/inbox')
const LOG = join(CFG.media, 'video/run.log')
const WAVE = Number(process.env.WAVE ?? 5)
const RENDER_MS = Number(process.env.RENDER_MS ?? 12 * 60_000)

type Shot = {
  key: string; still: string | null; plate: string | null; src: string | null; out: string; motion: string; character: string | null
  model: string; aspect: '16:9' | '9:16'; mode: string; duration: number
}
// shots.py exits non-zero (with the reason on stderr) when the scene has no video settings.
const all: Shot[] = JSON.parse(execFileSync('python3', [join(HERE, 'shots.py'), SCENE], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'inherit'] }))
for (const s of all) {
  const gap = (['model', 'aspect', 'mode', 'duration'] as const).filter(k => s[k] === undefined || s[k] === null || s[k] === '')
  if (gap.length) throw new Error(`${s.key}: no video ${gap.join(', ')} — set "video" in scene.json from the story's look.md`)
  if (s.mode !== 'Frames') throw new Error(`${s.key}: mode ${s.mode} — run.mts only drives Frames`)
}
const only = process.argv.slice(3)
const shots = all.filter(s => s.plate && (!only.length || only.includes(s.key)))
mkdirSync(STAGE, { recursive: true })
mkdirSync(INBOX, { recursive: true })

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}
const SETTINGS = join(INBOX, 'settings.json')
/** What each submit actually asked Flow for, keyed by shot — match.py puts it on the recipe card. */
const recordSettings = (s: Shot) => {
  const all = existsSync(SETTINGS) ? JSON.parse(readFileSync(SETTINGS, 'utf8')) : {}
  all[s.key] = { model: s.model, aspect: s.aspect, mode: s.mode, durationSeconds: s.duration, count: 1, resolution: '720p', at: new Date().toISOString() }
  writeFileSync(SETTINGS, JSON.stringify(all, null, 1))
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
  const cfg = { model: s.model, aspect: s.aspect, duration: s.duration, count: 1, frames: true }
  try { await c.ensureVideoConfigRebuilt(cfg) }
  catch { await sleep(1500); await c.ensureVideoConfigRebuilt(cfg) }
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
  recordSettings(s)
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
  try { execFileSync('python3', [join(HERE, 'match.py'), SCENE, '--apply'], { stdio: 'inherit' }) }
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
