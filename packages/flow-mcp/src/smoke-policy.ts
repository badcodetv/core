/**
 * Manual check — does a policy block abort FAST and legibly? NOT part of CI.
 *
 * The entire point of detectFailureCard() is that a refused generation returns POLICY_BLOCKED
 * in seconds instead of burning the full ~90s turn timeout and reporting TIMEOUT. That claim
 * has never been tested against a real refusal; the card's DOM shape was never mapped, so it
 * is entirely possible the classifier is correct but unreachable.
 *
 * Uses a named real person, which is the reliable trigger (it is how a morning was lost on
 * 2026-08-12). Costs nothing when it works — a blocked generation produces no image.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-policy.ts
 */
import { mkdtemp } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const dir = await mkdtemp(join(tmpdir(), 'flow-policy-'))
  const started = Date.now()
  try {
    const res = await client.generateImage(
      'A photorealistic portrait of Taylor Swift seated at a desk, smiling at the camera.',
      join(dir, 'blocked.jpg'),
    )
    console.log(`NOT BLOCKED after ${((Date.now() - started) / 1000).toFixed(1)}s:`, res)
    console.log('Inconclusive — pick a stronger trigger and rerun.')
  } catch (err) {
    const secs = ((Date.now() - started) / 1000).toFixed(1)
    const e = err as { code?: string; message?: string }
    console.log(`threw after ${secs}s`)
    console.log('  message:', e.message)
    // The client throws a bare Error whose MESSAGE is the sentinel; server.ts maps that
    // message to the caller-facing `code`. Asserting on err.code here would fail a working
    // implementation — which it did on first run.
    const blocked = e.message === 'POLICY_BLOCKED'
    console.log(
      blocked
        ? Number(secs) < 40
          ? `  => PASS: classified, and aborted in ${secs}s rather than the ~90s turn timeout`
          : '  => PARTIAL: correctly classified but no faster than a timeout'
        : '  => FAIL: not classified as a policy block',
    )
  }
} finally {
  await client.close()
}
