// Scratch: a Character chip is already in the compose bar. Type the prompt, submit, wait, save the newest image.
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, promptFile, out, shot] = process.argv.slice(2);
const prompt = readFileSync(promptFile, 'utf8').trim();
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const box = page.locator('div[contenteditable="true"]').first();
await box.evaluate((el) => el.focus());
await page.keyboard.press('Control+End');
await page.keyboard.insertText(' ' + prompt);
await page.waitForTimeout(1000);
console.log('box:', (await box.innerText()).replace(/\s+/g, ' ').slice(0, 90));
const sub = await page.evaluate(() => {
  const b = [...document.querySelectorAll('button')].filter((x) => /arrow_forward/.test(x.innerText)).pop();
  if (b) b.click();
  return !!b;
});
console.log('submitted:', sub);
await page.waitForTimeout(6000);
await page.evaluate(() => {
  const el = [...document.querySelectorAll('mat-list-item,a,button')].find((e) => /All media$/.test((e.innerText || '').trim()));
  el?.click();
});
await page.waitForTimeout(4000);
for (let i = 0; i < 50; i++) {
  const busy = await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText));
  if (!busy && i > 3) break;
  await page.waitForTimeout(4000);
}
await page.waitForTimeout(3000);
await page.screenshot({ path: shot });
const data = await page.evaluate(async () => {
  const imgs = [...document.querySelectorAll('main img, img')].filter((i) => i.naturalWidth > 300);
  const top = imgs.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top || a.getBoundingClientRect().left - b.getBoundingClientRect().left)[0];
  if (!top) return null;
  const blob = await (await fetch(top.src)).blob();
  const buf = new Uint8Array(await blob.arrayBuffer());
  let s = ''; for (const b of buf) s += String.fromCharCode(b);
  return { src: top.src.slice(0, 120), b64: btoa(s), type: blob.type };
});
if (data) { writeFileSync(out, Buffer.from(data.b64, 'base64')); console.log('saved', data.type, data.src); } else console.log('no image found');
await browser.close();
