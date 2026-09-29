import { chromium } from 'playwright'
import { writeFileSync } from 'fs'
const ID = '1127446d-abe8-4079-9bbe-6b281e12aa74'
const browser = await chromium.connectOverCDP(process.env.SUNO_CDP_ENDPOINT ?? 'http://127.0.0.1:9222')
const ctx = browser.contexts()[0]
const page = await ctx.newPage()
await page.goto(`https://suno.com/song/${ID}`, { waitUntil: 'networkidle' }).catch(() => {})
await page.waitForTimeout(8000)
const txt = await page.evaluate(`document.body.innerText`) as string
console.log('LEN', txt.length)
console.log(txt.slice(0, 4000))
writeFileSync('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r58-page.txt', txt)
await page.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/439ecc98-bfeb-4a9e-b96d-09ff32143750/scratchpad/song.png', fullPage: false })
await page.close()
await browser.close()
