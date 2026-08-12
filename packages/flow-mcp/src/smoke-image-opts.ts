/**
 * Manual check — are `model` and `aspect` actually honoured per image call, and does the
 * no-arguments path still behave as before? NOT part of CI. Costs a few image generations.
 *
 * The regression this watches for: refine()/generateImage() previously asserted NO project or
 * image mode, deliberately trusting session state, so an edit loop mid-session must not be
 * disturbed by the new options plumbing.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-image-opts.ts
 */
import { mkdtemp } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const dir = await mkdtemp(join(tmpdir(), 'flow-imgopts-'))
  const PROMPT = 'A single plain metal disc resting on a dark tabletop, one soft light.'

  console.log('--- 16:9 ---')
  const wide = await client.generateImage(PROMPT, join(dir, 'wide.jpg'), { aspect: '16:9' })
  console.log(wide, 'ratio:', (wide.width / wide.height).toFixed(2), '(expect ~1.78)')

  console.log('--- 9:16 ---')
  const tall = await client.generateImage(PROMPT, join(dir, 'tall.jpg'), { aspect: '9:16' })
  console.log(tall, 'ratio:', (tall.width / tall.height).toFixed(2), '(expect ~0.56)')

  console.log('--- no options (must not disturb session state) ---')
  const plain = await client.generateImage(PROMPT, join(dir, 'plain.jpg'))
  console.log(plain, 'ratio:', (plain.width / plain.height).toFixed(2))

  const ok = wide.width > wide.height && tall.height > tall.width
  console.log(ok ? 'ASPECT OK — orientation followed the request' : 'ASPECT FAIL')
} finally {
  await client.close()
}
