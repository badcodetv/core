import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = await b.contexts()[0].newPage()
await p.goto('https://suno.com/song/03e29295-d33a-4db7-b566-64a58e83a196', { waitUntil: 'domcontentloaded' })
await p.waitForTimeout(6000)
console.log(await p.evaluate(() => [...document.querySelectorAll('button')].map(b => (b.getAttribute('aria-label') || '') + '|' + (b as HTMLElement).innerText.trim().slice(0, 20)).filter(t => t !== '|').slice(0, 40)))
// click the 6th round button in the action row (the ... one) by position: right of Share
const box = await p.locator('button[aria-label="Share"]').first().boundingBox()
if (box) { await p.mouse.click(box.x + box.width + 40, box.y + box.height / 2) }
await p.waitForTimeout(1500)
console.log(await p.evaluate(() => document.querySelector('[data-radix-popper-content-wrapper], [role="menu"]')?.textContent?.slice(0, 600)))
await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/orig-menu.png' })
await p.close(); process.exit(0)
