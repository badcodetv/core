import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const d = p.locator('[role="dialog"]').last()
await d.locator('input[placeholder="Search"]').fill('instrumental')
await p.waitForTimeout(2500)
console.log(await d.evaluate(el=>[...el.querySelectorAll('a[href*="/song/"]')].map(a=>a.getAttribute('href')+' '+(a as HTMLElement).innerText.slice(0,40))))
await p.screenshot({path:'/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/suno4.png'})
process.exit(0)
