import { describe, it, expect } from 'vitest'
import {
  CMD_NAMES,
  CmdArgsSchemas,
  CmdResultSchemas,
  CmdSchema,
  ErrorCodeSchema,
  HelloSchema,
  IncomingFrameSchema,
  LogSchema,
  ResultSchema,
  coerceParamValue,
  type CmdArgs,
  type CmdResult,
  type SequenceState,
} from './protocol'

const clip = 'v0:0'

const sequenceStateFixture: SequenceState = {
  project: { name: 'gitpush-origin-master', path: '/mnt/d/badcode-videos/gitpush-origin-master/gitpush-origin-master.prproj' },
  sequence: { name: 's00', guid: '{1234-GUID}', timebase: '10160640000', frameRate: 25, frameSize: { w: 1920, h: 1080 }, end: 12.5, playhead: 0 },
  videoTracks: [
    {
      index: 0,
      label: 'V1',
      name: 'Video 1',
      muted: false,
      transitionCount: 0,
      items: [
        {
          ref: 'v0:0',
          name: 'clip-a.mp4',
          start: 0,
          end: 5,
          duration: 5,
          inPoint: 0,
          outPoint: 5,
          mediaPath: '/mnt/d/badcode-videos/gitpush-origin-master/s00/final/clip-a.mp4',
          disabled: false,
          speed: 1,
          components: [
            {
              index: 0,
              matchName: 'AE.ADBE Motion',
              displayName: 'Motion',
              params: [{ index: 0, name: 'Scale', value: 100, timeVarying: false }],
            },
          ],
          transitions: {},
        },
      ],
    },
  ],
  audioTracks: [{ index: 0, label: 'A1', name: 'Audio 1', muted: false, items: [], transitionCount: 0 }],
  markers: [{ name: 'beat', start: 3, duration: 0, comments: '' }],
}

// One realistic fixture per command — the round-trip test below is the contract that every
// entry here matches its schema in CmdArgsSchemas/CmdResultSchemas.
const argsFixtures: CmdArgs = {
  status: {},
  open_project: { path: 'D:\\badcode-videos\\gpom\\gpom.prproj', create: false },
  save: {},
  import: { paths: ['/mnt/c/Users/kai/Desktop/s00/final/a.mp4'], bin: 's00' },
  list_items: { bin: 's00' },
  create_sequence: { name: 's00', preset: 'C:\\preset.sqpreset', fromItems: ['a.mp4'] },
  list_sequences: {},
  set_active: { name: 's00' },
  get_sequence: { name: 's00' },
  insert_clip: { item: 'a.mp4', time: 0, videoTrack: 0, audioTrack: 0, mode: 'overwrite', limitShift: false },
  move_clip: { clip, deltaSeconds: 2 },
  trim_clip: { clip, inPoint: 0, outPoint: 4 },
  remove_clip: { clips: [clip], ripple: true },
  clone_clip: { clip, deltaSeconds: 10, videoTrackOffset: 0, audioTrackOffset: 0, mode: 'insert' },
  list_transitions: { query: 'dissolve' },
  add_transition: { clip, matchName: 'Cross Dissolve', at: 'start', duration: 1, alignment: 0.5 },
  remove_transition: { clip, at: 'start' },
  list_effects: { query: 'blur' },
  describe_effect: { clip, component: 'Gaussian Blur (Legacy)' },
  apply_effect: { clip, matchName: 'Gaussian Blur', params: { Blurriness: 20 }, index: 0 },
  set_param: { clip, component: 'Gaussian Blur', param: 'Blurriness', value: 40, time: 2, interpolation: 'bezier' },
  remove_effect: { clip, component: 0 },
  insert_mogrt: { path: 'C:\\mogrts\\title.mogrt', time: 5, videoTrack: 1, audioTrack: 0 },
  add_marker: { name: 'beat', time: 3, duration: 0, comments: 'hit' },
  set_playhead: { time: 1.5 },
  export_frame: { time: 1.5, dir: 'D:\\badcode-videos\\x\\frames', filename: 's00-1.5s.png', width: 1920, height: 1080 },
  export_sequence: { outputFile: 'D:\\badcode-videos\\x\\renders\\s00.mp4', preset: 'C:\\preset.epr', exportFull: true },
  eval: { code: 'return 1', timeoutMs: 5000 },
  ping: {},
}

