/**
 * Live proof of `refineVideo` — "like that clip, but different", with no source still on disk.
 *
 * ⚠️ Spends credits for ONE clip. That is the point: the whole claim is that Flow's per-clip
 * `Reuse prompt` restores the original source frame, so a caller who no longer has the still can
 * still re-run the turn. Nothing short of generating proves it.
 *
 * Verifies by MEASURING, not by the return value: a new media id, a real duration off ffprobe,
 * and a first frame written out to be looked at. A refine that silently regenerated nothing
 * would otherwise return a perfectly healthy-looking result.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-refine.ts <projectId> <clipMediaId> <outDir>
 */
import { execFileSync } from 'node:child_process'
import { statSync } from 'node:fs'
import { FlowClient } from './flow-client'

const [projectId, clipId, outDir] = process.argv.slice(2)
if (!projectId || !clipId || !outDir) throw new Error('usage: smoke-video-refine.ts <projectId> <clipMediaId> <outDir>')

const MOTION = 'Slow pull back. The light fades down to almost nothing by the end. No cuts.'
const out = `${outDir}/refined.mp4`

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const started = Date.now()
  const result = await client.refineVideo({ mediaId: clipId, motion: MOTION, outPath: out })
  console.log(`refined in ${((Date.now() - started) / 1000).toFixed(1)}s`)
  console.log(`original prompt Flow restored: ${JSON.stringify(result.originalPrompt)}`)
  console.log(`new mediaId: ${result.mediaId}`)

  if (result.mediaId === clipId) throw new Error('SAME mediaId — nothing was generated')
  const size = statSync(out).size
  if (size < 50_000) throw new Error(`suspiciously small clip: ${size} bytes`)
  const probe = execFileSync('ffprobe', [
    '-v', 'error', '-show_entries', 'format=duration', '-show_entries', 'stream=width,height',
    '-of', 'default=noprint_wrappers=1', out,
  ]).toString().trim()
  console.log(`ffprobe:\n${probe}`)
  // A frame to actually LOOK at — twice now a healthy file has been the wrong content.
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', out, '-vf', 'select=eq(n\\,0)', '-vframes', '1', `${outDir}/refined-first.jpg`])
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-sseof', '-0.5', '-i', out, '-vframes', '1', `${outDir}/refined-last.jpg`])
  console.log(`frames written: ${outDir}/refined-first.jpg, ${outDir}/refined-last.jpg`)
  console.log('REFINE OK — new clip, real duration; now LOOK at the frames')
} finally {
  await client.close()
}
