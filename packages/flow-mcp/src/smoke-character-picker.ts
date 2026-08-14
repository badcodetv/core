/**
 * Does the asset picker let you ATTACH a character while the bar is in video mode?
 *
 * `addCharacterToPrompt` gets as far as the Characters tab and then waits out its timeout on
 * "Add to prompt". Two explanations, and they are very different answers to "can a character be
 * cast in a video?": either the tile click did not select, or Flow simply does not offer the
 * attach for a video turn. Dumps the picker in BOTH modes to tell them apart.
 *
 * Credit-free. Usage: npx tsx packages/flow-mcp/src/smoke-character-picker.ts <projectId> <characterName>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, characterName] = process.argv.slice(2)
if (!projectId || !characterName) throw new Error('usage: smoke-character-picker.ts <projectId> <characterName>')

const DUMP = `(() => {
  const dlg = [...document.querySelectorAll('[role="dialog"]')].pop()
  if (!dlg) return { dialog: false }
  return {
    dialog: true,
    tabs: [...dlg.querySelectorAll('[role="tab"]')].map(t => ({ t: (t.textContent||'').trim(), sel: t.getAttribute('aria-selected') })),
    buttons: [...dlg.querySelectorAll('button')].filter(b => b.getBoundingClientRect().width > 0).map(b => (b.textContent||'').trim()).filter(t => t && t.length < 40),
    options: [...dlg.querySelectorAll('[role="option"]')].map(o => (o.textContent||'').trim().slice(0, 30)),
  }
})()`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    ensureFramesMode(): Promise<void>
    reloadProject(): Promise<void>
    ensureImageMode(c?: number): Promise<void>
    openAssetPicker(): Promise<Locator>
    closeAssetPicker(): Promise<void>
    tabClick(l: Locator): Promise<void>
    forceClick(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  for (const mode of ['video', 'image'] as const) {
    // Reload between modes: a dialog left open by a previous attempt makes `dialog.last()` point
    // at a dead container, and the picker then never "opens" no matter how it is triggered.
    await inner.reloadProject()
    await page.waitForTimeout(1500)
    if (mode === 'video') await inner.ensureFramesMode()
    else await inner.ensureImageMode()
    const dialog = await inner.openAssetPicker()
    const charactersTab = dialog.getByRole('tab', { name: /Characters/i })
    const hasTab = await charactersTab.isVisible().catch(() => false)
    console.log(`\n[${mode}] Characters tab present: ${hasTab}`)
    if (hasTab) {
      await inner.tabClick(charactersTab)
      await page.waitForTimeout(1200)
      console.log(`[${mode}] after tab: ${JSON.stringify(await page.evaluate(DUMP))}`)
      const tile = dialog.getByText(characterName, { exact: true }).first()
      if (await tile.isVisible().catch(() => false)) {
        await inner.forceClick(tile)
        await page.waitForTimeout(1200)
        console.log(`[${mode}] after clicking the tile: ${JSON.stringify(await page.evaluate(DUMP))}`)
      } else {
        console.log(`[${mode}] no tile named ${characterName}`)
      }
    }
    await page.keyboard.press('Escape')
    await inner.closeAssetPicker()
    await page.waitForTimeout(500)
  }
} finally {
  await client.close()
}
