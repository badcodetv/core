/**
 * The Gemini API transport — the automated path.
 *
 * Measured on this key, 2026-09-12:
 *   - `gemini-3.5-flash` accepts audio and answers. ✅ (5 s 440 Hz tone → "a continuous, steady
 *     sine wave … approximately 220 Hz … A3")
 *   - `gemini-3.1-pro-preview` is LISTED by /models but returns **429 RESOURCE_EXHAUSTED**
 *     ("check your plan and billing details"). So listing a model is not permission to call it,
 *     and the 2026-09-11 research was right that Pro is off the free tier.
 *   - `gemini-2.5-flash` → 404, retired for new users.
 *   - `gemini-3.8-flash` → 503 "experiencing high demand" (transient, worth retrying).
 *
 * 🔑 That tone result is also a calibration fact worth keeping: it named the pitch an OCTAVE LOW.
 * Gemini's absolute numbers are not reliable — which is exactly why this package measures tempo,
 * loudness and brightness locally and never asks Gemini for a figure.
 */
import { readFile } from 'node:fs/promises'
import { extname } from 'node:path'
import type { DescribeRequest, DescribeResponse, Transport } from './transport'

const ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/models'

/** Default model: the newest Flash measured to accept audio on our key. */
export const DEFAULT_API_MODEL = 'gemini-3.5-flash'

/**
 * Inline audio is capped well below the API's request limit. Above this the Files API is the
 * right tool; failing loudly beats a truncated or rejected request nobody can explain.
 */
export const MAX_INLINE_BYTES = 15 * 1024 * 1024

const MIME: Record<string, string> = {
  '.mp3': 'audio/mp3',
  '.wav': 'audio/wav',
  '.m4a': 'audio/mp4',
  '.aac': 'audio/aac',
  '.ogg': 'audio/ogg',
  '.flac': 'audio/flac',
}

export function mimeFor(path: string): string {
  const m = MIME[extname(path).toLowerCase()]
  if (!m) throw new Error(`UNSUPPORTED_AUDIO: ${extname(path) || path} — Gemini takes ${Object.keys(MIME).join(', ')}`)
  return m
}

/** 503 is the model being busy and is worth retrying; 429 and 4xx are not. */
export const isRetryable = (status: number): boolean => status === 503 || status === 500 || status === 502

export class GeminiApi implements Transport {
  readonly name = 'api'

  constructor(
    private readonly apiKey: string,
    private readonly fetchImpl: typeof fetch = fetch,
    private readonly sleep: (ms: number) => Promise<void> = (ms) => new Promise((r) => setTimeout(r, ms)),
  ) {
    if (!apiKey.trim()) {
      throw new Error(
        'NO_API_KEY: GEMINI_API_KEY is not set. Add `export GEMINI_API_KEY=…` to .env (gitignored) ' +
          'or get a key at aistudio.google.com/apikey.',
      )
    }
  }

  async run(req: DescribeRequest): Promise<DescribeResponse> {
    const parts: unknown[] = [{ text: req.prompt }]
    if (req.audioPath) {
      const buf = await readFile(req.audioPath)
      if (buf.byteLength > MAX_INLINE_BYTES) {
        throw new Error(
          `AUDIO_TOO_LARGE: ${(buf.byteLength / 1e6).toFixed(1)} MB exceeds the ${MAX_INLINE_BYTES / 1e6} MB ` +
            `inline limit. Cut a range with start/end, or add Files API support.`,
        )
      }
      parts.push({ inline_data: { mime_type: mimeFor(req.audioPath), data: buf.toString('base64') } })
    }

    const body = JSON.stringify({ contents: [{ parts }] })
    let lastErr = ''
    for (let attempt = 0; attempt < 4; attempt++) {
      if (attempt) await this.sleep(2000 * attempt)
      const res = await this.fetchImpl(`${ENDPOINT}/${encodeURIComponent(req.model)}:generateContent`, {
        method: 'POST',
        headers: { 'x-goog-api-key': this.apiKey, 'Content-Type': 'application/json' },
        body,
      })
      const json = (await res.json().catch(() => ({}))) as {
        error?: { code?: number; status?: string; message?: string }
        candidates?: Array<{ content?: { parts?: Array<{ text?: string }> }; finishReason?: string }>
        modelVersion?: string
      }

      if (json.error) {
        const { code, status, message } = json.error
        lastErr = `${code} ${status}: ${(message ?? '').slice(0, 200)}`
        if (code && isRetryable(code)) continue
        if (code === 429) {
          throw new Error(
            `QUOTA_EXCEEDED: ${req.model} is not available on this key's quota (${lastErr}). ` +
              `Pick a Flash model (default ${DEFAULT_API_MODEL}) or raise the plan.`,
          )
        }
        throw new Error(`API_ERROR: ${lastErr}`)
      }
      if (!res.ok) {
        lastErr = `HTTP ${res.status}`
        if (isRetryable(res.status)) continue
        throw new Error(`API_ERROR: ${lastErr}`)
      }

      const text = (json.candidates?.[0]?.content?.parts ?? [])
        .map((p) => p.text ?? '')
        .join('')
        .trim()
      if (!text) {
        // A blocked or truncated answer is NOT a timeout and must not read like one.
        throw new Error(
          `EMPTY_REPLY: ${req.model} returned no text (finishReason: ${json.candidates?.[0]?.finishReason ?? 'unknown'})`,
        )
      }
      return { text, modelShown: json.modelVersion ?? req.model }
    }
    throw new Error(`API_ERROR: ${req.model} failed after 4 attempts — last: ${lastErr}`)
  }
}
