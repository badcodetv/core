// Scratch: print the text of every failed tile in the open Flow project. usage: node br-failcards.mjs <port> <projectId>
import { chromium } from 'playwright';
const [port, id] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.goto(`https://flow.google.com/project/${id}`); await page.waitForTimeout(8000);
const t = await page.evaluate(() => [...document.querySelectorAll('flow-video-tile, flow-image-tile')].map((e) => (e.textContent || '').replace(/\s+/g, ' ').trim()).filter((x) => /Fail|policy|violat|unusual|couldn|can.t/i.test(x)).map((x) => x.slice(0, 260)));
console.log(t.join('\n---\n') || 'no failed tiles in view');
await browser.close();
