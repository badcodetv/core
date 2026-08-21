/**
 * T7's check: sequence tools and the shape `normalise.ts` produces from a real timeline.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-sequence.ts
 *   SMOKE_CAPTURE=1 npx tsx packages/premiere-mcp/src/smoke-sequence.ts   # refresh the fixtures
 *
 * Runs in a scratch project so it can never disturb real work.
 */
import fs from 'node:fs'
import { Checks, call, captureRawDump, connectServer } from './smoke-client'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/t7-sequence.prproj'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'
const EMPTY = 's00-empty'
const FROM_MEDIA = 's01-from-media'

interface Clip {
  ref: string
  name: string
  start: number
  end: number
  duration: number
  mediaPath: string | null
  speed: number
  components: { matchName: string; displayName: string; params: { name: string; value: unknown }[] }[]
  transitions?: Record<string, unknown>
}
interface Track {
  index: number
  label: string
  items: Clip[]
}
interface State {
  sequence: { name: string; frameSize: { w: number; h: number }; end: number }
  videoTracks: Track[]
  audioTracks: Track[]
  markers: unknown[]
}

const c = new Checks()

async function main(): Promise<void> {
  const { client, close } = await connectServer()
  try {
    c.section('bridge')
    const status = await call(client, 'premiere_status')
    if (!c.check('panel connected', status.connected === true, status)) return

    c.section('scratch project')
    const opened = await call(client, 'premiere_open_project', { path: PROJECT })
    if (!c.check('project open', Boolean((opened.project as { path?: string } | undefined)?.path), opened)) return

    c.section(`premiere_create_sequence — empty ("${EMPTY}")`)
    const empty = (await call(client, 'premiere_create_sequence', { name: EMPTY })) as unknown as State
    if (!c.check('created and returned a state', empty.sequence?.name === EMPTY, empty)) return
    c.check('frame size reported', empty.sequence.frameSize.w > 0 && empty.sequence.frameSize.h > 0, empty.sequence)
    c.check('has video tracks', empty.videoTracks.length > 0, empty.videoTracks.length)
    c.check('tracks are labelled 1-based', empty.videoTracks[0]?.label === 'V1', empty.videoTracks[0])
    c.check('audio tracks labelled A1…', empty.audioTracks[0]?.label === 'A1', empty.audioTracks[0])
    c.check('no clips yet', empty.videoTracks.every((t) => t.items.length === 0), empty.videoTracks)
    c.note(`${empty.videoTracks.length} video / ${empty.audioTracks.length} audio tracks, ${empty.sequence.frameSize.w}x${empty.sequence.frameSize.h}`)
    await captureRawDump(client, EMPTY, 'dump-empty.json')

    c.section('premiere_create_sequence — from media')
    if (!fs.existsSync(MEDIA)) {
      c.note(`skipped: ${MEDIA} is missing. Set SMOKE_MEDIA.`)
    } else {
      const imported = await call(client, 'premiere_import', { paths: [MEDIA], bin: 'takes' })
      const items = (imported.items as { id: string; name: string }[] | undefined) ?? []
      if (!c.check('media imported', items.length === 1, imported)) return

      const built = (await call(client, 'premiere_create_sequence', {
        name: FROM_MEDIA,
        fromItems: [items[0].id],
      })) as unknown as State
      c.check('sequence built from media', built.sequence?.name === FROM_MEDIA, built.sequence)

      const clips = built.videoTracks.flatMap((t) => t.items)
      if (c.check('the clip landed on the timeline', clips.length >= 1, built.videoTracks)) {
        const clip = clips[0]
        c.check('ref is v<track>:<item>', /^v\d+:\d+$/.test(clip.ref), clip.ref)
        c.check('times are seconds', clip.end > clip.start && clip.duration > 0, clip)
        c.check('mediaPath came back in WSL form', clip.mediaPath?.startsWith('/mnt/') === true, clip.mediaPath)
        c.check('speed defaults to 1', clip.speed === 1, clip.speed)
        c.check('carries an effect chain', clip.components.length > 0, clip.components.length)
        c.check('transitions field present and empty', JSON.stringify(clip.transitions ?? {}) === '{}', clip.transitions)

        // The intrinsics are needed constantly from T10 onward and are not documented anywhere.
        console.log('\n  INTRINSIC COMPONENTS (record these in docs/premiere/api-notes.md):')
        for (const comp of clip.components) {
          const params = comp.params.map((prm) => `${prm.name}=${JSON.stringify(prm.value)}`).join(', ')
          console.log(`    ${comp.displayName.padEnd(14)} ${comp.matchName}`)
          console.log(`      ${params}`)
        }

        // Only assert the audio side when the source actually HAS audio. The default test clip
        // is a Flow render with a single h264 stream and no audio at all, so "no audio clips" is
        // Premiere being correct, not a bug — an earlier version of this check failed on it.
        const audio = built.audioTracks.flatMap((t) => t.items)
        if (audio.length > 0) {
          c.check('audio ref is a<track>:<item>', /^a\d+:\d+$/.test(audio[0].ref), audio[0].ref)
        } else {
          c.note('source has no audio stream — audio tracks are empty, as expected')
        }
      }
      await captureRawDump(client, FROM_MEDIA, 'dump-one-clip.json')
    }

    c.section('premiere_list_sequences')
    const listed = await call(client, 'premiere_list_sequences')
    const sequences = (listed.sequences as { name: string; active: boolean }[] | undefined) ?? []
    c.check('both sequences listed', sequences.length >= 2, sequences)
    c.check('exactly one is active', sequences.filter((s) => s.active).length === 1, sequences)

    c.section('premiere_set_active')
    const back = (await call(client, 'premiere_set_active', { name: EMPTY })) as unknown as State
    c.check('switched back to the empty sequence', back.sequence?.name === EMPTY, back.sequence)
    const relisted = await call(client, 'premiere_list_sequences')
    const nowActive = ((relisted.sequences as { name: string; active: boolean }[]) ?? []).find((s) => s.active)
    c.check('list agrees on which is active', nowActive?.name === EMPTY, nowActive)

    const missing = await call(client, 'premiere_set_active', { name: 'no-such-sequence' })
    c.check('unknown sequence → NO_SEQUENCE', missing.code === 'NO_SEQUENCE', missing)
    c.check('…and the error names what IS open', String(missing.message ?? '').includes(EMPTY), missing)

    c.section('premiere_get_sequence')
    const read = (await call(client, 'premiere_get_sequence', { name: FROM_MEDIA })) as unknown as State
    c.check('reads a sequence by name without activating it', read.sequence?.name === FROM_MEDIA, read.sequence)
    const stillActive = await call(client, 'premiere_list_sequences')
    c.check(
      'reading did not change the active sequence',
      ((stillActive.sequences as { name: string; active: boolean }[]) ?? []).find((s) => s.active)?.name === EMPTY,
      stillActive
    )

    const withParams = Date.now()
    await call(client, 'premiere_get_sequence', { name: FROM_MEDIA, params: true })
    const withParamsMs = Date.now() - withParams
    const withoutParams = Date.now()
    const lean = (await call(client, 'premiere_get_sequence', { name: FROM_MEDIA, params: false })) as unknown as State
    const withoutParamsMs = Date.now() - withoutParams
    c.check(
      'params:false drops the effect chains',
      lean.videoTracks.flatMap((t) => t.items).every((clip) => clip.components.length === 0),
      lean.videoTracks
    )
    c.note(`param walk cost: ${withParamsMs}ms with params, ${withoutParamsMs}ms without`)
  } finally {
    await close()
  }
  c.finish('T7 smoke')
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
