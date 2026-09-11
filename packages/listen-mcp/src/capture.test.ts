import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { execFileSync, spawn, type ChildProcess } from 'node:child_process'
import { createHash } from 'node:crypto'
import { appendFileSync, existsSync, mkdtempSync, readFileSync, rmSync, statSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import {
  PREVIEW_FILTER,
  sinkName,
  parseSinks,
  parseShortSinks,
  parseSinkInputs,
  parsePsPairs,
  descendantsOf,
  parseMaxVolume,
  parseSilenceEnd,
  wavDataOffset,
  nullSinkArgs,
  loopbackArgs,
  recordArgs,
  previewArgs,
  trimArgs,
  waitForAudio,
  firstSoundAt,
  isSilent,
  trim,
  makePreview,
  ensureSink,
  removeSink,
  pinVolume,
  moveChromeStreams,
  startRecording,
} from './capture'

// ── fixtures: real output captured on 2026-09-11 (WSLg PulseAudio, ffmpeg 4.4) ─────────────────

/** `pactl list short sinks` with a temporary null sink loaded. */
const SHORT_SINKS = `1\tRDPSink\tmodule-rdp-sink.c\ts16le 2ch 44100Hz\tSUSPENDED
7\tbadcode_fixture_1136272\tmodule-null-sink.c\ts16le 2ch 44100Hz\tRUNNING
`

/** `pactl list sink-inputs` while `paplay --device=badcode_fixture_1136272 tone.wav` ran. */
const SINK_INPUT_PAPLAY = `Sink Input #37
\tDriver: protocol-native.c
\tOwner Module: 21
\tClient: 120
\tSink: 7
\tSample Specification: s16le 2ch 44100Hz
\tChannel Map: front-left,front-right
\tFormat: pcm, format.sample_format = "\\"s16le\\""  format.rate = "44100"  format.channels = "2"  format.channel_map = "\\"front-left,front-right\\""
\tCorked: no
\tMute: no
\tVolume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
\t        balance 0.00
\tBuffer Latency: 2000000 usec
\tSink Latency: 993898 usec
\tResample method: n/a
\tProperties:
\t\tmedia.software = "Lavf58.76.100"
\t\tmedia.format = "WAV (Microsoft)"
\t\tapplication.name = "paplay"
\t\tmedia.name = "tone.wav"
\t\tnative-protocol.peer = "UNIX socket client"
\t\tnative-protocol.version = "35"
\t\tapplication.process.id = "1136341"
\t\tapplication.process.user = "kai"
\t\tapplication.process.host = "phat"
\t\tapplication.process.binary = "pacat"
\t\tapplication.language = "C.UTF-8"
\t\twindow.x11.display = ":0"
\t\tapplication.process.machine_id = "62b96989895d419d8e9a4325dfd7285f"
\t\tmodule-stream-restore.id = "sink-input-by-application-name:paplay"
`

/** The same real block again, as a second stream on the RDP sink with no process id reported. */
const SINK_INPUT_NO_PID = SINK_INPUT_PAPLAY.replace('#37', '#38')
  .replace('Sink: 7', 'Sink: 1')
  .replace(/^\t\tapplication\.process\.id = .*\n/m, '')

/** ffmpeg -af volumedetect stderr tail, 2 s of digital silence. */
const VOLUMEDETECT_SILENT = `size=N/A time=00:00:01.99 bitrate=N/A speed= 944x
video:0kB audio:345kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
[Parsed_volumedetect_0 @ 0x63f02fae1180] n_samples: 176400
[Parsed_volumedetect_0 @ 0x63f02fae1180] mean_volume: -91.0 dB
[Parsed_volumedetect_0 @ 0x63f02fae1180] max_volume: -91.0 dB
[Parsed_volumedetect_0 @ 0x63f02fae1180] histogram_91db: 176400
`

/** ffmpeg -af volumedetect stderr tail, 1 s silence then a 1 kHz tone. */
const VOLUMEDETECT_TONE = `[Parsed_volumedetect_0 @ 0x5b847dcfc180] n_samples: 264600
[Parsed_volumedetect_0 @ 0x5b847dcfc180] mean_volume: -25.8 dB
[Parsed_volumedetect_0 @ 0x5b847dcfc180] max_volume: -20.6 dB
[Parsed_volumedetect_0 @ 0x5b847dcfc180] histogram_20db: 13200
`

/** silencedetect=n=-60dB:d=0.05 on 1 s silence then a 2 s tone. */
const SILENCE_LEADING = `  Stream #0:0: Audio: pcm_s16le, 44100 Hz, stereo, s16, 1411 kb/s
[silencedetect @ 0x644908af01c0] silence_start: 0
[silencedetect @ 0x644908af01c0] silence_end: 1.00002 | silence_duration: 1.00002
size=N/A time=00:00:02.99 bitrate=N/A speed=1.36e+03x
`

/** silencedetect on 2 s of pure silence: the end is reported at EOF. */
const SILENCE_ALL = `[silencedetect @ 0x61b68f6dc1c0] silence_start: 0
size=N/A time=00:00:01.99 bitrate=N/A speed= 872x
video:0kB audio:345kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
[silencedetect @ 0x61b68f6dc1c0] silence_end: 2 | silence_duration: 2
`

/** silencedetect on a tone that starts at 0: the filter prints nothing. */
const SILENCE_NONE = `size=N/A time=00:00:01.99 bitrate=N/A speed= 776x
video:0kB audio:345kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
`

/** `ps -e -o pid=,ppid=` shape (right-aligned); a chrome-like tree under 5000. */
const PS = `      1       0
      2       1
   5000       1
   5001    5000
   5002    5001
   5003    5000
   6000       1
   6001    6000
`

// ── pure ───────────────────────────────────────────────────────────────────────────────────────

describe('constants', () => {
  it('PREVIEW_FILTER is exactly the string in decision 9', () => {
    expect(PREVIEW_FILTER).toBe('lowpass=f=8000:poles=2,lowpass=f=8000:poles=2')
  })
  it('sinkName', () => {
    expect(sinkName(3)).toBe('badcode_ch3')
  })
})

describe('parseSinks / parseShortSinks', () => {
  it('reads names and indexes from real pactl output', () => {
    expect(parseSinks(SHORT_SINKS)).toEqual(['RDPSink', 'badcode_fixture_1136272'])
    expect(parseShortSinks(SHORT_SINKS)).toEqual([
      { index: 1, name: 'RDPSink' },
      { index: 7, name: 'badcode_fixture_1136272' },
    ])
  })
  it('empty output → no sinks', () => {
    expect(parseSinks('')).toEqual([])
  })
})

describe('parseSinkInputs', () => {
  it('reads index, sink and process id from a real block', () => {
    expect(parseSinkInputs(SINK_INPUT_PAPLAY)).toEqual([{ index: 37, sink: 7, pid: 1136341 }])
  })
  it('splits several blocks; a missing process id is null', () => {
    expect(parseSinkInputs(SINK_INPUT_PAPLAY + '\n' + SINK_INPUT_NO_PID)).toEqual([
      { index: 37, sink: 7, pid: 1136341 },
      { index: 38, sink: 1, pid: null },
    ])
  })
  it('no streams → empty', () => {
    expect(parseSinkInputs('')).toEqual([])
  })
})

describe('descendantsOf', () => {
  it('finds the whole tree under a pid, and nothing beside it', () => {
    const fam = descendantsOf(5000, parsePsPairs(PS))
    expect([...fam].sort()).toEqual([5000, 5001, 5002, 5003])
  })
  it('a pid with no children is just itself', () => {
    expect([...descendantsOf(6001, parsePsPairs(PS))]).toEqual([6001])
  })
})

describe('parseMaxVolume', () => {
  it('max_volume: -91.0 dB (digital silence) → -91, which is silent (<= -80)', () => {
    const v = parseMaxVolume(VOLUMEDETECT_SILENT)
    expect(v).toBe(-91)
    expect(v! <= -80).toBe(true)
  })
  it('a tone → -20.6', () => {
    expect(parseMaxVolume(VOLUMEDETECT_TONE)).toBe(-20.6)
  })
  it('-inf and absent', () => {
    expect(parseMaxVolume('max_volume: -inf dB')).toBe(-Infinity)
    expect(parseMaxVolume(SILENCE_NONE)).toBeNull()
  })
})

describe('parseSilenceEnd', () => {
  it('leading silence → its end', () => {
    expect(parseSilenceEnd(SILENCE_LEADING)).toBeCloseTo(1.00002, 5)
  })
  it('no silence → null', () => {
    expect(parseSilenceEnd(SILENCE_NONE)).toBeNull()
  })
  it('all silent → the EOF end (isSilent owns that case)', () => {
    expect(parseSilenceEnd(SILENCE_ALL)).toBe(2)
  })
  it('a start within 0.01 s of 0 counts as leading; later silence does not', () => {
    expect(parseSilenceEnd('silence_start: 0.00498\nsilence_end: 0.8 | silence_duration: 0.795')).toBe(0.8)
    expect(parseSilenceEnd('silence_start: 12.5\nsilence_end: 13 | silence_duration: 0.5')).toBeNull()
  })
})

describe('command builders', () => {
  it('null sink and loopback', () => {
    expect(nullSinkArgs('badcode_ch2')).toEqual([
      'load-module', 'module-null-sink', 'sink_name=badcode_ch2', 'sink_properties=device.description=badcode_ch2',
    ])
    expect(loopbackArgs('badcode_ch2')).toEqual([
      'load-module', 'module-loopback', 'source=badcode_ch2.monitor', 'sink=@DEFAULT_SINK@', 'latency_msec=60',
    ])
  })
  it('record reads the monitor at 44.1 kHz stereo', () => {
    expect(recordArgs('badcode_ch2', '/x/raw.wav')).toEqual([
      '-v', 'error', '-y', '-f', 'pulse', '-fragment_size', '4096', '-i', 'badcode_ch2.monitor',
      '-ac', '2', '-ar', '44100', '-flush_packets', '1', '/x/raw.wav',
    ])
  })
  it('preview carries the filter and 320k mp3; trim does not filter', () => {
    const p = previewArgs('/x/raw.wav', '/x/p.mp3')
    expect(p[p.indexOf('-af') + 1]).toBe(PREVIEW_FILTER)
    expect(p.slice(-5)).toEqual(['-c:a', 'libmp3lame', '-b:a', '320k', '/x/p.mp3'])
    expect(trimArgs('/x/a.wav', 1.5, 30, '/x/b.wav')).not.toContain('-af')
  })
})

describe('wavDataOffset', () => {
  it('finds the data chunk in a real ffmpeg header (longer than 44 bytes)', () => {
    const dir = mkdtempSync(join(tmpdir(), 'capture-hdr-'))
    try {
      const f = join(dir, 'a.wav')
      execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '0.1', f])
      const buf = readFileSync(f)
      const off = wavDataOffset(buf)
      expect(off).not.toBeNull()
      expect(buf.subarray(off! - 8, off! - 4).toString()).toBe('data')
      expect(wavDataOffset(buf.subarray(0, off! - 4))).toBeNull()
    } finally {
      rmSync(dir, { recursive: true, force: true })
    }
  })
  it('not a wav → null', () => {
    expect(wavDataOffset(new Uint8Array(100))).toBeNull()
  })
})

