// Scratch: wait for the Character portrait to finish, screenshot, press Done.
import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
if (!page) { console.log('no character page open'); process.exit(1); }
for (let i = 0; i < 60; i++) {
  const busy = await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText));
  if (!busy) break;
  await page.waitForTimeout(3000);
}
await page.waitForTimeout(2000);
await page.screenshot({ path: shot });
const done = page.locator('button', { hasText: /^Done$/ }).first();
await done.evaluate((el) => el.click());
await page.waitForTimeout(3000);
console.log('after done:', page.url());
await browser.close();
