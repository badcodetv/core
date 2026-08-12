/**
 * Manual DOM-mapping probe for character cards on the project root — NOT part of CI.
 *
 * listCharacters() reported 1 character where the UI plainly shows 3, so the card selector
 * needs mapping against the real DOM rather than another inference.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-chars-raw.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
  }
  await inner.ensureProjectRoot()
  await inner.page.waitForTimeout(2000)

  const rows = await inner.page.evaluate(`(() => {
    const seen = []
    for (const a of document.querySelectorAll('a[href*="/character/"]')) {
      const img = a.querySelector('img')
      seen.push({
        via: 'anchor',
        href: a.getAttribute('href'),
        imgAlt: img ? img.getAttribute('alt') : null,
        text: (a.textContent || '').trim().slice(0, 80),
        ariaLabel: a.getAttribute('aria-label'),
      })
    }
    return seen
  })()`)
  console.log('=== a[href*="/character/"] ===')
  console.log(JSON.stringify(rows, null, 2))

  // How does the UI render the two portrait-less cards? Find every node whose own text is
  // exactly the visible label, and describe its nearest enclosing link/card.
  const labelled = await inner.page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('*')) {
      if (el.children.length) continue
      const t = (el.textContent || '').trim()
      if (t !== 'Untitled Character') continue
      const link = el.closest('a')
      const card = el.closest('[data-media-id], [role="listitem"], li, article')
      out.push({
        tag: el.tagName,
        linkHref: link ? link.getAttribute('href') : null,
        cardTag: card ? card.tagName : null,
        cardAttrs: card ? [...card.attributes].map(a => a.name + '=' + a.value).join(' ').slice(0, 200) : null,
      })
    }
    return out
  })()`)
  console.log('\n=== nodes labelled "Untitled Character" ===')
  console.log(JSON.stringify(labelled, null, 2))
} finally {
  await client.close()
}
