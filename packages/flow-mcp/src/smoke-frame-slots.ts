/**
 * C1 spike, part 2: how do you FILL the Start and End frame slots?
 *
 * The compose bar in Frames mode reads "Start | swap_horiz Swap first and last frames | End".
 * This dumps the two slots' actual DOM (they carry no text of their own beyond the label) and
 * clicks Start to see what opens — a file chooser, a project-media picker, or a menu.
 *
 * Credit-free: nothing is submitted.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frame-slots.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-frame-slots.ts <projectId>')

/** The slot elements themselves: every element whose own text is exactly Start or End. */
const SLOTS = `() => {
  const hits = [...document.querySelectorAll('button, div, span, label')].filter(el => {
    const t = (el.textContent || '').trim()
    return (t === 'Start' || t === 'End') && el.children.length <= 3
  })
  return hits.map(el => {
    const clickable = el.closest('button') || el
    return {
      text: (el.textContent || '').trim(),
      tag: el.tagName,
      cls: String(el.className || '').slice(0, 50),
      clickableTag: clickable.tagName,
      clickableRole: clickable.getAttribute('role') || undefined,
      clickableAria: clickable.getAttribute('aria-label') || undefined,
      // Walk up for the drop target: Flow renders these as click-or-drop tiles.
      parentCls: String(el.parentElement?.className || '').slice(0, 50),
      parentTag: el.parentElement?.tagName,
      hasImg: !!el.parentElement?.querySelector('img'),
    }
  })
}`

const MENU = `() => {
  const roots = [...document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [role="menu"][data-state="open"]')]
  const root = roots.length ? roots[roots.length - 1] : null
  if (!root) return { open: false, fileInputs: document.querySelectorAll('input[type=file]').length }
  return {
    open: true,
    root: root.tagName + '.' + String(root.className || '').slice(0, 40),
    rows: [...root.querySelectorAll('button, [role="menuitem"], [role="option"]')].map(el => ({
      tag: el.tagName,
      role: el.getAttribute('role') || undefined,
      text: (el.textContent || '').trim().slice(0, 50),
    })),
    fileInputs: document.querySelectorAll('input[type=file]').length,
  }
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    pointerClick(l: Locator): Promise<void>
    tabClick(l: Locator): Promise<void>
    forceClick(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  const crop = page.getByRole('button', { name: /crop_/ }).first()
  if (!(await crop.count())) {
    const agent = page.getByRole('button', { name: 'Agent', exact: true })
    if (await agent.count()) await inner.forceClick(agent)
  }
  await crop.waitFor({ state: 'visible', timeout: 30_000 })

  // Make sure we are in Video + Frames.
  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  if ((await videoTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(videoTab)
  const framesTab = page.locator('button[role="tab"]').filter({ hasText: /Frames/ }).first()
  if ((await framesTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(framesTab)
  await page.keyboard.press('Escape')
  await page.waitForTimeout(700)

  console.log('=== slots ===')
  console.log(JSON.stringify(await page.evaluate(`(${SLOTS})()`), null, 2))
  console.log('\nfile inputs before:', await page.locator('input[type=file]').count())

  console.log('\n=== clicking Start ===')
  const start = page.getByText('Start', { exact: true }).first()
  if (await start.count()) {
    await inner.forceClick(start)
    await page.waitForTimeout(1200)
    console.log(JSON.stringify(await page.evaluate(`(${MENU})()`), null, 2))
    await page.keyboard.press('Escape')
  } else {
    console.log('no Start element found')
  }
} finally {
  await client.close()
}
