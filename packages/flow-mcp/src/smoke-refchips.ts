/**
 * Manual probe — what reference chips are attached right now, and to what media? NOT part of CI.
 * Usage: npx tsx packages/flow-mcp/src/smoke-refchips.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: import('playwright-core').Page }).page
  const chips = await page.evaluate(`(() => {
    const out = []
    for (const im of document.querySelectorAll('img[alt]')) {
      const alt = im.getAttribute('alt') || ''
      if (!/^Reference media/.test(alt)) continue
      const s = im.currentSrc || im.src || im.getAttribute('src') || ''
      let name = null
      try { name = new URL(s, location.href).searchParams.get('name') } catch (e) {}
      const r = im.getBoundingClientRect()
      out.push({ alt, name, visible: !!(r.width && r.height), x: Math.round(r.left), y: Math.round(r.top) })
    }
    return out
  })()`)
  console.log('reference chips:', JSON.stringify(chips, null, 2))

  const uploads = await page.evaluate(`(() => {
    const out = []
    for (const im of document.querySelectorAll('img[alt="Generated image"]')) {
      const s = im.currentSrc || im.src || im.getAttribute('src') || ''
      let name = null
      try { name = new URL(s, location.href).searchParams.get('name') } catch (e) {}
      const r = im.getBoundingClientRect()
      out.push({ name, y: Math.round(r.top) })
    }
    return out
  })()`)
  console.log('generated-image tiles:', JSON.stringify(uploads, null, 2))
} finally {
  await client.close()
}
