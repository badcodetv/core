/**
 * Download Flow's "1080p Upscaled" version of every video in a scene's Flow project (free on paid plans;
 * docs/flow/platform-controls.md). Flow makes video at 720p; this is the better upscale (Kai, 10 Nov: "you can tell
 * the quality is low"). Files land as <media>/video/inbox-1080/raw-NNN.mp4, tile order; match1080.py names them.
 *
 *   FLOW_CDP_PORT=<port> npx tsx scripts/scene/upscale.mts <scene-dir> [maxTiles]
 *
 * The menu (docs/flow/automation-2026-09-rebuild.md item 16): More options → Download → 1080p Upscaled. Flow renders
 * the upscale on demand, so the download event can take a minute or more. Never run beside another Flow runner.
 */
import { existsSync, mkdirSync, readFileSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const SCENE = process.argv[2]
const MAX = Number(process.argv[3] ?? 999)
const CFG = JSON.parse(readFileSync(join(SCENE, 'scene.json'), 'utf8'))
const OUT = join(CFG.media, 'video/inbox-1080')
mkdirSync(OUT, { recursive: true })
const c: any = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
const page = c.page
await page.goto(`https://flow.google.com/project/${CFG.flow_project}`, { waitUntil: 'domcontentloaded' })
await page.waitForTimeout(6000)
// scroll so every tile is in the DOM
for (let k = 0; k < 8; k++) { await page.mouse.wheel(0, 4000); await page.waitForTimeout(700) }
await page.evaluate(() => window.scrollTo(0, 0))
const n = Math.min(MAX, await page.locator('flow-video-tile').count())
console.log(JSON.stringify({ tiles: n }))
for (let i = 0; i < n; i++) {
  const out = join(OUT, `raw-${String(i).padStart(3, '0')}.mp4`)
  if (existsSync(out) && statSync(out).size > 0) { console.log(JSON.stringify({ i, skip: out })); continue }
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      const tile = page.locator('flow-video-tile').nth(i)
      await tile.scrollIntoViewIfNeeded().catch(() => {})
      const dl = page.waitForEvent('download', { timeout: 300_000 }); dl.catch(() => {})
      await tile.evaluate((e: any) => { const b = [...e.querySelectorAll('button')].find((b: any) => b.getAttribute('aria-label') === 'More options') as any; b?.click() })
      const item = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /^\s*download\s*Download\s*$/ }).first()
      await item.waitFor({ state: 'visible', timeout: 15_000 }); await item.click()
      const up = page.locator('.cdk-overlay-container [role="menuitem"]').filter({ hasText: /1080p/i }).first()
      await up.waitFor({ state: 'visible', timeout: 15_000 }); await up.click()
      await (await dl).saveAs(out)
      await page.keyboard.press('Escape').catch(() => {})
      console.log(JSON.stringify({ i, saved: out, attempt }))
      break
    } catch (err) {
      console.log(JSON.stringify({ i, attempt, error: (err as Error).message.split('\n')[0].slice(0, 160) }))
      await page.keyboard.press('Escape').catch(() => {}); await page.keyboard.press('Escape').catch(() => {})
      await page.waitForTimeout(3000)
    }
  }
}
process.exit(0)
