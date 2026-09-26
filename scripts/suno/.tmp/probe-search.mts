import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
let p = b.contexts().flatMap(c => c.pages()).find(x => x.url().includes('suno.com'))
if (!p) { p = await b.contexts()[0].newPage() }
if (!p.url().includes('/create')) await p.goto('https://suno.com/create?wid=a54391b0-9ad8-499f-b0d4-6de914bfd557')
const s = p.locator('input[aria-label="Search clips"]')
await s.waitFor({ timeout: 30000 })
await s.fill('r71-wordsonly-v6-w40')
await p.waitForTimeout(4000)
console.log(p.url(), await p.evaluate(`document.querySelectorAll('a[href="/song/36d0b981-5ffb-482b-9b9b-ab9e50f3a56b"]').length`))
process.exit(0)
