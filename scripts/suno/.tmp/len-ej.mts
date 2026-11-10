import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
console.log(await p.evaluate(`(() => { const a=[...document.querySelectorAll('a[href*="b1fecf5a"]')].find(e=>e.offsetParent); let r=a; for(let i=0;i<8&&r;i++){ if(/\\d:\\d\\d/.test(r.innerText)) break; r=r.parentElement } return r? r.innerText.replace(/\\s+/g,' ').slice(0,300):'none' })()`))
process.exit(0)
