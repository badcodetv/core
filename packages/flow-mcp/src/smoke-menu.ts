/**
 * Manual probe — dump the shape of whatever menu is currently open. NOT part of CI.
 * Usage: npx tsx packages/flow-mcp/src/smoke-menu.ts <text-to-find>
 */
import { FlowClient } from './flow-client'

const needle = process.argv[2] ?? 'Veo'

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page
  const out = await page.evaluate(
    (n) => {
      const res: unknown[] = []
      for (const el of document.querySelectorAll('*')) {
        if (el.children.length) continue
        // Skip <script>/<style>: Flow embeds a large Next.js JSON payload that contains a
        // session access token, and dumping it would splatter a live credential into logs.
        if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) continue
        const t = (el.textContent || '').trim()
        if (t.length > 80 || !t.includes(n)) continue
        const rect = el.getBoundingClientRect()
        if (!rect.width || !rect.height) continue
        const chain: string[] = []
        let p: Element | null = el
        for (let i = 0; i < 4 && p; i++) {
          chain.push(`${p.tagName}${p.getAttribute('role') ? `[role=${p.getAttribute('role')}]` : ''}`)
          p = p.parentElement
        }
        const r = el.getBoundingClientRect()
        res.push({ text: t, visible: !!(r.width && r.height), chain: chain.join(' < ') })
      }
      return res
    },
    needle,
  )
  console.log(JSON.stringify(out, null, 2))
} finally {
  await client.close()
}
