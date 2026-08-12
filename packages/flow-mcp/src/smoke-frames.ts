/**
 * C1 spike: map the Frames source mode (first frame / last frame) in the compose popover.
 *
 * Credit-free — it opens tabs and dumps the DOM, it never submits. Answers:
 *   Q1: with a source chip attached by Animate, which source tab is active — Frames or
 *       Ingredients? That decides how much of the merged tool already exists.
 *   Q2: does the Frames tab offer a LAST-frame slot on this tier, or only a first frame?
 *   Q3: what are the slots' selectors, and how does a file reach them?
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frames.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-frames.ts <projectId>')

/** Everything clickable in the open popover, plus any file inputs anywhere on the page. */
const DUMP = `() => {
  const roots = [...document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [data-state="open"][role="menu"]')]
  const root = roots.length ? roots[roots.length - 1] : document.body
  return {
    root: root.tagName + '.' + String(root.className || '').slice(0, 40),
    rows: [...root.querySelectorAll('button, [role="tab"], [role="menuitem"], input')].map(el => ({
      tag: el.tagName,
      role: el.getAttribute('role') || undefined,
      type: el.getAttribute('type') || undefined,
      text: (el.textContent || '').trim().slice(0, 50),
      aria: el.getAttribute('aria-label') || undefined,
      selected: el.getAttribute('aria-selected') || undefined,
      state: el.getAttribute('data-state') || undefined,
    })),
    fileInputs: [...document.querySelectorAll('input[type=file]')].map(i => ({
      accept: i.getAttribute('accept') || undefined,
      multiple: i.hasAttribute('multiple'),
      id: i.id || undefined,
    })),
  }
}`

/** The compose bar itself, once the popover is closed — where the frame slots would live. */
const BAR = `() => {
  const box = document.querySelector('div[role="textbox"][contenteditable="true"]')
  const bar = box ? box.closest('form, div[class*="composer"], div[class*="Composer"]') || box.parentElement.parentElement.parentElement : null
  if (!bar) return { error: 'no compose bar found' }
  return {
    text: (bar.textContent || '').trim().slice(0, 200),
    buttons: [...bar.querySelectorAll('button')].map(b => ({
      text: (b.textContent || '').trim().slice(0, 40),
      aria: b.getAttribute('aria-label') || undefined,
    })),
    imgs: [...bar.querySelectorAll('img')].map(im => ({
      alt: (im.getAttribute('alt') || '').slice(0, 60),
      w: im.width,
    })),
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
  console.log('trigger:', ((await crop.textContent()) ?? '').trim())

  const videoTab = page.locator('button[role="tab"]').filter({ hasText: /videocam\s*Video/i }).first()
  if (!(await videoTab.isVisible().catch(() => false))) await inner.pointerClick(crop)
  await videoTab.waitFor({ state: 'visible', timeout: 30_000 })
  if ((await videoTab.getAttribute('aria-selected')) !== 'true') await inner.tabClick(videoTab)
  await page.waitForTimeout(600)

  // Q1: which source tab is active right now?
  for (const t of ['Frames', 'Ingredients']) {
    const tab = page.locator('button[role="tab"]').filter({ hasText: new RegExp(t) }).first()
    console.log(
      `source tab ${t}:`,
      (await tab.count()) ? `selected=${await tab.getAttribute('aria-selected')} text="${((await tab.textContent()) ?? '').trim()}"` : 'ABSENT',
    )
  }

  // Q2/Q3: switch to Frames and see what the popover AND the bar then offer.
  const frames = page.locator('button[role="tab"]').filter({ hasText: /Frames/ }).first()
  if (await frames.count()) {
    await inner.tabClick(frames)
    await page.waitForTimeout(900)
    console.log('\n=== popover, Frames selected ===')
    console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))
    await page.keyboard.press('Escape')
    await page.waitForTimeout(600)
    console.log('\n=== compose bar, Frames selected ===')
    console.log(JSON.stringify(await page.evaluate(`(${BAR})()`), null, 2))
    console.log('\ntrigger now:', ((await crop.textContent()) ?? '').trim())
  } else {
    console.log('no Frames tab')
  }
} finally {
  await client.close()
}
