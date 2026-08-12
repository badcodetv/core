/**
 * Manual check — does a STALE failure card poison later generations? NOT part of CI.
 *
 * Flow leaves a refused generation's "Failed / might violate our policies" card in the
 * project gallery permanently. detectFailureCard() matches card text page-globally, so the
 * worry is a false POLICY_BLOCKED on a perfectly good prompt — which would be far worse than
 * the timeout it replaced, because it is instant, confident, and wrong.
 *
 * Run this in a project that ALREADY contains at least one blocked card.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-stale-card.ts
 */
import { mkdtemp } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    detectFailureCard(): Promise<string | null>
  }
  await inner.ensureProjectRoot()
  console.log('stale cards present ->', await inner.detectFailureCard())

  const dir = await mkdtemp(join(tmpdir(), 'flow-stale-'))
  const started = Date.now()
  try {
    const res = await client.generateImage(
      'A wide landscape photograph of an empty wooden bench beside a young tree in a public park, overcast morning light, muted colours.',
      join(dir, 'benign.jpg'),
    )
    console.log(`benign prompt SUCCEEDED after ${((Date.now() - started) / 1000).toFixed(1)}s`)
    console.log('  =>', res)
  } catch (err) {
    const secs = ((Date.now() - started) / 1000).toFixed(1)
    const msg = (err as Error).message
    console.log(`benign prompt THREW after ${secs}s: ${msg}`)
    console.log(
      msg === 'POLICY_BLOCKED'
        ? '  => BUG CONFIRMED: a stale card poisons unrelated generations'
        : '  => threw for some other reason; investigate',
    )
  }
} finally {
  await client.close()
}
