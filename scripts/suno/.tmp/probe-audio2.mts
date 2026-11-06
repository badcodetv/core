import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.locator('button[aria-label="Add audio - Browse, upload, or record audio"]').click()
await p.waitForTimeout(1500)
const items = await p.evaluate(()=>[...document.querySelectorAll('[role="menuitem"],[role="dialog"] button,[role="option"]')].map(b=>(b.getAttribute('aria-label')||'')+'|'+(b as HTMLElement).innerText.trim().slice(0,50)))
console.log(items.slice(0,40))
await p.screenshot({path:'/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/suno2.png'})
process.exit(0)
