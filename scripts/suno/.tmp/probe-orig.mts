import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const ctx = b.contexts()[0]
const p = await ctx.newPage()
await p.goto('https://suno.com/song/03e29295-d33a-4db7-b566-64a58e83a196', { waitUntil: 'domcontentloaded' })
await p.waitForTimeout(6000)
console.log(await p.title())
const txt = await p.evaluate(() => document.body.innerText.slice(0, 2500))
console.log(txt)
await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/orig.png' })
await p.close()
process.exit(0)
