/**
 * Tests for the state view.
 *
 * **The fixture is the real thing.** `state-camping.json.gz` is the exact `SequenceState` that
 * came back from Jack's hand-cut camping project on 2026-08-21 — 149 video clips, 135 audio
 * clips, 6,819 parameters, 573,065 bytes — gzipped because that is 12 KB on disk instead of 560.
 * Every size assertion below is measured against it rather than against something hand-written,
 * for the reason T7 learned the hard way: invented fixtures agree with whatever the code does.
 */
import { gunzipSync } from 'node:zlib'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'
import { describe, expect, it } from 'vitest'
import type { SequenceState } from './protocol'
import { DEFAULT_BUDGET, buildView, diffStates, fitToBudget, foldNoiseParams, type SequenceView } from './view'

const here = dirname(fileURLToPath(import.meta.url))

function camping(): SequenceState {
  return JSON.parse(gunzipSync(readFileSync(join(here, 'fixtures/state-camping.json.gz'))).toString()) as SequenceState
}

const size = (v: unknown): number => JSON.stringify(v).length

describe('the problem this file exists to solve', () => {
  it('a real hand-cut timeline does not fit through the transport', () => {
    // The regression guard. If this ever stops being true the whole design can be revisited;
    // until then it is the reason nothing returns a raw SequenceState.
    expect(size(camping())).toBeGreaterThan(500_000)
  })

  it('the same timeline as a digest fits in about a kilobyte', () => {
    const view = buildView(camping())
    // Deliberately tight. If a field is added that pushes the digest past this, that is worth
    // failing over — the whole design rests on the summary staying trivially small.
    expect(size(view)).toBeLessThan(2_500)
    expect(size(view)).toBeLessThan(size(camping()) / 100)
  })
})

describe('buildView — the digest', () => {
  it('describes every track without listing a single clip', () => {
    const view = buildView(camping())
    expect(view.videoTracks).toHaveLength(6)
    expect(view.audioTracks).toHaveLength(6)
    for (const t of [...view.videoTracks, ...view.audioTracks]) expect(t.clips).toBeUndefined()
  })

  it('carries the clip counts the raw state had', () => {
    const state = camping()
    const view = buildView(state)
    expect(view.videoTracks.map((t) => t.clipCount)).toEqual(state.videoTracks.map((t) => t.items.length))
    expect(view.totals.videoClips).toBe(149)
    expect(view.totals.audioClips).toBe(135)
    expect(view.totals.params).toBe(6819)
  })

  it('reports each track span, and null on an empty track', () => {
    const view = buildView(camping())
    // V1 is empty in Jack's cut; V3 is the spine.
    expect(view.videoTracks[0]?.clipCount).toBe(0)
    expect(view.videoTracks[0]?.span).toBeNull()
    const v3 = view.videoTracks[2]
    expect(v3?.clipCount).toBe(84)
    expect(v3?.span?.[0]).toBeCloseTo(0, 3)
    expect(v3?.span?.[1]).toBeGreaterThan(100)
  })

  it('keeps the mute flags, because half of camping is muted', () => {
    const view = buildView(camping())
    expect(view.audioTracks.filter((t) => t.muted).map((t) => t.label)).toEqual(['A2', 'A3', 'A4', 'A5'])
  })

  it('does not grow with the size of the edit', () => {
    // The property that makes the digest safe: bounded by tracks, not clips.
    const state = camping()
    const trimmed: SequenceState = {
      ...state,
      videoTracks: state.videoTracks.map((t) => ({ ...t, items: t.items.slice(0, 1) })),
      audioTracks: state.audioTracks.map((t) => ({ ...t, items: t.items.slice(0, 1) })),
    }
    const full = size(buildView(state))
    const tiny = size(buildView(trimmed))
    expect(Math.abs(full - tiny)).toBeLessThan(400)
  })

  it('survives a state with no tracks at all', () => {
    const empty: SequenceState = { ...camping(), videoTracks: [], audioTracks: [], markers: [] }
    const view = buildView(empty)
    expect(view.totals).toEqual({ videoClips: 0, audioClips: 0, components: 0, params: 0 })
    expect(view.markers).toEqual({ count: 0 })
  })
})

