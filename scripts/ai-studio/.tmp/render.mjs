// Render narrator lines on the AI Studio speech page (3.1 Flash TTS, Composer) over CDP.
// usage: node render.mjs <lines.json> <outdir> [voice]
// lines.json: [{ "file": "name.wav", "text": "..." }, ...]
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
const [linesFile, outDir, voice = 'Zubenelgenubi'] = process.argv.slice(2);
const lines = JSON.parse(fs.readFileSync(linesFile, 'utf8'));
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('aistudio.google.com'));

// voice: open the panel, pick it unless it is already Current, close
await page.getByRole('button', { name: 'Open voice settings' }).click().catch(() => {});
const dialog = page.locator('[role=dialog],mat-dialog-container').filter({ hasText: 'Speaker settings' }).first();
await dialog.waitFor({ timeout: 5000 }).catch(() => {});
if (await dialog.isVisible().catch(() => false)) {
  const accent = await dialog.evaluate((d) => d.innerText.match(/Accent\s+language\s+([^\n]+)/)?.[1]);
  console.log('accent menu:', accent);
  await dialog.getByText(voice, { exact: true }).first().click();
  await page.waitForTimeout(800);
  const cur = await dialog.evaluate((d) => d.innerText.match(/([A-Za-z]+)\nCurrent/)?.[1]);
  console.log('current voice:', cur);
  await dialog.getByRole('button', { name: /close/i }).first().click().catch(() => page.keyboard.press('Escape'));
  await page.waitForTimeout(800);
}

const wav = (pcm, rate = 24000, ch = 1, bits = 16) => {
  const h = Buffer.alloc(44);
  h.write('RIFF', 0); h.writeUInt32LE(36 + pcm.length, 4); h.write('WAVE', 8); h.write('fmt ', 12);
  h.writeUInt32LE(16, 16); h.writeUInt16LE(1, 20); h.writeUInt16LE(ch, 22); h.writeUInt32LE(rate, 24);
  h.writeUInt32LE(rate * ch * bits / 8, 28); h.writeUInt16LE(ch * bits / 8, 32); h.writeUInt16LE(bits, 34);
  h.write('data', 36); h.writeUInt32LE(pcm.length, 40);
  return Buffer.concat([h, pcm]);
};

const ta = page.getByRole('textbox', { name: 'Speech block text' });
for (const { file, text } of lines) {
  await ta.click();
  await ta.fill(text);
  await page.waitForTimeout(500);
  const respP = page.waitForResponse((r) => r.url().includes('GenerateContent') && r.request().method() === 'POST', { timeout: 120000 });
  await ta.hover();
  await page.getByRole('button', { name: 'Preview this block' }).click({ force: true });
  const resp = await respP;
  const req = resp.request().postData() || '';
  const body = await resp.text();
  const chunks = [...body.matchAll(/"audio\/l16;[^"]*","([A-Za-z0-9+\/=]+)"/gi)].map((m) => Buffer.from(m[1], 'base64'));
  const pcm = Buffer.concat(chunks);
  const secs = pcm.length / 48000;
  const ok = req.includes(voice) && req.includes('Accent: British (Brixton)') && req.includes(text.slice(0, 20));
  console.log(`${file} | http ${resp.status()} | ${secs.toFixed(2)}s | request has voice+accent+text: ${ok}`);
  if (!ok) console.log('  REQUEST:', req.slice(0, 600));
  if (pcm.length) fs.writeFileSync(path.join(outDir, file), wav(pcm));
  // wait for the preview to stop playing before the next one
  await page.getByRole('button', { name: 'Preview this block' }).waitFor({ state: 'attached', timeout: 60000 }).catch(() => {});
  await page.waitForTimeout(1500);
}
await browser.close();
