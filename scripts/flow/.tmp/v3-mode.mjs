// Scratch: open the compose settings trigger and click a sequence of controls by regex. usage: node v3-mode.mjs <shot.png> <rx1> <rx2> ...
import { chromium } from 'playwright';
const [shot, ...rxs] = process.argv.slice(2);
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = (rx) => page.evaluate((rx) => {
  const re = new RegExp(rx);
  const el = [...document.querySelectorAll('button,[role=tab],[role=radio],[role=option],[role=menuitem],[role=menuitemradio]')].find((e) => e.getBoundingClientRect().width > 0 && re.test(e.innerText.trim().replace(/\s+/g, ' ')));
  if (!el) return null;
  el.focus?.();
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return el.innerText.trim().replace(/\s+/g, ' ');
}, rx);
const dump = () => page.evaluate(() => [...document.querySelectorAll('button,[role=tab],[role=radio],[role=option],[role=menuitem],[role=menuitemradio]')].filter((e) => e.getBoundingClientRect().width > 0).map((b) => `${b.getAttribute('role')||'btn'}${b.getAttribute('aria-selected')==='true'||b.getAttribute('data-state')==='active'||b.getAttribute('aria-checked')==='true'?'*':''}:${b.innerText.trim().replace(/\s+/g, ' ')}`).filter((t) => !/:$/.test(t)).join(' | '));
for (const rx of rxs) { console.log('click', rx, '=>', await fire(rx)); await page.waitForTimeout(1500); }
console.log((await dump()).slice(-1200));
await page.screenshot({ path: shot });
await browser.close();
