/**
 * Pure classifier for Flow's status/warning cards. The wait loops in flow-client.ts poll
 * `detectFailureCard()` every tick so a policy block aborts in seconds instead of burning the
 * full generation timeout (docs/flow/failure-modes.md §A1) — this module is the one place that
 * maps observed card text to a verdict, so the wiring is a single call site rather than
 * scattered `getByText` regexes making their own judgement calls.
 *
 * The three known states (real strings observed live, see docs/flow/failure-modes.md §A1 and
 * docs/flow/automation-video.md:41-49):
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
 * chat transcript accumulates messages rather than replacing them — automation-video.md documents the
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

/**
 * Remove the cards that were ALREADY on the page before this turn started, returning only the
 * ones that are genuinely new.
 *
 * Flow keeps a refused generation's card in the project gallery permanently, so classifying
 * every card on the page means one blocked prompt poisons the project forever: every later
 * generation aborts instantly with POLICY_BLOCKED, confident and wrong. Confirmed live
 * 2026-08-12 — a plainly benign prompt failed in 5.5s in a project holding two old blocked
 * cards. That is strictly worse than the ~90s timeout this fast-abort was built to replace,
 * because a timeout is at least honest about not knowing.
 *
 * Compares as a MULTISET, not a set, and never by position:
 * - Repeated identical text is normal (retrying a blocked prompt produces a second card with
 *   byte-identical text), so a plain set difference would hide the new one behind the old.
 * - New cards may be prepended or appended depending on the gallery's sort, so "the last N"
 *   is not safe either.
 *
 * If `baseline` is empty this is a no-op, which is the correct behaviour for a first turn.
 * If the baseline is somehow stale (too many entries), the result is that a real block gets
 * subtracted away and the caller falls back to waiting out its timeout — the safe direction
 * to fail in, and exactly the behaviour that existed before the fast-abort.
 */
export function newCardsSince(current: string[], baseline: string[]): string[] {
  const remaining = new Map<string, number>()
  for (const t of baseline) remaining.set(t, (remaining.get(t) ?? 0) + 1)
  const fresh: string[] = []
  for (const t of current) {
    const n = remaining.get(t) ?? 0
    if (n > 0) remaining.set(t, n - 1)
    else fresh.push(t)
  }
  return fresh
}
