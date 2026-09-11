/**
 * Record what a Chrome plays, without a Suno download (decisions 8 and 9 of
 * design/2026-09-11-understand-song-loop.md; the method is proven in
 * design/2026-09-11-suno-playback-recording-findings.md).
 *
 * Each channel's Chrome plays into its own PulseAudio null sink (`badcode_ch<N>`, a silent virtual
 * speaker); ffmpeg records that sink's monitor. The raw wav is for Claude; the preview mp3 — Kai's
 * low-pass, applied to a COPY — is for the human. 🔴 The filter never touches the raw file: it would
 * falsify every brightness and loudness measurement taken from it.
 *
 * Everything is spawned with execFile/spawn (no shell). pactl runs with LC_ALL=C so its output is
 * the English the parsers below expect.
 */
import { execFile, spawn } from 'node:child_process'
import { existsSync, realpathSync } from 'node:fs'
import { open, rm, stat } from 'node:fs/promises'
import { resolve } from 'node:path'
import { promisify } from 'node:util'

const run = promisify(execFile)

/** Kai's preview filter, picked from an 8-way A/B (findings doc, "Kai's preview filter"). */
export const PREVIEW_FILTER = 'lowpass=f=8000:poles=2,lowpass=f=8000:poles=2'

export const sinkName = (channel: number): string => `badcode_ch${channel}`

const tail = (s: string, n = 500): string => (s.length > n ? s.slice(-n) : s).trim()

function pactl(args: string[]): Promise<string> {
  return run('pactl', args, { env: { ...process.env, LC_ALL: 'C' }, maxBuffer: 8 << 20 }).then(
    ({ stdout }) => String(stdout),
    (err: { stderr?: unknown; message: string }) => {
      throw new Error(`PULSE_FAILED: pactl ${args.join(' ')}: ${tail(String(err.stderr ?? '')) || err.message}`)
    },
  )
}

// ── pure parsers ─────────────────────────────────────────────────────────────────────────────────

export interface ShortSink {
  index: number
  name: string
}

/** `pactl list short sinks` → index + name per line (tab-separated: index, name, driver, spec, state). */
export function parseShortSinks(pactlShort: string): ShortSink[] {
  const out: ShortSink[] = []
  for (const line of pactlShort.split('\n')) {
    const [idx, name] = line.split('\t')
    if (!idx || !name || !/^\d+$/.test(idx.trim())) continue
    out.push({ index: Number(idx), name: name.trim() })
  }
  return out
}

/** `pactl list short sinks` → sink names. */
export function parseSinks(pactlShort: string): string[] {
  return parseShortSinks(pactlShort).map((s) => s.name)
}

export interface SinkInput {
  index: number
  /** the sink's index, as in `pactl list short sinks` */
  sink: number
  /** `application.process.id`, when the client reported one */
  pid: number | null
}

