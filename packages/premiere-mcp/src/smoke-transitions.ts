/**
 * T9's check: transitions, markers, playhead.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-transitions.ts
 *
 * The setup matters more here than in the other smokes. **A transition needs media beyond the
 * cut to dissolve into**, so both clips are trimmed to leave handles at either end before any
 * transition is asked for — otherwise Premiere quietly gives a shorter one, or none, and the
 * failure looks like a bug in the tool rather than a fact about editing.
 *
 * Runs in a scratch project. Nothing it does can touch real work.
 */
import fs from 'node:fs'
import { Checks, call, connectServer } from './smoke-client'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/t9-transitions.prproj'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'

interface TransitionInfo {
  matchName: string
  duration: number
}
interface Clip {
  ref: string
  start: number
  end: number
  duration: number
  transitions?: { start?: TransitionInfo; end?: TransitionInfo }
}
interface Marker {
  name: string
  start: number
  duration: number
  comments: string
}
interface State {
  sequence: { name: string; frameRate: number }
  videoTracks: { items: Clip[]; transitionCount: number }[]
  markers: Marker[]
}

let halfFrame = 0.03
const near = (a: number, b: number, tol = halfFrame): boolean => Math.abs(a - b) <= tol

const c = new Checks()
const v0 = (s: State): Clip[] => s.videoTracks?.[0]?.items ?? []
const transitionCount = (s: State): number => s.videoTracks?.[0]?.transitionCount ?? -1

