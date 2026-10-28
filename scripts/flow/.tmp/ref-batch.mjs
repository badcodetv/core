// Scratch: for each prompt, attach a reference image AND a Character through the "@" picker, submit with Enter, save the newest tile.
// Recipe: docs/flow/automation-2026-09-rebuild.md, 2 October entries.
// usage: node cast-ref-batch.mjs <port> <prompts.json> <refRowName> <character> <outDir>
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, file, refName, character, outDir] = process.argv.slice(2);
const prompts = JSON.parse(readFileSync(file, 'utf8'));
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`;
const box = page.locator('div[contenteditable="true"]').first();
const rows = () => page.evaluate(() => document.querySelectorAll('[role=option]').length);
const topSrc = () => page.evaluate(() => {
  const r = (i) => i.getBoundingClientRect();
  const imgs = [...document.querySelectorAll('img')].filter((i) => r(i).width > 200);
  return imgs.sort((a, b) => (r(a).top - r(b).top) || (r(a).left - r(b).left))[0]?.src ?? '';
});
async function attach(name) {
  if ((await rows()) === 0) {
    await box.evaluate((el) => el.focus());
    await page.keyboard.press('Control+End');
    await page.keyboard.type('@');
    await page.waitForSelector('[role=option]', { timeout: 15000 });
    await page.waitForTimeout(1500);
  }
  const ok = await page.evaluate(([name, fire]) => {
    const el = [...document.querySelectorAll('[role=option]')].find((r) => r.innerText.trim().startsWith(name));
    if (el) eval(fire)(el);
    return !!el;
  }, [name, fire]);
  if (!ok) throw new Error('row not found: ' + name);
  await page.waitForTimeout(1500);
  if ((await rows()) > 0) {
    await page.evaluate((fire) => { const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Add to prompt'); if (b) eval(fire)(b); }, fire);
    await page.waitForTimeout(1500);
  }
  if ((await rows()) > 0) throw new Error('picker still open after adding ' + name);
}
let first = true;
for (const { id, p } of prompts) {
  try {
    const before = await topSrc();
    await attach(refName);
    if (character !== '-') await attach(character);
    if (first) { await page.screenshot({ path: `${outDir}/${id}-bar.png` }); first = false; }
    await box.evaluate((el) => el.focus());
    await page.keyboard.press('Control+End');
    await page.keyboard.insertText(' ' + p);
    await page.waitForTimeout(800);
    await page.keyboard.press('Enter');
    let changed = false;
    for (let i = 0; i < 60; i++) {
      await page.waitForTimeout(4000);
      const busy = await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText));
      const now = await topSrc();
      if (!busy && now && now !== before && i > 2) { changed = true; break; }
    }
    if (!changed) { console.log(id, 'NO NEW TILE (blocked or slow)'); await page.screenshot({ path: `${outDir}/${id}-fail.png` }); continue; }
    await page.waitForTimeout(2500);
    const b64 = await page.evaluate(async (src) => {
      const buf = new Uint8Array(await (await (await fetch(src)).blob()).arrayBuffer());
      let s = ''; for (const b of buf) s += String.fromCharCode(b);
      return btoa(s);
    }, await topSrc());
    writeFileSync(`${outDir}/${id}.webp`, Buffer.from(b64, 'base64'));
    console.log(id, 'saved');
  } catch (e) {
    console.log(id, 'ERROR', String(e.message).slice(0, 160));
    await page.screenshot({ path: `${outDir}/${id}-err.png` }).catch(() => {});
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(1000);
  }
}
await browser.close();
