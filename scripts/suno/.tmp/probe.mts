import { connect } from '../suno.mts'
const { browser, page } = await connect()
const r = await page.evaluate(() => {
  const s = [...document.querySelectorAll('[role="slider"]')].map(e => ({ label: e.getAttribute('aria-label'), now: e.getAttribute('aria-valuenow'), min: e.getAttribute('aria-valuemin'), max: e.getAttribute('aria-valuemax'), text: e.getAttribute('aria-valuetext'), visible: (e as HTMLElement).offsetParent !== null, y: e.getBoundingClientRect().y }))
  const nums = [...document.querySelectorAll('input[type=number]')].map(i => ({ ph: i.getAttribute('placeholder'), v: (i as HTMLInputElement).value, vis: (i as HTMLElement).offsetParent !== null }))
  return { s, nums }
})
console.log(JSON.stringify(r, null, 1))
const el = page.locator('[role="slider"][aria-label="Duration"]').last()
await el.scrollIntoViewIfNeeded().catch(() => {})
await page.screenshot({ path: 'scripts/suno/.tmp/form.png' })
await browser.close()