// ── offline, with generated files ──────────────────────────────────────────────────────────────

function header(dataLen = 0): Buffer {
  const h = Buffer.alloc(44)
  h.write('RIFF', 0)
  h.writeUInt32LE(36 + dataLen, 4)
  h.write('WAVE', 8)
  h.write('fmt ', 12)
  h.writeUInt32LE(16, 16)
  h.writeUInt16LE(1, 20)
  h.writeUInt16LE(2, 22)
  h.writeUInt32LE(44100, 24)
  h.writeUInt32LE(44100 * 4, 28)
  h.writeUInt16LE(4, 32)
  h.writeUInt16LE(16, 34)
  h.write('data', 36)
  h.writeUInt32LE(dataLen, 40)
  return h
}

describe('waitForAudio (the startRecording gate)', () => {
  let dir: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'capture-wait-'))
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  it('does not resolve on a bare header; resolves once samples follow it', async () => {
    const f = join(dir, 'grow.wav')
    writeFileSync(f, header())
    let resolvedAt = 0
    const started = Date.now()
    const p = waitForAudio(f, { timeoutMs: 3000, pollMs: 20 }).then(() => {
      resolvedAt = Date.now()
    })
    await new Promise((r) => setTimeout(r, 300))
    expect(resolvedAt).toBe(0)
    appendFileSync(f, Buffer.alloc(4096))
    await p
    expect(resolvedAt - started).toBeGreaterThanOrEqual(290)
  })
  it('throws CAPTURE_NOT_STARTED when only the header ever arrives', async () => {
    const f = join(dir, 'stuck.wav')
    writeFileSync(f, header())
    await expect(waitForAudio(f, { timeoutMs: 200, pollMs: 20 })).rejects.toThrow(/^CAPTURE_NOT_STARTED/)
  })
  it('throws CAPTURE_NOT_STARTED at once when the writer died', async () => {
    await expect(waitForAudio(join(dir, 'never.wav'), { timeoutMs: 3000, isDead: () => 'exit 1 no such source' })).rejects.toThrow(
      /^CAPTURE_NOT_STARTED: .*no such source/,
    )
  })
})

