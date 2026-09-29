import { chromium } from 'playwright'
const ID = '1127446d-abe8-4079-9bbe-6b281e12aa74'
const browser = await chromium.connectOverCDP(process.env.SUNO_CDP_ENDPOINT ?? 'http://127.0.0.1:9222')
const ctx = browser.contexts()[0]
// A NEW tab — never navigate the create tab, that wipes the form.
const page = await ctx.newPage()
await page.goto(`https://suno.com/song/${ID}`, { waitUntil: 'domcontentloaded' })
await page.waitForTimeout(6000)
const out = await page.evaluate(`(() => {
  const txt = document.body.innerText
  let nd = null
  try { const n = document.querySelector('#__NEXT_DATA__'); if (n) nd = n.textContent } catch (e) {}
  return { url: location.href, txt, nd }
})()`) as { url: string; txt: string; nd: string | null }
console.log('URL', out.url)
console.log('--- TEXT ---')
console.log(out.txt)
if (out.nd) {
  const m = out.nd.match(/"(prompt|tags|negative_tags|metadata)":/g)
  console.log('--- NEXT_DATA keys seen:', m ? [...new Set(m)].join(' ') : 'none')
  require('fs').writeFileSync('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r58-nextdata.json', out.nd)
}
await page.close()
await browser.close()
