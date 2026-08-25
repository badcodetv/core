import { describe, it, expect } from 'vitest'
import { normaliseSequence } from './normalise'
import type { Param } from './protocol'
import emptyDump from './fixtures/dump-empty.json'
import oneClipDump from './fixtures/dump-one-clip.json'

/**
 * `dump-empty.json` and `dump-one-clip.json` are REAL Premiere output, captured live by
 * `smoke-sequence.ts` (re-capture with `SMOKE_CAPTURE=1`). They are the guard against
 * normalising something that agrees with our idea of Premiere rather than with Premiere.
 *
 * Anything Premiere did not hand us on that run — transitions, keyframes, markers, malformed
 * dumps — is exercised with inline objects further down. Do not hand-edit the fixtures to add
 * those; capture a real one instead.
 */
describe('normaliseSequence — a real empty sequence', () => {
  const state = normaliseSequence(emptyDump)

  it('strips the \\\\?\\ prefix and translates the project path to WSL form', () => {
    expect(state.project.path).toBe('/mnt/d/badcode-videos/_smoke/t7-sequence.prproj')
  })

  it('keeps the sequence header intact', () => {
    expect(state.sequence).toMatchObject({ name: 's00-empty', frameSize: { w: 1920, h: 1080 }, end: 0 })
  })

  // Premiere snaps every edit to a frame boundary, so a caller that cannot see the rate cannot
  // predict where a clip will land. Derived from `timebase` (ticks per frame) here so it always
  // agrees with the sequence it came from.
  it('derives the frame rate from the timebase', () => {
    expect(state.sequence.timebase).toBe('10594584000')
    expect(state.sequence.frameRate).toBeCloseTo(23.976, 3)
  })

  it('labels tracks 1-based even though the API is 0-based', () => {
    expect(state.videoTracks.map((t) => t.label)).toEqual(['V1', 'V2', 'V3'])
    expect(state.videoTracks.map((t) => t.index)).toEqual([0, 1, 2])
    expect(state.audioTracks.map((t) => t.label)).toEqual(['A1', 'A2', 'A3', 'A4'])
  })

  it('has no clips anywhere', () => {
    expect(state.videoTracks.every((t) => t.items.length === 0)).toBe(true)
    expect(state.audioTracks.every((t) => t.items.length === 0)).toBe(true)
  })
})

describe('normaliseSequence — a real clip with its intrinsics', () => {
  const state = normaliseSequence(oneClipDump)
  const clip = state.videoTracks[0].items[0]

  it('assigns a ref from track and item index', () => {
    expect(clip.ref).toBe('v0:0')
  })

  it('reports this sequence as 25fps', () => {
    expect(state.sequence.frameRate).toBe(25)
  })

  it('reports times in seconds', () => {
    expect(clip).toMatchObject({ start: 0, end: 56, duration: 56, inPoint: 0, outPoint: 56, speed: 1 })
  })

  it('translates the media path to WSL form', () => {
    expect(clip.mediaPath).toBe('/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4')
  })

  // Order is Opacity THEN Motion — the reverse of how Premiere's Effect Controls panel shows it.
  it('carries both intrinsics, in chain order', () => {
    expect(clip.components.map((c) => [c.index, c.matchName, c.displayName])).toEqual([
      [0, 'AE.ADBE Opacity', 'Opacity'],
      [1, 'AE.ADBE Motion', 'Motion'],
    ])
  })

  // The wrapper `{ value: 100 }` that getValueAtTime returns must never reach the caller.
  it('unwraps param values', () => {
    const opacity = clip.components[0].params.find((p) => p.index === 0)
    expect(opacity).toMatchObject({ name: 'Opacity', value: 100, timeVarying: false })
  })

  it('keeps PointF params as normalised [x, y] arrays', () => {
    const position = clip.components[1].params.find((p) => p.name === 'Position')
    expect(position?.value).toEqual([0.5, 0.5]) // centre of frame, not pixels
  })

  // Two traps that make index the authoritative address, both from the live capture.
  it('preserves duplicate display names rather than collapsing them', () => {
    const blendModes = clip.components[0].params.filter((p) => p.name === 'Blend Mode')
    expect(blendModes.map((p) => p.index)).toEqual([1, 2])
  })

  it('preserves a blank display name', () => {
    expect(clip.components[1].params.find((p) => p.index === 3)?.name).toBe(' ')
  })

  it('gives an untransitioned clip an empty transitions object', () => {
    expect(clip.transitions).toEqual({})
  })
})

