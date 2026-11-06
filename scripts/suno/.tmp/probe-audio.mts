import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const btns = await p.evaluate(()=>[...document.querySelectorAll('button')].map(b=>(b.getAttribute('aria-label')||'')+'|'+b.innerText.trim().slice(0,30)).filter(t=>/audio|upload|add/i.test(t)))
console.log(btns)
await p.screenshot({path:'/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/suno1.png'})
process.exit(0)
