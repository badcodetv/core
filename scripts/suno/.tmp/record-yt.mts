// Record a YouTube video's audio by PLAYING it on channel 1 (no download). Waits out ads.
import { chromium } from 'playwright'
import { join } from 'node:path'
import * as cap from '../../../packages/listen-mcp/src/capture'
const [url, name] = process.argv.slice(2)
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
    return { ad: !!(pl && pl.classList.contains('ad-showing')), t: v.currentTime, d: v.duration, paused: v.paused, ended: v.ended } })()`) as Promise<any>
  // wait out ads
  for (let i = 0; i < 240; i++) {
    const s = await st()
    if (!s.ad && Number.isFinite(s.d) && s.d > 30) break
    await p.evaluate(`(() => { const v=document.querySelector('video'); if (v && v.paused) v.play(); const sk=document.querySelector('.ytp-skip-ad-button, .ytp-ad-skip-button, .ytp-ad-skip-button-modern'); if (sk) sk.click(); })()`)
    await p.waitForTimeout(1000)
  }
  await p.evaluate(`(() => { const v=document.querySelector('video'); v.pause(); v.currentTime=0; v.muted=false; v.volume=1; })()`)
  await cap.pinVolume(sink).catch(() => {})
  const raw = join(OUTDIR, `${name}.wav`)
  const rec = await cap.startRecording(sink, raw, { startTimeoutMs: 8000 }).catch(async () => {
    await p.evaluate(`document.querySelector('video').play()`); return cap.startRecording(sink, raw, { startTimeoutMs: 8000 })
  })
  await p.evaluate(`document.querySelector('video').play()`)
  let last = 0
  for (;;) {
    await p.waitForTimeout(1000)
    const s = await st()
    if (s.ad) { console.error('ad mid-roll at', last) }
    last = s.t
    if (s.ended || s.t >= s.d - 0.3) break
  }
  await p.waitForTimeout(1500)
  const out = await rec.stop()
  await cap.makePreview(raw, join(OUTDIR, `${name}.preview.mp3`))
  console.log(JSON.stringify({ name, seconds: out.seconds, raw, silent: await cap.isSilent(raw) }))
} finally { await p.close(); process.exit(0) }
