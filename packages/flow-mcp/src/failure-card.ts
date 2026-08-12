/**
 * Pure classifier for Flow's status/warning cards. The wait loops in flow-client.ts poll
 * `detectFailureCard()` every tick so a policy block aborts in seconds instead of burning the
 * full generation timeout (docs/flow/failure-modes.md §A1) — this module is the one place that
 * maps observed card text to a verdict, so the wiring is a single call site rather than
 * scattered `getByText` regexes making their own judgement calls.
 *
 * The three known states (real strings observed live, see docs/flow/failure-modes.md §A1 and
 * docs/superpowers/flow-video.md:41-49):
 *
 * - `blocked` — policy. Never retry; the prompt (or a field/reference image, §A2) must be
 *   rewritten. Two variants seen, one sentence-case, one Title Case ("This Prompt Might
 *   Violate Our Policies About Generating Prominent People…") — matched case-insensitively.
 * - `queued` — benign. "Your video has been scheduled and is waiting in the queue due to high
 *   demand." A `warning Failed`-looking icon can render WHILE queued; that is not a real
 *   failure and must not be read as one.
 * - `error` — transient. "Oops, something went wrong!" Flow re-posts the credit-approval gate
 *   for this one; the existing retry (re-approve) path stays valid.
 *
 * Precedence when more than one pattern matches the same string. This matters because a Flow
 * chat transcript accumulates messages rather than replacing them — flow-video.md documents the
 * queue message surviving in the DOM even after the clip has finished — so by the time we poll,
 * more than one of these strings can legitimately be present at once:
 *
 *   blocked > error > queued > null
 *
 * - `blocked` wins over everything: it is the one verdict that changes caller behaviour (stop,
 *   rewrite, never retry), so any ambiguity must resolve in its favour rather than risk masking
 *   it behind a stale, unrelated card.
 * - `error` wins over `queued`: the queue text is stale-tolerant by design (its mere presence
 *   proves nothing — it can be left over from a completed clip), while an error card is only
 *   ever (re-)posted for a real, actionable event. Treating a co-occurring error as real and a
 *   co-occurring queue message as noise matches the behaviour `waitForVideoClip` already had
 *   (it watched for "Oops, something went wrong" and ignored the queue text entirely) — this
 *   module generalises that judgement rather than changing it.
 * - `queued` alone means "keep waiting" — explicitly benign, including while the misleading
 *   `warning Failed`-looking icon is on screen.
 */

export type CardState = 'blocked' | 'queued' | 'error' | null

// Both observed policy-block strings share this phrase; matching the phrase rather than the
// full sentence also survives Flow varying the wording around it. Case-insensitive to catch
// the Title Case "Might Violate Our Policies" variant.
const BLOCKED_RE = /might violate our policies/i

const QUEUED_RE = /scheduled and is waiting in the queue/i

const ERROR_RE = /oops,?\s*something went wrong/i

/** Single source of truth for "is this text worth reading at all" — used to scope the DOM probe. */
export const ANY_CARD_RE = new RegExp(`${BLOCKED_RE.source}|${QUEUED_RE.source}|${ERROR_RE.source}`, 'i')

export function classifyCard(text: string | null): CardState {
  if (!text) return null
  if (BLOCKED_RE.test(text)) return 'blocked'
  if (ERROR_RE.test(text)) return 'error'
  if (QUEUED_RE.test(text)) return 'queued'
  return null
}
