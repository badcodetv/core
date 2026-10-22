import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`[...document.querySelectorAll('[aria-label^="Play brj-fp-"]')].map(pl=>{let row=pl;for(let i=0;i<8;i++){row=row.parentElement;if(row.querySelector('a[href*="/song/"]'))break}
 const a=row.querySelector('a[href*="/song/"]'); const d=(row.innerText.match(/\\b\\d:\\d\\d\\b/)||[''])[0]
 return pl.getAttribute('aria-label').slice(5)+' — '+d+' — https://suno.com/song/'+a.getAttribute('href').split('/').pop()})`)
console.log(r.join('\n')); console.log(r.length)
console.log(await p.evaluate(`document.body.innerText.match(/Credits remaining[^\\n]*/)?.[0] ?? ''`))
await b.close()
