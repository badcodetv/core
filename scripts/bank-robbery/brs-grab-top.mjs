// Scratch: save the newest (top-left) image in the open Flow PROJECT tab at full resolution.
// grab-top.mjs picks the first flow.google.com tab, which can be a stray home tab; this one wants /project/.
// usage: node brs-grab-top.mjs <port> <out.jpg> [n]   (n = 0 for the top-left tile, 1 for the next, ...)
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, out, n = '0'] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com/project/'));
if (!page) { console.log('NO_PROJECT_TAB'); process.exit(1); }
await page.keyboard.press('Escape');
const src = await page.evaluate((n) => {
  const r = (i) => i.getBoundingClientRect();
  const imgs = [...document.querySelectorAll('img')].filter((i) => r(i).width > 100 && r(i).top > 100 && r(i).left > 200);
  imgs.sort((a, b) => (Math.round(r(a).top / 40) - Math.round(r(b).top / 40)) || (r(a).left - r(b).left));
  return imgs[n]?.src ?? '';
}, Number(n));
if (!src) { console.log('NO_TILE'); process.exit(1); }
const b64 = await page.evaluate(async (src) => {
  const buf = new Uint8Array(await (await (await fetch(src)).blob()).arrayBuffer());
  let s = ''; for (const b of buf) s += String.fromCharCode(b);
  return btoa(s);
}, src);
writeFileSync(out, Buffer.from(b64, 'base64'));
console.log('saved', out);
await browser.close();
