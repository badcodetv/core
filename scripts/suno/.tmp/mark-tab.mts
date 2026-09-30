import { chromium } from 'playwright'
const ENDPOINT = process.env.SUNO_CDP_ENDPOINT ?? 'http://127.0.0.1:9222'
const browser = await chromium.connectOverCDP(ENDPOINT)
const ctx = browser.contexts()[0]
let marked = 0
for (const p of ctx.pages()) {
  if (p.url().includes('suno.com/create')) {
    await p.evaluate(`sessionStorage.setItem('__badcode_suno_tab','1')`)
    marked++
    console.log('marked:', p.url())
  }
}
if (!marked) console.log('no suno.com/create tab found')
await browser.close()
