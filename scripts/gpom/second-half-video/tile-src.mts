/**
 * Recovery when the runner's download fails with saveAs ENOENT: list the top N video tiles' media
 * src and (with OUT set) save tile I's video by fetching its src inside the page (same cookies).
 *   FLOW_CDP_PORT=9222 npx tsx tile-src.mts <n>            list
 *   FLOW_CDP_PORT=9222 npx tsx tile-src.mts <i> <out.mp4>  save tile i
 */
import { writeFileSync } from 'node:fs'
import { FlowClient } from '../../../packages/flow-mcp/src/flow-client'
const c: any = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT}`)
const page = c.page
const [a, out] = process.argv.slice(2)
const tiles = await page.locator('flow-video-tile').evaluateAll((els: any[]) => els.slice(0, 12).map((e) => {
  const v = e.querySelector('video[src]'); const t = (e.textContent || '').replace(/\s+/g, ' ').slice(0, 60)
  return { src: v ? v.src : '', text: t }
}))
if (!out) { tiles.slice(0, Number(a)).forEach((t: any, i: number) => console.log(i, t.src.split('?')[0].slice(-40), t.text)) }
else {
  const tile = page.locator('flow-video-tile').nth(Number(a))
  await tile.scrollIntoViewIfNeeded().catch(() => {})
  await tile.hover()
  let src = ''
  for (let k = 0; k < 30 && !src; k++) { await page.waitForTimeout(500); src = await tile.evaluate((e: any) => (e.querySelector('video[src]') as any)?.src || '') }
  if (!src) throw new Error('NO_VIDEO_SRC after hover')
  const b64: string = await page.evaluate(async (src: string) => {
    const r = await fetch(src); const buf = new Uint8Array(await r.arrayBuffer())
    let s = ''; for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode(...buf.subarray(i, i + 0x8000))
    return btoa(s)
  }, src)
  writeFileSync(out, Buffer.from(b64, 'base64')); console.log('saved', out, Buffer.from(b64, 'base64').length)
}
await c.close?.().catch(() => {})