const resultFixtures: CmdResult = {
  status: {
    connected: true,
    appVersion: '26.3.2',
    project: { name: 's00', path: '/mnt/d/badcode-videos/gitpush-origin-master/gitpush-origin-master.prproj' },
    activeSequence: 's00',
    mediaRoot: 'D:\\badcode-videos',
  },
  open_project: { project: { name: 'gpom', path: '/mnt/d/badcode-videos/gpom/gpom.prproj' }, created: true, sequences: ['s00'] },
  save: { path: '/mnt/d/badcode-videos/gpom/gpom.prproj' },
  import: { items: [{ id: '1', name: 'a.mp4', mediaPath: '/mnt/c/Users/kai/Desktop/s00/final/a.mp4' }], bin: 's00' },
  list_items: {
    items: [{ id: '1', name: 'a.mp4', type: 'clip', mediaPath: '/mnt/c/Users/kai/Desktop/s00/final/a.mp4', bin: 's00' }],
  },
  create_sequence: sequenceStateFixture,
  list_sequences: { sequences: [{ name: 's00', guid: '{1234-GUID}', active: true }] },
  set_active: sequenceStateFixture,
  get_sequence: sequenceStateFixture,
  insert_clip: sequenceStateFixture,
  move_clip: sequenceStateFixture,
  trim_clip: sequenceStateFixture,
  remove_clip: sequenceStateFixture,
  clone_clip: sequenceStateFixture,
  list_transitions: { transitions: [{ matchName: 'Cross Dissolve' }] },
  add_transition: sequenceStateFixture,
  remove_transition: sequenceStateFixture,
  list_effects: { effects: [{ matchName: 'AE.ADBE Gaussian Blur', displayName: 'Gaussian Blur' }] },
  describe_effect: {
    matchName: 'AE.ADBE Gaussian Blur 2',
    displayName: 'Gaussian Blur (Legacy)',
    componentIndex: 2,
    params: [{ index: 0, name: 'Blurriness', value: 20, keyframable: true, timeVarying: false }],
  },
  apply_effect: sequenceStateFixture,
  set_param: sequenceStateFixture,
  remove_effect: sequenceStateFixture,
  insert_mogrt: sequenceStateFixture,
  add_marker: sequenceStateFixture,
  set_playhead: { playhead: 1.5 },
  export_frame: { path: 'D:\\badcode-videos\\gpom\\frames\\s00-1.5s.png', time: 1.5, width: 1920, height: 1080, sequence: 's00' },
  export_sequence: { path: 'D:\\badcode-videos\\gpom\\renders\\s00-20260821-1200.mp4', sequence: 's00', exportFull: true },
  eval: { value: 1, logs: ['starting'] },
  ping: { appVersion: '26.3.2', project: { name: 'gpom', path: 'D:\\badcode-videos\\gpom\\gpom.prproj' }, sequence: 's00' },
}

describe('CmdArgsSchemas / CmdResultSchemas', () => {
  it.each(CMD_NAMES)('round-trips the %s fixture', (name) => {
    expect(() => CmdArgsSchemas[name].parse(argsFixtures[name])).not.toThrow()
    expect(() => CmdResultSchemas[name].parse(resultFixtures[name])).not.toThrow()
  })
})

describe('ErrorCodeSchema', () => {
  it('includes BAD_CONFIG alongside the panel/bridge error codes', () => {
    expect(ErrorCodeSchema.options).toContain('BAD_CONFIG')
    expect(ErrorCodeSchema.options).toContain('PANEL_NOT_CONNECTED')
    expect(ErrorCodeSchema.options).toContain('TIMEOUT')
  })
})

