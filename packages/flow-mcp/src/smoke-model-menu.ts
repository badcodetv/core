/**
 * Manual probe — open the video model dropdown and dump its option rows. NOT part of CI.
 * The menu closes as soon as the session ends, so it must be opened and read in one run.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-model-menu.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    forceClick(l: unknown): Promise<void>
    pointerClick(l: unknown): Promise<void>
  }
  const page = inner.page
  await inner.ensureProjectRoot()

  const heading = page.getByText('Video generation default', { exact: true })
  const settingsBtn = page.locator('button').filter({ hasText: /^tune\s*Settings$/i }).first()
  const agentBtn = page.locator('button').filter({ hasText: /^Agent$/i }).first()
  if (!(await heading.count())) {
    if (!(await settingsBtn.count()) && (await agentBtn.count())) await inner.forceClick(agentBtn)
    await settingsBtn.waitFor({ state: 'visible', timeout: 60_000 })
    await inner.pointerClick(settingsBtn)
  }
  const section = heading.locator('xpath=..')
  await section.waitFor({ state: 'visible', timeout: 60_000 })

  const modelBtn = section.locator('button').filter({ hasText: /Omni Flash|Veo/i }).first()
  console.log('trigger text:', JSON.stringify(await modelBtn.textContent()))
  await inner.pointerClick(modelBtn)
  await page.waitForTimeout(1500)

  const rows = await page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('*')) {
      if (el.children.length) continue
      if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) continue
      const t = (el.textContent || '').trim()
      if (!t || t.length > 60 || !/Veo|Omni/.test(t)) continue
      const r = el.getBoundingClientRect()
      if (!r.width || !r.height) continue
      const chain = []
      let p = el
      for (let i = 0; i < 4 && p; i++) {
        chain.push(p.tagName + (p.getAttribute('role') ? '[role=' + p.getAttribute('role') + ']' : ''))
        p = p.parentElement
      }
      out.push({ text: t, chain: chain.join(' < ') })
    }
    return out
  })()`)
  console.log(JSON.stringify(rows, null, 2))

  // Can Playwright's own text engine see them, and can we reach the clickable ancestor?
  const label = page.getByText('Veo 3.1 - Fast', { exact: true })
  console.log('getByText exact count:', await label.count())
  const btn = label.locator('xpath=ancestor::button[1]')
  console.log('ancestor button count:', await btn.count())
  console.log('ancestor button visible:', await btn.first().isVisible().catch(e => `ERR ${e}`))
} finally {
  await client.close()
}
