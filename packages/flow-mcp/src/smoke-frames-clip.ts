/**
 * C2 live proof: generate a clip from a FIRST and a LAST frame.
 *
 * ⚠️ SPENDS CREDITS (one clip). The check that matters is not that an mp4 came back — it is
 * that its first frame is the start image and its LAST frame is the end image. Run ffmpeg on
 * the result and look at both ends; a first/last generation that silently ignored the end
 * frame returns a perfectly healthy file.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-frames-clip.ts <projectId> <startImg> <endImg> <outPath>
 */
import { FlowClient } from './flow-client'

const [projectId, startImage, endImage, outPath] = process.argv.slice(2)
if (!projectId || !startImage || !endImage || !outPath) {
  throw new Error('usage: smoke-frames-clip.ts <projectId> <startImg> <endImg> <outPath>')
}

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const started = Date.now()
  const res = await client.generateVideo({
    // Start+end prompts name ONLY the connecting move — the two stills carry the content.
    motion: 'The camera holds steady and pushes in slowly.',
    outPath,
    startImage,
    endImage,
    model: 'Veo 3.1 - Fast',
    aspect: '16:9',
    durationSeconds: 4,
  })
  console.log(`clip in ${((Date.now() - started) / 1000).toFixed(1)}s:`, JSON.stringify(res))
} finally {
  await client.close()
}
