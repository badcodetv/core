/**
 * Manual end-to-end video check — NOT part of CI. SPENDS CREDITS.
 *
 * Veo 3.1 - Fast is 20 credits; Quality is 100. Pass the model as argv[2]; the default is
 * deliberately the cheap tier, because this is the one smoke script that costs real money
 * every time it runs.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-clip.ts <source.jpg> [model] [out.mp4]
 */
import { stat } from 'node:fs/promises'
import { FlowClient } from './flow-client'

const source = process.argv[2]
if (!source) throw new Error('usage: smoke-video-clip.ts <source.jpg> [model] [out.mp4]')
const model = process.argv[3] ?? 'Veo 3.1 - Fast'
const out = process.argv[4] ?? '/tmp/flow-clip.mp4'

const client = await FlowClient.connect()
try {
  const started = Date.now()
  const res = await client.generateVideo({
    startImage: source,
    // Motion only — the still already carries subject, scene and style (flow-prompt rule 2).
    motion: 'The camera pushes in slowly. Leaves stir in a light breeze. Nothing else moves.',
    outPath: out,
    model,
    aspect: '16:9',
    count: 1,
  })
  const { size } = await stat(res.path)
  console.log(`clip in ${((Date.now() - started) / 1000).toFixed(1)}s:`, res, 'bytes:', size)
  if (size < 10_000) throw new Error('file suspiciously small')
  console.log('VIDEO SMOKE OK')
} finally {
  await client.close()
}
