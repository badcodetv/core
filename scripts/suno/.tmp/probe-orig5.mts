import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = await b.contexts()[0].newPage()
await p.goto('https://suno.com/song/03e29295-d33a-4db7-b566-64a58e83a196', { waitUntil: 'domcontentloaded' })
await p.waitForTimeout(6000)
await p.locator('button[aria-label="More options"]').first().click()
await p.waitForTimeout(1200)
const e = p.getByRole('menuitem', { name: 'Edit', exact: true }).first()
const bb = await e.boundingBox(); if (bb) { await p.mouse.move(bb.x + 20, bb.y + bb.height/2); await p.waitForTimeout(400); await p.mouse.move(bb.x + bb.width - 10, bb.y + bb.height/2) }
await p.waitForTimeout(1500)
console.log(await p.evaluate(() => [...document.querySelectorAll('[role="menuitem"]')].map(x => (x as HTMLElement).innerText.trim().replace(/\s+/g,' '))))
await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/orig-edit.png' })
await p.keyboard.press('Escape'); await p.close(); process.exit(0)
