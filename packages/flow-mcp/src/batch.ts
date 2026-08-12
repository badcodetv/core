/** Deterministic per-index output path: <outDir>/<NN>.jpg (NN = 2-digit zero-padded index). */
export function batchOutPath(outDir: string, index: number): string {
  const dir = outDir.replace(/\/+$/, '')
  return `${dir}/${String(index).padStart(2, '0')}.jpg`
}

/** Same shape as FlowClient's `ImageResult`, duplicated rather than imported: every other pure
 * module in this package (canvas.ts, project.ts, compose.ts, …) is a leaf that flow-client.ts
 * depends on, never the reverse, and this file keeps that one-way shape rather than being the
 * first exception. TS's structural typing means an ImageResult assigns here with no conversion. */
export interface BatchCandidate {
  path: string
  mediaId: string
  width: number
  height: number
}

/** One prompt's successful result within a batch. Mirrors ImageResult's multi-output shape
 * (candidates[]/partial) rather than inventing a second one, for a per-item numOutputs > 1:
 * `path`/`mediaId`/`width`/`height` are always candidate 0, `candidates` carries all of them,
 * and `partial` (item-scoped) means fewer candidates landed for THIS item than requested — not
 * to be confused with BatchResult.partial (batch-scoped: fewer PROMPTS completed than asked). */
export interface BatchItem {
  index: number
  prompt: string
  path: string
  mediaId: string
  width: number
  height: number
  candidates?: BatchCandidate[]
  partial?: boolean
  /** True when this item was NOT generated on this run — its file was already on disk. */
  skipped?: boolean
}

/** One prompt that did NOT produce a BatchItem, and why. `code` is the raw error string
 * (e.g. `POLICY_BLOCKED`, `TIMEOUT`, `SUBMIT_FAILED`) so a caller can branch on it the same
 * way toToolError does; `error` is currently identical to `code` (no richer message exists at
 * this layer yet) but is kept as its own field so a future nicer message doesn't require a
 * shape change. */
export interface BatchFailure {
  index: number
  prompt: string
  code: string
  error: string
}

/**
 * `generateBatch`'s return shape. Chosen over throwing on the first failure (the old
 * behaviour) because a batch is expensive to re-run from scratch — losing 6 good images to a
 * 7th prompt that was always going to fail (e.g. it names a real person) burns both wall-clock
 * and Flow credits for nothing. `items` holds every prompt that completed, in submission order.
 * `failed` holds every prompt that did NOT, each with the index/prompt/error needed to retry
 * just that one — or, when the batch stopped early (see `shouldContinueAfterFailure`), to
 * resume: prompts are attempted strictly in order and never skipped without being recorded in
 * one of the two arrays, so `items.length + failed.length` is always the exact count of prompts
 * attempted, and `prompts.slice(items.length + failed.length)` is always the untried remainder.
 * `partial` is `failed.length > 0` — true whenever the caller should look at `failed` before
 * assuming the run is complete.
 */
export interface BatchResult {
  items: BatchItem[]
  failed: BatchFailure[]
  partial: boolean
}

/**
 * Decide, per prompt, whether to generate it or skip it because its output already exists.
 *
 * This is what makes a long run RESUMABLE. `batchOutPath` is deterministic, so re-running the
 * same prompt list against the same `outDir` can pick up exactly where a dead session left off
 * instead of re-generating — and re-paying for — everything that already landed. A two-hour
 * unattended run that dies at prompt 14 is otherwise a two-hour loss.
 *
 * Deliberately keyed on the FILE, not on a recorded index: the file is the artifact the caller
 * actually wanted, it survives a crashed process that never got to write a manifest, and a
 * human who deletes one bad image gets exactly that one regenerated on the next run.
 */
export function planBatch(
  prompts: string[],
  outDir: string,
  exists: (path: string) => boolean,
): { index: number; prompt: string; path: string; skip: boolean }[] {
  return prompts.map((prompt, index) => {
    const path = batchOutPath(outDir, index)
    return { index, prompt, path, skip: exists(path) }
  })
}

/** Accumulator threaded through the submission loop in FlowClient.generateBatch. */
export interface BatchAccumulator {
  items: BatchItem[]
  failed: BatchFailure[]
}

export function emptyBatchAccumulator(): BatchAccumulator {
  return { items: [], failed: [] }
}

/**
 * Whether a batch should keep submitting the remaining prompts after item `code` failed.
 *
 * The rule: `POLICY_BLOCKED` is per-prompt — Flow classified THAT prompt (or the character/
 * reference it referenced) as a policy risk, which says nothing about whether the next prompt
 * in the list is fine. Skipping it and continuing is what makes a batch actually useful for
 * scene lists where one shot out of a dozen names something risky — the human fixes that one
 * prompt later, off the `failed` entry, without re-running the eleven that were never a problem.
 *
 * Every other failure code (`TIMEOUT`, `SUBMIT_FAILED`, a raw Playwright error, …) stops the
 * batch instead. Those are signals about the SESSION, not the prompt — a wedged compose bar or
 * a dead page will fail the next prompt too, so ploughing on would just burn the remaining
 * prompts' turn-timeouts for more of the same, with none of the diagnostic value a fast stop
 * gives ("it broke at index 4, on this prompt, with this code"). Silently swallowing a
 * `POLICY_BLOCKED` (continuing without recording it) would be worse than either of these
 * choices: it's the one card state that exists specifically to tell a human to rewrite, and a
 * caller that never saw `failed` would just quietly ship a batch with a hole in it.
 */
export function shouldContinueAfterFailure(code: string): boolean {
  return code === 'POLICY_BLOCKED'
}

/** What FlowClient.generateBatch reports back for one prompt, before it's folded in. */
export type BatchOutcome =
  | { ok: true; item: Omit<BatchItem, 'index' | 'prompt'> }
  | { ok: false; code: string }

/**
 * Fold one prompt's outcome into the accumulator and decide whether to keep going. Pure and
 * synchronous by design — `FlowClient.generateBatch` does the actual (unavoidably impure)
 * submit/wait/harvest per prompt, then calls this to update state and get its next move.
 */
export function foldBatchOutcome(
  acc: BatchAccumulator,
  index: number,
  prompt: string,
  outcome: BatchOutcome,
): { acc: BatchAccumulator; continue: boolean } {
  if (outcome.ok) {
    const item: BatchItem = { index, prompt, ...outcome.item }
    return { acc: { items: [...acc.items, item], failed: acc.failed }, continue: true }
  }
  const failure: BatchFailure = { index, prompt, code: outcome.code, error: outcome.code }
  return {
    acc: { items: acc.items, failed: [...acc.failed, failure] },
    continue: shouldContinueAfterFailure(outcome.code),
  }
}

/** Turn the accumulator into the final BatchResult once the loop stops (exhausted or aborted). */
export function finalizeBatch(acc: BatchAccumulator): BatchResult {
  return { items: acc.items, failed: acc.failed, partial: acc.failed.length > 0 }
}
