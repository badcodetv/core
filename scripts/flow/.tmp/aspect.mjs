// Scratch: set the image frame shape by hand. usage: node aspect.mjs <port> <16:9|4:3|1:1|3:4|9:16>
import { chromium } from 'playwright';
const [port, want] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = (rx) => page.evaluate((rx) => {
  const re = new RegExp(rx);
  const el = [...document.querySelectorAll('button,[role=tab],[role=radio]')].find((e) => e.getBoundingClientRect().width > 0 && re.test(e.innerText.trim().replace(/\s+/g, ' ')));
  if (!el) return null;
  el.focus?.();
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return el.innerText.trim().replace(/\s+/g, ' ');
}, rx);
const open = () => page.evaluate(() => [...document.querySelectorAll('button,[role=tab]')].some((e) => e.getBoundingClientRect().width > 0 && /9:16$/.test(e.innerText.trim())));
if (!(await open())) { console.log('open:', await fire('Banana.*x\\d$')); await page.waitForTimeout(1500); }
console.log('pick:', await fire(want + '$'));
await page.waitForTimeout(1000);
await page.keyboard.press('Escape');
await page.waitForTimeout(800);
console.log('label:', await page.evaluate(() => [...document.querySelectorAll('button')].map((b) => b.innerText.trim().replace(/\s+/g, ' ')).filter((t) => /Banana.*x\d$/.test(t)).join(' | ')));
await browser.close();
