import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:9222`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
console.log(page.url());
console.log(await page.evaluate(() => [...document.querySelectorAll('button')].map(b => b.innerText.trim().replace(/\s+/g,' ')).filter(t => /crop_|x\d|Banana|Veo|Omni/i.test(t)).join(' | ')));
console.log('box:', await page.evaluate(() => (document.querySelector('div[contenteditable="true"]')?.innerText || '').length));
await browser.close();
