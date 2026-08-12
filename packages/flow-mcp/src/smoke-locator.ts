/**
 * Manual probe — narrow down which link in a locator chain breaks. NOT part of CI.
 * Usage: npx tsx packages/flow-mcp/src/smoke-locator.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page

  const heading = page.getByText('Video generation default', { exact: true })
  console.log('heading count:', await heading.count())

  const section = heading.locator('xpath=..')
  console.log('section count:', await section.count())
  console.log('section text:', (await section.first().textContent())?.slice(0, 120))

  console.log('buttons in section:', await section.getByRole('button').count())
  const names = await section.getByRole('button').evaluateAll(els =>
    els.map(e => ({ text: (e.textContent || '').trim().slice(0, 40), aria: e.getAttribute('aria-label') })),
  )
  console.log(JSON.stringify(names, null, 2))

  console.log(
    'byRole(name=/arrow_drop_down/):',
    await section.getByRole('button', { name: /arrow_drop_down/i }).count(),
  )
  console.log(
    'byRole(name=/Omni Flash|Veo/):',
    await section.getByRole('button', { name: /Omni Flash|Veo/i }).count(),
  )
  console.log('tabs in section (getByRole):', await section.getByRole('tab').count())
  console.log('tabs in section (CSS):', await section.locator('button[role="tab"]').count())
  console.log('buttons in section (CSS):', await section.locator('button').count())
  console.log('page-wide getByRole(tab):', await page.getByRole('tab').count())
  console.log('page-wide CSS button[role=tab]:', await page.locator('button[role="tab"]').count())

  // What ARE these elements? Dump every descendant that carries text, with its tag/role.
  const shapes = await section.first().evaluate(el => {
    const out: unknown[] = []
    for (const d of el.querySelectorAll('*')) {
      const t = (d.textContent || '').trim()
      if (!t || t.length > 40) continue
      out.push({
        tag: d.tagName,
        role: d.getAttribute('role'),
        cls: (d.getAttribute('class') || '').slice(0, 40),
        aria: d.getAttribute('aria-label'),
        sel: d.getAttribute('aria-selected') ?? d.getAttribute('data-state'),
        text: t,
      })
    }
    return out
  })
  console.log(JSON.stringify(shapes, null, 2))
} finally {
  await client.close()
}
