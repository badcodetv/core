// Scratch: list the top tiles of the open Flow project, click the newest 4:3 still to open it full size, and screenshot.
// usage: node show-top.mjs <port> <shot.png>
import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((x) => x.url().includes('flow.google.com'));
await page.bringToFront();
await page.waitForTimeout(4000);
const tiles = await page.evaluate(() => {
  const r = (i) => i.getBoundingClientRect();
  return [...document.querySelectorAll('img')].filter((i) => r(i).width > 200)
    .sort((a, b) => (r(a).top - r(b).top) || (r(a).left - r(b).left)).slice(0, 8)
    .map((i) => ({ w: Math.round(r(i).width), h: Math.round(r(i).height), nw: i.naturalWidth, nh: i.naturalHeight, top: Math.round(r(i).top), left: Math.round(r(i).left), alt: i.alt, src: i.src.slice(0, 90) }));
});
console.log(JSON.stringify(tiles, null, 1));
const clicked = await page.evaluate(() => {
  const r = (i) => i.getBoundingClientRect();
  const imgs = [...document.querySelectorAll('img')].filter((i) => r(i).width > 200)
    .sort((a, b) => (r(a).top - r(b).top) || (r(a).left - r(b).left));
  const el = imgs.find((i) => i.naturalWidth > i.naturalHeight && Math.abs(i.naturalWidth / i.naturalHeight - 4 / 3) < 0.06);
  if (!el) return null;
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return el.src.slice(0, 90);
});
console.log('clicked', clicked);
await page.waitForTimeout(4000);
console.log('url', page.url());
await page.screenshot({ path: shot });
await browser.close();
