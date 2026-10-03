import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.keyboard.press('Escape');
await page.waitForTimeout(800);
await page.reload({ waitUntil: 'domcontentloaded' });
await page.waitForTimeout(5000);
const r = await page.evaluate(() => {
  const el = [...document.querySelectorAll('a,button,[role=tab],mat-list-item,div')]
    .filter((e) => (e.innerText || '').trim().replace(/\s+/g, ' ').endsWith('Characters') && e.innerText.length < 40)
    .sort((a, b) => a.innerText.length - b.innerText.length)[0];
  if (!el) return null;
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
    el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return el.tagName;
});
await page.waitForTimeout(4000);
console.log('clicked', r, 'url', page.url());
console.log((await page.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ').slice(0, 500));
await page.screenshot({ path: shot });
await browser.close();
