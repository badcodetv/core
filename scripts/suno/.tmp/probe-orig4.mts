import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = await b.contexts()[0].newPage()
await p.goto('https://suno.com/song/03e29295-d33a-4db7-b566-64a58e83a196', { waitUntil: 'domcontentloaded' })
await p.waitForTimeout(6000)
await p.locator('button[aria-label="More options"]').first().click()
await p.waitForTimeout(1500)
const read = () => p.evaluate(() => [...document.querySelectorAll('[role="menuitem"]')].map(x => (x as HTMLElement).innerText.trim().replace(/\s+/g,' ')))
const top = await read(); console.log('top', top)
for (const t of top) { if (/^edit$|^manage$/i.test(t)) { await p.keyboard.press('Escape'); await p.waitForTimeout(500); await p.locator('button[aria-label="More options"]').first().click(); await p.waitForTimeout(1000); await p.getByRole('menuitem', { name: t, exact: true }).first().hover(); await p.waitForTimeout(1200); console.log(t, '→', (await read()).filter(x => !top.includes(x))) } }
await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/orig-menu.png' })
await p.keyboard.press('Escape'); await p.close(); process.exit(0)
