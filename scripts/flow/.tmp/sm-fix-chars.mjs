// Scratch (2026-10-28): finish two half-made Characters in the Speakeasy Mint ALT project.
// usage: node sm-fix-chars.mjs <port> <projectId> <outDir>
import { chromium } from 'playwright';
const [port, projectId, outDir] = process.argv.slice(2);
const H = process.env.HOME;
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const byText = (rx) => page.evaluate((rx) => { const re = new RegExp(rx); const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && re.test(x.innerText.trim().replace(/\s+/g, ' '))); b?.click(); return !!b; }, rx);
const tabs = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /(Portrait|Body|Create body|Create portrait)$/.test(b.innerText.trim().replace(/\s+/g, ' '))).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | '));
const idle = async () => { await page.waitForTimeout(5000); for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText)))) break; await page.waitForTimeout(3000); } await page.waitForTimeout(3000); };
const upload = async (file) => { await page.waitForTimeout(2500); const [ch] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), byText('^upload Upload$')]); await ch.setFiles(file); await idle(); };
const open = async (id) => { await page.goto(`https://flow.google.com/project/${projectId}/character/${id}`, { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(6000); };
// 1. Baker: add the missing Portrait
await open('28973903-3d35-42a0-aaa6-443837f525e3');
console.log('baker before:', await tabs());
if (await byText('Create portrait$')) await upload(`${H}/.cache/sm-cast/baker.jpg`);
await byText('^Done$'); await page.waitForTimeout(4000);
await open('28973903-3d35-42a0-aaa6-443837f525e3');
console.log('baker after reload:', await tabs());
await page.screenshot({ path: `${outDir}/fix-baker.png` });
await byText('^Done$'); await page.waitForTimeout(3000);
// 2. Untitled (the Red Leader portrait): name it, add the Body
const RL = 'd3a3258f-1b0a-44d4-b186-5b92f41533bf';
await open(RL);
console.log('red before:', await tabs());
await page.locator('button[aria-label="Edit name"]').first().evaluate((el) => el.click());
const input = page.locator('input[aria-label="Character name"]');
await input.waitFor({ timeout: 10000 }); await input.fill('SM Red Leader'); await input.press('Enter');
await page.waitForTimeout(2000);
if (await byText('Create body$')) await upload(`${H}/.cache/sm-cast/redleader-body.jpg`);
await page.screenshot({ path: `${outDir}/fix-red.png` });
await byText('^Done$'); await page.waitForTimeout(4000);
await open(RL);
console.log('red after reload:', await tabs(), '| title:', await page.evaluate(() => document.body.innerText.includes('SM Red Leader')));
await page.screenshot({ path: `${outDir}/fix-red-after.png` });
await byText('^Done$'); await page.waitForTimeout(3000);
await browser.close();
