import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const d = p.locator('[role="dialog"]').last()
const row = d.locator('text=camping-instrumental').first()
const box = row.locator('xpath=ancestor::*[.//button[normalize-space()="Remix"]][1]')
await box.locator('button:has-text("Remix")').first().click()
await p.waitForTimeout(3000)
const btns = await p.evaluate(()=>[...document.querySelectorAll('button')].map(b=>(b as HTMLElement).innerText.trim()).filter(t=>/cover|vocal|instrument|remix|inspo|sample/i.test(t)))
console.log(btns)
await p.screenshot({path:'/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/suno5.png'})
process.exit(0)
