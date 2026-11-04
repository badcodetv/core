import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9224')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com/create'))!
await p.screenshot({ path: '/tmp/claude-1000/suno-form.png' })
console.log(await p.evaluate(`JSON.stringify({ph:[...document.querySelectorAll('input,textarea')].filter(e=>e.offsetParent).map(e=>e.placeholder||e.getAttribute('aria-label')).slice(0,30), btn:[...document.querySelectorAll('button')].filter(e=>e.offsetParent).map(e=>e.innerText.trim()).filter(Boolean).slice(0,60)})`))
await b.close()
