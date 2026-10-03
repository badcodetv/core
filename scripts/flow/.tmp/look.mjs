// Scratch: optionally goto a url, then screenshot and list the page's controls.
// usage: node look.mjs <port> <shot> [url]
import { chromium } from 'playwright';
const [port, shot, url] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
if (url) { await page.goto(url, { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(6000); }
console.log('url', page.url());
console.log('controls:', await page.evaluate(() => [...document.querySelectorAll('button,[role=button],[role=tab],[role=option],[role=menuitem],textarea,input')].map((e) => `${e.tagName.toLowerCase()}[${e.getAttribute('aria-label') || ''}]${(e.innerText || e.placeholder || '').trim().replace(/\s+/g, ' ').slice(0, 50)}`).filter((s) => s.length > 10).join(' | ').slice(0, 2500)));
await page.screenshot({ path: shot });
await browser.close();
