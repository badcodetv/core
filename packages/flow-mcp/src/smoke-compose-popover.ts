/**
 * Manual DOM-mapping probe for the compose-bar config popover — NOT part of CI, costs nothing.
 *
 * The popover carries a PER-TURN config (Image/Video mode, model, aspect, duration, count) and
 * has never been mapped: docs/flow/automation-video.md still claims aspect is only settable in
 * the Settings panel and does not mention duration at all. It is also where the `1x` count tab
 * lives, which is silently failing to land on Nano Banana Pro (label stays `x2`).
 *
 * Dumps every tab/button/radio inside the popover in BOTH modes, raw.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-compose-popover.ts <projectId>
 */
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-compose-popover.ts <projectId>')

const DUMP = `() => {
  // Radix popovers portal to the body; find the open one, else fall back to whole document.
  const roots = [...document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [data-state="open"][role="menu"]')]
  const root = roots.length ? roots[roots.length - 1] : document.body
  const rows = [...root.querySelectorAll('button, [role="tab"], [role="radio"], [role="menuitem"], [role="option"], input, select')]
  return {
    rootTag: root.tagName + (root.className ? '.' + String(root.className).slice(0, 60) : ''),
    rowCount: rows.length,
    rows: rows.map(el => ({
      tag: el.tagName,
      role: el.getAttribute('role') || undefined,
      text: (el.textContent || '').trim().slice(0, 60),
      ariaLabel: el.getAttribute('aria-label') || undefined,
      state: el.getAttribute('data-state') || undefined,
      selected: el.getAttribute('aria-selected') || el.getAttribute('aria-checked') || undefined,
      disabled: el.hasAttribute('disabled') || el.getAttribute('aria-disabled') === 'true' || undefined,
    })),
  }
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    pointerClick(l: import('playwright-core').Locator): Promise<void>
    tabClick(l: import('playwright-core').Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  const crop = page.getByRole('button', { name: /crop_/ }).first()
  console.log('trigger label:', ((await crop.textContent()) ?? '').trim())

  // The trigger TOGGLES — only click when the popover is not already showing.
  const imageTab = page.locator('button[role="tab"]').filter({ hasText: /^imageImage$/i }).first()
  if (!(await imageTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await imageTab.waitFor({ state: 'visible', timeout: 30_000 })

  console.log('\n=== POPOVER (as opened) ===')
  console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))

  console.log('\n=== after clicking the Video tab ===')
  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (await videoTab.count()) {
    await inner.tabClick(videoTab)
    await page.waitForTimeout(800)
    console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))
  } else {
    console.log('  no videocam Video tab found')
  }

  console.log('\n=== back to Image ===')
  await inner.tabClick(imageTab)
  await page.waitForTimeout(800)
  console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))
  await page.keyboard.press('Escape')
  console.log('\ntrigger label after:', ((await crop.textContent()) ?? '').trim())
} finally {
  await client.close()
}
