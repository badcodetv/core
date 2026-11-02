// Render gfx.html scenes to transparent ProRes 4444 overlays (or PNG stills with --still).
//   node render.mjs jobs.json            jobs: [{name, scene, dur, args:[...], out}]   (out = .mov)
//   node render.mjs --still scene t out.png [args...]
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
const here = path.dirname(new URL(import.meta.url).pathname);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
await page.goto('file://' + path.join(here, 'gfx.html'));
await page.evaluate(() => window.fontsReady);
await page.waitForTimeout(400);
const shot = async (scene, t, args, file) => {
  await page.evaluate(([s, t, a]) => window.render(s, t, ...a), [scene, t, args]);
  await page.screenshot({ path: file, omitBackground: true });
};
if (process.argv[2] === '--still') {
  const [, , , scene, t, out, ...args] = process.argv;
  await shot(scene, +t, args, out);
} else {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  for (const j of jobs) {
    if (fs.existsSync(j.out) && !process.env.FORCE) { console.log('skip', j.name); continue; }
    const dir = fs.mkdtempSync('/tmp/gfx-');
    const n = Math.round(j.dur * 24);
    for (let i = 0; i < n; i++) await shot(j.scene, i / 24, j.args || [], path.join(dir, String(i).padStart(5, '0') + '.png'));
    const opaque = j.opaque;
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', '24', '-i', path.join(dir, '%05d.png'),
      ...(opaque ? ['-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p'] : ['-c:v', 'prores_ks', '-profile:v', '4', '-pix_fmt', 'yuva444p10le']), j.out]);
    fs.rmSync(dir, { recursive: true });
    console.log('done', j.name, n, 'frames');
  }
}
await browser.close();
