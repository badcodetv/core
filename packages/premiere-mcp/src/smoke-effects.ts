/**
 * T10's check: the effect tools.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-effects.ts
 *
 * Runs in a scratch project on a fresh sequence. Nothing it does can touch real work.
 *
 * The two behaviours worth knowing before reading the assertions:
 *   - An UN-INSERTED effect has no readable params at all, so `describe_effect` needs a clip.
 *   - Applying an effect and setting its params are two transactions, because Actions in one
 *     CompoundAction cannot address something an earlier Action created.
 */
import fs from 'node:fs'
import { Checks, call, connectServer } from './smoke-client'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/t10-effects.prproj'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'

const GAUSSIAN = 'AE.ADBE Gaussian Blur 2' // "Gaussian Blur (Legacy)" — 3 clean params
const LUMETRI = 'AE.ADBE Lumetri'

interface Param {
  index: number
  name: string
  value: unknown
  timeVarying: boolean
  keyframes?: { t: number; value: unknown }[]
  unreadable?: boolean
}
interface Component {
  index: number
  matchName: string
  displayName: string
  params: Param[]
}
interface Clip {
  ref: string
  components: Component[]
}
interface State {
  sequence: { name: string; frameRate: number }
  videoTracks: { items: Clip[] }[]
}

let halfFrame = 0.03
const near = (a: number, b: number, tol = halfFrame): boolean => Math.abs(a - b) <= tol

const c = new Checks()
const clip0 = (s: State): Clip | undefined => s.videoTracks?.[0]?.items?.[0]
const comp = (s: State, matchName: string): Component | undefined =>
  clip0(s)?.components?.find((x) => x.matchName === matchName)
