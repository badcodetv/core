// Scratch: attach several assets (a reference image and/or Characters) by searching the "@" picker for each, then submit one prompt and save the newest tile.
// usage: node cast-many.mjs <port> <prompt.txt> <out.webp> <name1> <name2> ...
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, file, out, ...names] = process.argv.slice(2);
const p = readFileSync(file, 'utf8').trim();
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((x) => x.url().includes('flow.google.com'));
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`;
const box = page.locator('div[contenteditable="true"]').first();
const rows = () => page.evaluate(() => document.querySelectorAll('[role=option]').length);
const topSrc = () => page.evaluate(() => {
  const r = (i) => i.getBoundingClientRect();
  const imgs = [...document.querySelectorAll('img')].filter((i) => r(i).width > 200);
  return imgs.sort((a, b) => (r(a).top - r(b).top) || (r(a).left - r(b).left))[0]?.src ?? '';
});
const before = await topSrc();
await page.keyboard.press('Escape');
await box.evaluate((el) => el.focus());
await page.keyboard.press('Control+A');
await page.keyboard.press('Backspace');
for (const name of names) {
  await box.evaluate((el) => el.focus());
  await page.keyboard.press('Control+End');
  await page.keyboard.type('@');
  await page.waitForSelector('[role=option]', { timeout: 15000 });
  await page.locator('input[aria-label="Search assets"]').fill(name);
  await page.waitForTimeout(2500);
  const ok = await page.evaluate(([name, fire]) => {
    const el = [...document.querySelectorAll('[role=option]')].find((r) => r.innerText.trim().startsWith(name));
    if (el) eval(fire)(el);
    return !!el;
  }, [name, fire]);
  if (!ok) { await page.screenshot({ path: out + '-err.png' }); throw new Error('row not found: ' + name); }
  await page.waitForTimeout(1500);
  if ((await rows()) > 0) {
    await page.evaluate((fire) => { const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Add to prompt'); if (b) eval(fire)(b); }, fire);
    await page.waitForTimeout(1500);
  }
  if ((await rows()) > 0) { await page.screenshot({ path: out + '-err.png' }); throw new Error('picker still open after ' + name); }
  console.log('attached', name);
}
await box.evaluate((el) => el.focus());
await page.keyboard.press('Control+End');
await page.keyboard.insertText(' ' + p);
await page.waitForTimeout(800);
await page.screenshot({ path: out + '-bar.png' });
console.log('box:', (await box.innerText()).replace(/\s+/g, ' ').slice(0, 200));
await page.keyboard.press('Enter');
let changed = false;
for (let i = 0; i < 60; i++) {
  await page.waitForTimeout(4000);
  const busy = await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText));
  const now = await topSrc();
  if (!busy && now && now !== before && i > 2) { changed = true; break; }
}
if (!changed) { console.log('NO NEW TILE (blocked or slow)'); await page.screenshot({ path: out + '-fail.png' }); }
else {
  await page.waitForTimeout(2500);
  const b64 = await page.evaluate(async (src) => {
    const buf = new Uint8Array(await (await (await fetch(src)).blob()).arrayBuffer());
    let s = ''; for (const b of buf) s += String.fromCharCode(b);
    return btoa(s);
  }, await topSrc());
  writeFileSync(out, Buffer.from(b64, 'base64'));
  console.log('saved', out);
}
await browser.close();
