import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
console.log('was', page.url());
if (!page.url().includes('cb27208c')) {
  const links = await page.evaluate(() => [...document.querySelectorAll('a[href*="/project/"]')].map((a) => a.href).slice(0, 10));
  console.log(links.join('\n'));
  const l = links.find((h) => h.includes('cb27208c-4b16-426d-9144-c394f2735c15'));
  await page.goto(l || page.url().replace(/\/?$/, '') + '/project/cb27208c-4b16-426d-9144-c394f2735c15');
  await page.waitForTimeout(8000);
}
console.log('now', page.url());
await page.screenshot({ path: process.argv[2] });
await browser.close();
