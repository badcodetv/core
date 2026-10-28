// Scratch: dialog open with a performance text typed. Name the custom voice, Save new voice, report what the dialog then offers.
// usage: node save-voice.mjs <port> <voiceName> <shot>
import { chromium } from 'playwright';
const [port, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
const inputs = await page.evaluate(() => [...document.querySelectorAll('input,textarea')].filter((e) => e.getBoundingClientRect().width > 0).map((e, i) => `${i}:${e.tagName}[${e.getAttribute('aria-label') || ''}]=${(e.value || '').slice(0, 30)}`));
console.log(inputs.join(' | '));
const h = await page.evaluateHandle(() => [...document.querySelectorAll('input,textarea')].find((e) => e.getBoundingClientRect().width > 0 && /custom$/.test(e.value || '')));
const el = h.asElement();
if (!el) { console.log('no voice-name field'); process.exit(1); }
await el.fill(name);
await page.waitForTimeout(600);
const click = (text) => page.evaluate((text) => { const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && x.innerText.replace(/\s+/g, ' ').includes(text)); b?.click(); return !!b; }, text);
console.log('save:', await click('Save new voice'));
await page.waitForTimeout(5000);
console.log('buttons:', await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).filter(Boolean).join(' | ').slice(-700)));
await page.screenshot({ path: shot });
await browser.close();
