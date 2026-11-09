import { chromium } from 'playwright'
const secs = Number(process.argv[2])
const b = await chromium.connectOverCDP('http://127.0.0.1:9223')
const p = b.contexts()[0].pages().find(p => p.url().includes('flow.google.com/project'))
const s = p.locator('.cdk-overlay-container input[type=range][aria-label=Length]')
if (!(await s.count())) { console.log('popover closed'); process.exit(0) }
await s.focus()
await p.keyboard.press('Home')
for (let k = 0; k < secs - 3; k++) await p.keyboard.press('ArrowRight')
await p.waitForTimeout(300)
console.log(await s.inputValue(), await p.locator('.cdk-overlay-container mat-slider').evaluate(e => e.parentElement.textContent.trim()))
console.log(await p.evaluate(() => [...document.querySelectorAll('button')].map(b=>b.textContent.trim()).filter(t=>/Video ·/.test(t))[0]))
await b.close().catch(()=>{})
