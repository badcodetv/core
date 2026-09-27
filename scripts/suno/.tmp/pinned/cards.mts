import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`(() => [...document.querySelectorAll('[aria-label^="Play "]')].filter(pl=>Math.round(pl.getBoundingClientRect().y)<290 && pl.getBoundingClientRect().y>150).map(pl => {
    let row = pl; for (let i=0;i<8;i++){ row=row.parentElement; if (row.querySelector('a[href*="/song/"]')) break }
    const a=row.querySelector('a[href*="/song/"]')
    return { title: pl.getAttribute('aria-label').slice(5), id: a.getAttribute('href').split('/').pop(), txt: row.innerText.replace(/\\s+/g,' ') }
  }))()`)
console.log(JSON.stringify(r, null, 1))
await b.close()
