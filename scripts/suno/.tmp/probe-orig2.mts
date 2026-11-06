import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = await b.contexts()[0].newPage()
await p.goto('https://suno.com/song/03e29295-d33a-4db7-b566-64a58e83a196', { waitUntil: 'domcontentloaded' })
await p.waitForTimeout(6000)
const items = async () => p.evaluate(() => [...document.querySelectorAll('[role="menuitem"],[role="menu"] button,[data-radix-popper-content-wrapper] button,[data-radix-popper-content-wrapper] [role="menuitem"]')].map(x => (x as HTMLElement).innerText.trim()).filter(Boolean))
const more = p.locator('button[aria-label*="More"], button:has(svg)').filter({ hasText: '' })
// click the "..." next to share
const btns = p.locator('main button')
const n = await btns.count()
for (let i = 0; i < n; i++) { const a = await btns.nth(i).getAttribute('aria-label'); if (a && /more/i.test(a)) { await btns.nth(i).click(); break } }
await p.waitForTimeout(1500)
console.log('menu:', await items())
for (const sub of ['Remix/Edit', 'Edit', 'Remix', 'Create']) {
  const s = p.getByText(sub, { exact: true }).first()
  if (await s.count()) { await s.hover(); await p.waitForTimeout(1200); console.log(sub, '→', await items()) }
}
await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/orig-menu.png' })
await p.close(); process.exit(0)
