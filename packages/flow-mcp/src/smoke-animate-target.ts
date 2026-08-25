/**
 * Manual end-to-end check for ANIMATE TARGETING on a CLUTTERED project — NOT part of CI.
 * SPENDS CREDITS (Veo 3.1 - Fast; the gate has quoted 10 credits, not the 20 in automation-video.md).
 *
 * The bug this exists for: on a project with many stills, generateVideo would animate the wrong
 * tile. A fresh project cannot test it — the sole-tile fallback in chooseAnimateTarget makes it
 * pass for free. So point this at a project that already holds several unrelated stills.
 *
 * And it checks the CLIP'S FIRST FRAME, not the file size. smoke-video-clip.ts once passed a
 * clip of the wrong image because a wrong clip is exactly as many bytes as a right one. The
 * frame is compared against BOTH the source and a decoy still already in the project: the
 * source must win by a clear margin, so "it targeted something" cannot pass as "it targeted
 * the right thing".
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-animate-target.ts <projectId> <source.jpg> <decoy.jpg> [out.mp4]
 */
import { execFile } from 'node:child_process'
import { readFile, stat } from 'node:fs/promises'
import { promisify } from 'node:util'
import { FlowClient } from './flow-client'

const run = promisify(execFile)
const [, , projectId, source, decoy, out = '/tmp/flow-animate-target.mp4'] = process.argv
if (!projectId || !source || !decoy) {
  throw new Error('usage: smoke-animate-target.ts <projectId> <source.jpg> <decoy.jpg> [out.mp4]')
}

/** Downscale to a 16x16 grayscale thumbprint — enough to tell two unrelated images apart. */
async function thumbprint(path: string, seek?: boolean): Promise<number[]> {
  const pgm = `${out}.${path.replace(/\W/g, '_').slice(-24)}.pgm`
  const args = seek
    ? ['-y', '-i', path, '-frames:v', '1', '-vf', 'scale=16:16', '-pix_fmt', 'gray', pgm]
    : ['-y', '-i', path, '-vf', 'scale=16:16', '-pix_fmt', 'gray', pgm]
  await run('ffmpeg', ['-hide_banner', '-loglevel', 'error', ...args])
  const buf = await readFile(pgm)
  // Binary PGM: "P5\n<w> <h>\n<max>\n" then w*h bytes. Take the last 256.
  return [...buf.subarray(buf.length - 256)]
}

const distance = (a: number[], b: number[]) =>
  a.reduce((sum, v, i) => sum + Math.abs(v - (b[i] ?? 0)), 0) / a.length

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const tiles = await client.listMedia()
  console.log(`project holds ${tiles.length} media rows — clutter is the point here`)

  const started = Date.now()
  const res = await client.generateVideo({
    startImage: source,
    // Motion only — the still already carries subject, scene and style (flow-prompt rule 2).
    motion: 'The camera pushes in very slowly. Dust drifts through the light. Nothing else moves.',
    outPath: out,
    model: 'Veo 3.1 - Fast',
    aspect: '16:9',
    count: 1,
  })
  const { size } = await stat(res.path)
  console.log(`clip in ${((Date.now() - started) / 1000).toFixed(1)}s:`, res, 'bytes:', size)

  const frame = `${out}.frame.png`
  await run('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', out, '-frames:v', '1', frame])
  console.log('first frame written to', frame, '— LOOK AT IT, do not trust the numbers alone')

  const [f, s, d] = [await thumbprint(frame), await thumbprint(source), await thumbprint(decoy)]
  const toSource = distance(f, s)
  const toDecoy = distance(f, d)
  console.log(`first-frame distance -> source: ${toSource.toFixed(1)}, decoy: ${toDecoy.toFixed(1)}`)
  console.log(
    toSource < toDecoy / 2
      ? 'TARGETING OK — the clip opens on the still we passed, not on the project clutter'
      : 'TARGETING SUSPECT — the first frame is not clearly our source; inspect the frame',
  )
} finally {
  await client.close()
}
