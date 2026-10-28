// Scratch: open a Character page and its "Select a voice" dialog. usage: node br-open-voices.mjs <port> <characterUrl>
import { chromium } from 'playwright';
const [port, url] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.goto(url, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6000);
console.log('opened:', await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && x.innerText.replace(/\s+/g, ' ').includes('Select a voice')); b?.click(); return !!b; }));
await page.waitForTimeout(3000);
await browser.close();
