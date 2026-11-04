import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9224')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com/create'))!
const r1 = await p.evaluate(`(()=>{const x=[...document.querySelectorAll('#cmp-banner-container button')].find(e=>/Reject All/i.test(e.innerText)); if(x){x.click();return 'cookies rejected'} return 'no banner'})()`)
const t = p.locator('[role=tab]', { hasText: /^Advanced$/ }).first()
await t.click()
await p.waitForTimeout(1200)
console.log(r1, await p.evaluate(`[...document.querySelectorAll('[role=tab]')].map(x=>x.innerText.trim()+':'+x.getAttribute('aria-selected')).join(' | ')`))
await b.close()
