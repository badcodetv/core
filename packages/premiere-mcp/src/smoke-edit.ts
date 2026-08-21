/**
 * T8's check: the edit tools, exercised as a real cut would exercise them.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-edit.ts
 *
 * Assertions are RELATIVE (this clip moved later by 2s, this one shortened) rather than pinned to
 * absolute timecodes, so the script keeps working with whatever test media is to hand instead of
 * silently depending on one file's duration.
 *
 * Runs in a scratch project. Nothing it does can touch real work.
 */
import fs from 'node:fs'
import { Checks, call, connectServer } from './smoke-client'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/t8-edit.prproj'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'
const SEQ = 'edit'

interface Clip {
  ref: string
  name: string
  start: number
  end: number
  duration: number
}
interface State {
  sequence: { name: string; end: number; frameRate: number }
  videoTracks: { index: number; label: string; items: Clip[] }[]
}

/**
 * 🔴 Premiere snaps every edit to a frame boundary. Ask for 4.0s in a 23.976 sequence and the
 * clip lands at 4.004. Exact-equality assertions on times are therefore WRONG, not strict — so
 * every time comparison here is within half a frame.
 */
let halfFrame = 0.03
const near = (a: number, b: number): boolean => Math.abs(a - b) <= halfFrame

const c = new Checks()
const v0 = (s: State): Clip[] => s.videoTracks?.[0]?.items ?? []
const show = (s: State): string => v0(s).map((k) => `${k.ref}[${k.start}→${k.end}]`).join(' ') || '(empty)'

