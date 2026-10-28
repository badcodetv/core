import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const s = p.getByPlaceholder('Search').first()
await s.fill(process.argv[2]); await p.keyboard.press('Enter'); await p.waitForTimeout(2500)
console.log(await p.evaluate(`[...document.querySelectorAll('[aria-label^="Play "]')].map(e=>e.getAttribute('aria-label')+'@'+Math.round(e.getBoundingClientRect().y)).join(' | ')`))
await b.close()
