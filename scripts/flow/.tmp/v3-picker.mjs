// Scratch: reload the project, open the "@" picker, optionally search, list the option rows.
import { chromium } from 'playwright';
const [shot, q] = process.argv.slice(2);
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.keyboard.press('Escape'); await page.waitForTimeout(500);
await page.reload({ waitUntil: 'domcontentloaded' }); await page.waitForTimeout(9000);
const box = page.locator('div[contenteditable="true"]').first();
await box.evaluate((el) => el.focus());
await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
await page.keyboard.type('@');
await page.waitForSelector('[role=option]', { timeout: 15000 });
if (q) { await page.locator('input[aria-label="Search assets"]').fill(q); }
await page.waitForTimeout(7000);
console.log((await page.evaluate(() => [...document.querySelectorAll('[role=option]')].map((r) => r.innerText.trim().replace(/\s+/g, ' ')).join(' || '))).slice(0, 900));
console.log('label:', await page.evaluate(() => [...document.querySelectorAll('button')].map((b) => b.innerText.trim().replace(/\s+/g, ' ')).filter((t) => /x\d$/.test(t)).join('|')));
await page.screenshot({ path: shot });
await page.keyboard.press('Escape'); await page.waitForTimeout(500);
await box.evaluate((el) => el.focus()); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
await browser.close();
