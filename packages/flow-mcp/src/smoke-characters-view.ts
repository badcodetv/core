/**
 * What is actually on screen after clicking the Characters sidebar button?
 *
 * `createCharacterFromMedia` handles BOTH known states (grid with a "New Character" tile, or an
 * empty project dropping straight into the editor with "Add from Project") and still timed out
 * on a project with zero characters — so there is a third state it does not know about.
 *
 * Credit-free. Usage: npx tsx packages/flow-mcp/src/smoke-characters-view.ts <projectId>
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-characters-view.ts <projectId>')

const VISIBLE = `(() => ({
  url: location.href,
  buttons: [...document.querySelectorAll('button, [role="tab"], [role="option"]')]
    .filter(el => el.getBoundingClientRect().width > 0)
    .map(el => (el.textContent || '').trim()).filter(t => t && t.length < 45),
  headings: [...document.querySelectorAll('h1,h2,h3,p,span,div')]
    .filter(el => el.children.length === 0 && el.getBoundingClientRect().width > 0)
    .map(el => (el.textContent || '').trim())
    .filter(t => t.length > 2 && t.length < 60).slice(0, 30),
}))()`

const client = await FlowClient.connect()
try {
  const inner = client as unknown as { page: Page; forceClick(l: Locator): Promise<void> }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(2500)
  await inner.forceClick(page.getByRole('button', { name: /accessibility_new\s*Characters/i }).first())
  await page.waitForTimeout(4000)
  const state = (await page.evaluate(VISIBLE)) as { url: string; buttons: string[]; headings: string[] }
  console.log(`url: ${state.url}`)
  console.log(`buttons:\n  ${state.buttons.join('\n  ')}`)
  console.log(`\ntext:\n  ${state.headings.join('\n  ')}`)
} finally {
  await client.close()
}
