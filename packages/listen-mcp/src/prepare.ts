/**
 * Turn whatever path the caller gave into two temp files: a wav Claude measures and an mp3 Gemini
 * hears. A range is cut here with ffmpeg, so Gemini hears only that range (decision 5) — its
 * timestamps are shifted back to source time later, by remap.ts.
 */
import { execFile } from 'node:child_process'
import { createHash } from 'node:crypto'
import { createReadStream, existsSync, statSync } from 'node:fs'
import { mkdtemp, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { basename, join } from 'node:path'
import { promisify } from 'node:util'
import type { Range } from './types'

const run = promisify(execFile)

/**
 * 'D:\a\b.mp3' or 'D:/a/b.mp3' → '/mnt/d/a/b.mp3'. Posix paths pass through. Deliberately not
 * `wslpath`: a spawn per call for a string rewrite, and it fails outright on a path that does not
 * exist yet — which is exactly the case FILE_NOT_FOUND should report clearly.
 */
export function toLinuxPath(p: string): string {
  const m = /^([A-Za-z]):[\\/](.*)$/.exec(p)
  if (!m) return p
  return `/mnt/${m[1]!.toLowerCase()}/${m[2]!.replace(/\\/g, '/')}`
}

/** 80 | '80' | '1:20' | '1:20.5' | '0:01:20' → seconds. Anything else throws RANGE_INVALID. */
export function parseTime(t: string | number): number {
  const bad = (): never => {
    throw new Error(`RANGE_INVALID: cannot read ${JSON.stringify(t)} as a time — use seconds, "M:SS" or "H:MM:SS"`)
  }
  if (typeof t === 'number') return Number.isFinite(t) && t >= 0 ? t : bad()
  const s = t.trim()
  if (/^\d+(?:\.\d+)?$/.test(s)) return Number(s)
  const m = /^(?:(\d+):)?(\d+):(\d{2}(?:\.\d+)?)$/.exec(s)
  if (!m) return bad()
  const [, h, mm, ss] = m
  const sec = Number(ss)
  if (sec >= 60) return bad()
  if (h !== undefined && Number(mm) >= 60) return bad()
  return (h ? Number(h) * 3600 : 0) + Number(mm) * 60 + sec
}

/**
 * null when neither end is given. start defaults to 0, end to the duration. Throws RANGE_INVALID
 * when start < 0, end > duration + 0.05 (containers round their durations), or start >= end.
 */
export function validateRange(durationSec: number, start?: number, end?: number): Range | null {
  if (start === undefined && end === undefined) return null
  const s = start ?? 0
  const e = end ?? durationSec
  if (s < 0) throw new Error(`RANGE_INVALID: start ${s}s is before the beginning`)
  if (e > durationSec + 0.05) throw new Error(`RANGE_INVALID: end ${e}s is past the end of the file (${durationSec.toFixed(2)}s)`)
  if (s >= e) throw new Error(`RANGE_INVALID: start ${s}s is not before end ${e}s`)
  return { start: s, end: e }
}

export interface Prepared {
  sourcePath: string
  sourceName: string
  sha256: string
  durationSec: number
  range: Range | null
  wavPath: string
  mp3Path: string
  cleanup(): Promise<void>
}

function sha256File(path: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const h = createHash('sha256')
    createReadStream(path)
      .on('data', (chunk) => h.update(chunk))
      .on('error', reject)
      .on('end', () => resolve(h.digest('hex')))
  })
}

async function probeDuration(path: string): Promise<number> {
  const { stdout } = await run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path])
  const d = Number(stdout.trim())
  if (!Number.isFinite(d) || d <= 0) throw new Error(`FILE_NOT_FOUND: ffprobe could not read a duration from ${path} — is it audio?`)
  return d
}

export async function prepare(
  path: string,
  opts: { start?: string | number; end?: string | number; tmpRoot?: string } = {},
): Promise<Prepared> {
  const sourcePath = toLinuxPath(path)
  if (!existsSync(sourcePath) || !statSync(sourcePath).isFile()) {
    throw new Error(`FILE_NOT_FOUND: ${sourcePath}`)
  }
  const durationSec = await probeDuration(sourcePath)
  const range = validateRange(
    durationSec,
    opts.start === undefined ? undefined : parseTime(opts.start),
    opts.end === undefined ? undefined : parseTime(opts.end),
  )
  const sha256 = await sha256File(sourcePath)

  const dir = await mkdtemp(join(opts.tmpRoot ?? tmpdir(), 'listen-'))
  const cleanup = () => rm(dir, { recursive: true, force: true })
  const wavPath = join(dir, 'seg.wav')
  const mp3Path = join(dir, 'seg.mp3')
  try {
    // Input-side seek (-ss/-to before -i) is fast, and accurate for audio. Channels are left as
    // they are: the stereo measurements need both.
    const cut = range ? ['-ss', String(range.start), '-to', String(range.end)] : []
    await run('ffmpeg', ['-v', 'error', '-y', ...cut, '-i', sourcePath, '-vn', '-c:a', 'pcm_s16le', '-ar', '44100', wavPath])
    await run('ffmpeg', ['-v', 'error', '-y', '-i', wavPath, '-c:a', 'libmp3lame', '-b:a', '192k', mp3Path])
  } catch (err) {
    await cleanup()
    throw err
  }
  return { sourcePath, sourceName: basename(sourcePath), sha256, durationSec, range, wavPath, mp3Path, cleanup }
}
