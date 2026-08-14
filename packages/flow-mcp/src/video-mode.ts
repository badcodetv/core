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
  const durationProblem = durationError(model, req.durationSeconds)
  if (durationProblem) return durationProblem
  const maxDuration = maxDurationForModel(model)
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

/** The two duration rules, shared by generate and refine (which validates it only if asked). */
function durationError(canonicalModel: string, seconds: number): string | null {
  if (!(VIDEO_DURATIONS as readonly number[]).includes(seconds)) {
    return `VIDEO_DURATION_INVALID: ${seconds}s — Flow offers ${VIDEO_DURATIONS.join('/')}s`
  }
  const max = maxDurationForModel(canonicalModel)
  if (seconds > max) {
    return `VIDEO_DURATION_UNAVAILABLE: ${seconds}s is not offered on ${canonicalModel} (max ${max}s) — only Omni Flash goes to 10s`
  }
  return null
}

/**
 * The reason Flow will refuse a REFINE request, or null.
 *
 * Refine re-runs an existing clip's own turn — Flow's per-clip `Reuse prompt` restores the
 * original prompt, its source frames and the compose mode, and we then overwrite the prompt.
 * So the source is a **media id already in the project**, never a local file: passing a path
 * is the mistake worth naming explicitly, because a path would otherwise simply never match a
 * tile and surface as a bare "clip not found".
 *
 * `durationSeconds` is optional here, and omitting it is the norm: whatever the original turn
 * used is what Reuse restores.
 */
export function refineRequestError(req: {
  mediaId: string
  motion: string
  model: string
  durationSeconds?: number
}): string | null {
  const id = (req.mediaId ?? '').trim()
  if (!id) return 'VIDEO_REFINE_NO_SOURCE: refine needs the mediaId of the clip to refine'
  if (/[/\\]/.test(id) || /\.(mp4|mov|webm|jpe?g|png)$/i.test(id)) {
    return `VIDEO_REFINE_NOT_A_MEDIA_ID: "${id}" looks like a file — refine targets a clip already in the project by the mediaId generate_video returned, not a path`
  }
  if (!(req.motion ?? '').trim()) {
    return 'VIDEO_REFINE_NO_PROMPT: refine needs the new motion prompt — to re-run a clip unchanged, just generate it again'
  }
  if (req.durationSeconds !== undefined) {
    return durationError(canonicalVideoModel(req.model), req.durationSeconds)
  }
  return null
}
