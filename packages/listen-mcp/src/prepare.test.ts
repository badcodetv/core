import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { execFileSync } from 'node:child_process'
import { mkdtempSync, rmSync, existsSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { toLinuxPath, parseTime, validateRange, prepare } from './prepare'

describe('toLinuxPath', () => {
  it('maps a backslash Windows path onto /mnt', () => {
    expect(toLinuxPath('D:\\a\\b.mp3')).toBe('/mnt/d/a/b.mp3')
  })
  it('maps a forward-slash Windows path and lower-cases the drive', () => {
    expect(toLinuxPath('C:/Users/kai/x y.wav')).toBe('/mnt/c/Users/kai/x y.wav')
  })
  it('passes posix paths through', () => {
    expect(toLinuxPath('/mnt/d/a/b.mp3')).toBe('/mnt/d/a/b.mp3')
    expect(toLinuxPath('rel/b.mp3')).toBe('rel/b.mp3')
  })
})

describe('parseTime', () => {
  it('accepts numbers and numeric strings', () => {
    expect(parseTime(80)).toBe(80)
    expect(parseTime('80')).toBe(80)
    expect(parseTime('12.5')).toBe(12.5)
  })
  it('accepts M:SS, M:SS.s and H:MM:SS', () => {
    expect(parseTime('1:20')).toBe(80)
    expect(parseTime('1:20.5')).toBe(80.5)
    expect(parseTime('0:01:20')).toBe(80)
    expect(parseTime('1:02:05')).toBe(3725)
  })
  it.each(['', 'abc', '1:2:3:4', '1:75', '-5', '1:-2', 'NaN', '1::20'])('rejects %j', (t) => {
    expect(() => parseTime(t)).toThrow(/^RANGE_INVALID/)
  })
  it('rejects negative and non-finite numbers', () => {
    expect(() => parseTime(-1)).toThrow(/^RANGE_INVALID/)
    expect(() => parseTime(Infinity)).toThrow(/^RANGE_INVALID/)
  })
})

describe('validateRange', () => {
  it('is null when neither end is given', () => {
    expect(validateRange(100)).toBeNull()
  })
  it('defaults start to 0 and end to the duration', () => {
    expect(validateRange(100, undefined, 30)).toEqual({ start: 0, end: 30 })
    expect(validateRange(100, 20)).toEqual({ start: 20, end: 100 })
  })
  it('tolerates an end up to 50 ms past the duration', () => {
    expect(validateRange(100, 0, 100.04)).toEqual({ start: 0, end: 100.04 })
    expect(() => validateRange(100, 0, 100.1)).toThrow(/^RANGE_INVALID/)
  })
  it('rejects a negative start and an empty or inverted range', () => {
    expect(() => validateRange(100, -1, 10)).toThrow(/^RANGE_INVALID/)
    expect(() => validateRange(100, 10, 10)).toThrow(/^RANGE_INVALID/)
    expect(() => validateRange(100, 20, 10)).toThrow(/^RANGE_INVALID/)
  })
})

describe('prepare (ffmpeg)', () => {
  let dir: string
  let tone: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'listen-prepare-test-'))
    tone = join(dir, 'tone.wav')
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=5', '-ac', '2', tone])
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  const probe = (p: string, entries: string): string =>
    execFileSync('ffprobe', ['-v', 'error', '-show_entries', entries, '-of', 'csv=p=0', p], { encoding: 'utf8' }).trim()

  it('cuts a stereo wav and an mp3 of the range', async () => {
    const p = await prepare(tone, { start: 1, end: 3, tmpRoot: dir })
    try {
      expect(p.range).toEqual({ start: 1, end: 3 })
      expect(p.durationSec).toBeCloseTo(5, 1)
      expect(p.sha256).toMatch(/^[0-9a-f]{64}$/)
      expect(p.sourceName).toBe('tone.wav')
      expect(Math.abs(Number(probe(p.wavPath, 'format=duration')) - 2)).toBeLessThanOrEqual(0.05)
      expect(probe(p.wavPath, 'stream=channels')).toBe('2')
      expect(Number(probe(p.mp3Path, 'format=duration'))).toBeGreaterThan(1.9)
    } finally {
      await p.cleanup()
    }
    expect(existsSync(p.wavPath)).toBe(false)
  }, 60_000)

  it('keeps the whole file when no range is given', async () => {
    const p = await prepare(tone, { tmpRoot: dir })
    try {
      expect(p.range).toBeNull()
      expect(Math.abs(Number(probe(p.wavPath, 'format=duration')) - 5)).toBeLessThanOrEqual(0.05)
    } finally {
      await p.cleanup()
    }
  }, 60_000)

  it('throws FILE_NOT_FOUND for a missing file', async () => {
    await expect(prepare(join(dir, 'nope.mp3'))).rejects.toThrow(/^FILE_NOT_FOUND/)
  })

  it('throws RANGE_INVALID before cutting anything', async () => {
    await expect(prepare(tone, { start: 4, end: 9, tmpRoot: dir })).rejects.toThrow(/^RANGE_INVALID/)
  }, 60_000)
})
