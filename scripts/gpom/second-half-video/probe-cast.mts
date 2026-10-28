/**
 * Probe, no credits: can a Character be cast into a FRAMES-mode video (start image locked)?
 * Fills the Start slot, then tries the "@" route (rebuild doc items 30-33) and reports what the
 * prompt bar holds. Never clicks Create; clears the bar with a reload at the end.
 *
 *   npx tsx scripts/gpom/second-half-video/probe-cast.mts <staged-plate-basename>
 */
import { FlowClient } from '../../../packages/flow-mcp/src/flow-client'

const PROJECT = 'be451638-f0ac-4f7e-8185-7b89f3c74f5c'
const plate = process.argv[2]!
const c: any = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
const page = c.page
const report: Record<string, unknown> = {}
try {
  await page.goto(`https://flow.google.com/project/${PROJECT}`, { waitUntil: 'domcontentloaded' })
  await page.waitForTimeout(5000)
  await c.ensureAgentOff()
  await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: 8, count: 1, frames: true }).catch(async () => {
    await page.waitForTimeout(1500)
    await c.ensureVideoConfigRebuilt({ model: 'Omni 1.1 Flash', aspect: '16:9', duration: 8, count: 1, frames: true })
  })
  await c.fillFrameSlotRebuilt('Start', plate)
  report.ingredientsButton = await page.getByRole('button', { name: 'Add ingredients to the prompt box' }).count()
  report.buttons = await page.evaluate(() => [...document.querySelectorAll('flow-prompt-box button')].map((b) => (b.getAttribute('aria-label') || b.textContent || '').trim()).filter(Boolean))
  const box = c.promptBox()
  await box.click()
  await page.keyboard.type('@')
  await page.waitForTimeout(2500)
  report.options = await page.evaluate(() => [...document.querySelectorAll('.cdk-overlay-container [role=option]')].map((r) => (r as HTMLElement).innerText.trim().replace(/\s+/g, ' ')).slice(0, 12))
  const clicked = await page.evaluate(() => {
    const el = [...document.querySelectorAll('.cdk-overlay-container [role=option]')].find((r) => /West Country Bot\s*Character/.test((r as HTMLElement).innerText))
    if (!el) return false
    for (const type of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
      el.dispatchEvent(new (type.startsWith('pointer') ? PointerEvent : MouseEvent)(type, { bubbles: true, cancelable: true, view: window }))
    return true
  })
  report.rowClicked = clicked
  await page.waitForTimeout(1500)
  if (await page.locator('.cdk-overlay-container [role=option]').count()) {
    report.addToPrompt = await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Add to prompt') as HTMLElement | undefined; b?.click(); return !!b })
    await page.waitForTimeout(1500)
  }
  report.chips = await page.locator('flow-prompt-box flow-ingredient-chip').count()
  report.boxText = (await box.innerText().catch(() => '')).slice(0, 120)
  report.startSlot = await page.evaluate(() => (document.querySelector('flow-prompt-box')?.textContent || '').replace(/\s+/g, ' ').slice(0, 200))
  report.trigger = ((await c.settingsTrigger().textContent()) ?? '').replace(/\s+/g, ' ').trim()
  await page.screenshot({ path: `${process.env.HOME}/.cache/badcode-gpom-second-half/probe-cast.png` })
} catch (err) {
  report.error = (err as Error).message.split('\n')[0]
} finally {
  console.log(JSON.stringify(report, null, 1))
  await page.keyboard.press('Escape').catch(() => {})
  await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
  await c.close?.().catch(() => {})
}
