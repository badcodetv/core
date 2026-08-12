/**
 * C2 live proof, part 2: the two modes with no start frame.
 *
 * ⚠️ SPENDS CREDITS (two clips; runs on Veo 3.1 Lite, the 10-credit tier, because what is
 * being proven is the plumbing, not the picture). Claiming a mode works without having run it
 * once is exactly how Wave A shipped selectors that matched nothing.
 *
 *   end-only : does Flow generate from a LAST frame alone?
 *   text     : does the video path still work with no frames attached at all?
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-modes.ts <projectId> <endImg> <outDir>
 */
import { FlowClient } from './flow-client'

const [projectId, endImage, outDir, model = 'Veo 3.1 - Lite'] = process.argv.slice(2)
if (!projectId || !endImage || !outDir) throw new Error('usage: smoke-video-modes.ts <projectId> <endImg> <outDir>')

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })

  console.log('=== end frame only ===')
  try {
    const res = await client.generateVideo({
      motion: 'The camera drifts slowly forward and settles.',
      outPath: `${outDir}/mode-end.mp4`,
      endImage,
      model,
      aspect: '16:9',
      durationSeconds: 4,
    })
    console.log('  ok:', JSON.stringify(res))
  } catch (err) {
    console.log('  FAILED:', err instanceof Error ? err.message : String(err))
  }

  console.log('=== text to video (no frames) ===')
  try {
    const res = await client.generateVideo({
      motion:
        'A single dark corridor of server racks, one thin vertical light at the far end. The camera pushes in very slowly. Nothing else moves.',
      outPath: `${outDir}/mode-text.mp4`,
      model,
      aspect: '16:9',
      durationSeconds: 4,
    })
    console.log('  ok:', JSON.stringify(res))
  } catch (err) {
    console.log('  FAILED:', err instanceof Error ? err.message : String(err))
  }
} finally {
  await client.close()
}