describe('normaliseSequence — keyframes', () => {
  const state = normaliseSequence({
    videoTracks: [
      {
        index: 0,
        items: [
          {
            start: 0,
            end: 4,
            components: [
              {
                index: 0,
                matchName: 'AE.ADBE Opacity',
                displayName: 'Opacity',
                params: [
                  {
                    index: 0,
                    name: 'Opacity',
                    value: 0,
                    timeVarying: true,
                    keyframes: [
                      { t: 0, value: 0 },
                      { t: 1, value: 100 },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  })

  it('keeps keyframes on a time-varying param', () => {
    const param = state.videoTracks[0].items[0].components[0].params[0]
    expect(param.timeVarying).toBe(true)
    expect(param.keyframes).toEqual([
      { t: 0, value: 0 },
      { t: 1, value: 100 },
    ])
  })

  it('omits the keyframes key entirely when the param is static', () => {
    const s = normaliseSequence({
      videoTracks: [{ items: [{ components: [{ params: [{ name: 'Scale', value: 100, timeVarying: false }] }] }] }],
    })
    expect('keyframes' in s.videoTracks[0].items[0].components[0].params[0]).toBe(false)
  })
})

describe('normaliseSequence — markers', () => {
  it('carries markers through', () => {
    const state = normaliseSequence({ markers: [{ name: 'beat', start: 3, duration: 0, comments: 'the turn' }] })
    expect(state.markers).toEqual([{ name: 'beat', start: 3, duration: 0, comments: 'the turn' }])
  })
})

// The return path of every mutating tool runs through here. A dump that is missing fields must
// degrade, never throw — otherwise one odd Premiere response takes down a call that succeeded.
describe('normaliseSequence — totality', () => {
  it('reports frameRate 0 rather than Infinity when the timebase is missing or nonsense', () => {
    expect(normaliseSequence({}).sequence.frameRate).toBe(0)
    expect(normaliseSequence({ sequence: { timebase: '0' } }).sequence.frameRate).toBe(0)
    expect(normaliseSequence({ sequence: { timebase: 'abc' } }).sequence.frameRate).toBe(0)
  })

  it('survives an empty object', () => {
    const state = normaliseSequence({})
    expect(state.videoTracks).toEqual([])
    expect(state.sequence.name).toBe('')
    expect(state.project.path).toBe('')
  })

  it.each([null, undefined, 42, 'nonsense', []])('survives %p', (input) => {
    expect(() => normaliseSequence(input)).not.toThrow()
  })

  it('fills missing clip fields with zeroes and nulls rather than throwing', () => {
    const state = normaliseSequence({ videoTracks: [{ items: [{}] }] })
    const clip = state.videoTracks[0].items[0]
    expect(clip).toMatchObject({ ref: 'v0:0', name: '', start: 0, end: 0, mediaPath: null, disabled: false })
    expect(clip.speed).toBe(1) // a missing speed is 1x, not 0x
  })

  it('falls back to positional indices when the dump omits them', () => {
    const state = normaliseSequence({ videoTracks: [{ items: [] }, { items: [] }] })
    expect(state.videoTracks.map((t) => t.index)).toEqual([0, 1])
    expect(state.videoTracks.map((t) => t.label)).toEqual(['V1', 'V2'])
  })

  it('treats a non-array components list as empty', () => {
    const state = normaliseSequence({ videoTracks: [{ items: [{ components: 'nope' }] }] })
    expect(state.videoTracks[0].items[0].components).toEqual([])
  })
})

describe('normaliseSequence — transitions', () => {
  const build = (tStart: number, tEnd: number) => ({
    videoTracks: [
      {
        index: 0,
        items: [
          { start: 0, end: 4 },
          { start: 4, end: 8 },
        ],
        transitions: [{ matchName: 'PR.ADBE Cross Dissolve', start: tStart, end: tEnd, duration: tEnd - tStart }],
      },
    ],
  })

  it('attaches a centred transition to both clips it sits between', () => {
    const [a, b] = normaliseSequence(build(3.5, 4.5)).videoTracks[0].items
    expect(a.transitions.end?.matchName).toBe('PR.ADBE Cross Dissolve')
    expect(a.transitions.end?.duration).toBe(1)
    expect(b.transitions.start?.matchName).toBe('PR.ADBE Cross Dissolve')
    expect(a.transitions.start).toBeUndefined()
    expect(b.transitions.end).toBeUndefined()
  })

  it('handles a start-at-cut alignment', () => {
    const [a, b] = normaliseSequence(build(4, 5)).videoTracks[0].items
    expect(a.transitions.end?.matchName).toBe('PR.ADBE Cross Dissolve')
    expect(b.transitions.start?.matchName).toBe('PR.ADBE Cross Dissolve')
  })

  it('handles an end-at-cut alignment', () => {
    const [a, b] = normaliseSequence(build(3, 4)).videoTracks[0].items
    expect(a.transitions.end?.matchName).toBe('PR.ADBE Cross Dissolve')
    expect(b.transitions.start?.matchName).toBe('PR.ADBE Cross Dissolve')
  })

  it('leaves clips untouched by a distant transition', () => {
    const [a, b] = normaliseSequence(build(6.5, 7)).videoTracks[0].items
    expect(a.transitions).toEqual({})
    expect(b.transitions.start).toBeUndefined()
  })

  it('gives audio clips no transitions field at all', () => {
    const state = normaliseSequence({ audioTracks: [{ index: 0, items: [{ start: 0, end: 1 }] }] })
    expect('transitions' in state.audioTracks[0].items[0]).toBe(false)
  })
})

describe('transitionCount', () => {
  /** Premiere hands back a null for every transition track item, so a count is the only
   * transition information there is. See docs/premiere/api-notes.md (T9). */
  it('carries the panel\'s count through', () => {
    const state = normaliseSequence({
      project: { name: 'p', path: 'D:\\x.prproj' },
      sequence: { name: 's', guid: 'g', timebase: '10594584000', frameSize: { w: 1920, h: 1080 }, end: 8, playhead: 0 },
      videoTracks: [{ index: 0, name: 'Video 1', muted: false, items: [], transitions: [], transitionCount: 2 }],
      audioTracks: [],
      markers: [],
    })
    expect(state.videoTracks[0].transitionCount).toBe(2)
  })

  it('is 0 when a dump does not mention it, rather than undefined', () => {
    const state = normaliseSequence({
      project: { name: 'p', path: 'D:\\x.prproj' },
      sequence: { name: 's', guid: 'g', timebase: '10594584000', frameSize: { w: 1920, h: 1080 }, end: 8, playhead: 0 },
      videoTracks: [{ index: 0, name: 'Video 1', muted: false, items: [] }],
      audioTracks: [],
      markers: [],
    })
    expect(state.videoTracks[0].transitionCount).toBe(0)
  })

  it('is 0 for the real captured fixtures, which carry no transitions', () => {
    const state = normaliseSequence(oneClipDump)
    expect(state.videoTracks.every((t) => t.transitionCount === 0)).toBe(true)
  })
})

describe('unreadable params', () => {
  /** 33 of Lumetri Color's 130 params refuse to yield a value by any route. The panel flags
   * them; the normaliser must carry the flag, because `value: null` alone is ambiguous —
   * a readable param may legitimately be null. */
  const dumpWith = (param: Record<string, unknown>): unknown => ({
    project: { name: 'p', path: 'D:\\x.prproj' },
    sequence: { name: 's', guid: 'g', timebase: '10594584000', frameSize: { w: 1920, h: 1080 }, end: 8, playhead: 0 },
    videoTracks: [
      {
        index: 0,
        name: 'Video 1',
        muted: false,
        transitionCount: 0,
        items: [
          {
            index: 0, name: 'clip', start: 0, end: 4, duration: 4, inPoint: 0, outPoint: 4,
            mediaPath: null, disabled: false, speed: 1,
            components: [{ index: 0, matchName: 'AE.ADBE Lumetri', displayName: 'Lumetri Color', params: [param] }],
          },
        ],
      },
    ],
    audioTracks: [],
    markers: [],
  })
  const first = (dump: unknown): Param => normaliseSequence(dump).videoTracks[0].items[0].components[0].params[0]

  it('carries the flag through', () => {
    const p = first(dumpWith({ index: 13, name: 'White Balance', value: null, timeVarying: false, unreadable: true }))
    expect(p.unreadable).toBe(true)
    expect(p.value).toBeNull()
    expect(p.name).toBe('White Balance')
  })

  it('leaves it unset for a param that simply reads as null', () => {
    const p = first(dumpWith({ index: 0, name: 'Opacity', value: null, timeVarying: false }))
    expect(p.unreadable).toBeUndefined()
    expect(p.value).toBeNull()
  })

  it('does not invent the flag from a falsy value', () => {
    const p = first(dumpWith({ index: 0, name: 'Rotation', value: 0, timeVarying: false }))
    expect(p.unreadable).toBeUndefined()
    expect(p.value).toBe(0)
  })
})
