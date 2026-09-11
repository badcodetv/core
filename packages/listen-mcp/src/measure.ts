/**
 * Run scripts/audio-measure.py on a segment and validate what it prints. The Python side owns the
 * signal processing; this side owns the contract — a schema failure is a MEASURE_FAILED, never a
 * half-typed object leaking into a prompt.
 */
import { execFile } from 'node:child_process'
import { z } from 'zod'
import type { Measurements } from './types'

const nullableNumber = z.number().nullable()

export const MeasurementsSchema: z.ZodType<Measurements> = z.object({
  durationSec: z.number(),
  integratedLufs: nullableNumber,
  truePeakDbtp: nullableNumber,
  loudnessRangeLu: nullableNumber,
  channels: z.number().int().positive(),
  stereoCorrelation: nullableNumber,
  sideToMidDb: nullableNumber,
  spectralCentroidHz: z.number(),
  tempo: z.object({
    bpm: nullableNumber,
    confidence: z.enum(['high', 'fair', 'tempo-only', 'unverified', 'none']),
  }),
})

const tail = (s: string, n = 500): string => (s.length > n ? s.slice(-n) : s).trim()

/**
 * `script` is the absolute path to scripts/audio-measure.py — the caller supplies it, so this
 * module never has to know where the repo is. The librosa import alone takes seconds, hence the
 * generous timeout.
 */
export function measure(wavPath: string, opts: { script: string; python?: string; timeoutMs?: number }): Promise<Measurements> {
  return new Promise((resolve, reject) => {
    execFile(
      opts.python ?? 'python3',
      [opts.script, wavPath],
      { timeout: opts.timeoutMs ?? 300_000, maxBuffer: 1 << 20 },
      (err, stdout, stderr) => {
        if (err) {
          reject(new Error(`MEASURE_FAILED: ${tail(String(stderr)) || err.message}`))
          return
        }
        let json: unknown
        try {
          json = JSON.parse(String(stdout))
        } catch {
          reject(new Error(`MEASURE_FAILED: not JSON: ${tail(String(stdout))} ${tail(String(stderr))}`.trim()))
          return
        }
        const parsed = MeasurementsSchema.safeParse(json)
        if (!parsed.success) {
          reject(new Error(`MEASURE_FAILED: unexpected shape: ${tail(parsed.error.message)}`))
          return
        }
        resolve(parsed.data)
      },
    )
  })
}
