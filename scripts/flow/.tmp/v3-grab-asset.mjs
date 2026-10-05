// Scratch: save a project image by its picker name. Opens "@", searches, and fetches the src of the row's own thumbnail (clicking the row can commit it and close the picker).
// usage: node v3-grab-asset.mjs <outDir> <name1> <name2> ...
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const [outDir, ...names] = process.argv.slice(2);
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`;
await page.keyboard.press('Escape'); await page.reload({ waitUntil: 'domcontentloaded' }); await page.waitForTimeout(9000);
const box = page.locator('div[contenteditable="true"]').first();
await box.evaluate((el) => el.focus()); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
await page.keyboard.type('@'); await page.waitForSelector('[role=option]', { timeout: 15000 });
for (const name of names) {
  await page.locator('input[aria-label="Search assets"]').fill(name); await page.waitForTimeout(6000);
  const src = await page.evaluate((name) => { const el = [...document.querySelectorAll('[role=option]')].find((r) => r.innerText.trim().startsWith(name)); return el?.querySelector('img')?.src ?? ''; }, name);
  console.log(name, src.slice(0, 140));
  if (!src) { console.log(name, 'NO PREVIEW'); continue; }
  const b64 = await page.evaluate(async (src) => { const buf = new Uint8Array(await (await (await fetch(src)).blob()).arrayBuffer()); let s = ''; for (const b of buf) s += String.fromCharCode(b); return btoa(s); }, src);
  writeFileSync(`${outDir}/${name}.bin`, Buffer.from(b64, 'base64')); console.log(name, 'saved', b64.length);
}
await page.keyboard.press('Escape'); await page.waitForTimeout(500);
await box.evaluate((el) => el.focus()); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
await browser.close();
