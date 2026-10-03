// Scratch: wait for the Character portrait's percentage to clear (no Done press).
import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${process.argv[2]}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
for (let i = 0; i < 60; i++) { if (!(await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText)))) break; await page.waitForTimeout(3000); }
await page.waitForTimeout(2000);
console.log('portrait ready at', page.url());
await browser.close();
