/**
 * The asset picker is unreachable after any video call.
 *
 * Found 2026-08-12 by adversarial review: `openAssetPicker` waits for the `add_2 Create`
 * trigger, and that button DOES NOT EXIST while the compose bar is in Video mode — where every
 * video call leaves it, persistently, surviving navigation. So `flow_list_media`,
 * `flow_create_character_from_media` and every character/reference attach hang for 90s and then
 * time out. The image tools escape it only because `ensureImageMode` runs first and flips the
 * bar back.
 *
 * That is precisely the "iterate on images and videos together" workflow — and the tool you need
 * to recover a clip's mediaId for `flow_refine_video` is one of the broken ones.
 *
 * This probe checks the fix candidate: `openAssetPicker`'s own docstring says typing `@` in the
 * prompt box opens the same dialog, and the prompt box exists in EVERY mode. Credit-free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-picker-in-video-mode.ts <projectId>
 */
import type { Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-picker-in-video-mode.ts <projectId>')

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; promptBox(): { focus(): Promise<void> } }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(2500)

  const trigger = page.getByRole('button', { name: /add_2\s*Create/i }).first()
  console.log(`compose bar mode markers: ${JSON.stringify(
    (await page.evaluate(`(() => [...document.querySelectorAll('button')].map(b => (b.textContent||'').trim()).filter(t => /Swap first and last|Video\\s*·|crop_/.test(t)))()`)) as string[],
  )}`)
  console.log(`add_2 Create trigger present: ${(await trigger.count()) ? 'YES' : 'NO — the picker is unreachable this way'}`)

  // The fix candidate: focus the prompt box and type '@'.
  const box = page.locator('div[role="textbox"][contenteditable="true"]').first()
  await box.waitFor({ state: 'visible', timeout: 30_000 })
  await box.evaluate((el) => (el as HTMLElement).focus())
  await page.keyboard.type('@')
  await page.waitForTimeout(2000)

  const dialog = page.getByRole('dialog').last()
  const upload = dialog.getByRole('button', { name: /upload\s*Upload media/i })
  const opened = await upload.isVisible().catch(() => false)
  console.log(`'@' opened the picker: ${opened ? 'YES' : 'no'}`)
  if (opened) {
    const tabs = (await page.evaluate(`(() => [...document.querySelectorAll('[role="tab"]')].map(t => (t.textContent||'').trim()))()`)) as string[]
    console.log(`picker tabs: ${JSON.stringify(tabs)}`)
  }
  await page.keyboard.press('Escape')
} finally {
  await client.close()
}
