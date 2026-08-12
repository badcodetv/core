/**
 * Manual DOM-mapping probe for the "create a Character from existing project media" path —
 * NOT part of CI, costs nothing.
 *
 * createCharacterFromMedia was written blind against a guessed sequence (sidebar Characters ->
 * a URL change to /characters -> an "Add from Project" button -> an "Add to Character" confirm).
 * This walks it one control at a time, SCREENSHOTTING each step as well as dumping buttons —
 * a dump alone was ambiguous (tile captions render outside the button they label).
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-charadd.ts <projectId> <shotDir>
 */
import { FlowClient } from './flow-client'

const [, , projectId, shotDir = '/tmp'] = process.argv
if (!projectId) throw new Error('usage: smoke-charadd.ts <projectId> <shotDir>')

const DUMP = `() => {
  const dialogs = [...document.querySelectorAll('[role="dialog"]')]
  const root = dialogs.length ? dialogs[dialogs.length - 1] : document.body
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 }
  return {
    inDialog: dialogs.length > 0,
    buttons: [...root.querySelectorAll('button, [role="button"]')].filter(vis)
      .map(el => (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0, 50)),
    optionCount: root.querySelectorAll('[role="option"]').length,
    options: [...root.querySelectorAll('[role="option"]')].slice(0, 3)
      .map(el => (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0, 70)),
  }
}`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    forceClick(l: import('playwright-core').Locator): Promise<void>
  }
  const page = inner.page
  let step = 0
  const dump = async (label: string) => {
    await page.waitForTimeout(1_500)
    const shot = `${shotDir}/char-${String(++step).padStart(2, '0')}.png`
    await page.screenshot({ path: shot })
    console.log(`\n=== ${label} -> ${shot} ===`)
    console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`)))
  }

  // Hard reload so no leftover view state from an earlier failed run is in play.
  await client.openProject({ id: projectId })
  await dump('project root')

  await inner.forceClick(page.getByRole('button', { name: /accessibility_new\s*Characters/i }).first())
  await dump('after sidebar Characters')

  // The "+ New Character" tile: try the caption text, which is what the UI shows.
  const tile = page.getByText('New Character', { exact: true }).first()
  if (await tile.count()) {
    await inner.forceClick(tile)
    await dump('after New Character tile')
  } else {
    console.log('\n(no "New Character" text found)')
  }

  const addFromProject = page.getByRole('button', { name: /add\s*Add from Project/i }).first()
  if (!(await addFromProject.count())) throw new Error('no Add from Project button')
  await inner.forceClick(addFromProject)
  await dump('after Add from Project')

  const option = page.getByRole('option').first()
  if (!(await option.count())) throw new Error('no [role=option] rows in the picker')
  await inner.forceClick(option)
  // Watch what the click actually did: does the dialog stay open with the option selected
  // (so "Add to Character" is the confirm), or does it close on select?
  for (const ms of [300, 1_500, 6_000]) {
    await page.waitForTimeout(ms)
    console.log(`  +${ms}: ${JSON.stringify(await page.evaluate(`(${DUMP})()`))}`.slice(0, 400))
  }
  await dump('settled after selecting the first media option')
} finally {
  await client.close()
}