describe('analysis on generated files (offline)', () => {
  let dir: string
  const gen = (name: string, args: string[]) => {
    const f = join(dir, name)
    execFileSync('ffmpeg', ['-v', 'error', '-y', ...args, f])
    return f
  }
  const sha = (f: string) => createHash('sha256').update(readFileSync(f)).digest('hex')
  let tone: string
  let lead: string
  let silent: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'capture-an-'))
    tone = gen('tone.wav', ['-f', 'lavfi', '-i', 'sine=frequency=1000:duration=2', '-ac', '2', '-ar', '44100'])
    silent = gen('silent.wav', ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '2'])
    lead = gen('lead.wav', [
      '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo:d=1',
      '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=2',
      '-filter_complex', '[0][1]concat=n=2:v=0:a=1,aformat=channel_layouts=stereo', '-ar', '44100',
    ])
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  it('firstSoundAt is 0 for a file with no leading silence', async () => {
    expect(await firstSoundAt(tone)).toBe(0)
  })
  it('firstSoundAt finds a 1 s lead-in', async () => {
    expect(await firstSoundAt(lead)).toBeCloseTo(1, 1)
  })
  it('isSilent', async () => {
    expect(await isSilent(silent)).toBe(true)
    expect(await isSilent(tone)).toBe(false)
  })
  it('trim cuts the lead-in off', async () => {
    const out = join(dir, 'trimmed.wav')
    await trim(lead, 1, 1.5, out)
    expect(await firstSoundAt(out)).toBe(0)
    await expect(trim(lead, 0, 1, lead)).rejects.toThrow(/^TRIM_REFUSED/)
  })
  it('makePreview writes an mp3 and never touches its input', async () => {
    const before = sha(tone)
    const out = join(dir, 'tone.preview.mp3')
    await makePreview(tone, out)
    expect(statSync(out).size).toBeGreaterThan(0)
    expect(sha(tone)).toBe(before)
  })
  it('makePreview refuses to write to its input path, even spelled differently', async () => {
    const before = sha(tone)
    await expect(makePreview(tone, tone)).rejects.toThrow(/^PREVIEW_REFUSED/)
    await expect(makePreview(tone, join(dir, '.', 'x', '..', 'tone.wav'))).rejects.toThrow(/^PREVIEW_REFUSED/)
    expect(sha(tone)).toBe(before)
  })
})

