import { chromium } from 'playwright';
const shot = process.argv[2];
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('aistudio.google.com'));
console.log(page.url());
await page.screenshot({ path: shot });
const info = await page.evaluate(() => {
  const tas = [...document.querySelectorAll('textarea')].map((t) => ({ aria: t.getAttribute('aria-label'), ph: t.placeholder, v: t.value.slice(0, 200) }));
  const btns = [...document.querySelectorAll('button')].map((b) => (b.getAttribute('aria-label') || b.innerText || '').trim().slice(0, 50) + (b.getAttribute('aria-disabled') === 'true' || b.disabled ? ' [disabled]' : '')).filter(Boolean);
  return { tas, btns };
});
console.log(JSON.stringify(info, null, 1));
await browser.close();
