import { chromium } from 'playwright';
const shot = process.argv[2];
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find((p) => p.url().includes('aistudio.google.com'));
await page.getByRole('button', { name: 'Open voice settings' }).click();
await page.waitForTimeout(1500);
await page.screenshot({ path: shot });
const info = await page.evaluate(() => ({
  selects: [...document.querySelectorAll('mat-select,[role=combobox],select')].map((s) => (s.getAttribute('aria-label') || '') + ' = ' + s.innerText.trim().slice(0, 60)),
  inputs: [...document.querySelectorAll('input,textarea')].map((t) => (t.getAttribute('aria-label') || t.placeholder || '') + ' = ' + t.value.slice(0, 60)),
  dialogs: [...document.querySelectorAll('[role=dialog],mat-dialog-container')].map((d) => d.innerText.slice(0, 1500)),
}));
console.log(JSON.stringify(info, null, 1));
await browser.close();
