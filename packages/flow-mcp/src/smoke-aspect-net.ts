/**
 * Manual probe — what does Flow actually SEND when we ask for an aspect ratio?
 *
 * The config trigger's label updates in ~80ms (smoke-aspect-race.ts), so the "poll the label
 * before submitting" theory is dead: the label is already right while the generation still
 * comes back at the PREVIOUS aspect. This watches the wire instead, to find where the aspect
 * really commits — a settings-persist request on tab click, or a field in the generate payload.
 *
 * Costs one image turn.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-aspect-net.ts <projectId> <aspect>
 */
import { mkdtemp } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'

const [, , projectId, aspect = '9:16'] = process.argv
if (!projectId) throw new Error('usage: smoke-aspect-net.ts <projectId> [aspect]')

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureImageMode(count?: number, model?: string, aspect?: string): Promise<void>
  }
  const page = inner.page

  const t0 = Date.now()
  const seen: string[] = []
  page.on('request', (req) => {
    const url = req.url()
    if (!/labs\.google|aisandbox|googleapis/.test(url)) return
    if (/\.(js|css|woff2?|png|jpg|svg|ico)(\?|$)/.test(url)) return
    const body = (req.postData() ?? '').slice(0, 1200)
    seen.push(`+${String(Date.now() - t0).padStart(6)}ms ${req.method()} ${url.slice(0, 130)}\n    ${body}`)
  })

  await client.openProject({ id: projectId })
  console.log('--- opened; clearing log ---')
  seen.length = 0

  const dir = await mkdtemp(join(tmpdir(), 'flow-aspnet-'))
  console.log(`--- generateImage({ aspect: ${aspect} }) — the real path ---`)
  void inner
  const res = await client.generateImage(
    'A single plain metal disc resting on a dark tabletop, one soft light.',
    join(dir, 'a.jpg'),
    { aspect },
  )
  console.log(seen.join('\n') || '  (no requests)')
  console.log('result:', res, 'ratio:', (res.width / res.height).toFixed(2))
} finally {
  await client.close()
}
