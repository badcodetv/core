/**
 * Download every finished video tile in the open Flow project into the scene's video/inbox, then name them with match.py.
 * For when run.mts's collect step missed tiles (2026-11-06: after its hard reload the tile list came back empty, nothing saved).
 *
 *   npx tsx scripts/scene/harvest.mts <scene-dir> [maxTiles]      (FLOW_CDP_PORT, default 9222)
 * Run it alone: one Flow user at a time.
 */
import { execFileSync } from 'node:child_process'
import { mkdirSync, readFileSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import { chromium } from 'playwright'

const SCENE = process.argv[2]
const MAX = Number(process.argv[3] ?? 50)
const CFG = JSON.parse(readFileSync(join(SCENE, 'scene.json'), 'utf8'))
const INBOX = join(CFG.media, 'video/inbox')
mkdirSync(INBOX, { recursive: true })
const b = await chromium.connectOverCDP(`http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
const page = b.contexts()[0].pages().find(p => p.url().includes(`/project/${CFG.flow_project}`))
if (!page) throw new Error(`project ${CFG.flow_project} is not open in the Flow browser`)
await page.locator('flow-video-tile').first().waitFor({ timeout: 30_000 })
const tiles = await page.locator('flow-video-tile').evaluateAll((els: any[]) => els.map(e => {
  const t = e.textContent || ''
  return { ok: !!e.querySelector('video[src], img[src]') && !/Failed/.test(t) && !/\d+\s*%/.test(t), text: t.replace(/\s+/g, ' ').slice(-60) }
}))
let order = readdirSync(INBOX).filter(f => f.endsWith('.mp4')).length
for (const [i, t] of tiles.slice(0, MAX).entries()) {
  if (!t.ok) { console.log(JSON.stringify({ skip: i, text: t.text })); continue }
  const tile = page.locator('flow-video-tile').nth(i)
  await tile.scrollIntoViewIfNeeded().catch(() => {})
  const dst = join(INBOX, `raw-${String(order++).padStart(3, '0')}.mp4`)
  const dl = page.waitForEvent('download', { timeout: 60_000 }); dl.catch(() => {})
  await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
  const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
  await item.waitFor({ state: 'visible', timeout: 15_000 }); await item.click()
  const orig = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /Original size/i }).first()
  await orig.waitFor({ state: 'visible', timeout: 15_000 }); await orig.click()
  await (await dl).saveAs(dst)
  await page.keyboard.press('Escape').catch(() => {})
  console.log(JSON.stringify({ harvested: i, file: dst, text: t.text }))
}
execFileSync('python3', [join(new URL('.', import.meta.url).pathname, 'match.py'), SCENE, '--apply'], { stdio: 'inherit' })
process.exit(0)
