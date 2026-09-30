import { connect } from '../suno.mts'
const { browser, page } = await connect()
const inp = page.locator('input[placeholder="Search or create..."]').first()
console.log('input visible', await inp.isVisible().catch(() => false), await inp.inputValue().catch(() => '?'))
const box = await inp.boundingBox()
console.log(box)
// the + button sits just right of the input
const btn = await page.evaluateHandle(() => {
  const i = document.querySelector('input[placeholder="Search or create..."]') as HTMLElement
  const r = i.getBoundingClientRect()
  const cands = [...document.querySelectorAll('button')].filter(b => { const q = b.getBoundingClientRect(); return q.width > 0 && q.left >= r.right - 5 && q.left < r.right + 60 && Math.abs((q.top + q.bottom) / 2 - (r.top + r.bottom) / 2) < 20 })
  return cands[0] ?? null
})
const el = btn.asElement()
console.log('plus', !!el, el ? await el.evaluate(b => b.outerHTML.slice(0, 200)) : '')
if (el) { await el.click(); await page.waitForTimeout(2500) }
await page.screenshot({ path: 'scripts/suno/.tmp/after-plus.png' })
console.log(await page.evaluate(() => { const l = [...document.querySelectorAll('div,section')].filter(e => (e as HTMLElement).offsetParent !== null && /^Save to\.\.\./.test((e.textContent||'').trim()) && (e.textContent||'').trim().length < 60).pop(); return l?.textContent }))
console.log(page.url())
await browser.close()
