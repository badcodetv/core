/**
 * T12's check: getting pixels out.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-export.ts
 *
 * This is the ticket that turns "drives Premiere" into "delivers a file", so the assertions are
 * about the FILE — it exists, ffprobe agrees with what we asked for, and the pixels are the
 * right size — rather than about what Premiere claimed.
 *
 * 🔴 Both exports resolve BEFORE their file is finished. Every check here runs after the server
 * has waited for a stable size; nothing asserts on the promise alone.
 *
 * Runs in a scratch project. Nothing it does can touch real work.
 */
import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import { Checks, call, connectServer } from './smoke-client'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/t12-export.prproj'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'
const CLIP_SECONDS = 6

const c = new Checks()

interface State {
  sequence: { name: string; frameRate: number; end: number }
  videoTracks: { items: { ref: string; start: number; end: number }[] }[]
}

function expectState(label: string, result: Record<string, unknown>): State | null {
  if (result.error === true || !Array.isArray(result.videoTracks)) {
    c.check(label, false, result)
    return null
  }
  return result as unknown as State
}

/** What ffprobe says, not what we hoped. */
function probe(path: string, entries: string): string {
  return execFileSync('ffprobe', ['-v', 'error', '-show_entries', entries, '-of', 'default=noprint_wrappers=1:nokey=1', path])
    .toString()
    .trim()
}

async function main(): Promise<void> {
  const { client, close } = await connectServer()
  try {
    c.section('setup')
    const status = await call(client, 'premiere_status')
    if (!c.check('panel connected', status.connected === true, status)) return
    if (!fs.existsSync(MEDIA)) {
      c.check(`test media exists (${MEDIA})`, false)
      return
    }

    const opened = await call(client, 'premiere_open_project', { path: PROJECT })
    c.check('project open', opened.error !== true, opened)
    c.check('frames/ and renders/ sit beside the project', typeof opened.framesDir === 'string' && typeof opened.rendersDir === 'string', {
      frames: opened.framesDir,
      renders: opened.rendersDir,
    })

    const imported = await call(client, 'premiere_import', { paths: [MEDIA], bin: 'takes' })
    const item = ((imported.items as { id: string }[] | undefined) ?? [])[0]
    if (!c.check('media imported', Boolean(item), imported)) return

    const listed = await call(client, 'premiere_list_sequences')
    const seqName = `out-${((listed.sequences as unknown[] | undefined) ?? []).length + 1}`
    let state = expectState('fresh sequence', await call(client, 'premiere_create_sequence', { name: seqName }))
    if (!state) return
    state = expectState('a clip', await call(client, 'premiere_insert_clip', { item: item.id, time: 0, mode: 'overwrite' }))
    if (!state) return
    state = expectState(`trimmed to ${CLIP_SECONDS}s`, await call(client, 'premiere_trim_clip', { clip: 'v0:0', end: CLIP_SECONDS }))
    if (!state) return
    const frameRate = state.sequence.frameRate
    c.note(`sequence "${seqName}" is ${frameRate.toFixed(3)}fps, ends at ${state.sequence.end}s`)

    c.section('export a frame')
    const frame = await call(client, 'premiere_export_frame', { time: 1.5 })
    if (!c.check('export_frame succeeded', frame.error !== true, frame)) return
    const framePath = String(frame.path)
    c.check('…returning a WSL path', framePath.startsWith('/mnt/'), framePath)
    c.check('…that actually exists', fs.existsSync(framePath), framePath)
    c.check('…with bytes in it', Number(frame.bytes) > 1000, frame.bytes)
    c.check('…under the project\'s frames/ directory', framePath.includes('/frames/'), framePath)
    if (fs.existsSync(framePath)) {
      const dims = probe(framePath, 'stream=width,height').split('\n')
      c.check('…at the sequence frame size', dims[0] === '1920' && dims[1] === '1080', dims)
      c.check('…and it is a real PNG', probe(framePath, 'stream=codec_name') === 'png', framePath)
    }

    c.section('export a frame somewhere else, at another size')
    const custom = '/mnt/d/badcode-videos/_smoke/probe-out/custom-frame.jpg'
    if (fs.existsSync(custom)) fs.unlinkSync(custom)
    const frame2 = await call(client, 'premiere_export_frame', { time: 3, outPath: custom, width: 640, height: 360 })
    if (c.check('an explicit outPath is honoured', frame2.error !== true, frame2)) {
      c.check('…written where asked', fs.existsSync(custom), custom)
      if (fs.existsSync(custom)) {
        const dims = probe(custom, 'stream=width,height').split('\n')
        c.check('…at the size asked for', dims[0] === '640' && dims[1] === '360', dims)
        c.check('…in the format the extension asked for', probe(custom, 'stream=codec_name').includes('jpeg'), custom)
      }
    }

    const badFormat = await call(client, 'premiere_export_frame', { time: 1, outPath: '/mnt/d/badcode-videos/_smoke/probe-out/x.webp' })
    c.check('an unsupported frame format is refused', badFormat.code === 'INVALID_ARGS', badFormat)
    c.check('…listing what it does support', /png/.test(String(badFormat.hint ?? '')), badFormat.hint)

    c.section('render the sequence')
    c.note('This renders in Premiere and blocks — expect a few seconds for 6s of video.')
    const t0 = Date.now()
    const render = await call(client, 'premiere_export_sequence', {})
    const took = Date.now() - t0
    if (!c.check('export_sequence succeeded', render.error !== true, render)) return
    const renderPath = String(render.path)
    c.note(`rendered in ${(took / 1000).toFixed(1)}s → ${renderPath}`)
    c.check('…returning a WSL path', renderPath.startsWith('/mnt/'), renderPath)
    c.check('…that exists', fs.existsSync(renderPath), renderPath)
    c.check('…under the project\'s renders/ directory', renderPath.includes('/renders/'), renderPath)
    c.check('…with real bytes', Number(render.bytes) > 10000, render.bytes)
    c.check('…and it says it rendered the whole sequence', render.renderedWholeSequence === true, render)

    // THE assertion that matters: the file is as long as the timeline said it was.
    const duration = Number(render.durationSeconds)
    c.check('…duration was measured, not assumed', Number.isFinite(duration), render.durationSeconds)
    c.check(`…and it is ~${CLIP_SECONDS}s`, Math.abs(duration - CLIP_SECONDS) < 0.1, { reported: duration, expected: CLIP_SECONDS })
    if (fs.existsSync(renderPath)) {
      c.check('…ffprobe agrees independently', Math.abs(Number(probe(renderPath, 'format=duration')) - CLIP_SECONDS) < 0.1, probe(renderPath, 'format=duration'))
      c.check('…and it carries a video stream', probe(renderPath, 'stream=codec_type').includes('video'), renderPath)
    }

    c.section('bad arguments')
    const badPreset = await call(client, 'premiere_export_sequence', { preset: '/mnt/d/nope/missing.epr' })
    c.check('a missing preset is caught before Premiere is asked', badPreset.code === 'INVALID_ARGS', badPreset)

    c.section('the round trip')
    c.note('Everything above went idea → timeline → file without a human touching Premiere.')
  } finally {
    await close()
  }
  c.finish('T12 smoke')
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
