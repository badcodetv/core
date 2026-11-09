// record.mjs <url> <outdir> [--at t1,t2,...] [--fps 24] [--w 1920 --h 1080] [--media bead-media.json] [--frames frames-beads]
// 1F: --media sets the per-bead stills/clips ({"0":{"src":...,"type":"video","fps":24}}, src relative to the page);
// frameAt then steps each clip to the source frame under t and waits for it (frame-exact), so a recorded bead never drifts.
// Film mode: window.hologram.film(w,h) then frameAt(t) per frame (every moving part is on the film clock). Frames -> <outdir>/frames/NNNNN.jpg
import { chromium } from 'playwright';
import fs from 'node:fs';
const [url, out, ...rest] = process.argv.slice(2);
const opt = k => { const i = rest.indexOf('--' + k); return i >= 0 ? rest[i + 1] : null };
const fps = +(opt('fps') || 24), W = +(opt('w') || 1920), H = +(opt('h') || 1080), at = opt('at');
const FD = out + '/' + (opt('frames') || 'frames'); fs.mkdirSync(FD, { recursive: true });
const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true, args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'] });
const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
const media = opt('media');
if (media) await p.addInitScript(m => { window.BEAD_MEDIA_OVERRIDE = m }, JSON.parse(fs.readFileSync(media, 'utf8')));
p.on('pageerror', e => console.error('PAGEERROR', e.message));
await p.goto(url, { waitUntil: 'networkidle' });
await p.waitForFunction(() => window.hologram && window.hologram.TD > 0, null, { timeout: 60000 });
await p.evaluate(([w, h]) => window.hologram.film(w, h), [W, H]);
console.log('bead media', await p.evaluate(() => window.hologram.mediaReady()));
const TD = await p.evaluate(() => window.hologram.TD);
const times = at ? at.split(',').map(Number) : Array.from({ length: Math.ceil(TD * fps) }, (_, i) => i / fps);
console.log('TD', TD.toFixed(3), 'frames', times.length);
let n = 0; const t0 = Date.now();
for (const t of times) {
  const d = await p.evaluate(t => window.hologram.frameAt(t, 'image/jpeg'), t);
  fs.writeFileSync(`${FD}/${String(n).padStart(5, '0')}.jpg`, Buffer.from(d.split(',')[1], 'base64'));
  if (++n % 120 === 0) console.log(n, ((Date.now() - t0) / n).toFixed(0) + 'ms/frame');
}
await b.close();
