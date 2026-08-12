/**
 * Does the Animate source chip survive leaving Agent mode?
 *
 * The Animate menuitem leaves the compose bar in AGENT mode with the still attached as a chip
 * (screenshotted 2026-08-12) — and Agent mode has no config popover at all, so the duration
 * tabs are unreachable from there. The cheap fix is to toggle into direct-generation mode
 * before submitting, but only if the attached source survives the toggle: if it does not, the
 * turn would generate text-to-video from nothing and still bill for it.
 *
 * Read-write but credit-free: it clicks the Agent toggle and reports, it never submits.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-agent-toggle.ts [projectId]
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]

const STATE = `() => ({
  crop: [...document.querySelectorAll('button')].map(b => (b.textContent || '').trim()).find(t => /crop_/.test(t)) || null,
  agentPill: [...document.querySelectorAll('button')].map(b => (b.textContent || '').trim()).filter(t => /^Agent$/i.test(t)).length,
  // Reference chips: the small thumbnails Flow renders INSIDE the compose bar.
  chips: [...document.querySelectorAll('img')]
    .filter(im => im.width > 10 && im.width < 120)
    .map(im => (im.getAttribute('alt') || '') + '|' + (im.currentSrc || im.src || '').slice(-24)),
})`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; forceClick(l: Locator): Promise<void> }
  const page = inner.page
  if (projectId) await client.openProject({ id: projectId })

  console.log('BEFORE:', JSON.stringify(await page.evaluate(`(${STATE})()`), null, 2))

  const agent = page.getByRole('button', { name: 'Agent', exact: true })
  if (!(await agent.count())) {
    console.log('no Agent pill on the bar — already in direct mode?')
  } else {
    await inner.forceClick(agent)
    await page.waitForTimeout(1200)
    console.log('AFTER toggle:', JSON.stringify(await page.evaluate(`(${STATE})()`), null, 2))
  }
} finally {
  await client.close()
}
