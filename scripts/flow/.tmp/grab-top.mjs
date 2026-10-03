// Scratch: save the top-left gallery tile's image (thumbnail resolution) for review.
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, out] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const data = await page.evaluate(async () => {
  const imgs = [...document.querySelectorAll('img')].filter((i) => i.getBoundingClientRect().width > 200);
  const top = imgs.sort((a, b) => (a.getBoundingClientRect().top - b.getBoundingClientRect().top) || (a.getBoundingClientRect().left - b.getBoundingClientRect().left))[0];
  const blob = await (await fetch(top.src)).blob();
  const buf = new Uint8Array(await blob.arrayBuffer());
  let s = ''; for (const b of buf) s += String.fromCharCode(b);
  return { b64: btoa(s), w: top.naturalWidth, h: top.naturalHeight };
});
writeFileSync(out, Buffer.from(data.b64, 'base64'));
console.log('saved', data.w, data.h);
await browser.close();