describe('envelope schemas', () => {
  it('parses a Hello frame', () => {
    const hello = { type: 'hello', appVersion: '26.3.2', panelVersion: '0.1.0', protocol: 1 }
    expect(HelloSchema.parse(hello)).toEqual(hello)
  })

  it('parses a Cmd frame and rejects an unknown cmd name', () => {
    expect(() => CmdSchema.parse({ type: 'cmd', id: 'c1', cmd: 'ping', args: {} })).not.toThrow()
    expect(() => CmdSchema.parse({ type: 'cmd', id: 'c1', cmd: 'not_a_real_command', args: {} })).toThrow()
  })

  it('parses an ok Result frame', () => {
    const result = { type: 'result', id: 'c1', ok: true, result: { appVersion: '26.3.2' } }
    expect(ResultSchema.parse(result)).toEqual(result)
  })

  it('parses an error Result frame', () => {
    const result = { type: 'result', id: 'c1', ok: false, code: 'TIMEOUT', message: 'timed out' }
    expect(ResultSchema.parse(result)).toEqual(result)
  })

  it('parses a Log frame', () => {
    const log = { type: 'log', level: 'warn', message: 'heads up' }
    expect(LogSchema.parse(log)).toEqual(log)
  })

  it('IncomingFrameSchema accepts hello, ok result, error result and log', () => {
    expect(() => IncomingFrameSchema.parse({ type: 'hello', appVersion: '1', panelVersion: '1', protocol: 1 })).not.toThrow()
    expect(() => IncomingFrameSchema.parse({ type: 'result', id: 'c1', ok: true, result: null })).not.toThrow()
    expect(() => IncomingFrameSchema.parse({ type: 'result', id: 'c1', ok: false, code: 'PANEL_ERROR', message: 'oops' })).not.toThrow()
    expect(() => IncomingFrameSchema.parse({ type: 'log', level: 'info', message: 'hi' })).not.toThrow()
  })

  it('IncomingFrameSchema rejects a cmd frame (that direction never flows panel -> bridge) and unknown shapes', () => {
    expect(() => IncomingFrameSchema.parse({ type: 'cmd', id: 'c1', cmd: 'ping', args: {} })).toThrow()
    expect(() => IncomingFrameSchema.parse({ type: 'mystery', foo: 'bar' })).toThrow()
    expect(() => IncomingFrameSchema.parse('not even an object')).toThrow()
  })
})

describe('coerceParamValue', () => {
  it('accepts a number, string and boolean', () => {
    expect(coerceParamValue(20)).toBe(20)
    expect(coerceParamValue('hold')).toBe('hold')
    expect(coerceParamValue(true)).toBe(true)
  })

  it('accepts a plain {x,y} object (PointF shape)', () => {
    expect(coerceParamValue({ x: 0.5, y: 0.25 })).toEqual({ x: 0.5, y: 0.25 })
  })

  it('accepts a plain {r,g,b,a?} object (Color shape), alpha optional', () => {
    expect(coerceParamValue({ r: 255, g: 0, b: 0 })).toEqual({ r: 255, g: 0, b: 0 })
    expect(coerceParamValue({ r: 255, g: 0, b: 0, a: 128 })).toEqual({ r: 255, g: 0, b: 0, a: 128 })
  })

  it('does not construct a ppro type — the result is always plain data', () => {
    const v = coerceParamValue({ x: 1, y: 2 })
    expect(v).toEqual({ x: 1, y: 2 })
    expect(Object.getPrototypeOf(v)).toBe(Object.prototype)
  })

  it('rejects a shape that matches neither number/string/boolean/PointF/Color', () => {
    expect(() => coerceParamValue({ foo: 1 })).toThrow()
    expect(() => coerceParamValue(null)).toThrow()
    expect(() => coerceParamValue([1, 2])).toThrow()
    expect(() => coerceParamValue(undefined)).toThrow()
  })
})
