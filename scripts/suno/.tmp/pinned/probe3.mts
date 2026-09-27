import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`(() => {
  const plays = [...document.querySelectorAll('[aria-label^="Play "]')].filter(e=>e.offsetParent!==null)
  return plays.map(pl => {
    let row = pl; for (let i=0;i<8;i++){ row=row.parentElement; if (row.querySelector('a[href*="/song/"]') && row.querySelectorAll('[aria-label^="Play "]').length===1 && row.getBoundingClientRect().height>40) break }
    const a=row.querySelector('a[href*="/song/"]')
    const btns=[...row.querySelectorAll('button')].map(x=>x.getAttribute('aria-label')||x.textContent.trim().slice(0,20)).filter(Boolean)
    return { title: pl.getAttribute('aria-label').slice(5), href: a&&a.getAttribute('href'), y: Math.round(row.getBoundingClientRect().y), btns: btns.join(' / '), txt: row.innerText.replace(/\\s+/g,' ').slice(0,120) }
  })
})()`)
console.log(JSON.stringify(r, null, 1))
await p.screenshot({ path: '/tmp/claude-1000/suno-ws.png' })
await b.close()
