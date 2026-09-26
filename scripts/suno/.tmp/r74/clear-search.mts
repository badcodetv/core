import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts().flatMap(c => c.pages()).find(x => x.url().includes('suno.com/create'))!
await p.locator('input[aria-label="Search clips"]').fill('')
await p.waitForTimeout(2000)
console.log('search cleared:', JSON.stringify(await p.locator('input[aria-label="Search clips"]').inputValue()))
process.exit(0)
