// Scratch: in a still's edit view, save the large image at full resolution.
// usage: node grab-edit.mjs <port> <out>
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, out] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/edit/'));
const data = await page.evaluate(async () => {
  const a = (i) => i.getBoundingClientRect().width * i.getBoundingClientRect().height;
  const top = [...document.querySelectorAll('img')].sort((x, y) => a(y) - a(x))[0];
  const blob = await (await fetch(top.src)).blob();
  const buf = new Uint8Array(await blob.arrayBuffer());
  let s = ''; for (let i = 0; i < buf.length; i += 8192) s += String.fromCharCode(...buf.subarray(i, i + 8192));
  return { b64: btoa(s), w: top.naturalWidth, h: top.naturalHeight, type: blob.type };
});
writeFileSync(out, Buffer.from(data.b64, 'base64'));
console.log('saved', data.w, data.h, data.type);
await browser.close();
