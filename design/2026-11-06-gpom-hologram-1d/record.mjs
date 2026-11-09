// record.mjs <url> <outdir> [--at t1,t2,...] [--fps 24] [--w 1920 --h 1080]
// Film mode: window.hologram.film(w,h) then frameAt(t) per frame (every moving part is on the film clock). Frames -> <outdir>/frames/NNNNN.jpg
import { chromium } from 'playwright';
import fs from 'node:fs';
const [url, out, ...rest] = process.argv.slice(2);
const opt = k => { const i = rest.indexOf('--' + k); return i >= 0 ? rest[i + 1] : null };
const fps = +(opt('fps') || 24), W = +(opt('w') || 1920), H = +(opt('h') || 1080), at = opt('at');
fs.mkdirSync(out + '/frames', { recursive: true });
const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true, args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
p.on('pageerror', e => console.error('PAGEERROR', e.message));
await p.goto(url, { waitUntil: 'networkidle' });
await p.waitForFunction(() => window.hologram && window.hologram.TD > 0, null, { timeout: 60000 });
await p.evaluate(([w, h]) => window.hologram.film(w, h), [W, H]);
const TD = await p.evaluate(() => window.hologram.TD);
const times = at ? at.split(',').map(Number) : Array.from({ length: Math.ceil(TD * fps) }, (_, i) => i / fps);
console.log('TD', TD.toFixed(3), 'frames', times.length);
let n = 0; const t0 = Date.now();
for (const t of times) {
  const d = await p.evaluate(t => window.hologram.frameAt(t, 'image/jpeg'), t);
  fs.writeFileSync(`${out}/frames/${String(n).padStart(5, '0')}.jpg`, Buffer.from(d.split(',')[1], 'base64'));
  if (++n % 120 === 0) console.log(n, ((Date.now() - t0) / n).toFixed(0) + 'ms/frame');
}
await b.close();
