// Scratch: click the first control whose text or aria-label matches, then screenshot and dump visible text + controls.
// usage: node click.mjs <port> <shot> <regex>
import { chromium } from 'playwright';
const [port, shot, re] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const hit = await page.evaluate((re) => {
  const rx = new RegExp(re, 'i');
  const els = [...document.querySelectorAll('button,[role=button],[role=tab],[role=option],[role=menuitem],[role=radio],li')].filter((e) => e.getBoundingClientRect().width > 0);
  const el = els.find((e) => rx.test((e.innerText || '').trim().replace(/\s+/g, ' ')) || rx.test(e.getAttribute('aria-label') || ''));
  if (!el) return null;
  el.focus?.();
  for (const t of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) el.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, { bubbles: true, cancelable: true, view: window }));
  return (el.innerText || el.getAttribute('aria-label')).trim().replace(/\s+/g, ' ').slice(0, 80);
}, re);
console.log('clicked:', hit);
await page.waitForTimeout(3500);
console.log('controls:', await page.evaluate(() => [...document.querySelectorAll('button,[role=button],[role=tab],[role=option],[role=menuitem],[role=radio],textarea,input')].filter((e) => e.getBoundingClientRect().width > 0).map((e) => `${e.tagName.toLowerCase()}${e.getAttribute('role') ? '.' + e.getAttribute('role') : ''}[${e.getAttribute('aria-label') || ''}]${(e.innerText || e.placeholder || '').trim().replace(/\s+/g, ' ').slice(0, 70)}`).join(' | ').slice(0, 4000)));
await page.screenshot({ path: shot });
await browser.close();
