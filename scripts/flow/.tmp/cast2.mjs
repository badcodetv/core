// Scratch: "@" picker is open. Click the Character row; press Add to prompt only if rows remain (item 26).
import { chromium } from 'playwright';
const [port, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`;
const row = await page.evaluate(([name, fire]) => {
  const rows = [...document.querySelectorAll('[role=option]')];
  const el = rows.find((r) => r.innerText.trim().startsWith(name) && /Character/.test(r.innerText));
  if (!el) return rows.map((r) => r.innerText.trim().slice(0, 30));
  eval(fire)(el);
  return 'clicked ' + el.innerText.trim().replace(/\s+/g, ' ');
}, [name, fire]);
console.log('row:', row);
await page.waitForTimeout(2000);
const left = await page.evaluate(() => document.querySelectorAll('[role=option]').length);
console.log('rows left:', left);
if (left > 0) {
  const add = await page.evaluate((fire) => {
    const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Add to prompt');
    if (b) eval(fire)(b);
    return !!b;
  }, fire);
  console.log('add to prompt:', add);
  await page.waitForTimeout(2000);
}
await page.screenshot({ path: shot });
await browser.close();
