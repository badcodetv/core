import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { execFileSync } from 'node:child_process'
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { MeasurementsSchema, measure } from './measure'
import type { Measurements } from './types'

const SCRIPT = resolve(__dirname, '..', '..', '..', 'scripts', 'audio-measure.py')

const fixture: Measurements = {
  durationSec: 25,
  integratedLufs: -9.8,
  truePeakDbtp: -0.4,
  loudnessRangeLu: 5.1,
  channels: 2,
  stereoCorrelation: 0.62,
  sideToMidDb: -11.3,
  spectralCentroidHz: 2140.5,
  tempo: { bpm: 174.2, confidence: 'high' },
}

describe('MeasurementsSchema', () => {
  it('accepts a valid fixture', () => {
    expect(MeasurementsSchema.parse(fixture)).toEqual(fixture)
  })
  it('accepts nulls where the interface allows them', () => {
    const silent = { ...fixture, integratedLufs: null, truePeakDbtp: null, loudnessRangeLu: null, stereoCorrelation: null, sideToMidDb: null, tempo: { bpm: null, confidence: 'none' } }
    expect(MeasurementsSchema.safeParse(silent).success).toBe(true)
  })
  it('rejects a missing key', () => {
    const { spectralCentroidHz: _, ...missing } = fixture
    expect(MeasurementsSchema.safeParse(missing).success).toBe(false)
  })
  it('rejects an unknown tempo confidence', () => {
    expect(MeasurementsSchema.safeParse({ ...fixture, tempo: { bpm: 1, confidence: 'great' } }).success).toBe(false)
  })
})

describe('measure', () => {
  let dir: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'listen-measure-test-'))
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  it('parses what a script prints', async () => {
    const fake = join(dir, 'fake-ok.py')
    writeFileSync(fake, `import json\nprint(json.dumps(${JSON.stringify(fixture)}))\n`)
    await expect(measure('/x.wav', { script: fake })).resolves.toEqual(fixture)
  })

  it('throws MEASURE_FAILED with stderr when the script exits 1', async () => {
    const fake = join(dir, 'fake-fail.py')
    writeFileSync(fake, `import sys\nprint('librosa exploded', file=sys.stderr)\nsys.exit(1)\n`)
    await expect(measure('/x.wav', { script: fake })).rejects.toThrow(/^MEASURE_FAILED: .*librosa exploded/)
  })

  it('throws MEASURE_FAILED when the shape is wrong', async () => {
    const fake = join(dir, 'fake-shape.py')
    writeFileSync(fake, `print('{"durationSec": 1}')\n`)
    await expect(measure('/x.wav', { script: fake })).rejects.toThrow(/^MEASURE_FAILED/)
  })

  it('measures a generated stereo tone with the real script', async () => {
    const tone = join(dir, 'tone.wav')
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=3', '-ac', '2', tone])
    const m = await measure(tone, { script: SCRIPT })
    expect(m.channels).toBe(2)
    expect(m.durationSec).toBeCloseTo(3, 1)
  }, 60_000)
})