/** `pactl list sink-inputs` (long form) → one record per `Sink Input #N` block. */
export function parseSinkInputs(pactlLong: string): SinkInput[] {
  const out: SinkInput[] = []
  for (const block of pactlLong.split(/^(?=Sink Input #)/m)) {
    const head = /^Sink Input #(\d+)/.exec(block)
    if (!head) continue
    const sink = /^\s*Sink:\s*(\d+)\s*$/m.exec(block)
    if (!sink) continue
    const pid = /^\s*application\.process\.id\s*=\s*"(\d+)"\s*$/m.exec(block)
    out.push({ index: Number(head[1]), sink: Number(sink[1]), pid: pid ? Number(pid[1]) : null })
  }
  return out
}

/** `ps -e -o pid=,ppid=` → [pid, ppid] pairs. */
export function parsePsPairs(ps: string): Array<[number, number]> {
  const out: Array<[number, number]> = []
  for (const line of ps.split('\n')) {
    const m = /^\s*(\d+)\s+(\d+)\s*$/.exec(line)
    if (m) out.push([Number(m[1]), Number(m[2])])
  }
  return out
}

/** root plus every process below it. Chrome's sound comes from its audio-service child, not root. */
export function descendantsOf(root: number, pairs: Array<[number, number]>): Set<number> {
  const children = new Map<number, number[]>()
  for (const [pid, ppid] of pairs) {
    if (pid === ppid) continue
    const list = children.get(ppid) ?? []
    list.push(pid)
    children.set(ppid, list)
  }
  const seen = new Set<number>([root])
  const queue = [root]
  while (queue.length) {
    for (const c of children.get(queue.shift()!) ?? []) {
      if (!seen.has(c)) {
        seen.add(c)
        queue.push(c)
      }
    }
  }
  return seen
}

/** volumedetect's `max_volume: -91.0 dB` → -91. null when the filter printed nothing (no samples). */
export function parseMaxVolume(ffmpegStderr: string): number | null {
  const m = /max_volume:\s*(-?(?:\d+(?:\.\d+)?|inf))\s*dB/.exec(ffmpegStderr)
  if (!m) return null
  return m[1] === '-inf' ? -Infinity : Number(m[1])
}

/** A silence_start this close to 0 counts as leading silence. */
const LEADING_EPS = 0.01

/**
 * silencedetect's first `silence_end`, but only when the first `silence_start` is at the very start
 * of the file (|start| ≤ 0.01 s) — i.e. how long the leading silence lasts. null otherwise.
 */
export function parseSilenceEnd(ffmpegStderr: string): number | null {
  const start = /silence_start:\s*(-?\d+(?:\.\d+)?(?:e-?\d+)?)/.exec(ffmpegStderr)
  if (!start || Math.abs(Number(start[1])) > LEADING_EPS) return null
  const end = /silence_end:\s*(-?\d+(?:\.\d+)?(?:e-?\d+)?)/.exec(ffmpegStderr.slice(start.index))
  return end ? Number(end[1]) : null
}

/**
 * Byte offset where a RIFF/WAVE file's sample data begins (just past the `data` chunk header), or
 * null when the header is not all there yet. ffmpeg writes a LIST/INFO chunk, so its header is
 * longer than the textbook 44 bytes — a fixed 44 would count a bare header as "audio flowing".
 */
export function wavDataOffset(head: Uint8Array): number | null {
  const tag = (at: number) => String.fromCharCode(...head.subarray(at, at + 4))
  if (head.length < 12 || tag(0) !== 'RIFF' || tag(8) !== 'WAVE') return null
  let at = 12
  while (at + 8 <= head.length) {
    const size = head[at + 4]! | (head[at + 5]! << 8) | (head[at + 6]! << 16) | (head[at + 7]! << 24)
    if (tag(at) === 'data') return at + 8
    at += 8 + (size >>> 0) + (size & 1)
  }
  return null
}

// ── command builders ─────────────────────────────────────────────────────────────────────────────

export const nullSinkArgs = (name: string): string[] => [
  'load-module',
  'module-null-sink',
  `sink_name=${name}`,
  `sink_properties=device.description=${name}`,
]

export const loopbackArgs = (name: string): string[] => [
  'load-module',
  'module-loopback',
  `source=${name}.monitor`,
  'sink=@DEFAULT_SINK@',
  'latency_msec=60',
]

/**
 * The plan's command plus two latency options, measured on WSLg's PulseAudio 17 (2026-09-11):
 * without `-fragment_size` ffmpeg's first read off a null-sink monitor is one huge block and the
 * output file does not even exist for ~4 s (past the 3 s start gate); with it, an idle sink's first
 * data lands at ~2.0 s and a playing one's at ~0.3 s. `-flush_packets 1` writes each packet as it
 * comes instead of in 256 KB lumps, so the gate sees audio as soon as it exists.
 */
export const recordArgs = (sink: string, outWav: string): string[] => [
  '-v', 'error', '-y', '-f', 'pulse', '-fragment_size', '4096', '-i', `${sink}.monitor`,
  '-ac', '2', '-ar', '44100', '-flush_packets', '1', outWav,
]

export const previewArgs = (inWav: string, outMp3: string): string[] => [
  '-v', 'error', '-y', '-i', inWav, '-vn', '-af', PREVIEW_FILTER, '-c:a', 'libmp3lame', '-b:a', '320k', outMp3,
]

export const trimArgs = (inWav: string, startSec: number, durSec: number, outWav: string): string[] => [
  '-v', 'error', '-y', '-ss', String(startSec), '-t', String(durSec), '-i', inWav, '-c:a', 'pcm_s16le', outWav,
]

// ── the virtual speaker ──────────────────────────────────────────────────────────────────────────

async function listSinks(): Promise<ShortSink[]> {
  return parseShortSinks(await pactl(['list', 'short', 'sinks']))
}

async function sinkIndex(sink: string): Promise<number> {
  const found = (await listSinks()).find((s) => s.name === sink)
  if (!found) throw new Error(`SINK_NOT_FOUND: no PulseAudio sink named ${sink} (pactl list short sinks)`)
  return found.index
}

/**
 * Idempotent: an existing sink of that name is left exactly as it is (created false, no module ids —
 * the caller does not own it and must not unload it). Otherwise loads a null sink and, unless
 * loopback === false, a loopback from its monitor to the default sink so it stays audible.
 * 🔴 Tests pass loopback: false — a loopback plays out loud.
 */
export async function ensureSink(
  name: string,
  opts: { loopback?: boolean } = {},
): Promise<{ sink: string; created: boolean; moduleIds: number[] }> {
  if ((await listSinks()).some((s) => s.name === name)) return { sink: name, created: false, moduleIds: [] }
  const moduleIds = [Number((await pactl(nullSinkArgs(name))).trim())]
  if (opts.loopback !== false) {
    try {
      moduleIds.push(Number((await pactl(loopbackArgs(name))).trim()))
    } catch (err) {
      await removeSink(moduleIds)
      throw err
    }
  }
  return { sink: name, created: true, moduleIds }
}

/** Unload each module, last-loaded first. A module that is already gone is not an error. */
export async function removeSink(moduleIds: number[]): Promise<void> {
  for (const id of [...moduleIds].reverse()) {
    if (!Number.isInteger(id)) continue
    try {
      await pactl(['unload-module', String(id)])
    } catch {
      // already unloaded
    }
  }
}

/**
 * Sink to 100% and unmuted, and every stream playing into it too. One run came out 21 dB quiet
 * without this (findings doc, "Volume"). 🔴 Call AFTER the stream exists (Chrome creates its
 * sink-input on Play); stream-restore may re-apply an old volume to a new stream.
 */
export async function pinVolume(sink: string): Promise<void> {
  const index = await sinkIndex(sink)
  await pactl(['set-sink-volume', sink, '100%'])
  await pactl(['set-sink-mute', sink, '0'])
  for (const input of parseSinkInputs(await pactl(['list', 'sink-inputs']))) {
    if (input.sink !== index) continue
    await pactl(['set-sink-input-volume', String(input.index), '100%'])
    await pactl(['set-sink-input-mute', String(input.index), '0'])
  }
}

/**
 * No-relaunch recovery for a Chrome launched before its channel had a sink: move every stream whose
 * application.process.id is chromePid or one of its descendants onto <sink>. Returns how many were
 * moved (streams already on <sink> are not counted).
 */
export async function moveChromeStreams(sink: string, chromePid: number): Promise<number> {
  const index = await sinkIndex(sink)
  const { stdout } = await run('ps', ['-e', '-o', 'pid=,ppid='], { maxBuffer: 8 << 20 })
  const family = descendantsOf(chromePid, parsePsPairs(String(stdout)))
  let moved = 0
  for (const input of parseSinkInputs(await pactl(['list', 'sink-inputs']))) {
    if (input.pid === null || !family.has(input.pid) || input.sink === index) continue
    await pactl(['move-sink-input', String(input.index), sink])
    moved++
  }
  return moved
}

// ── recording ────────────────────────────────────────────────────────────────────────────────────

export interface Recording {
  stop(): Promise<{ path: string; seconds: number }>
}

const BYTES_PER_SEC = 44100 * 2 * 2

async function readHead(path: string, n = 4096): Promise<Uint8Array> {
  const fh = await open(path, 'r')
  try {
    const buf = new Uint8Array(n)
    const { bytesRead } = await fh.read(buf, 0, n, 0)
    return buf.subarray(0, bytesRead)
  } finally {
    await fh.close()
  }
}

/**
 * Resolves once <path> holds sample data past its WAV header; throws CAPTURE_NOT_STARTED after
 * timeoutMs, or at once when isDead() says the writer has gone. Exported for the unit test.
 */
export async function waitForAudio(
  path: string,
  opts: { timeoutMs?: number; pollMs?: number; isDead?: () => string | null } = {},
): Promise<void> {
  const deadline = Date.now() + (opts.timeoutMs ?? 3000)
  for (;;) {
    const dead = opts.isDead?.()
    if (dead !== null && dead !== undefined) throw new Error(`CAPTURE_NOT_STARTED: the recorder exited before any audio arrived: ${dead}`)
    try {
      const { size } = await stat(path)
      const offset = size > 44 ? wavDataOffset(await readHead(path)) : null
      if (offset !== null && size > offset) return
    } catch {
      // not created yet
    }
    if (Date.now() >= deadline) {
      throw new Error(`CAPTURE_NOT_STARTED: ${path} got no audio past its header within ${opts.timeoutMs ?? 3000} ms`)
    }
    await new Promise((r) => setTimeout(r, opts.pollMs ?? 50))
  }
}

async function wavSeconds(path: string): Promise<number> {
  try {
    const { stdout } = await run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path])
    const d = Number(String(stdout).trim())
    if (Number.isFinite(d) && d >= 0) return d
  } catch {
    // fall through to the byte count
  }
  const { size } = await stat(path)
  const offset = wavDataOffset(await readHead(path)) ?? 44
  return Math.max(0, size - offset) / BYTES_PER_SEC
}

