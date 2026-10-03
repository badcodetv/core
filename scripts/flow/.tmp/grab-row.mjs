// Scratch: save the first N gallery tiles (reading order) under the given names. Portrait tiles are under 200px wide,
// which is why cast-batch's "width > 200" top-tile test saved the wrong image on 2026-10-03.
// usage: node grab-row.mjs <port> <outDir> <name1> <name2> ...
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, outDir, ...names] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.evaluate(() => window.scrollTo(0, 0));
const srcs = await page.evaluate((n) => {
  const r = (i) => i.getBoundingClientRect();
  return [...document.querySelectorAll('img')].filter((i) => r(i).width > 120 && r(i).height > 120).sort((a, b) => (Math.round(r(a).top / 40) - Math.round(r(b).top / 40)) || (r(a).left - r(b).left)).slice(0, n).map((i) => i.src);
}, names.length);
for (let k = 0; k < names.length; k++) {
  const b64 = await page.evaluate(async (src) => { const buf = new Uint8Array(await (await (await fetch(src)).blob()).arrayBuffer()); let s = ''; for (const b of buf) s += String.fromCharCode(b); return btoa(s); }, srcs[k]);
  writeFileSync(`${outDir}/${names[k]}.webp`, Buffer.from(b64, 'base64'));
  console.log(names[k], 'saved');
}
await browser.close();