describe('buildView — selection', () => {
  it('expands only the track asked for', () => {
    const view = buildView(camping(), { tracks: ['v2'] })
    expect(view.videoTracks[2]?.clips).toHaveLength(84)
    expect(view.videoTracks[1]?.clips).toBeUndefined()
    expect(view.audioTracks).toHaveLength(6) // guard: an every() over [] passes vacuously
    expect(view.audioTracks.every((t) => t.clips === undefined)).toBe(true)
  })

  it('accepts the UI label and the API index as the same track', () => {
    // V3 (what Premiere shows) and v2 (what the API counts) must resolve identically.
    const byLabel = buildView(camping(), { tracks: ['V3'] })
    const byIndex = buildView(camping(), { tracks: ['v2'] })
    expect(byLabel.videoTracks[2]?.clips?.length).toBe(byIndex.videoTracks[2]?.clips?.length)
    expect(byLabel.videoTracks[2]?.clips?.length).toBe(84)
  })

  it('expands named clips, and their track only', () => {
    const view = buildView(camping(), { clips: ['v2:0', 'v2:1'] })
    expect(view.videoTracks[2]?.clips?.map((c) => c.ref)).toEqual(['v2:0', 'v2:1'])
    expect(view.videoTracks[3]?.clips).toBeUndefined()
  })

  it('expands a time window across every track', () => {
    const view = buildView(camping(), { range: [0, 10] })
    const listed = [...view.videoTracks, ...view.audioTracks].flatMap((t) => t.clips ?? [])
    expect(listed.length).toBeGreaterThan(0)
    for (const c of listed) {
      expect(c.start).toBeLessThan(10)
      expect(c.end).toBeGreaterThan(0)
    }
  })

  it('leaves a selected-but-empty track as a summary, not an empty list', () => {
    // "nothing here" and "you did not ask" must stay distinguishable.
    const view = buildView(camping(), { range: [1_000, 1_010] })
    expect(view.videoTracks).toHaveLength(6) // guard: an every() over [] passes vacuously
    expect(view.videoTracks.every((t) => t.clips === undefined)).toBe(true)
  })

  it('ignores a track that does not exist rather than throwing', () => {
    const view = buildView(camping(), { tracks: ['v99'] })
    expect(view.videoTracks).toHaveLength(6) // guard: an every() over [] passes vacuously
    expect(view.videoTracks.every((t) => t.clips === undefined)).toBe(true)
  })

  it('omits parameters when params is false, keeping the count', () => {
    const withParams = buildView(camping(), { tracks: ['a1'] })
    const without = buildView(camping(), { tracks: ['a1'], params: false })
    expect(size(without)).toBeLessThan(size(withParams))
    const comp = without.audioTracks[1]?.clips?.[0]?.components?.[1]
    expect(comp?.params).toBeUndefined()
    expect(comp?.paramCount).toBe(33)
  })
})

describe('foldNoiseParams', () => {
  it('folds away the 30 blank channel slots Premiere pads a stereo clip with', () => {
    const state = camping()
    const channelVolume = (state.audioTracks[1]?.items[0]?.components ?? []).find(
      (c) => c.matchName === 'Internal Channel Volume Stereo'
    )
    expect(channelVolume?.params).toHaveLength(33)

    const folded = foldNoiseParams(channelVolume!.params)
    expect(folded.omitted).toBe(30)
    expect(folded.params.map((p) => p.name)).toEqual(['Bypass', 'Left', 'Right'])
  })

  it('keeps a param whose name is a single space — that is Uniform Scale, not padding', () => {
    // AE.ADBE Motion index 3 is named " ". It is a real control and must survive.
    const params = [
      { index: 0, name: 'Scale', value: 100 },
      { index: 1, name: ' ', value: 100 },
    ]
    const folded = foldNoiseParams(params)
    expect(folded.omitted).toBe(0)
    expect(folded.params).toHaveLength(2)
  })

  it('keeps a blank-named param carrying a value no named param has', () => {
    const params = [
      { index: 0, name: 'Left', value: 0.5 },
      { index: 1, name: '', value: 0.5 },
      { index: 2, name: '', value: 0.9 },
    ]
    const folded = foldNoiseParams(params)
    expect(folded.omitted).toBe(1)
    expect(folded.params.map((p) => p.index)).toEqual([0, 2])
  })

  it('shows up as omittedParams on the component, so nothing vanishes silently', () => {
    const view = buildView(camping(), { clips: ['a1:0'] })
    const comp = view.audioTracks[1]?.clips?.[0]?.components?.[1]
    expect(comp?.displayName).toBe('Channel Volume')
    expect(comp?.omittedParams).toBe(30)
  })
})

