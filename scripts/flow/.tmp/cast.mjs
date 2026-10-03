// Scratch: with the "@" asset picker already open, pick a Character and add it to the prompt.
import { chromium } from 'playwright';
const [port, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
// full pointer+mouse sequence, in-page (law 7)
const press = (src) => page.evaluate((src) => {
  const rx = new RegExp(src, 'i');
  const search = document.querySelector('input[placeholder*="Search assets" i]');
  let root = search;
  for (let i = 0; i < 8 && root?.parentElement; i++) root = root.parentElement;
  const els = [...(root ?? document.body).querySelectorAll('*')]
    .filter((e) => rx.test((e.innerText || '').trim()))
    .sort((a, b) => a.innerText.length - b.innerText.length);
  const el = els[0]?.closest('button,[role=tab],[role=option]') ?? els[0];
  if (!el) return null;
  el.focus?.();
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
    el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return `${el.tagName} ${el.getAttribute('role') ?? ''} "${el.innerText.trim().slice(0, 60)}"`;
}, src);
console.log('tab:', await press('^Characters$'));
await page.waitForTimeout(2500);
await page.screenshot({ path: shot.replace('.png', '-a.png') });
console.log('row:', await press(`^${name}`));
await page.waitForTimeout(2000);
await page.screenshot({ path: shot });
await browser.close();
