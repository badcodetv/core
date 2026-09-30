import { chromium } from 'playwright'
const ID = process.argv[2]
const ENDPOINT = process.env.SUNO_CDP_ENDPOINT ?? 'http://127.0.0.1:9222'
const browser = await chromium.connectOverCDP(ENDPOINT)
const ctx = browser.contexts()[0]
let page = ctx.pages().find((p) => p.url().includes(`/song/${ID}`))
if (!page) { console.log('NO TAB on that song — open it by hand first'); await browser.close(); process.exit(1) }
await page.bringToFront()
await page.waitForTimeout(1500)
// Pull the whole visible text plus any JSON the page carries about this clip.
const out = await page.evaluate(`(() => {
  const txt = document.body.innerText
  let clip = null
  try {
    const nd = document.querySelector('#__NEXT_DATA__')
    if (nd) clip = JSON.parse(nd.textContent)
  } catch (e) {}
  return { url: location.href, txt, clip: clip ? JSON.stringify(clip).slice(0, 20000) : null }
})()`)
console.log(JSON.stringify(out, null, 2))
await browser.close()
