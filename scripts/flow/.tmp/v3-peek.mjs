import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const pages = browser.contexts()[0].pages();
console.log(pages.map(p=>p.url()).join('\n'));
const page = pages.find((p) => p.url().includes('flow.google.com'));
console.log((await page.evaluate(() => [...document.querySelectorAll('button')].filter(e=>e.getBoundingClientRect().width>0).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).filter(Boolean).join(' | '))).slice(0,1500));
await page.screenshot({ path: process.argv[2] });
await browser.close();
