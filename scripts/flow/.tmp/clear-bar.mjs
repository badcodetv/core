// Scratch: close the "@" picker and empty the prompt box.
import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${process.argv[2]}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.keyboard.press('Escape');
await page.waitForTimeout(800);
const box = page.locator('div[contenteditable="true"]').first();
await box.evaluate((el) => el.focus());
await page.keyboard.press('Control+A');
await page.keyboard.press('Backspace');
await page.waitForTimeout(500);
console.log('options:', await page.evaluate(() => document.querySelectorAll('[role=option]').length), 'box:', JSON.stringify((await box.innerText()).trim()));
await browser.close();
