/**
 * Does `count` on a video turn actually give you N candidate clips — and do we get them all?
 *
 * `flow_generate_video` accepts count 1–4 and `ensureVideoSettings` asserts it, but nothing has
 * ever run it above 1, and `waitForVideoClip` returns the FIRST new clip it sees. The suspicion:
 * Flow bills and generates two clips while we harvest one and abandon the other. If so, the
 * headline "two candidates for one turn's wait" is only true once the harvest is plumbed
 * through, exactly as `harvestCandidates` already does for images.
 *
 * ⚠️ Spends credits for `count` clips (Veo 3.1 Lite ≈ 10 each).
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-count.ts <projectId> <outDir> [count]
 */
import { execFileSync } from 'node:child_process'
import { readFileSync, statSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { FlowClient } from './flow-client'

const [projectId, outDir, countArg] = process.argv.slice(2)
if (!projectId || !outDir) throw new Error('usage: smoke-video-count.ts <projectId> <outDir> [count]')
const count = Number(countArg ?? 2)

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const started = Date.now()
  const clip = await client.generateVideo({
    motion: 'A single plain metal disc on a dark table, one thin light above. The light dims. No cuts.',
    outPath: `${outDir}/count.mp4`,
    model: 'Veo 3.1 Lite',
    durationSeconds: 4,
    count,
  })
  const secs = ((Date.now() - started) / 1000).toFixed(1)
  console.log(`returned ${clip.mediaId} in ${secs}s (via=${clip.via ?? 'animate/frames as requested'})`)
  console.log(`candidates: ${JSON.stringify(clip.candidates?.map((c) => c.path) ?? null)}${clip.partial ? '  PARTIAL' : ''}`)

  // The real check is the harvest, not a raw gallery diff: a diff has to guess which ids the
  // turn produced, and the grid keeps hydrating underneath it. Candidates must exist, be
  // distinct files, and each be a real clip.
  const paths = clip.candidates?.map((c) => c.path) ?? [clip.path]
  if (paths.length !== count) throw new Error(`asked for ${count} clips, harvested ${paths.length}`)
  const digests = new Set<string>()
  for (const p of paths) {
    const size = statSync(p).size
    const md5 = createHash('md5').update(readFileSync(p)).digest('hex').slice(0, 10)
    const probe = execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', p]).toString().trim().replace(/\n/g, ' ')
    console.log(`   ${p}  ${size} bytes  md5=${md5}  ${probe}`)
    if (size < 50_000) throw new Error(`${p} is too small to be a clip`)
    digests.add(md5)
  }
  if (digests.size !== paths.length) throw new Error('candidates are the SAME file — one clip harvested twice')
  console.log(`\nCOUNT OK — ${paths.length} distinct clips from ONE turn in ${secs}s`)
} finally {
  await client.close()
}
