// Scratch: for each prompt, cast a Flow Character by hand ("@" picker), submit with Enter, wait, save the newest tile.
// Recipe: docs/flow/automation-2026-09-rebuild.md items 29-31. usage: node cast-batch.mjs <port> <prompts.json> <character> <outDir>
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, file, character, outDir] = process.argv.slice(2);
const prompts = JSON.parse(readFileSync(file, 'utf8'));
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const fire = `(el) => { el.focus?.(); for (const t of ['pointerdown','mousedown','pointerup','mouseup','click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window })); }`;
const box = page.locator('div[contenteditable="true"]').first();
const topSrc = () => page.evaluate(() => {
  const imgs = [...document.querySelectorAll('img')].filter((i) => i.getBoundingClientRect().width > 200);
  const r = (i) => i.getBoundingClientRect();
  return imgs.sort((a, b) => (r(a).top - r(b).top) || (r(a).left - r(b).left))[0]?.src ?? '';
});
for (const { id, p } of prompts) {
  try {
    const before = await topSrc();
    await box.evaluate((el) => el.focus());
    await page.keyboard.type('@');
    await page.waitForSelector('[role=option]', { timeout: 15000 });
    await page.waitForTimeout(1500);
    const row = await page.evaluate(([name, fire]) => {
      const el = [...document.querySelectorAll('[role=option]')].find((r) => r.innerText.trim().startsWith(name) && /Character/.test(r.innerText));
      if (el) eval(fire)(el);
      return !!el;
    }, [character, fire]);
    if (!row) throw new Error('character row not found');
    await page.waitForTimeout(1500);
    if (await page.evaluate(() => document.querySelectorAll('[role=option]').length) > 0) {
      await page.evaluate((fire) => { const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Add to prompt'); if (b) eval(fire)(b); }, fire);
      await page.waitForTimeout(1500);
    }
    const tag = await box.innerText();
    if (!tag.includes(character)) throw new Error('chip not attached: ' + tag.slice(0, 40));
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
  }
}
await browser.close();
