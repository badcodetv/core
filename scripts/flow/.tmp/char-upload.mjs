// Scratch: on an open Character page whose stage reads "Generate or add an image of your character", upload one file.
// usage: node char-upload.mjs <port> <file> <shot>
import { chromium } from 'playwright';
const [port, file, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
const [chooser] = await Promise.all([
  page.waitForEvent('filechooser', { timeout: 15000 }),
  page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && /^upload\s*Upload$/.test(x.innerText.trim().replace(/\s+/g, ' '))); b.click(); }),
]);
await chooser.setFiles(file);
await page.waitForTimeout(5000);
for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText)))) break; await page.waitForTimeout(3000); }
await page.waitForTimeout(3000);
console.log('tabs:', await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /Portrait|body|Body/.test(b.innerText)).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | ')));
console.log('toast:', await page.evaluate(() => [...document.querySelectorAll('[role=status],[role=alert]')].map((e) => e.innerText.trim()).filter(Boolean).join(' | ').slice(0, 200)));
await page.screenshot({ path: shot });
await browser.close();
