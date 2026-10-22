import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const c = await p.evaluate(`[...document.querySelectorAll('button,a')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.x<90||r.y<70)}).map(e=>e.tagName+' | '+(e.innerText||'').trim().slice(0,30)+' | '+e.getAttribute('aria-label')+' | '+e.getAttribute('href')+' @'+Math.round(e.getBoundingClientRect().x)+','+Math.round(e.getBoundingClientRect().y))`)
console.log(c.join('\n'))
await b.close()
