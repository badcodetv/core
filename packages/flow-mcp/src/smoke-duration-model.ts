/**
 * Second half of the C4 probe: how do the duration tabs behave per VIDEO MODEL?
 *
 * platform-controls.md claims 10s is Gemini Omni Flash only and the Veo 3.1 tiers cap at 8s —
 * a transcription from Google's docs that we have never tested. If Flow disables or removes
 * the 10s tab on Veo, the guard is a readback; if it leaves it clickable and silently
 * delivers 8s, the guard has to be a hard-coded model rule. This tells us which.
 *
 * Spends no credits — it only opens menus.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-duration-model.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-duration-model.ts <projectId>')

const MODELS = ['Veo 3.1 - Fast', 'Veo 3.1 - Quality', 'Omni Flash']

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
  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  await inner.tabClick(videoTab)
  await page.waitForTimeout(500)

  const durations = async () => {
    const out: string[] = []
    for (const d of ['4s', '6s', '8s', '10s']) {
      const t = page.locator('button[role="tab"]').filter({ hasText: new RegExp(`^${d}$`) }).first()
      if (!(await t.count())) {
        out.push(`${d}:ABSENT`)
        continue
      }
      out.push(
        `${d}:${(await t.getAttribute('aria-selected')) === 'true' ? 'SEL' : 'sel-'}` +
          `${(await t.isDisabled()) ? '/DISABLED' : ''}` +
          `${t ? '' : ''}`,
      )
    }
    return out.join('  ')
  }

  for (const model of MODELS) {
    const modelBtn = page
      .locator('button')
      .filter({ hasText: /(Omni Flash|Veo).*arrow_drop_down/i })
      .first()
    const option = page.getByText(model, { exact: true }).locator('xpath=ancestor::button[1]').first()
    if (!(await option.isVisible().catch(() => false))) {
      await inner.pointerClick(modelBtn)
      await option.waitFor({ state: 'visible', timeout: 15_000 }).catch(() => {})
    }
    if (!(await option.count())) {
      console.log(`\n### ${model}: option not found`)
      continue
    }
    await inner.forceClick(option)
    await page.waitForTimeout(900)
    console.log(`\n### ${model}`)
    console.log('  trigger  :', ((await crop.textContent()) ?? '').trim())
    console.log('  model row:', ((await modelBtn.textContent()) ?? '').trim())
    console.log('  durations:', await durations())

    // If 10s is present and enabled on a Veo tier, try clicking it and see what sticks.
    const ten = page.locator('button[role="tab"]').filter({ hasText: /^10s$/ }).first()
    if ((await ten.count()) && !(await ten.isDisabled())) {
      await inner.tabClick(ten)
      await page.waitForTimeout(500)
      console.log('  after clicking 10s → trigger:', ((await crop.textContent()) ?? '').trim())
      const back = page.locator('button[role="tab"]').filter({ hasText: /^8s$/ }).first()
      if (await back.count()) await inner.tabClick(back)
      await page.waitForTimeout(300)
    }
  }

  await page.keyboard.press('Escape')
  console.log('\nfinal trigger:', ((await crop.textContent()) ?? '').trim())
} finally {
  await client.close()
}
