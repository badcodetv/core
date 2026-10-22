import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.evaluate(`[...document.querySelectorAll('button')].find(e=>/Show new clips/.test(e.innerText))?.click()`)
await p.waitForTimeout(2500)
await b.close()
