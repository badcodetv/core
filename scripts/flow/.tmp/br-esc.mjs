// Scratch: screenshot the Flow page, print any toast/dialog text, press Escape x3 to close a stuck picker.
// usage: node br-esc.mjs <port> <shot>
import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
console.log('url', page.url());
await page.screenshot({ path: shot });
console.log('overlay:', (await page.evaluate(() => document.querySelector('.cdk-overlay-container')?.innerText ?? '')).replace(/\s+/g, ' ').slice(0, 500));
for (let i = 0; i < 3; i++) { await page.keyboard.press('Escape'); await page.waitForTimeout(400); }
console.log('options left:', await page.evaluate(() => document.querySelectorAll('[role=option]').length));
await browser.close();
