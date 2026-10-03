import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
for (const p of browser.contexts()[0].pages()) console.log('page', p.url());
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.screenshot({ path: shot });
await browser.close();
