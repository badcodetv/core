// Scratch: on an open Character page, build a custom voice (preset + performance text), save it under a name, attach it.
// Mapped 2026-10-03. Any click on a preset row commits the BARE preset and closes the dialog, so the row is never
// clicked: search narrows the list to one row, which is then the selected one.
// usage: node voice-full.mjs <port> <preset> <voiceName> <performance> <shot>
import { chromium } from 'playwright';
const [port, preset, name, perf, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
if (!page) { console.log('no character page open'); process.exit(1); }
const click = (text, exact) => page.evaluate(([text, exact]) => {
  const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && (exact ? x.innerText.trim() === text : x.innerText.replace(/\s+/g, ' ').includes(text)));
  b?.click(); return !!b;
}, [text, exact]);
const rows = () => page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ') + ' [sel=' + r.getAttribute('aria-selected') + ']'));
const idle = async () => { for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /hourglass/.test(document.body.innerText)))) break; await page.waitForTimeout(2000); } await page.waitForTimeout(1500); };
if (await click('Remove', true)) { console.log('removed old voice'); await page.waitForTimeout(2500); }
const search = page.locator('input[aria-label="Search assets"]');
if (!(await search.count())) { await click('Select a voice'); await page.waitForTimeout(2500); }
await search.fill(preset);
await page.waitForTimeout(1800);
let r = await rows();
if (r.length !== 1 || !r[0].startsWith(preset) || !r[0].includes('sel=true')) { console.log('preset not the single selected row:', r.join(' | ')); process.exit(1); }
await page.locator('textarea[placeholder^="Describe the voice performance"]').fill(perf);
await page.waitForTimeout(1200);
const h = (await page.evaluateHandle(() => [...document.querySelectorAll('input')].find((e) => e.getBoundingClientRect().width > 0 && /custom$/.test(e.value || '')))).asElement();
if (!h) { console.log('no voice-name field'); process.exit(1); }
await h.fill(name);
await page.waitForTimeout(600);
console.log('save:', await click('Save new voice'));
await page.waitForTimeout(3000);
await idle();
await search.fill(name);
await page.waitForTimeout(2500);
r = await rows();
if (r.length !== 1 || !r[0].includes(name)) { console.log('saved voice not found:', r.join(' | ').slice(0, 300)); await page.screenshot({ path: shot }); process.exit(1); }
if (!r[0].includes('sel=true')) { console.log('saved voice row not selected'); process.exit(1); }
console.log('add:', await click('Add to character', true));
await page.waitForTimeout(4000);
console.log('chip:', (await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => /voice_selection|settings_2/.test(b.innerText) && b.getBoundingClientRect().width > 0).map((b) => b.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ')).join(' | '))).slice(0, 120));
await page.screenshot({ path: shot });
await browser.close();
