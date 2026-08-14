/**
 * Live proof for C4: does `durationSeconds` actually change the clip Flow returns?
 *
 * ⚠️ SPENDS CREDITS (one clip, default tier Veo 3.1 - Fast = 20). The whole point is that a
 * duration request which is silently ignored produces a perfectly valid 8s file, so the only
 * evidence that counts is ffprobe on the harvested mp4 — never the request, never the size.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-duration.ts <projectId> <imagePath> <outPath> [seconds]
 */
import { FlowClient } from './flow-client'

const [projectId, imagePath, outPath, seconds = '4'] = process.argv.slice(2)
if (!projectId || !imagePath || !outPath) {
  throw new Error('usage: smoke-video-duration.ts <projectId> <imagePath> <outPath> [seconds]')
}

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const res = await client.generateVideo({
    startImage: imagePath,
    motion: 'Slow push in. The light holds steady. No cuts.',
    outPath,
    aspect: '16:9',
    // `seconds` of "default" omits the parameter entirely, to prove the asserted default.
    ...(seconds === 'default' ? {} : { durationSeconds: Number(seconds) }),
  })
  console.log('result:', JSON.stringify(res))
} finally {
  await client.close()
}
