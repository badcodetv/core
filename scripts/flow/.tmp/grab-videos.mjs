// Scratch (2026-10-19): download the newest N video tiles of the open project. flow_generate_video can no longer
// see its finished clip (rebuild doc item 20), so harvest by hand: hover each tile for its <video src>, fetch it.
// usage: node grab-videos.mjs <port> <n> <outPrefix>
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, n, prefix] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const tiles = page.locator('flow-video-tile');
const count = await tiles.count(); console.log('video tiles', count);
for (let i = 0; i < Math.min(+n, count); i++) {
  const t = tiles.nth(i); await t.scrollIntoViewIfNeeded(); await t.hover(); await page.waitForTimeout(2500);
  const src = await t.evaluate((el) => el.querySelector('video')?.src || null);
  const label = await t.evaluate((el) => (el.innerText || '').trim().slice(0, 60));
  if (!src) { console.log(i, 'no video src', label); continue; }
  const b64 = await page.evaluate(async (u) => { const b = new Uint8Array(await (await fetch(u)).arrayBuffer()); let s = ''; for (let k = 0; k < b.length; k += 8192) s += String.fromCharCode(...b.subarray(k, k + 8192)); return btoa(s); }, src);
  const out = `${prefix}-${i}.mp4`; writeFileSync(out, Buffer.from(b64, 'base64')); console.log(i, label, out);
}
await browser.close();
