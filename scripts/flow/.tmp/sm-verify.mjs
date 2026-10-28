// Scratch (2026-10-28): print each Character's tabs (Portrait / Body present?).
import { chromium } from 'playwright';
const [port, projectId, ...pairs] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts()[0].pages().find((p) => p.url().includes('flow.google.com'));
const tabs = () => page.evaluate(() => [...document.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width > 0 && /(Portrait|Body|Create body|Create portrait)$/.test(b.innerText.trim().replace(/\s+/g, ' '))).map((b) => b.innerText.trim().replace(/\s+/g, ' ')).join(' | '));
for (const p of pairs) {
  const [name, id] = p.split('=');
  await page.goto(`https://flow.google.com/project/${projectId}/character/${id}`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);
  const title = await page.evaluate(() => document.querySelector('h1,h2')?.innerText ?? '');
  console.log(name.padEnd(16), '|', await tabs(), '|', title);
}
await page.goto(`https://flow.google.com/project/${projectId}`, { waitUntil: 'domcontentloaded' });
await browser.close();
