/**
 * C1 spike, part 4: step-by-step, screenshotted probe of the frame-slot picker.
 *
 * The batch attempt (smoke-frame-fill.ts) left both slots empty with "Add to Prompt" still
 * disabled, so this walks one slot one click at a time and photographs each state rather than
 * inferring it from attributes.
 *
 * Credit-free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frame-pick.ts <projectId> <shotDir>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, shotDir = '/tmp'] = process.argv.slice(2)
if (!projectId) throw new Error('usage: smoke-frame-pick.ts <projectId> <shotDir>')

const SLOTS = `() => {
  const swap = [...document.querySelectorAll('button')].find(b => /Swap first and last frames/.test(b.textContent || ''))
  if (!swap || !swap.parentElement) return { error: 'swap button not found' }
  return [...swap.parentElement.children].map(c => ({
    text: (c.textContent || '').trim().slice(0, 30),
    imgs: [...c.querySelectorAll('img')].length,
  }))
}`

/** The picker's own state: is it open, what is selected, is the confirm enabled? */
const PICKER = `() => {
  const opts = [...document.querySelectorAll('[role="option"]')]
  const add = [...document.querySelectorAll('button')].find(b => /^Add to Prompt$/.test((b.textContent || '').trim()))
  return {
    optionCount: opts.length,
    selectedOptions: opts.filter(o => o.getAttribute('aria-selected') === 'true' || o.getAttribute('data-state') === 'checked').length,
    firstThree: opts.slice(0, 3).map(o => ({
      text: (o.textContent || '').trim().slice(0, 30),
      selected: o.getAttribute('aria-selected') || undefined,
      state: o.getAttribute('data-state') || undefined,
      cls: String(o.className || '').slice(0, 40),
    })),
    addExists: !!add,
    addDisabled: add ? add.hasAttribute('disabled') || add.getAttribute('aria-disabled') === 'true' : null,
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

  const shot = async (n: string) => {
    await page.screenshot({ path: `${shotDir}/pick-${n}.png` })
    console.log(`  shot: ${shotDir}/pick-${n}.png`)
  }

  // Reach Video + Frames.
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
  console.log('slots:', JSON.stringify(await page.evaluate(`(${SLOTS})()`)))

  console.log('\n1) click Start')
  await inner.forceClick(page.getByText('Start', { exact: true }).first())
  await page.waitForTimeout(1500)
  console.log('  picker:', JSON.stringify(await page.evaluate(`(${PICKER})()`)))
  await shot('1-open')

  console.log('\n2) pointerClick the first option row')
  const row = page.locator('[role="option"]').first()
  await inner.pointerClick(row)
  await page.waitForTimeout(1500)
  console.log('  picker:', JSON.stringify(await page.evaluate(`(${PICKER})()`)))
  console.log('  slots :', JSON.stringify(await page.evaluate(`(${SLOTS})()`)))
  await shot('2-rowclick')

  console.log('\n3) click Add to Prompt if still there')
  const add = page.locator('button').filter({ hasText: /^Add to Prompt$/ }).first()
  if (await add.isVisible().catch(() => false)) {
    await inner.forceClick(add)
    await page.waitForTimeout(1800)
    console.log('  slots :', JSON.stringify(await page.evaluate(`(${SLOTS})()`)))
    await shot('3-added')
  } else {
    console.log('  Add to Prompt is gone — the row click was the confirm')
  }
} finally {
  await client.close()
}
