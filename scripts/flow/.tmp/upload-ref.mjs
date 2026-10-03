// Scratch: open the "@" picker, upload one reference file through "Upload media", screenshot what happens.
import { chromium } from 'playwright';
const [port, file, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const box = page.locator('div[contenteditable="true"]').first();
await box.evaluate((el) => el.focus());
await page.keyboard.type('@');
await page.waitForSelector('[role=option]', { timeout: 15000 });
const [chooser] = await Promise.all([
  page.waitForEvent('filechooser', { timeout: 15000 }),
  page.evaluate(() => {
    const el = [...document.querySelectorAll('button,[role=button],div,span')].filter((e) => /Upload media$/.test((e.innerText || '').trim())).sort((a, b) => a.innerText.length - b.innerText.length)[0];
    const t = el.closest('button') ?? el;
    for (const n of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) t.dispatchEvent(new (n.startsWith('pointer') ? PointerEvent : MouseEvent)(n, { bubbles: true, cancelable: true, view: window }));
  }),
]);
await chooser.setFiles(file);
await page.waitForTimeout(12000);
await page.screenshot({ path: shot });
console.log('options:', await page.evaluate(() => [...document.querySelectorAll('[role=option]')].slice(0, 4).map((r) => r.innerText.trim().replace(/\s+/g, ' '))));
console.log('box:', JSON.stringify((await box.innerText()).slice(0, 80)));
await browser.close();
