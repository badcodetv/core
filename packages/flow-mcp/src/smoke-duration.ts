/**
 * Manual DOM-mapping probe for the compose popover's VIDEO-mode duration tabs — NOT part of
 * CI, spends no credits.
 *
 * smoke-compose-popover.ts dumped these tabs read-only (4s / 6s / 8s / 10s) and nothing has
 * ever CLICKED one. This probe answers the three questions C4 depends on:
 *   1. does a duration tab click stick (aria-selected flips)?
 *   2. does the collapsed trigger label carry the duration, so a readback guard can work?
 *   3. is the 10s tab present-and-disabled, or absent, on a Veo tier vs Omni Flash?
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-duration.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-duration.ts <projectId>')

/** Dump every tab in the open popover, with the state attributes a guard would read. */
const DUMP = `() => {
  const roots = [...document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [data-state="open"][role="menu"]')]
  const root = roots.length ? roots[roots.length - 1] : document.body
  return [...root.querySelectorAll('button, [role="tab"], [role="menuitem"]')].map(el => ({
    tag: el.tagName,
    role: el.getAttribute('role') || undefined,
    text: (el.textContent || '').trim().slice(0, 60),
    state: el.getAttribute('data-state') || undefined,
    selected: el.getAttribute('aria-selected') || undefined,
    disabled: el.hasAttribute('disabled') || el.getAttribute('aria-disabled') === 'true' || undefined,
  }))
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    pointerClick(l: Locator): Promise<void>
    tabClick(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  const crop = page.getByRole('button', { name: /crop_/ }).first()
  const label = async () => ((await crop.textContent()) ?? '').trim()
  console.log('trigger label at start:', await label())

  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  // Every trigger TOGGLES — only click when the popover is not already showing.
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  await inner.tabClick(videoTab)
  await page.waitForTimeout(600)

  console.log('\n=== VIDEO MODE, as opened ===')
  console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))

  // --- Q1/Q2: click each duration in turn and read the trigger back -------------------
  for (const want of ['4s', '6s', '8s']) {
    const tab = page.locator('button[role="tab"]').filter({ hasText: new RegExp(`^${want}$`) }).first()
    if (!(await tab.count())) {
      console.log(`\n[${want}] NO TAB FOUND`)
      continue
    }
    await inner.tabClick(tab)
    await page.waitForTimeout(400)
    console.log(
      `\n[${want}] aria-selected=${await tab.getAttribute('aria-selected')}`,
      `data-state=${await tab.getAttribute('data-state')}`,
      `| trigger="${await label()}"`,
    )
  }

  // --- Q3: what happens to 10s across models -----------------------------------------
  const tenState = async () => {
    const t = page.locator('button[role="tab"]').filter({ hasText: /^10s$/ }).first()
    if (!(await t.count())) return 'ABSENT'
    return `present disabled=${await t.getAttribute('aria-disabled')}/${await t.isDisabled()} selected=${await t.getAttribute('aria-selected')}`
  }
  console.log('\n10s with current model:', await tenState())

  const modelBtn = page
    .locator('button')
    .filter({ hasText: /(Omni Flash|Veo).*arrow_drop_down/i })
    .first()
  if (await modelBtn.count()) {
    console.log('\nvideo model trigger:', ((await modelBtn.textContent()) ?? '').trim())
    await inner.pointerClick(modelBtn)
    await page.waitForTimeout(700)
    console.log('=== video model menu ===')
    console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))
    // Leave the menu open for the caller to read; Escape closes just the nested menu.
    await page.keyboard.press('Escape')
  } else {
    console.log('\nno video model trigger found in popover')
  }

  await page.keyboard.press('Escape')
  console.log('\ntrigger label at end:', await label())
} finally {
  await client.close()
}