const chainNames = (s: State): string => (clip0(s)?.components ?? []).map((x) => `${x.index}:${x.matchName}`).join(' ')

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
    const seqName = `fx-${((listed.sequences as unknown[] | undefined) ?? []).length + 1}`
    let state = expectState('fresh sequence', await call(client, 'premiere_create_sequence', { name: seqName }))
    if (!state) return
    halfFrame = state.sequence.frameRate > 0 ? 0.5 / state.sequence.frameRate : 0.03

    state = expectState('a clip to work on', await call(client, 'premiere_insert_clip', { item: item.id, time: 0, mode: 'overwrite' }))
    if (!state) return
    state = expectState('trimmed to 6s', await call(client, 'premiere_trim_clip', { clip: 'v0:0', end: 6 }))
    if (!state) return
    c.check('the clip is born with the two intrinsics', chainNames(state) === '0:AE.ADBE Opacity 1:AE.ADBE Motion', chainNames(state))

    c.section('the catalogue')
    const all = await call(client, 'premiere_list_effects')
    const effects = ((all.effects as { matchName: string; displayName: string }[] | undefined) ?? [])
    if (!c.check('Premiere listed its effects', effects.length > 0, all)) return
    c.note(`${effects.length} video effects on this install`)

    const blurs = await call(client, 'premiere_list_effects', { query: 'blur' })
    const blurList = ((blurs.effects as { matchName: string; displayName: string }[] | undefined) ?? [])
    c.check('query filters', blurList.length > 0 && blurList.length < effects.length, blurList.length)
    c.check('Gaussian Blur is findable', blurList.some((e) => e.matchName === GAUSSIAN), blurList.map((e) => e.matchName))
    c.check('every effect has a display name too', effects.every((e) => typeof e.displayName === 'string'), effects[0])
    c.check('Lumetri Color is in the catalogue', effects.some((e) => e.matchName === LUMETRI), LUMETRI)

    c.section('apply, with params, in one call')
    state = expectState(
      'apply Gaussian Blur with Blurriness 20',
      await call(client, 'premiere_apply_effect', { clip: 'v0:0', matchName: GAUSSIAN, params: { '0': 20 } })
    )
    if (!state) return
    const blur = comp(state, GAUSSIAN)
    c.check('it is on the chain', Boolean(blur), chainNames(state))
    c.check('…appended after the intrinsics', blur?.index === 2, chainNames(state))
    c.check('…and Blurriness reads back as 20', blur?.params?.[0]?.value === 20, blur?.params?.[0])
    c.check('…named "Blurriness"', blur?.params?.[0]?.name === 'Blurriness', blur?.params?.[0])

    c.section('apply by DISPLAY name, not just match name')
    state = expectState(
      'apply "Lumetri Color"',
      await call(client, 'premiere_apply_effect', { clip: 'v0:0', matchName: 'Lumetri Color' })
    )
    if (!state) return
    const lumetri = comp(state, LUMETRI)
    c.check('the display name resolved to the right effect', Boolean(lumetri), chainNames(state))
    c.check('Lumetri has ~130 params', (lumetri?.params?.length ?? 0) > 100, lumetri?.params?.length)

    // 🔴 33 of Lumetri's params refuse to yield a value by ANY route — getValueAtTime throws,
    // and the getKeyframePtr it recommends returns null. They are flagged, not hidden, and
    // their display names still read.
    const unreadable = (lumetri?.params ?? []).filter((p) => p.unreadable)
    // `every()` on an empty array is true, so each of these asserts the list is non-empty FIRST.
    // Without that guard a dropped flag reads as three passing checks — which is exactly how
    // this bug first hid.
    c.check('the unreadable params are flagged rather than dropped', unreadable.length > 0, unreadable.length)
    c.check(
      '…and they kept their real display names',
      unreadable.length > 0 && unreadable.every((p) => !p.name.startsWith('(unreadable')),
      unreadable.slice(0, 3)
    )
    c.check(
      '…with a null value, not an error string',
      unreadable.length > 0 && unreadable.every((p) => p.value === null),
      unreadable.slice(0, 3)
    )
    c.check('…and the readable majority still read', (lumetri?.params ?? []).some((p) => !p.unreadable && p.value !== null), null)
    c.note(`${unreadable.length} of ${lumetri?.params?.length} Lumetri params are unreadable — expected, documented`)

    c.section('describe_effect')
    const described = await call(client, 'premiere_describe_effect', { clip: 'v0:0', component: GAUSSIAN })
    c.check('it describes by match name', described.matchName === GAUSSIAN, described)
    c.check('…reporting the component index', described.componentIndex === 2, described)
    const dparams = (described.params as { index: number; name: string; keyframable: boolean }[] | undefined) ?? []
    c.check('…with all three params', dparams.length === 3, dparams)
    c.check('…each carrying its index', dparams.every((p) => typeof p.index === 'number'), dparams)
    c.check('…and whether it takes keyframes', dparams.every((p) => typeof p.keyframable === 'boolean'), dparams)

    const byIndex = await call(client, 'premiere_describe_effect', { clip: 'v0:0', component: 1 })
    c.check('a component can be addressed by index', byIndex.matchName === 'AE.ADBE Motion', byIndex)

    c.section('set a fixed param on an intrinsic')
    state = expectState(
      'Motion → Scale 120',
      await call(client, 'premiere_set_param', { clip: 'v0:0', component: 'AE.ADBE Motion', param: 1, value: 120 })
    )
    if (!state) return
    c.check('Scale is 120', comp(state, 'AE.ADBE Motion')?.params?.[1]?.value === 120, comp(state, 'AE.ADBE Motion')?.params?.[1])

    state = expectState(
      'Motion → Position off-centre',
      await call(client, 'premiere_set_param', { clip: 'v0:0', component: 1, param: 0, value: { x: 0.25, y: 0.75 } })
    )
    if (!state) return
    // Points are 0–1 fractions of the frame, and come BACK as a two-element array.
    const pos = comp(state, 'AE.ADBE Motion')?.params?.[0]?.value as number[] | undefined
    c.check('a {x,y} written as fractions reads back as [x, y]', Array.isArray(pos) && near(pos[0], 0.25, 0.001) && near(pos[1], 0.75, 0.001), pos)

    c.section('keyframes — a slow push in')
    state = expectState(
      'Scale 100 at 0s',
      await call(client, 'premiere_set_param', { clip: 'v0:0', component: 1, param: 1, value: 100, time: 0, interpolation: 'linear' })
    )
    if (!state) return
    state = expectState(
      'Scale 120 at 2s, bezier',
      await call(client, 'premiere_set_param', { clip: 'v0:0', component: 1, param: 1, value: 120, time: 2, interpolation: 'bezier' })
    )
    if (!state) return
    const scale = comp(state, 'AE.ADBE Motion')?.params?.[1]
    c.check('Scale is now time-varying', scale?.timeVarying === true, scale)
    c.check('…with two keyframes', (scale?.keyframes?.length ?? 0) === 2, scale?.keyframes)
    c.check('…the first at ~0s valued 100', near(scale?.keyframes?.[0]?.t ?? -1, 0) && scale?.keyframes?.[0]?.value === 100, scale?.keyframes)
    c.check('…the second at ~2s valued 120', near(scale?.keyframes?.[1]?.t ?? -1, 2) && scale?.keyframes?.[1]?.value === 120, scale?.keyframes)

    c.section('remove')
    state = expectState('remove Lumetri', await call(client, 'premiere_remove_effect', { clip: 'v0:0', component: LUMETRI }))
    if (!state) return
    c.check('Lumetri is gone', !comp(state, LUMETRI), chainNames(state))
    c.check('…and the blur is still there', Boolean(comp(state, GAUSSIAN)), chainNames(state))

    const intrinsic = await call(client, 'premiere_remove_effect', { clip: 'v0:0', component: 'AE.ADBE Motion' })
    c.check('an intrinsic cannot be removed', intrinsic.code === 'INVALID_ARGS', intrinsic)
    c.check('…and the message explains why', /intrinsic/i.test(String(intrinsic.message ?? '')), intrinsic.message)

    c.section('bad arguments')
    const unknownFx = await call(client, 'premiere_apply_effect', { clip: 'v0:0', matchName: 'Gausian Blurr' })
    c.check('an unknown effect → EFFECT_NOT_FOUND', unknownFx.code === 'EFFECT_NOT_FOUND', unknownFx)
    c.check('…naming near matches', /blur/i.test(String(unknownFx.message ?? '')), unknownFx.message)

    const badParam = await call(client, 'premiere_set_param', { clip: 'v0:0', component: 2, param: 99, value: 1 })
    c.check('an out-of-range param index → PARAM_NOT_FOUND', badParam.code === 'PARAM_NOT_FOUND', badParam)
    c.check('…saying how many there are', /has 3/.test(String(badParam.message ?? '')), badParam.message)

    // "Blend Mode" appears twice on Opacity, so resolving it by name must refuse rather than guess.
    const ambiguous = await call(client, 'premiere_set_param', { clip: 'v0:0', component: 0, param: 'Blend Mode', value: 0 })
    c.check('an ambiguous param name is refused, not guessed', ambiguous.code === 'PARAM_NOT_FOUND', ambiguous)
    c.check('…and says to use an index', /index/i.test(String(ambiguous.message ?? '')), ambiguous.message)

    const badValue = await call(client, 'premiere_set_param', { clip: 'v0:0', component: 2, param: 0, value: { nope: 1 } })
    const rejected = badValue.error === true || /-32602|validation/i.test(String(badValue.raw ?? ''))
    c.check('a malformed value is rejected', rejected, badValue)

    c.section('cost')
    const t0 = Date.now()
    await call(client, 'premiere_get_sequence')
    const withParams = Date.now() - t0
    const t1 = Date.now()
    await call(client, 'premiere_get_sequence', { params: false })
    const without = Date.now() - t1
    c.note(`get_sequence: ${withParams}ms with params, ${without}ms without (one blurred clip)`)
    c.check('the param walk stays under a second', withParams < 1000, withParams)
  } finally {
    await close()
  }
  c.finish('T10 smoke')
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
