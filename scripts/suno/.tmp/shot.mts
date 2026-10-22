import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.screenshot({ path: process.argv[2] })
const r = await p.evaluate(`[...document.querySelectorAll('[aria-label^="Play "]')].slice(0,30).map(e=>e.getAttribute('aria-label')+' @'+Math.round(e.getBoundingClientRect().y))`)
console.log(r.join('\n'))
await b.close()
