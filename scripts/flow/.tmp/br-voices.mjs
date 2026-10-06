// Scratch: for each Character, open its page, build a custom voice (preset + performance), save it, attach it, Done.
// The per-voice steps are voice-full.mjs (docs/flow/automation-2026-09-rebuild.md items 37-40), looped.
// usage: node br-voices.mjs <port> <list.json> <outDir>   list: [{ name, url, preset, voiceName, perf }]
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const [port, listFile, outDir] = process.argv.slice(2);
const list = JSON.parse(readFileSync(listFile, 'utf8'));
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const click = (text, exact) => page.evaluate(([text, exact]) => {
  const b = [...document.querySelectorAll('button')].find((x) => x.getBoundingClientRect().width > 0 && (exact ? x.innerText.trim() === text : x.innerText.replace(/\s+/g, ' ').includes(text)));
  b?.click(); return !!b;
}, [text, exact]);
const rows = () => page.evaluate(() => [...document.querySelectorAll('button[role=option]')].map((r) => r.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ') + ' [sel=' + r.getAttribute('aria-selected') + ']'));
const idle = async () => { for (let i = 0; i < 40; i++) { if (!(await page.evaluate(() => /hourglass/.test(document.body.innerText)))) break; await page.waitForTimeout(2000); } await page.waitForTimeout(1500); };
const chip = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => /voice_selection|settings_2/.test(b.innerText) && b.getBoundingClientRect().width > 0).map((b) => b.innerText.replace(/voice_selection|settings_2/g, '').trim().replace(/\s+/g, ' ')).join(' | '));
const out = [];
for (const c of list) {
  const shot = `${outDir}/voice-${c.name.replace(/\s+/g, '-')}.png`;
  try {
    await page.goto(c.url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);
    const search = page.locator('input[aria-label="Search assets"]');
    if (!(await search.count())) { if (!(await click('Select a voice'))) throw new Error('no Select a voice button (already has one?) chip=' + (await chip()).slice(0, 80)); await page.waitForTimeout(2500); }
    await search.fill(c.preset);
    await page.waitForTimeout(1800);
    let r = await rows();
    if (r.length !== 1 || !r[0].startsWith(c.preset) || !r[0].includes('sel=true')) throw new Error('preset not the single selected row: ' + r.join(' | ').slice(0, 200));
    await page.locator('textarea[placeholder^="Describe the voice performance"]').fill(c.perf);
    await page.waitForTimeout(1200);
    const h = (await page.evaluateHandle(() => [...document.querySelectorAll('input')].find((e) => e.getBoundingClientRect().width > 0 && /custom$/.test(e.value || '')))).asElement();
    if (!h) throw new Error('no voice-name field');
    await h.fill(c.voiceName);
    await page.waitForTimeout(600);
    if (!(await click('Save new voice'))) throw new Error('no Save new voice button');
    await page.waitForTimeout(3000);
    await idle();
    await search.fill(c.voiceName);
    await page.waitForTimeout(2500);
    r = await rows();
    if (r.length !== 1 || !r[0].includes(c.voiceName) || !r[0].includes('sel=true')) throw new Error('saved voice not the single selected row: ' + r.join(' | ').slice(0, 200));
    if (!(await click('Add to character', true))) throw new Error('no Add to character button');
    await page.waitForTimeout(4000);
    const ch = (await chip()).slice(0, 160);
    await page.screenshot({ path: shot });
    const done = await click('Done', true);
    await page.waitForTimeout(3500);
    out.push({ name: c.name, chip: ch, done });
    console.log(c.name, '| chip:', ch, '| done:', done);
  } catch (e) {
    console.log(c.name, 'ERROR', String(e.message).slice(0, 260));
    await page.screenshot({ path: shot }).catch(() => {});
    out.push({ name: c.name, error: String(e.message).slice(0, 260) });
    for (let i = 0; i < 3; i++) await page.keyboard.press('Escape').catch(() => {});
  }
  writeFileSync(`${outDir}/voices.json`, JSON.stringify(out, null, 2));
}
await browser.close();
