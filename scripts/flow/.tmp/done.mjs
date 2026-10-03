import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${process.argv[2]}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
const ok = await page.evaluate(() => {
  const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Done');
  if (b) b.click();
  return !!b;
});
await page.waitForTimeout(4000);
console.log('clicked', ok, 'now at', page.url());
await browser.close();
