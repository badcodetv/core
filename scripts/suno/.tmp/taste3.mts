import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.getByRole('button', { name: 'More', exact: true }).first().click()
await p.waitForTimeout(800)
const c = await p.evaluate(`[...document.querySelectorAll('[role=menu] *, [role=dialog] a, [role=dialog] button,[data-radix-popper-content-wrapper] *')].filter(e=>e.children.length==0&&e.innerText&&e.innerText.trim()).map(e=>e.innerText.trim()).slice(0,40)`)
console.log(c.join(' | '))
await p.keyboard.press('Escape')
await b.close()