function expectState(label: string, result: Record<string, unknown>): State | null {
  if (result.error === true || !Array.isArray(result.videoTracks)) {
    c.check(label, false, result)
    return null
  }
  return result as unknown as State
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

    await call(client, 'premiere_open_project', { path: PROJECT })
    const imported = await call(client, 'premiere_import', { paths: [MEDIA], bin: 'takes' })
    const item = ((imported.items as { id: string }[] | undefined) ?? [])[0]
    if (!c.check('media imported', Boolean(item), imported)) return

    const listed = await call(client, 'premiere_list_sequences')
    const seqName = `trans-${((listed.sequences as unknown[] | undefined) ?? []).length + 1}`
    let state = expectState('fresh sequence', await call(client, 'premiere_create_sequence', { name: seqName }))
    if (!state) return
    halfFrame = state.sequence.frameRate > 0 ? 0.5 / state.sequence.frameRate : 0.03
    c.note(`${state.sequence.frameRate.toFixed(3)}fps — times compared within ±${halfFrame.toFixed(4)}s`)

    c.section('the catalogue')
    const all = await call(client, 'premiere_list_transitions')
    const names = ((all.transitions as { matchName: string }[] | undefined) ?? []).map((t) => t.matchName)
    if (!c.check('Premiere listed its video transitions', names.length > 0, all)) return
    c.note(`${names.length} video transitions on this install`)
    c.note(`first five: ${names.slice(0, 5).join(' | ')}`)

    const dissolves = await call(client, 'premiere_list_transitions', { query: 'dissolve' })
    const dissolveNames = ((dissolves.transitions as { matchName: string }[] | undefined) ?? []).map((t) => t.matchName)
    c.check('query filters', dissolveNames.length > 0 && dissolveNames.length < names.length, dissolveNames)

    const CROSS = names.find((n) => /cross\s*dissolve/i.test(n))
    const DIP = names.find((n) => /dip\s*to\s*black/i.test(n))
    c.check('Cross Dissolve is in the catalogue', Boolean(CROSS), { CROSS, dissolveNames })
    c.check('Dip to Black is in the catalogue', Boolean(DIP), { DIP })
    // These two names go straight into api-notes.md — printed loudly so they cannot be missed.
    console.log(`\n  📋 RECORD IN api-notes.md:\n     Cross Dissolve = ${CROSS ?? '(NOT FOUND)'}\n     Dip to Black   = ${DIP ?? '(NOT FOUND)'}\n`)
    if (!CROSS) return

    c.section('two clips with handles at the cut')
    // A transition needs unused source media beyond the cut on BOTH sides. A gets its tail
    // handle by ending short of the source; B needs a HEAD handle, which means moving its
    // in-point off zero.
    //
    // 🔴 `inPoint` and `start` must NOT be sent in the same trim_clip call. Every Action in a
    // CompoundAction is computed against the state at the START of the transaction, so a
    // head-trim of +1s and a "start at 4" fight each other and the clip lands at 5. Trim first,
    // then move — two calls, predictable result.
    state = expectState('A at 0', await call(client, 'premiere_insert_clip', { item: item.id, time: 0, mode: 'overwrite' }))
    if (!state) return
    state = expectState('trim A to 4s', await call(client, 'premiere_trim_clip', { clip: 'v0:0', end: 4 }))
    if (!state) return
    c.check('A runs 0 → ~4', near(v0(state)[0]?.start ?? -1, 0) && near(v0(state)[0]?.end ?? -1, 4), v0(state)[0])

    state = expectState('B at 4', await call(client, 'premiere_insert_clip', { item: item.id, time: 4, mode: 'overwrite' }))
    if (!state) return
    state = expectState('trim B to end at 8', await call(client, 'premiere_trim_clip', { clip: 'v0:1', end: 8 }))
    if (!state) return
    state = expectState('give B a head handle', await call(client, 'premiere_trim_clip', { clip: 'v0:1', inPoint: 1 }))
    if (!state) return
    c.check('a head trim pushes the clip later, leaving a gap', near(v0(state)[1]?.start ?? -1, 5), v0(state)[1])
    state = expectState('close the gap', await call(client, 'premiere_move_clip', { clip: 'v0:1', deltaSeconds: -1 }))
    if (!state) return
    c.check('B is flush against A again', near(v0(state)[1]?.start ?? -1, v0(state)[0]?.end ?? -99), v0(state).map((k) => [k.start, k.end]))
    c.check('no transitions yet', transitionCount(state) === 0, state.videoTracks?.[0])

    c.section('a 1s cross dissolve on the cut')
    state = expectState(
      'add_transition',
      await call(client, 'premiere_add_transition', { clip: 'v0:0', matchName: CROSS, at: 'end', duration: 1 })
    )
    if (!state) return
    c.check('the track now reports one transition', transitionCount(state) === 1, state.videoTracks?.[0])

    // 🔴 Premiere returns `null` for every transition track item, so the match name and timing
    // cannot be read back through the API at all — only counted. This asserts the documented
    // behaviour so that the day it changes, this test tells us.
    c.check(
      'per-clip `transitions` is empty — Premiere will not marshal a transition track item',
      !v0(state)[0]?.transitions?.end && !v0(state)[1]?.transitions?.start,
      { outgoing: v0(state)[0]?.transitions, incoming: v0(state)[1]?.transitions }
    )
    c.note('The dissolve IS on the timeline — verified in the saved .prproj XML, not through the API.')

    state = expectState(
      'a second transition elsewhere',
      await call(client, 'premiere_add_transition', { clip: 'v0:1', matchName: DIP ?? CROSS, at: 'end', duration: 1 })
    )
    if (!state) return
    c.check('the count tracks it', transitionCount(state) === 2, state.videoTracks?.[0])

    c.section('and off again')
    state = expectState('remove_transition', await call(client, 'premiere_remove_transition', { clip: 'v0:0', at: 'end' }))
    if (!state) return
    c.check('the count went back down', transitionCount(state) === 1, state.videoTracks?.[0])
    state = expectState('remove the other', await call(client, 'premiere_remove_transition', { clip: 'v0:1', at: 'end' }))
    if (!state) return
    c.check('…and down to none', transitionCount(state) === 0, state.videoTracks?.[0])
    const noop = expectState('removing nothing', await call(client, 'premiere_remove_transition', { clip: 'v0:0', at: 'start' }))
    c.check('removing a transition that is not there is a no-op, not an error', Boolean(noop) && transitionCount(noop!) === 0, noop?.videoTracks?.[0])

    c.section('no handles is NOT a refusal')
    // v0:0 sits at source in-point 0, so there is nothing before it to dissolve from. Premiere
    // takes it anyway and makes the transition SINGLE-SIDED — confirmed in the saved .prproj as
    // `HasOutgoingClip=true, HasIncomingClip=false`, i.e. a frame-hold on the empty side.
    // Worth asserting: an editor expecting a refusal here would be wrong, and so was this test.
    const noHandles = expectState(
      'a transition with no handles',
      await call(client, 'premiere_add_transition', { clip: 'v0:0', matchName: CROSS, at: 'start', duration: 1 })
    )
    if (!noHandles) return
    c.check('Premiere accepts it and makes it single-sided', transitionCount(noHandles) === 1, noHandles.videoTracks?.[0])
    c.note('Single-sidedness is only visible in the saved .prproj — the API will not say.')
    state = expectState('tidy up', await call(client, 'premiere_remove_transition', { clip: 'v0:0', at: 'start' }))
    if (!state) return
    c.check('…and it comes off again', transitionCount(state) === 0, state.videoTracks?.[0])

    c.section('bad arguments')
    const unknown = await call(client, 'premiere_add_transition', { clip: 'v0:0', matchName: 'AE.ADBE Cross Disolve', at: 'end' })
    c.check('an unknown matchName → TRANSITION_NOT_FOUND', unknown.code === 'TRANSITION_NOT_FOUND', unknown)
    c.check('…and it names the nearest few', String(unknown.message ?? '').includes(CROSS), unknown.message)

    const audio = await call(client, 'premiere_add_transition', { clip: 'a0:0', matchName: CROSS, at: 'end' })
    const audioRejected = audio.error === true || /-32602|validation/i.test(String(audio.raw ?? ''))
    c.check('an audio ref is rejected', audioRejected, audio)
    c.check('…and says transitions are video-only', /video-only/i.test(JSON.stringify(audio)), audio)

    c.section('markers')
    state = expectState(
      'add_marker',
      await call(client, 'premiere_add_marker', { name: 'beat', time: 3, comments: 'the drop lands here' })
    )
    if (!state) return
    const marker = (state.markers ?? []).find((m) => m.name === 'beat')
    c.check('the marker is in the state', Boolean(marker), state.markers)
    c.check('…at ~3s', near(marker?.start ?? -1, 3), marker)
    c.check('…with its comment', marker?.comments === 'the drop lands here', marker)

    state = expectState(
      'a second, spanning marker',
      await call(client, 'premiere_add_marker', { name: 'section', time: 5, duration: 2, comments: '' })
    )
    if (!state) return
    const span = (state.markers ?? []).find((m) => m.name === 'section')
    c.check('a duration makes it a span', near(span?.duration ?? -1, 2), span)
    c.check('two markers now', (state.markers ?? []).length >= 2, state.markers)

    c.section('playhead')
    const moved = await call(client, 'premiere_set_playhead', { time: 2.5 })
    c.check('set_playhead answers with where it landed', typeof moved.playhead === 'number', moved)
    c.check('…which is ~2.5s', near(Number(moved.playhead ?? -1), 2.5), moved)
    const reread = expectState('re-read the sequence', await call(client, 'premiere_get_sequence', { params: false }))
    if (reread) {
      c.check(
        'the sequence agrees about the playhead',
        near(Number((reread.sequence as unknown as { playhead: number }).playhead ?? -1), 2.5),
        reread.sequence
      )
    }
    c.note('Look at Premiere: the program monitor should be sitting at 2.5s.')
  } finally {
    await close()
  }
  c.finish('T9 smoke')
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
