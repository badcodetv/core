import { connect, setSlider } from '../suno.mts'
const { browser, page } = await connect()
console.log(await setSlider(page, 'Duration', 45))
console.log(await page.evaluate(() => ({ slider: document.querySelector('[role="slider"][aria-label="Duration"]')?.getAttribute('aria-valuenow'), num: (document.querySelector('input[placeholder="Auto"][type=number]') as HTMLInputElement)?.value })))
// open the workspace picker and type the new name
await page.evaluate(() => {
  const label = [...document.querySelectorAll('div,section')].filter(e => (e as HTMLElement).offsetParent !== null && /^Save to\.\.\./.test((e.textContent||'').trim()) && (e.textContent||'').trim().length < 60).pop()
  const btn = label?.querySelector('button') || label?.parentElement?.querySelector('button'); (btn as HTMLElement)?.click()
})
await page.waitForTimeout(1200)
await page.locator('input[placeholder="Search or create..."]').first().fill('camping background music')
await page.waitForTimeout(1200)
await page.screenshot({ path: 'scripts/suno/.tmp/picker.png' })
const rows = await page.evaluate(() => [...document.querySelectorAll('[role="dialog"] *, [role="menu"] *, [role="listbox"] *')].filter(e => (e as HTMLElement).offsetParent !== null && e.children.length === 0 && (e.textContent||'').trim()).map(e => e.tagName + ':' + (e.textContent||'').trim()).slice(0, 40))
console.log(rows)
await browser.close()
