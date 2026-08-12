/**
 * Where does a VIDEO turn's output count actually live?
 *
 * A `count: 2` request came back with one clip and left the compose trigger reading `x1` — so
 * the Settings-panel count `ensureVideoSettings` asserts is not what governs the turn. Same
 * shape as the duration discovery: the compose-bar popover holds the per-turn controls, and the
 * Settings panel holds defaults that something else overrides.
 *
 * Credit-free: opens the popover in Video mode and dumps its tabs.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-count-popover.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-count-popover.ts <projectId>')

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    ensureComposeVisible(): Promise<void>
    pointerClick(l: Locator): Promise<void>
    tabClick(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(2500)
  await inner.ensureComposeVisible()

  const crop = page.getByRole('button', { name: /crop_/ }).first()
  if (!(await crop.count())) {
    const agent = page.getByRole('button', { name: 'Agent', exact: true })
    if (await agent.count()) await page.locator('button').filter({ hasText: /^Agent$/ }).first().click()
  }
  await crop.waitFor({ state: 'visible', timeout: 60_000 })
  console.log(`trigger before: ${JSON.stringify(await crop.textContent())}`)
  await inner.pointerClick(crop)
  await page.waitForTimeout(1200)

  const tabs = (await page.evaluate(`(() => [...document.querySelectorAll('button[role="tab"]')]
    .filter(t => t.getBoundingClientRect().width > 0)
    .map(t => ({ text: (t.textContent||'').trim(), selected: t.getAttribute('aria-selected') })))()`)) as {
    text: string
    selected: string | null
  }[]
  console.log('popover tabs:')
  for (const t of tabs) console.log(`   ${t.selected === 'true' ? '*' : ' '} ${JSON.stringify(t.text)}`)

  // Try selecting x2 and read the trigger back — the only proof that it is the governing control.
  const x2 = page.locator('button[role="tab"]').filter({ hasText: /^x2$/ }).first()
  if (await x2.count()) {
    await inner.tabClick(x2)
    await page.waitForTimeout(800)
    await page.keyboard.press('Escape')
    await page.waitForTimeout(500)
    console.log(`trigger after clicking x2: ${JSON.stringify(await crop.textContent())}`)
  } else {
    console.log('no x2 tab in this popover')
  }
} finally {
  await client.close()
}
