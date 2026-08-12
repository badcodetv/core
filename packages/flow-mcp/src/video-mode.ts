/**
 * Which video mode a request means, and whether Flow can actually do it.
 *
 * Pure, so the rules can be tested without a browser — the browser work
 * (`framesToVideo`, `ensureVideoDuration`) stays in flow-client.ts. Every rule below was
 * settled by running it against the live UI on 2026-08-12, not from Google's documentation,
 * which is wrong about two of them.
 */
import { VIDEO_DURATIONS, canonicalVideoModel, maxDurationForModel } from './compose'

/**
 * `animate` — one start frame, the long-proven Animate-menuitem path.
 * `frames`  — the compose bar's Start/End slots (start+end, or neither).
 * Both live under one tool: they are two source tabs of one Flow composer, not two features.
 */
export type VideoMode = 'animate' | 'frames'

export function chooseVideoMode(startImage?: string, endImage?: string): VideoMode {
  return startImage && !endImage ? 'animate' : 'frames'
}

/**
 * The reason Flow will refuse this request, or null if it will accept it.
 *
 * Returns the full error string (CODE: detail) so the caller just throws it, and so the code
 * and its explanation cannot drift apart.
 */
export function videoRequestError(req: {
  startImage?: string
  endImage?: string
  model: string
  durationSeconds: number
}): string | null {
  const model = canonicalVideoModel(req.model)
  if (!(VIDEO_DURATIONS as readonly number[]).includes(req.durationSeconds)) {
    return `VIDEO_DURATION_INVALID: ${req.durationSeconds}s — Flow offers ${VIDEO_DURATIONS.join('/')}s`
  }
  const maxDuration = maxDurationForModel(model)
  if (req.durationSeconds > maxDuration) {
    return `VIDEO_DURATION_UNAVAILABLE: ${req.durationSeconds}s is not offered on ${model} (max ${maxDuration}s) — only Omni Flash goes to 10s`
  }
  // A last frame with no first frame is not a mode Flow has: the slot fills and is then marked
  // invalid. Tested on Veo 3.1 Fast and Lite.
  if (req.endImage && !req.startImage) {
    return 'VIDEO_END_ONLY_UNSUPPORTED: Flow rejects a last frame with no first frame — supply startImage too'
  }
  // Omni Flash takes a first frame but rejects a last one; the error badge clears the moment
  // you switch to any Veo 3.1 tier. Keyed off the 10s capability because that is the same
  // Omni-Flash-only line, and there is exactly one such model.
  if (req.endImage && maxDuration === 10) {
    return `VIDEO_FRAMES_UNAVAILABLE: ${model} does not accept a last frame — use a Veo 3.1 tier`
  }
  return null
}
