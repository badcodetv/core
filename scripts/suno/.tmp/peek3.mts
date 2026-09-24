import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const pages = b.contexts().flatMap(c => c.pages())
for (const p of pages) console.log('TAB', p.url())
const p = pages.find(p => p.url().includes('suno.com/create')) ?? pages.find(p => p.url().includes('suno.com'))
if (p) {
  await p.bringToFront()
  await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/439ecc98-bfeb-4a9e-b96d-09ff32143750/scratchpad/suno-now.png' })
  const txt = await p.evaluate(`document.body.innerText`) as string
  console.log('--- page text ---')
  console.log(txt.slice(0, 1500))
}
await b.close()
