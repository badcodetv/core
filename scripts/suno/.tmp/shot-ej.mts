import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
console.log(p.url())
await p.screenshot({ path: '/tmp/claude-1000/-home-kai-projects-badcode-badcode/0d8449af-726d-4f3d-be95-a69c9bb27d47/scratchpad/suno-now.png' })
console.log(await p.evaluate(`JSON.stringify([...document.querySelectorAll('a[href*="/song/"]')].filter(e=>e.offsetParent).map(a=>[a.innerText.trim().slice(0,60),a.href]).slice(0,12))`))
