import { FlowClient } from '../../../packages/flow-mcp/src/flow-client'
const c: any = await FlowClient.connect(`http://localhost:9222`)
const page = c.page
await page.keyboard.press('Escape').catch(() => {})
await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
await page.waitForTimeout(4000)
if (await page.locator('flow-agent-panel').count()) {
  await page.evaluate(() => { const p = document.querySelector('flow-agent-panel'); const b = p && [...p.querySelectorAll('button')].find((b) => b.getAttribute('aria-label') === 'Close') as HTMLElement | undefined; b?.click() })
}
await c.ensureAgentOff?.()
await page.waitForTimeout(6000)
console.log('reloaded', page.url())
process.exit(0)