/**
 * Record <sink>.monitor into <outWav> (16-bit stereo 44.1 kHz). Resolves only once audio is
 * actually landing in the file (default gate 3 s, else CAPTURE_NOT_STARTED). stop() sends SIGINT —
 * ffmpeg then finalises the WAV header — and waits for it to exit.
 *
 * Measured 2026-09-11 on WSLg: a null sink with NO client holding it at low latency renders ~2 s
 * idle blocks, so the gate opens at 2.0–2.9 s and a stream started afterwards lands ~2 s into the
 * file (firstSoundAt + trim remove it). With a steady low-latency client on the monitor — in
 * production that is flow-chrome.sh's loopback (latency_msec=60) — the gate opens in ~0.1 s and
 * sound lands at ~0.06 s. Callers on a loopback-less sink should pass a wider startTimeoutMs.
 */
export async function startRecording(sink: string, outWav: string, opts: { startTimeoutMs?: number } = {}): Promise<Recording> {
  // A leftover file from an earlier take would pass the gate before ffmpeg truncates it (-y).
  await rm(outWav, { force: true })
  const child = spawn('ffmpeg', recordArgs(sink, outWav), { stdio: ['ignore', 'ignore', 'pipe'] })
  let stderr = ''
  child.stderr!.on('data', (d: Buffer) => {
    stderr += d.toString()
    if (stderr.length > 8192) stderr = stderr.slice(-8192)
  })
  let exited: string | null = null
  const exit = new Promise<void>((res) => {
    child.on('error', (err) => {
      exited = err.message
      res()
    })
    child.on('exit', (code, signal) => {
      exited = `${signal ?? `exit ${code}`} ${tail(stderr)}`.trim()
      res()
    })
  })

  try {
    await waitForAudio(outWav, { timeoutMs: opts.startTimeoutMs ?? 3000, isDead: () => exited })
  } catch (err) {
    if (exited === null) {
      child.kill('SIGKILL')
      await exit
    }
    throw err
  }

  return {
    async stop() {
      if (exited === null) {
        child.kill('SIGINT')
        const timer = setTimeout(() => child.kill('SIGKILL'), 5000)
        await exit
        clearTimeout(timer)
      }
      if (!existsSync(outWav)) throw new Error(`CAPTURE_NOT_STARTED: ${outWav} is missing after the recorder exited: ${exited}`)
      return { path: outWav, seconds: await wavSeconds(outWav) }
    },
  }
}

