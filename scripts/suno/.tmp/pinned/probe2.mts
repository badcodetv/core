import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`(() => {
  const labs = [...document.querySelectorAll('[aria-label]')].map(e=>e.getAttribute('aria-label')).filter(a=>/\\b(un)?pin/i.test(a) && !/camping/i.test(a))
  const uniq = {}; labs.forEach(l=>uniq[l]=(uniq[l]||0)+1)
  // text near a "Pinned" heading
  const heads = [...document.querySelectorAll('*')].filter(e=>e.children.length===0 && /^pinned/i.test(e.textContent.trim())).map(e=>e.textContent.trim())
  // for each unpin button, find the row's clip link
  const rows = [...document.querySelectorAll('[aria-label]')].filter(e=>/unpin/i.test(e.getAttribute('aria-label'))).map(btn=>{
     let el=btn; for(let i=0;i<12&&el;i++){ const a=el.querySelector && el.querySelector('a[href*="/song/"]'); if(a) return a.getAttribute('href')+' | '+a.textContent.trim(); el=el.parentElement } return 'no-link' })
  return { uniq, heads, rows }
})()`)
console.log(JSON.stringify(r, null, 1))
await b.close()
