// Scratch: wait until no hourglass is showing, then list visible buttons + option rows and screenshot.
import { chromium } from 'playwright';
const [port, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /hourglass/.test(document.body.innerText)))) break; await page.waitForTimeout(2000); }
await page.waitForTimeout(1500);
console.log('rows:', await page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace('voice_selection', '').trim().replace(/\s+/g, ' ')).join(' | ')));
console.log('buttons:', await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0).map((b) => b.innerText.trim().replace(/\s+/g, ' ') + (b.disabled ? '(off)' : '')).filter(Boolean).join(' | ').slice(-500)));
console.log('toast:', await page.evaluate(() => [...document.querySelectorAll('[role=status],[role=alert],snack-bar-container,simple-snack-bar')].map((e) => e.innerText.trim()).join(' | ')));
await page.screenshot({ path: shot });
await browser.close();
