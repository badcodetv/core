/**
 * C1 Q2, settled by clicking: is first+last frame available on our tier?
 *
 * Filling Start succeeded and End came back with an ERROR badge on the model the popover
 * happened to be on. platform-controls.md's matrix (transcribed from Google, never tested)
 * says first+last is ✅ on Veo 3.1 Lite, "coming soon" on Fast/Quality, and ✗ on Omni Flash —
 * which would explain it exactly. This walks every tier and reports what each does with a
 * second frame.
 *
 * Credit-free: it fills slots and reads them back, it never submits.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frame-tier.ts <projectId> <startName> <endName>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, startName = 'register-anchor.jpg', endName = 'server-hall-monolith.jpg'] = process.argv.slice(2)
if (!projectId) throw new Error('usage: smoke-frame-tier.ts <projectId> [startName] [endName]')

const MODELS = ['Omni Flash', 'Veo 3.1 - Fast', 'Veo 3.1 - Lite', 'Veo 3.1 - Quality']

/** Both slots: what they hold, and any error/title text Flow attaches. */
const SLOTS = `() => {
  const swap = [...document.querySelectorAll('button')].find(b => /Swap first and last frames/.test(b.textContent || ''))
  if (!swap || !swap.parentElement) return { error: 'swap button not found' }
  return [...swap.parentElement.children].map(c => ({
    text: (c.textContent || '').trim().slice(0, 40),
    imgs: [...c.querySelectorAll('img')].length,
    title: c.getAttribute('title') || [...c.querySelectorAll('[title]')].map(e => e.getAttribute('title'))[0] || undefined,
    aria: c.getAttribute('aria-label') || [...c.querySelectorAll('[aria-label]')].map(e => e.getAttribute('aria-label'))[0] || undefined,
  }))
}`

/** Any toast/card Flow posted (the error's explanation usually lands here, not on the slot). */
const CARDS = `() => [...document.querySelectorAll('div')]
  .map(d => (d.textContent || '').trim())
  .filter(t => t.length < 200 && /(not supported|unsupported|only|cannot|failed|error|unavailable)/i.test(t))
  .slice(0, 5)`

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
  const openPopover = async () => {
    if (!(await crop.count())) {
      const agent = page.getByRole('button', { name: 'Agent', exact: true })
      if (await agent.count()) await inner.forceClick(agent)
    }
    await crop.waitFor({ state: 'visible', timeout: 30_000 })
    const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
    if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
    await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
    if ((await videoTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(videoTab)
  }

  /** Pick an existing project asset into a slot. Assets are already uploaded, so no chooser. */
  const fill = async (label: 'Start' | 'End', name: string) => {
    const slot = page.getByText(label, { exact: true }).first()
    if (!(await slot.count())) {
      console.log(`    [${label}] no empty slot to click (already filled?)`)
      return
    }
    await inner.forceClick(slot)
    await page.waitForTimeout(1200)
    console.log(`    [${label}] picker options: ${await page.locator('[role="option"]').count()}`)
    const row = page.locator('[role="option"]').filter({ hasText: name }).first()
    await row.waitFor({ state: 'visible', timeout: 30_000 })
    await inner.pointerClick(row)
    await page.waitForTimeout(1000)
    console.log(`    [${label}] selected=${await row.getAttribute('aria-selected').catch(() => '?')}`)
    // Selecting is not confirming. The row click only confirms when the row was ALREADY the
    // highlighted one (which a freshly-uploaded asset always is, since it lands at the top of
    // the Recent sort — that is why the upload path appeared to work in one click). For any
    // other row, "Add to Prompt" is the confirm.
    const add = page.locator('button').filter({ hasText: /^Add to Prompt$/ }).first()
    if (await add.isVisible().catch(() => false)) {
      await inner.pointerClick(add)
      await page.waitForTimeout(2000)
    }
    console.log(`    [${label}] options after confirm: ${await page.locator('[role="option"]').count()}`)
  }

  /** Empty both slots by clicking their cancel badges, so each tier starts clean. */
  const clearSlots = async () => {
    for (let i = 0; i < 4; i++) {
      const cancel = page.locator('button').filter({ hasText: /^cancel$/ }).first()
      if (!(await cancel.isVisible().catch(() => false))) break
      await inner.forceClick(cancel)
      await page.waitForTimeout(600)
    }
  }

  for (const model of MODELS) {
    console.log(`\n### ${model}`)
    await openPopover()
    const framesTab = page.locator('button[role="tab"]').filter({ hasText: /Frames/ }).first()
    if ((await framesTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(framesTab)
    const modelBtn = page.locator('button').filter({ hasText: /(Omni Flash|Veo).*arrow_drop_down/i }).first()
    const option = page.getByText(model, { exact: true }).locator('xpath=ancestor::button[1]').first()
    if (!(await option.isVisible().catch(() => false))) {
      await inner.pointerClick(modelBtn)
      await option.waitFor({ state: 'visible', timeout: 15_000 }).catch(() => {})
    }
    if (await option.count()) await inner.forceClick(option)
    await page.waitForTimeout(800)
    await page.keyboard.press('Escape')
    await page.waitForTimeout(600)

    await clearSlots()
    await fill('Start', startName)
    await fill('End', endName)
    console.log('  slots:', JSON.stringify(await page.evaluate(`(${SLOTS})()`)))
    const cards = (await page.evaluate(`(${CARDS})()`)) as string[]
    if (cards.length) console.log('  cards:', JSON.stringify(cards.slice(0, 2)))
  }
} finally {
  await client.close()
}
