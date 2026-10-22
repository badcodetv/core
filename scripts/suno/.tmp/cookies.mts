import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`(()=>{const x=[...document.querySelectorAll('#cmp-banner-container button')].find(e=>/Reject All/i.test(e.innerText)); if(x){x.click();return 'clicked'} return 'none'})()`)
await p.waitForTimeout(1000)
console.log(r, await p.evaluate(`!!document.querySelector('#cmp-first-layer.cmp-visible')`))
await b.close()
