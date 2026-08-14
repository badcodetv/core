/**
 * C1, last piece: the DOM of a FILLED frame slot — its remove control and its error badge.
 *
 * Needed for two guards in C2: clearing stale frames before a new call (they persist on the
 * bar), and refusing to submit when Flow has flagged a frame as invalid (an End frame on Omni
 * Flash renders an "error" badge and would otherwise be submitted and billed).
 *
 * Credit-free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-slot-dom.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-slot-dom.ts <projectId>')

const DOM = `() => {
  const swap = [...document.querySelectorAll('button')].find(b => /Swap first and last frames/.test(b.textContent || ''))
  if (!swap || !swap.parentElement) return { error: 'swap button not found' }
  const walk = (el, depth) => ({
    tag: el.tagName,
    role: el.getAttribute('role') || undefined,
    aria: el.getAttribute('aria-label') || undefined,
    title: el.getAttribute('title') || undefined,
    text: (el.textContent || '').trim().slice(0, 24),
    cls: String(el.className || '').slice(0, 30),
    kids: depth > 0 ? [...el.children].map(c => walk(c, depth - 1)) : undefined,
  })
  return [...swap.parentElement.children].map(c => walk(c, 3))
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

  // ⚠️ Frame slots do NOT survive navigation — openProject resets them to empty. So fill one
  // in this same session before dumping, or you photograph an empty bar.
  const crop = page.getByRole('button', { name: /crop_/ }).first()
  if (!(await crop.count())) {
    const agent = page.getByRole('button', { name: 'Agent', exact: true })
    if (await agent.count()) await inner.forceClick(agent)
  }
  await crop.waitFor({ state: 'visible', timeout: 30_000 })
  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  if ((await videoTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(videoTab)
  const framesTab = page.locator('button[role="tab"]').filter({ hasText: /Frames/ }).first()
  if ((await framesTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(framesTab)
  await page.keyboard.press('Escape')
  await page.waitForTimeout(600)

  await inner.forceClick(page.getByText('Start', { exact: true }).first())
  await page.waitForTimeout(1200)
  const row = page.locator('[role="option"]').first()
  await inner.pointerClick(row)
  await page.waitForTimeout(1000)
  const add = page.locator('button').filter({ hasText: /^Add to Prompt$/ }).first()
  if (await add.isVisible().catch(() => false)) await inner.pointerClick(add)
  await page.waitForTimeout(2000)

  console.log(JSON.stringify(await page.evaluate(`(${DOM})()`), null, 1))
} finally {
  await client.close()
}
