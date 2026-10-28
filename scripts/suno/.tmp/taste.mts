import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const links = await p.evaluate(`[...document.querySelectorAll('a,button')].filter(e=>/taste/i.test(e.innerText+e.getAttribute('aria-label')+e.getAttribute('href'))).map(e=>e.tagName+' | '+e.innerText.trim().slice(0,40)+' | '+e.getAttribute('aria-label')+' | '+e.getAttribute('href'))`)
console.log(links.join('\n'))
await b.close()
