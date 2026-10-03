// Scratch: press a button INSIDE the dialog whose text contains <dialogText>. Never match by bare button text:
// the Character page's top bar has its own "Delete" (aria-label) that deletes the whole Character (2026-10-03).
// usage: node dialog.mjs <port> <dialogText> <buttonText> <shot>
import { chromium } from 'playwright';
const [port, dtext, btext, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const r = await page.evaluate(([dtext, btext]) => {
  const btns = [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && b.innerText.trim() === btext);
  for (const b of btns) {
    let n = b.parentElement;
    for (let i = 0; i < 6 && n; i++, n = n.parentElement) {
      const t = n.innerText || '';
      if (t.includes(dtext) && t.length < 300) { b.click(); return 'clicked in: ' + t.replace(/\s+/g, ' '); }
    }
  }
  return 'not found (' + btns.length + ' candidate buttons)';
}, [dtext, btext]);
console.log(r);
await page.waitForTimeout(3000);
console.log('dialog texts left:', await page.evaluate(() => [...document.querySelectorAll('[role=dialog],[role=alertdialog]')].map((d) => d.innerText.replace(/\s+/g, ' ').slice(0, 80)).join(' || ')));
await page.screenshot({ path: shot });
await browser.close();
