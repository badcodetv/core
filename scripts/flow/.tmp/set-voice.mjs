// Scratch: on an open Character page, pick a preset voice, write its performance text, add it to the Character.
// usage: node set-voice.mjs <port> <voiceName> <performance> <shot>
import { chromium } from 'playwright';
const [port, voice, perf, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('/character/'));
if (!page) { console.log('no character page open'); process.exit(1); }
const fire = (sel, text) => page.evaluate(([sel, text]) => {
  const el = [...document.querySelectorAll(sel)].find((e) => e.getBoundingClientRect().width > 0 && (e.innerText || '').replace(/\s+/g, ' ').includes(text));
  if (!el) return false;
  el.focus?.();
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return true;
}, [sel, text]);
if (await fire('button', 'Remove')) { console.log('removed old voice'); await page.waitForTimeout(2500); }
const search = page.locator('input[aria-label="Search assets"]');
if (!(await search.count())) { console.log('open dialog:', await fire('button', 'Select a voice')); await page.waitForTimeout(2500); }
// Performance text FIRST: a synthetic pointer sequence on a row commits at once (2026-10-03), so the row gets one native click.
const ta = page.locator('textarea[placeholder^="Describe the voice performance"]');
await search.fill(voice);
await page.waitForTimeout(1500);
// 2026-10-03: any click on a row commits the bare preset and closes the dialog. Search down to one row instead: the top row is the selected one.
console.log('rows after search:', await page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace('voice_selection', '').trim().replace(/\s+/g, ' ') + (r.getAttribute('aria-selected') ? ' [aria-selected=' + r.getAttribute('aria-selected') + ']' : '')).join(' | ')));
console.log('dialog still open:', await ta.count());
if (await ta.count()) { await ta.fill(perf); await page.waitForTimeout(800); console.log('perf in box:', (await ta.inputValue()).length, 'chars'); }
await page.screenshot({ path: shot.replace('.png', '-dialog.png') });
console.log('add:', await fire('button', 'Add to character'));
await page.waitForTimeout(4000);
await page.screenshot({ path: shot });
console.log('voice button now:', await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => /voice_selection|graphic_eq|voice/i.test(b.innerText)).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | ')));
await browser.close();
