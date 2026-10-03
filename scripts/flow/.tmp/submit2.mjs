// Scratch: prompt + Character chip already in the bar. Submit, wait for a NEW top tile, save it.
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [port, out, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const count = () => page.evaluate(() => document.querySelectorAll('img').length);
const boxLen = () => page.evaluate(() => (document.querySelector('div[contenteditable="true"]')?.innerText || '').length);
const before = await count();
const r = await page.evaluate(() => {
  const btns = [...document.querySelectorAll('button')].filter((x) => x.innerText.trim() === 'arrow_forward' || /arrow_forward\s*Create/i.test(x.innerText));
  const b = btns.pop();
  if (!b) return null;
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
    b.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return b.innerText.trim() + ' disabled=' + b.disabled;
});
console.log('submit button:', r);
await page.waitForTimeout(3000);
if ((await boxLen()) > 200) {
  console.log('still in box, trying Enter');
  await page.locator('div[contenteditable="true"]').first().evaluate((el) => el.focus());
  await page.keyboard.press('Control+End');
  await page.keyboard.press('Enter');
  await page.waitForTimeout(3000);
}
console.log('box length after submit:', await boxLen());
for (let i = 0; i < 60; i++) {
  await page.waitForTimeout(4000);
  const busy = await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText));
  if (!busy && i > 4) break;
}
await page.waitForTimeout(3000);
await page.screenshot({ path: shot });
console.log('imgs before/after:', before, await count());
await browser.close();