// ── analysis and derived files ───────────────────────────────────────────────────────────────────

async function ffmpegFilterStderr(wav: string, filter: string): Promise<string> {
  try {
    const { stderr } = await run('ffmpeg', ['-hide_banner', '-nostats', '-i', wav, '-af', filter, '-f', 'null', '-'], {
      maxBuffer: 8 << 20,
    })
    return String(stderr)
  } catch (err) {
    const e = err as { stderr?: unknown; message: string }
    throw new Error(`ANALYSE_FAILED: ffmpeg ${filter} on ${wav}: ${tail(String(e.stderr ?? '')) || e.message}`)
  }
}

/**
 * Seconds of leading silence (quieter than thresholdDb) — where the song actually starts in a
 * recording. 0 when there is no leading silence. An all-silent file is isSilent's job, not this one's.
 */
export async function firstSoundAt(wav: string, thresholdDb = -60): Promise<number> {
  return parseSilenceEnd(await ffmpegFilterStderr(wav, `silencedetect=n=${thresholdDb}dB:d=0.05`)) ?? 0
}

/** max_volume ≤ -80 dB (digital silence reads -91 dB). A file with no samples at all is silent too. */
export async function isSilent(wav: string): Promise<boolean> {
  const max = parseMaxVolume(await ffmpegFilterStderr(wav, 'volumedetect'))
  return max === null || max <= -80
}

/** true when a and b name the same file (after resolving symlinks, when both exist). */
function samePath(a: string, b: string): boolean {
  if (resolve(a) === resolve(b)) return true
  try {
    return existsSync(b) && realpathSync(a) === realpathSync(b)
  } catch {
    return false
  }
}

export async function trim(inWav: string, startSec: number, durSec: number, outWav: string): Promise<void> {
  if (samePath(inWav, outWav)) throw new Error(`TRIM_REFUSED: output ${outWav} is the input — ffmpeg would destroy it`)
  if (!(startSec >= 0) || !(durSec > 0)) throw new Error(`TRIM_REFUSED: start ${startSec}s / duration ${durSec}s is not a range`)
  await run('ffmpeg', trimArgs(inWav, startSec, durSec, outWav))
}

/**
 * The human's copy: PREVIEW_FILTER + 320k mp3. 🔴 Refuses to write to its input — the raw wav is
 * what gets measured and must never carry the filter.
 */
export async function makePreview(inWav: string, outMp3: string): Promise<void> {
  if (samePath(inWav, outMp3)) {
    throw new Error(`PREVIEW_REFUSED: output ${outMp3} is the raw input — the filter must never touch the raw file`)
  }
  await run('ffmpeg', previewArgs(inWav, outMp3))
}
