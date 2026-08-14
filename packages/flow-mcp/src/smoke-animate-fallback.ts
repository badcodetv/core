/**
 * L4 · Prove the Animate → Frames fallback in the project where Animate actually breaks.
 *
 * Animate finds the still you uploaded by diffing the tile grid, and that diff failed with
 * ANIMATE_NOT_FOUND in a ~30-item project while the identical call worked in a fresh one. Frames
 * mode never touches the grid. This runs a start-only request in the CLUTTERED project, so a
 * pass means the fallback carried it — run it anywhere clean and it proves nothing.
 *
 * ⚠️ Spends credits for one clip. Verifies by extracting the first frame: the fallback must
 * animate the still we passed, not whatever the failed Animate attempt left lying around.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-animate-fallback.ts <clutteredProjectId> <still> <outDir>
 */
import { execFileSync } from 'node:child_process'
import { statSync } from 'node:fs'
import { FlowClient } from './flow-client'

const [projectId, still, outDir] = process.argv.slice(2)
if (!projectId || !still || !outDir) throw new Error('usage: smoke-animate-fallback.ts <projectId> <still> <outDir>')

const out = `${outDir}/fallback.mp4`
const client = await FlowClient.connect()
try {
  // FORCE the failure rather than hoping the cluttered project reproduces it. A run that simply
  // succeeds proves nothing about the fallback — and the first attempt at this test could not
  // tell which path had carried it, which is also why generateVideo now reports `via`.
  ;(client as unknown as { animateToVideo: () => Promise<never> }).animateToVideo = async () => {
    throw new Error('ANIMATE_NOT_FOUND')
  }
  await client.openProject({ id: projectId })
  const started = Date.now()
  const clip = await client.generateVideo({
    motion: 'Very slow push in. Nothing else moves. No cuts.',
    outPath: out,
    startImage: still,
    model: 'Veo 3.1 Lite',
    durationSeconds: 4,
  })
  console.log(`clip ${clip.mediaId} in ${((Date.now() - started) / 1000).toFixed(1)}s, ${statSync(out).size} bytes`)
  if (clip.via !== 'frames-fallback') throw new Error(`expected via=frames-fallback, got ${JSON.stringify(clip.via)}`)
  console.log('via: frames-fallback — the fallback carried it')
  console.log(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-show_entries', 'stream=width,height', '-of', 'default=noprint_wrappers=1', out]).toString().trim())
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', out, '-vf', 'select=eq(n\\,0)', '-vframes', '1', `${outDir}/fallback-first.jpg`])
  console.log(`first frame: ${outDir}/fallback-first.jpg — LOOK at it: it must be the still that was passed in`)
} finally {
  await client.close()
}
