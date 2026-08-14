/**
 * Manual DOM-mapping probe for the aspect race — NOT part of CI.
 *
 * Question it answers: after ensureImageMode() clicks the aspect tab and returns, does the
 * config trigger's label ALREADY show the new aspect, or does it lag? If it lags, polling the
 * label before submitting is a real fix; if it updates instantly while the generation still
 * comes back at the old aspect, the commit is somewhere else and polling would be theatre.
 *
 * Spends no credits — it never submits a prompt.
 *
 * Pre-req: ./scripts/flow-chrome.sh, logged in.
 * Usage: npx tsx packages/flow-mcp/src/smoke-aspect-race.ts [projectId]
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureImageMode(count?: number, model?: string, aspect?: string): Promise<void>
  }
  const page = inner.page

  const id = process.argv[2]
  if (id) await client.openProject({ id })
  else console.log('project:', await client.createProject())
  console.log('url:', page.url())

  const crop = () => page.getByRole('button', { name: /crop_/ }).first()
  const label = async () => ((await crop().textContent()) ?? '').trim()

  for (const aspect of ['9:16', '16:9', '9:16']) {
    console.log(`\n=== asking for ${aspect} ===`)
    console.log('  before:', await label())
    const t0 = Date.now()
    await inner.ensureImageMode(1, undefined, aspect)
    console.log(`  ensureImageMode returned after ${Date.now() - t0}ms`)
    // Watch the label for 6s, logging every change.
    let last = ''
    const deadline = Date.now() + 6_000
    while (Date.now() < deadline) {
      const now = await label()
      if (now !== last) {
        console.log(`  +${String(Date.now() - t0).padStart(5)}ms  ${now}`)
        last = now
      }
      await page.waitForTimeout(150)
    }
  }
} finally {
  await client.close()
}
