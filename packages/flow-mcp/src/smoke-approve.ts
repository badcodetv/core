/**
 * Manual probe — can we see and click the credit-approval gate? NOT part of CI.
 * Run while a gate is on screen. Pass `click` as argv[2] to actually approve.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-approve.ts [click]
 */
import { FlowClient } from './flow-client'

const doClick = process.argv[2] === 'click'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    forceClick(l: unknown): Promise<void>
  }
  const page = inner.page

  console.log('getByRole(button, /^Approve$/):', await page.getByRole('button', { name: /^Approve$/ }).count())
  console.log('CSS button hasText /^Approve$/:', await page.locator('button').filter({ hasText: /^Approve$/ }).count())
  console.log('getByText Approve exact:', await page.getByText('Approve', { exact: true }).count())

  const shapes = await page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('*')) {
      if (el.children.length) continue
      if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) continue
      const t = (el.textContent || '').trim()
      if (!/^(Approve|Approve, do not ask again|Reject)$/.test(t)) continue
      const r = el.getBoundingClientRect()
      const chain = []
      let p = el
      for (let i = 0; i < 4 && p; i++) {
        chain.push(p.tagName + (p.getAttribute('role') ? '[role=' + p.getAttribute('role') + ']' : ''))
        p = p.parentElement
      }
      out.push({ text: t, visible: !!(r.width && r.height), chain: chain.join(' < ') })
    }
    return out
  })()`)
  console.log(JSON.stringify(shapes, null, 2))

  if (doClick) {
    const label = page.getByText('Approve', { exact: true }).first()
    const clickable = label.locator('xpath=ancestor-or-self::*[self::button or @role="button"][1]')
    const n = await clickable.count()
    console.log('clickable ancestor count:', n)
    await inner.forceClick(n ? clickable.first() : label)
    console.log('clicked Approve')
  }
} finally {
  await client.close()
}
