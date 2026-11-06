import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.locator('button:has-text("Cover")').first().click()
await p.waitForTimeout(1200)
const opts = await p.evaluate(()=>[...document.querySelectorAll('[role="menuitem"],[role="option"],[role="menuitemradio"]')].map(x=>(x as HTMLElement).innerText.trim()))
console.log(opts)
const ev = p.getByText('Edit vocals', { exact: true }).first()
await ev.click()
await p.waitForTimeout(1500)
console.log('edit vocals btn', await p.locator('button:has-text("Edit vocals")').count(), 'cover btn', await p.locator('button:has-text("Cover")').count())
process.exit(0)
