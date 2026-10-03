// Scratch: close any picker and reload the project page (new Characters only reach the picker after a reload, item 29).
import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${process.argv[2]}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.keyboard.press('Escape');
await page.reload({ waitUntil: 'domcontentloaded' });
await page.waitForTimeout(7000);
console.log('reloaded', page.url());
await browser.close();
