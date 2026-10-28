// Scratch: dialog open. Search for a saved custom voice by name; if it is the one selected row, press Add to character.
// usage: node add-saved-voice.mjs <port> <voiceName> <shot>
import { chromium } from 'playwright';
const [port, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
const search = page.locator('input[aria-label="Search assets"]');
await search.fill(name);
await page.waitForTimeout(2500);
const rows = await page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ') + ' [sel=' + r.getAttribute('aria-selected') + ']'));
console.log('rows:', rows.join(' | '));
await page.screenshot({ path: shot.replace('.png', '-found.png') });
if (rows.length === 1 && rows[0].includes(name)) {
  if (!rows[0].includes('sel=true')) { await page.evaluate(() => document.querySelector('button[role=option]').click()); await page.waitForTimeout(2000); }
  const still = await search.count();
  if (still) console.log('add:', await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Add to character'); b?.click(); return !!b; }));
  await page.waitForTimeout(4000);
}
console.log('chip:', await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => /voice_selection/.test(b.innerText) && b.getBoundingClientRect().width > 0).map((b) => b.innerText.replace(/voice_selection|settings_2/g, '').trim()).join(' | ')));
await page.screenshot({ path: shot });
await browser.close();