/**
 * A tool error is `{ error: true, code, message }` — it has no `videoTracks`, so reading one
 * blindly crashes the script with a TypeError and hides the actual failure. Check, report, stop.
 */
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

    // A fresh sequence per run, so a re-run never inherits the last one's timeline.
    const stamp = String(await nextSuffix(client))
    const seqName = `${SEQ}-${stamp}`
    const created = expectState('fresh sequence', await call(client, 'premiere_create_sequence', { name: seqName }))
    if (!created) return
    if (!c.check('sequence is named as asked', created.sequence?.name === seqName, created.sequence)) return
    halfFrame = created.sequence.frameRate > 0 ? 0.5 / created.sequence.frameRate : 0.03
    c.note(`sequence is ${created.sequence.frameRate.toFixed(3)}fps — times compared within ±${halfFrame.toFixed(4)}s (half a frame)`)

    c.section('overwrite two clips and trim them short')
    let state = expectState('overwrite A at 0', await call(client, 'premiere_insert_clip', { item: item.id, time: 0, mode: 'overwrite' }))
    if (!state) return
    c.check('clip A landed at 0', near(v0(state)[0]?.start ?? -1, 0), show(state))
    const fullDuration = v0(state)[0]?.duration ?? 0

    state = expectState('trim A', await call(client, 'premiere_trim_clip', { clip: 'v0:0', end: 4 }))
    if (!state) return
    c.check('A trimmed to end at ~4s', near(v0(state)[0]?.end ?? -1, 4), show(state))
    c.check('…and its duration followed', near(v0(state)[0]?.duration ?? -1, 4), v0(state)[0])

    state = expectState('overwrite B at 4', await call(client, 'premiere_insert_clip', { item: item.id, time: 4, mode: 'overwrite' }))
    if (!state) return
    c.check('clip B landed at ~4', near(v0(state)[1]?.start ?? -1, 4), show(state))

    state = expectState('trim B', await call(client, 'premiere_trim_clip', { clip: 'v0:1', end: 8 }))
    if (!state) return
    c.check('B trimmed to ~8', near(v0(state)[1]?.end ?? -1, 8), show(state))
    c.check('two clips on V1', v0(state).length === 2, show(state))

    c.section('insert shifts what follows; overwrite does not')
    const beforeInsert = v0(state).map((k) => k.start)
    state = expectState('insert at 0', await call(client, 'premiere_insert_clip', { item: item.id, time: 0, mode: 'insert' }))
    if (!state) return
    c.check('three clips now', v0(state).length === 3, show(state))
    c.check('the new clip is first, at 0', near(v0(state)[0]?.start ?? -1, 0), show(state))
    c.check(
      'the old clips were pushed later by the inserted duration',
      near(v0(state)[1]?.start ?? -1, beforeInsert[0] + fullDuration),
      { was: beforeInsert, now: v0(state).map((k) => k.start), pushedBy: fullDuration }
    )

    state = expectState('ripple remove', await call(client, 'premiere_remove_clip', { clips: ['v0:0'], ripple: true }))
    if (!state) return
    c.check('ripple remove closed the gap', near(v0(state)[0]?.start ?? -1, 0) && v0(state).length === 2, show(state))

    c.section('move')
    const bStart = v0(state)[1].start
    state = expectState('move +2', await call(client, 'premiere_move_clip', { clip: 'v0:1', deltaSeconds: 2 }))
    if (!state) return
    c.check('B moved later by ~2s', near(v0(state)[1]?.start ?? -1, bStart + 2), show(state))

    state = expectState('move -2', await call(client, 'premiere_move_clip', { clip: 'v0:1', deltaSeconds: -2 }))
    if (!state) return
    c.check('…and back again', near(v0(state)[1]?.start ?? -1, bStart), show(state))

    c.section('clone')
    const countBefore = v0(state).length
    state = expectState('clone +100', await call(client, 'premiere_clone_clip', { clip: 'v0:0', deltaSeconds: 100, mode: 'overwrite' }))
    if (!state) return
    c.check('a clip was added', v0(state).length === countBefore + 1, show(state))
    const clone = v0(state)[v0(state).length - 1]
    c.check('the clone sits ~100s after the original', near(clone?.start ?? -1, 100), clone)
    c.check('the clone kept the trim', near(clone?.duration ?? -1, 4), clone)

    state = expectState('remove clone', await call(client, 'premiere_remove_clip', { clips: [clone.ref], ripple: false }))
    if (!state) return
    c.check('clone removed', v0(state).length === countBefore, show(state))
    c.check('non-ripple removal left the others where they were', near(v0(state)[0]?.start ?? -1, 0), show(state))

    c.section('stale and bad refs')
    const stale = await call(client, 'premiere_remove_clip', { clips: ['v0:99'] })
    c.check('a ref past the end → CLIP_NOT_FOUND', stale.code === 'CLIP_NOT_FOUND', stale)
    c.check('…and the message says how many clips there are', /has \d+ clip/.test(String(stale.message ?? '')), stale)

    // A zod violation is caught by the MCP layer BEFORE the tool handler runs, so it comes back
    // as a protocol error (`MCP error -32602`), NOT as our `{ error, code, message, hint }` shape.
    // Both forms mean "rejected"; a caller has to recognise both.
    const malformed = await call(client, 'premiere_move_clip', { clip: 'not-a-ref', deltaSeconds: 1 })
    const rejected = malformed.error === true || /-32602|validation/i.test(String(malformed.raw ?? ''))
    c.check('a malformed ref is rejected before it reaches Premiere', rejected, malformed)
    c.check('…by schema validation, not by Premiere', /Invalid arguments/.test(String(malformed.raw ?? '')), malformed)

    const noEdges = await call(client, 'premiere_trim_clip', { clip: 'v0:0' })
    c.check('trim with no edges → INVALID_ARGS', noEdges.code === 'INVALID_ARGS', noEdges)

    c.section('undo')
    c.note('Each call above should be ONE entry in Edit ▸ Undo, labelled "BadCode: …".')
    c.note('Premiere exposes no undo-history API — this is the one thing here a human must eyeball.')
  } finally {
    await close()
  }
  c.finish('T8 smoke')
}

/** Sequence names must not collide across runs; ask the project what already exists. */
async function nextSuffix(client: Awaited<ReturnType<typeof connectServer>>['client']): Promise<number> {
  const listed = await call(client, 'premiere_list_sequences')
  return ((listed.sequences as unknown[] | undefined) ?? []).length + 1
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
