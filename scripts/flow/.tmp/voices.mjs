// Scratch: with the "Select a voice" dialog open, scroll the list and print every voice row.
import { chromium } from 'playwright';
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${process.argv[2]}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const seen = new Map();
for (let i = 0; i < 12; i++) {
  const rows = await page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace('voice_selection', '').trim().replace(/\s+/g, ' ')));
  rows.forEach((r) => seen.set(r, 1));
  await page.evaluate(() => { const r = [...document.querySelectorAll('button[role=option]')].pop(); r?.scrollIntoView({ block: 'start' }); });
  await page.waitForTimeout(700);
}
console.log([...seen.keys()].join('\n'));
console.log('dropdown:', await page.evaluate(() => [...document.querySelectorAll('[role=combobox],select,mat-select')].map((e) => e.innerText.trim()).join(' | ')));
await browser.close();
