// Record SEGMENTS of a YouTube video by playing them on channel 1 (no download). args: url name start:dur[,start:dur...]
import { chromium } from 'playwright'
import { join } from 'node:path'
import * as cap from '../../../packages/listen-mcp/src/capture'
const [url, name, segs] = process.argv.slice(2)
const ROOT = process.cwd(), OUTDIR = process.env.LISTEN_MEDIA_ROOT!
await cap.useChannelAudioServer(ROOT, 1)
const sink = cap.sinkName(1)
await cap.ensureSink(sink)
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = await b.contexts()[0].newPage()
try {
  await p.goto(url, { waitUntil: 'domcontentloaded' })
  for (const t of ['Reject all', 'Accept all']) {
    const btn = p.getByRole('button', { name: t }).first()
    if (await btn.isVisible({ timeout: 3000 }).catch(() => false)) { await btn.click(); break }
  }
  await p.waitForSelector('video', { timeout: 30000 })
  const st = () => p.evaluate(`(() => { const v=document.querySelector('video'); const pl=document.querySelector('#movie_player');
    return { ad: !!(pl && pl.classList.contains('ad-showing')), t: v.currentTime, d: v.duration } })()`) as Promise<any>
  const waitAds = async () => { for (let i = 0; i < 240; i++) { const s = await st(); if (!s.ad && Number.isFinite(s.d) && s.d > 30) return
    await p.evaluate(`(() => { const v=document.querySelector('video'); if (v && v.paused) v.play(); const sk=document.querySelector('.ytp-skip-ad-button, .ytp-ad-skip-button, .ytp-ad-skip-button-modern'); if (sk) sk.click(); })()`)
    await p.waitForTimeout(1000) } }
  await waitAds()
  await cap.pinVolume(sink).catch(() => {})
  for (const [i, sg] of segs.split(',').entries()) {
    const [start, dur] = sg.split(':').map(Number)
    await p.evaluate(`(() => { const v=document.querySelector('video'); v.pause(); v.currentTime=${start}; v.muted=false; v.volume=1; })()`)
    await p.waitForTimeout(2500)
    const raw = join(OUTDIR, `${name}-${i + 1}.wav`)
    const rec = await cap.startRecording(sink, raw, { startTimeoutMs: 8000 }).catch(async () => {
      await p.evaluate(`document.querySelector('video').play()`); return cap.startRecording(sink, raw, { startTimeoutMs: 8000 }) })
    await p.evaluate(`document.querySelector('video').play()`)
    await p.waitForTimeout(dur * 1000)
    if ((await st()).ad) console.error('ad during segment', i + 1)
    const out = await rec.stop()
    console.log(JSON.stringify({ seg: i + 1, start, seconds: out.seconds, raw, silent: await cap.isSilent(raw) }))
  }
} catch (e) { console.error("ERR", e) } finally { await p.close(); process.exit(0) }