// ── opt-in: real PulseAudio. Null sinks only, never a loopback — nothing here is audible. ───────

describe.skipIf(process.env.LISTEN_PULSE_IT !== '1')('PulseAudio integration (LISTEN_PULSE_IT=1)', () => {
  const name = `badcode_test_${process.pid}`
  const other = `badcode_test_${process.pid}_b`
  const modules: number[] = []
  let dir: string
  let tone: string
  const players: ChildProcess[] = []
  const sinkCount = (n: string) => parseSinks(execFileSync('pactl', ['list', 'short', 'sinks']).toString()).filter((s) => s === n).length
  const play = (sink: string) => {
    const p = spawn('paplay', [`--device=${sink}`, tone], { stdio: 'ignore' })
    players.push(p)
    return p
  }

  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'capture-it-'))
    tone = join(dir, 'tone.wav')
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=8', '-ac', '2', '-ar', '44100', tone])
  })
  afterAll(async () => {
    for (const p of players) p.kill('SIGKILL')
    await removeSink(modules)
    rmSync(dir, { recursive: true, force: true })
  })

  it('ensureSink twice makes one sink', { timeout: 60_000 }, async () => {
    const a = await ensureSink(name, { loopback: false })
    modules.push(...a.moduleIds)
    expect(a.created).toBe(true)
    expect(a.moduleIds).toHaveLength(1)
    const b = await ensureSink(name, { loopback: false })
    expect(b).toEqual({ sink: name, created: false, moduleIds: [] })
    expect(sinkCount(name)).toBe(1)
  })

  it('an idle sink (nothing holding it at low latency) still opens the gate', { timeout: 60_000 }, async () => {
    // ~2 s idle blocks on WSLg — see startRecording's doc — so this gate is widened on purpose.
    const rec = await startRecording(name, join(dir, 'idle.wav'), { startTimeoutMs: 6000 })
    const { seconds } = await rec.stop()
    expect(seconds).toBeGreaterThan(0)
  })

  it('records 3 s of a tone played into the sink', { timeout: 60_000 }, async () => {
    // Stand-in for production's loopback: a low-latency reader on the monitor that writes to
    // /dev/null. It keeps the sink out of its idle blocks, and unlike a loopback it is inaudible.
    const keep = spawn('parecord', ['--latency-msec=60', `--device=${name}.monitor`, '--raw', '/dev/null'], { stdio: 'ignore' })
    players.push(keep)
    await new Promise((r) => setTimeout(r, 2500))
    const raw = join(dir, 'raw.wav')
    const rec = await startRecording(name, raw)
    const player = spawn('paplay', ['--latency-msec=30', `--device=${name}`, tone], { stdio: 'ignore' })
    players.push(player)
    await new Promise((r) => setTimeout(r, 1000))
    await pinVolume(name)
    await new Promise((r) => setTimeout(r, 2000))
    const { path, seconds } = await rec.stop()
    player.kill('SIGKILL')
    keep.kill('SIGKILL')
    expect(path).toBe(raw)
    expect(seconds).toBeGreaterThan(2.8)
    expect(await isSilent(raw)).toBe(false)
    expect(await firstSoundAt(raw)).toBeLessThan(1.5)
    const preview = join(dir, 'raw.preview.mp3')
    await makePreview(raw, preview)
    expect(existsSync(preview)).toBe(true)
  })

  it('moveChromeStreams moves a process tree’s streams onto the sink', { timeout: 60_000 }, async () => {
    const b = await ensureSink(other, { loopback: false })
    modules.push(...b.moduleIds)
    const player = play(other)
    await new Promise((r) => setTimeout(r, 700))
    // this test process is the "chrome": paplay is its descendant
    expect(await moveChromeStreams(name, process.pid)).toBe(1)
    expect(await moveChromeStreams(name, process.pid)).toBe(0)
    player.kill('SIGKILL')
  })

  it('startRecording throws CAPTURE_NOT_STARTED for a sink that does not exist', { timeout: 60_000 }, async () => {
    await expect(startRecording(`badcode_test_missing_${process.pid}`, join(dir, 'none.wav'))).rejects.toThrow(/^CAPTURE_NOT_STARTED/)
  })
})
