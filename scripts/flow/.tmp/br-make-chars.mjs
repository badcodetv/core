// Scratch: create Flow Characters by hand over CDP, each from a portrait file, a body file and a name.
// Built from make-character.mjs + char-sheet.mjs (docs/flow/automation-2026-09-rebuild.md items 25, 32, 42).
// usage: node br-make-chars.mjs <port> <projectId> <list.json> <outDir>
// list.json: [{ "name": "...", "portrait": "/abs.jpg", "body": "/abs.jpg" }]
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, projectId, listFile, outDir] = process.argv.slice(2);
const list = JSON.parse(readFileSync(listFile, 'utf8'));
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const byText = (rx) => page.evaluate((rx) => { const re = new RegExp(rx); const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && re.test(x.innerText.trim().replace(/\s+/g, ' '))); b?.click(); return !!b; }, rx);
const idle = async () => { await page.waitForTimeout(5000); for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /\b\d{1,3}%/.test(document.body.innerText)))) break; await page.waitForTimeout(3000); } await page.waitForTimeout(3000); };
const tabs = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /^(Portrait|Body|accessibility_new Create body|portrait Create portrait)$/.test(b.innerText.trim().replace(/\s+/g, ' '))).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | '));
const agree = () => page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.innerText.trim() === 'I agree'); b?.click(); return !!b; });
const results = [];
for (const c of list) {
  try {
    await page.goto(`https://flow.google.com/project/${projectId}/character`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(5000);
    const [chooser] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), byText('^upload Upload$')]);
    await chooser.setFiles(c.portrait);
    await page.waitForTimeout(3000);
    if (await agree()) console.log('agreed rights dialog');
    await page.waitForURL(/\/character\/[0-9a-f-]{36}/, { timeout: 90000 });
    const url = page.url();
    await idle();
    await page.locator('button[aria-label="Edit name"]').first().evaluate((el) => el.click());
    const input = page.locator('input[aria-label="Character name"]');
    await input.waitFor({ timeout: 10000 });
    await input.fill(c.name);
    await input.press('Enter');
    await page.waitForTimeout(2000);
    let body = false;
    if (await byText('^accessibility_new Create body$')) {
      await page.waitForTimeout(2500);
      const [ch2] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), byText('^upload Upload$')]);
      await ch2.setFiles(c.body);
      await idle();
      body = /(^| )Body( |$)/.test(await tabs());
    }
    const t = await tabs();
    await page.screenshot({ path: `${outDir}/char-${c.name.replace(/\s+/g, '-')}.png` });
    const done = await byText('^Done$');
    await page.waitForTimeout(4000);
    results.push({ name: c.name, url, id: url.split('/').pop(), tabs: t, body, done });
    console.log(c.name, url, '| tabs:', t, '| done:', done);
  } catch (e) {
    console.log(c.name, 'ERROR', String(e.message).slice(0, 200));
    await page.screenshot({ path: `${outDir}/char-${c.name.replace(/\s+/g, '-')}-err.png` }).catch(() => {});
    results.push({ name: c.name, error: String(e.message).slice(0, 200) });
    await page.keyboard.press('Escape').catch(() => {});
  }
  writeFileSync(`${outDir}/characters.json`, JSON.stringify(results, null, 2));
}
await browser.close();