describe('fitToBudget', () => {
  it('leaves a view that already fits completely alone', () => {
    const view = buildView(camping())
    expect(fitToBudget(view)).toBe(view)
  })

  it('always fits, whatever it is handed', () => {
    // Every selection that could plausibly be asked for, including the worst one.
    const selections = [
      {},
      { tracks: ['v2'] },
      { tracks: ['v2', 'v3', 'a1', 'a2'] },
      { range: [0, 220] as [number, number] },
      { tracks: ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5'] },
    ]
    for (const selection of selections) {
      const fitted = fitToBudget(buildView(camping(), selection))
      expect(size(fitted)).toBeLessThanOrEqual(DEFAULT_BUDGET)
    }
  })

  it('says what it dropped and where the rest is', () => {
    const view = buildView(camping(), { tracks: ['a1'] })
    view.statePath = '/mnt/d/badcode-videos/camping/.bridge/state-camping.json'
    const fitted = fitToBudget(view)
    expect(fitted.notes?.length).toBeGreaterThan(0)
    expect(fitted.notes?.join(' ')).toContain('/mnt/d/badcode-videos/camping/.bridge/state-camping.json')
  })

  it('gives up parameters before it gives up clips, and counts what it dropped', () => {
    // The ladder's ordering is the whole point: a caller asking for one track wants its clips.
    // Measured on this fixture: 82,813 bytes whole → 32,833 without params → 19,645 without
    // chains, so v2 lands on rung 2 and every clip must survive with its component count intact.
    const clips = fitToBudget(buildView(camping(), { tracks: ['v2'] })).videoTracks[2]?.clips
    expect(clips).toHaveLength(84)
    expect(clips!.every((c) => c.components === undefined)).toBe(true)
    // Nothing vanishes silently: the count of what was dropped is still there.
    expect(clips!.every((c) => typeof c.componentCount === 'number')).toBe(true)
    expect(clips![0]?.componentCount).toBe(2)
    // …and the times, the whole reason for asking, are untouched.
    expect(clips![0]?.start).toBeCloseTo(0, 6)
  })

  it('falls all the way back to the digest when even the clips will not fit', () => {
    const everything = { tracks: ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5'] }
    const fitted = fitToBudget(buildView(camping(), everything))
    const tracks = [...fitted.videoTracks, ...fitted.audioTracks]
    expect(tracks).toHaveLength(12) // guard: an every() over [] passes vacuously
    expect(tracks.every((t) => t.clips === undefined)).toBe(true)
    // …and still reports the shape of the timeline it could not spell out.
    expect(fitted.totals.videoClips).toBe(149)
    expect(fitted.notes?.join(' ')).toContain('tracks')
  })

  it('respects a smaller budget', () => {
    const fitted = fitToBudget(buildView(camping()), 100_000)
    expect(size(fitted)).toBeLessThanOrEqual(100_000)
  })
})

describe('diffStates', () => {
  const move = (state: SequenceState, ref: string, delta: number): SequenceState => ({
    ...state,
    videoTracks: state.videoTracks.map((t) => ({
      ...t,
      items: t.items.map((c) => (c.ref === ref ? { ...c, start: c.start + delta, end: c.end + delta } : c)),
    })),
  })

  it('returns nothing when there is no previous state to compare against', () => {
    expect(diffStates(null, camping())).toBeUndefined()
  })

  it('reports no changes between a state and itself', () => {
    const state = camping()
    expect(diffStates(state, state)).toEqual({ added: [], removed: [], modified: [] })
  })

  it('finds a moved clip and reports where it was and where it is', () => {
    const before = camping()
    const after = move(before, 'v2:5', 3)
    const diff = diffStates(before, after)
    expect(diff?.modified).toHaveLength(1)
    expect(diff?.modified[0]?.ref).toBe('v2:5')
    expect(diff?.modified[0]?.now.start).toBeCloseTo((diff?.modified[0]?.was.start ?? 0) + 3, 6)
  })

  it('finds an added clip — which is how insert_clip learns its own ref', () => {
    const before = camping()
    const newClip = { ...before.videoTracks[5]!.items[0]!, ref: 'v5:3', name: 'brand-new.mp4' }
    const after: SequenceState = {
      ...before,
      videoTracks: before.videoTracks.map((t, i) => (i === 5 ? { ...t, items: [...t.items, newClip] } : t)),
    }
    const diff = diffStates(before, after)
    expect(diff?.added.map((c) => c.ref)).toEqual(['v5:3'])
    expect(diff?.added[0]?.name).toBe('brand-new.mp4')
  })

  it('finds a removed clip', () => {
    const before = camping()
    const after: SequenceState = {
      ...before,
      videoTracks: before.videoTracks.map((t, i) => (i === 5 ? { ...t, items: t.items.slice(0, -1) } : t)),
    }
    const diff = diffStates(before, after)
    expect(diff?.removed).toHaveLength(1)
    expect(diff?.removed[0]?.ref).toBe('v5:2')
  })

  it('ignores float noise below a fraction of a frame', () => {
    const before = camping()
    const after = move(before, 'v2:5', 1e-9)
    expect(diffStates(before, after)?.modified).toHaveLength(0)
  })

  it('caps how much of a huge ripple it spells out, and says it capped', () => {
    const before = camping()
    // A ripple that shifts every clip on the busiest track.
    const after: SequenceState = {
      ...before,
      videoTracks: before.videoTracks.map((t, i) =>
        i === 2 ? { ...t, items: t.items.map((c) => ({ ...c, start: c.start + 1, end: c.end + 1 })) } : t
      ),
    }
    const diff = diffStates(before, after)
    expect(diff?.modified.length).toBe(40)
    expect(diff?.more?.modified).toBe(84)
  })

  it('refuses to compare two different sequences', () => {
    const before = camping()
    const after: SequenceState = { ...before, sequence: { ...before.sequence, guid: 'a-different-guid' } }
    expect(diffStates(before, after)).toBeUndefined()
  })

  it('a change report still fits the budget on a whole-track ripple', () => {
    const before = camping()
    const after: SequenceState = {
      ...before,
      videoTracks: before.videoTracks.map((t, i) =>
        i === 2 ? { ...t, items: t.items.map((c) => ({ ...c, start: c.start + 1, end: c.end + 1 })) } : t
      ),
    }
    const view: SequenceView = buildView(after)
    view.changed = diffStates(before, after)
    expect(size(fitToBudget(view))).toBeLessThanOrEqual(DEFAULT_BUDGET)
  })
})
