// Scratch: create a Flow Character from one uploaded portrait, by hand over CDP.
// Follows docs/flow/automation-2026-09-rebuild.md items 25-27. Not part of the MCP.
// usage: node make-character.mjs <port> <projectId> <portraitPath> <name> <shotPath>
import { chromium } from 'playwright';

const [port, projectId, portrait, name, shot] = process.argv.slice(2);
const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const ctx = browser.contexts()[0];
const page = ctx.pages().find((p) => p.url().includes('flow.google.com')) ?? ctx.pages()[0];

await page.goto(`https://flow.google.com/project/${projectId}/character`, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(4000);
console.log('at', page.url());

const upload = page.getByText(/^\s*(upload\s*)?Upload\s*$/i).first();
const [chooser] = await Promise.all([
  page.waitForEvent('filechooser', { timeout: 15000 }),
  upload.evaluate((el) => (el.closest('button') ?? el).click()),
]);
await chooser.setFiles(portrait);
console.log('uploaded');

await page.waitForURL(/\/character\/[0-9a-f-]{36}/, { timeout: 90000 });
console.log('character url', page.url());
await page.waitForTimeout(2000);

await page.locator('button[aria-label="Edit name"]').first().evaluate((el) => el.click());
const input = page.locator('input[aria-label="Character name"]');
await input.waitFor({ timeout: 10000 });
await input.fill(name);
await input.press('Enter');
await page.waitForTimeout(1500);
console.log('named');

await page.screenshot({ path: shot });
console.log('buttons:', await page.locator('button').allInnerTexts().then((t) => t.filter(Boolean).join(' | ').slice(0, 600)));
await browser.close();
