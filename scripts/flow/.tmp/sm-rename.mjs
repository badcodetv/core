// Scratch (2026-10-28): name a Character by id, then report its tabs after a reopen.
import { chromium } from 'playwright';
const [port, projectId, id, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const byText = (rx) => page.evaluate((rx) => { const re = new RegExp(rx); const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && re.test(x.innerText.trim().replace(/\s+/g, ' '))); b?.click(); return !!b; }, rx);
const tabs = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /(Portrait|Body|Create body|Create portrait)$/.test(b.innerText.trim().replace(/\s+/g, ' '))).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | '));
await page.goto(`https://flow.google.com/project/${projectId}/character/${id}`, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(7000);
console.log('tabs:', await tabs());
await page.locator('button[aria-label="Edit name"]').first().evaluate((el) => el.click());
const input = page.locator('input[aria-label="Character name"]');
await input.waitFor({ timeout: 10000 }); await input.fill(name); await input.press('Enter');
await page.waitForTimeout(2500);
await page.screenshot({ path: shot });
await byText('^Done$'); await page.waitForTimeout(5000);
await browser.close();
