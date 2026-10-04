// Scratch: go to a project's gallery view. usage: node goto-project.mjs <port> <projectId>
import { chromium } from 'playwright';
const [port, id] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.goto(`https://flow.google.com/project/${id}`);
await page.waitForTimeout(8000);
console.log('now', page.url());
await browser.close();
