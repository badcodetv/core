/**
 * One describe, end to end: cut → measure → compose the instruction → drive AI Studio → shift the
 * timestamps back to source time → write the ledger.
 *
 * Dependencies are injected so this is testable without a browser or a repo: the server binds the
 * real `Studio`, the real measuring script and the real `writeLedger`.
 *
 * 🔴 Order matters. The measurements are taken from the CUT WAV, not the source, so a ranged
 * describe reports the range's loudness rather than the whole track's — the numbers must describe
 * what Gemini actually heard, or they contradict each other in the answer.
 */
import { basename } from 'node:path'
import { prepare } from './prepare'
import { loadLens } from './lens'
import { buildPrompt } from './prompt'
import { remapTimestamps } from './remap'
import { rangeLabel, writeLedger as realWriteLedger, type LedgerRecord } from './ledger'
import type { DescribeArgs, DescribeResult, Measurements } from './types'
import type { Studio } from './studio-client'

export interface DescribeDeps {
  studio: Studio
  defaultModel: string
  lensDir: string
  logDir: string
  /** Only so `ledgerPath` can be reported repo-relative. */
  repoRoot: string
  measure: (wavPath: string) => Promise<Measurements>
  writeLedger?: typeof realWriteLedger
  now?: () => Date
  /** Reply budget. A long track on a Pro model is slow; default 8 minutes. */
  replyTimeoutMs?: number
}

export async function describe(args: DescribeArgs, deps: DescribeDeps): Promise<DescribeResult> {
  const lensName = args.lens?.trim() || 'music'
  const lens = loadLens(deps.lensDir, lensName)
  const modelRequested = args.model?.trim() || deps.defaultModel

  // 🔴 Fail before touching the browser if the caller has passed boxes to a lens that ignores
  // them: silently dropping the prompt would turn a diff into a review and nobody would notice.
  if (args.sunoBoxes && !/suno/i.test(lensName)) {
    throw new Error(
      `LENS_MISMATCH: sunoBoxes was given but lens "${lensName}" does not use it. Use lens "suno-diff".`,
    )
  }

  const prep = await prepare(args.path, { start: args.start, end: args.end })
  try {
    const measurements = await deps.measure(prep.wavPath)
    const instruction = buildPrompt({
      lens,
      measurements,
      question: args.question,
      rangeLabel: prep.range ? rangeLabel(prep.range) : undefined,
      sunoBoxes: args.sunoBoxes,
    })

    await deps.studio.ensureSignedIn()
    await deps.studio.newChat()
    const modelShown = await deps.studio.selectModel(modelRequested)
    await deps.studio.disableSearchGrounding()
    await deps.studio.attachAudio(prep.mp3Path)
    await deps.studio.submit(instruction)
    const raw = await deps.studio.waitForReply(deps.replyTimeoutMs ?? 8 * 60_000)

    // Gemini times a cut clip from the clip's own zero. Shift it back so a timestamp in the
    // answer means the same thing as a timestamp in the source file.
    const shifted = prep.range && prep.range.start > 0 ? remapTimestamps(raw, prep.range.start) : { text: raw, count: 0 }

    const record: LedgerRecord = {
      at: (deps.now ?? (() => new Date()))(),
      sourceName: basename(prep.sourcePath),
      sha256: prep.sha256,
      range: prep.range,
      lens,
      modelRequested,
      modelShown,
      measurements,
      instruction,
      description: shifted.text,
      remapped: shifted.count > 0,
      question: args.question,
    }
    const abs = await (deps.writeLedger ?? realWriteLedger)(deps.logDir, record)
    const ledgerPath = abs.startsWith(deps.repoRoot) ? abs.slice(deps.repoRoot.length).replace(/^\//, '') : abs

    return {
      description: shifted.text,
      measurements,
      modelShown,
      lens: `${lens.name}@${lens.hash}`,
      range: prep.range,
      sha256: prep.sha256,
      ledgerPath,
      remapped: shifted.count > 0,
    }
  } finally {
    await prep.cleanup()
  }
}
