// Scratch: give an existing Character a Body image and swap its Portrait, keeping its voice. Mapped 2026-10-03.
// Order matters: Body first, so the Character is never left with no image.
// 🔴 The image's delete is button[aria-label="Delete image"]. button[aria-label="Delete"] in the top bar deletes the
// whole Character. Confirm only inside the dialog that reads "Delete this image?".
// usage: node char-sheet.mjs <port> <characterUrl> <portraitFile> <bodyFile> <shot>
import { chromium } from 'playwright';
const [port, url, portrait, body, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
await page.goto(url, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6000);
const byText = (rx) => page.evaluate((rx) => { const re = new RegExp(rx); const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && re.test(x.innerText.trim().replace(/\s+/g, ' '))); b?.click(); return !!b; }, rx);
const idle = async () => { await page.waitForTimeout(5000); for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText)))) break; await page.waitForTimeout(3000); } await page.waitForTimeout(3000); };
const upload = async (file) => {
  const [chooser] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), byText('^upload Upload$')]);
  await chooser.setFiles(file); await idle();
};
const tabs = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /^(Portrait|Body|accessibility_new Create body|portrait Create portrait)$/.test(b.innerText.trim().replace(/\s+/g, ' '))).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | '));
console.log('start tabs:', await tabs());
if (!(await byText('^accessibility_new Create body$'))) { console.log('no Create body tab; stopping'); process.exit(1); }
await page.waitForTimeout(2500);
await upload(body);
console.log('after body:', await tabs());
if (!(await byText('^Portrait$'))) { console.log('no Portrait tab; stopping'); process.exit(1); }
await page.waitForTimeout(2500);
const del = page.locator('button[aria-label="Delete image"]');
if ((await del.count()) !== 1) { console.log('Delete image buttons:', await del.count(), '; stopping'); process.exit(1); }
await del.evaluate((el) => el.click());
await page.waitForTimeout(2000);
const ok = await page.evaluate(() => {
  const d = [...document.querySelectorAll('[role=dialog],[role=alertdialog]')].find((x) => x.innerText.includes('Delete this image?'));
  const b = d && [...d.querySelectorAll('button')].find((x) => x.innerText.trim() === 'Delete');
  b?.click(); return !!b;
});
console.log('image delete confirmed:', ok);
if (!ok) process.exit(1);
await page.waitForTimeout(4000);
await upload(portrait);
console.log('after portrait:', await tabs());
await page.screenshot({ path: shot });
console.log('voice:', (await page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => /voice_selection|settings_2/.test(b.innerText) && b.getBoundingClientRect().width > 0).map((b) => b.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ')).join(' | '))).slice(0, 60));
console.log('done:', await byText('^Done$'));
await page.waitForTimeout(4000);
await browser.close();
