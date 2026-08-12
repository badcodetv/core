/**
 * Live validation of `generateBatch` as it stands after Wave A — which changed the count tab
 * (`1x` → `x1`), added `character`, and raised the cap to 20, and none of which has been run
 * against the real UI. This is the batch equivalent of Wave B.
 *
 * ⚠️ SPENDS CREDITS (one image per prompt; runs on the cheapest image tier).
 *
 * Checks what the return value cannot tell you: that the files exist, are real images, and are
 * DIFFERENT from each other — a batch that quietly harvested the same canvas three times would
 * return three healthy-looking items.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-batch-live.ts <projectId> <outDir>
 */
import { stat, readFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { FlowClient } from './flow-client'

const [projectId, outDir] = process.argv.slice(2)
if (!projectId || !outDir) throw new Error('usage: smoke-batch-live.ts <projectId> <outDir>')

const PROMPTS = [
  'A single plain metal disc resting on a dark wooden table, one thin light from above. Grounded, cinematic.',
  'A long empty corridor of server racks, one thin vertical light at the far end. Grounded, cinematic.',
  'A folding camp chair knocked over on wet grass at dawn. Grounded, cinematic.',
]

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const started = Date.now()
  const result = await client.generateBatch(PROMPTS, outDir, { model: 'Nano Banana 2 Lite' })
  const secs = ((Date.now() - started) / 1000).toFixed(1)
  console.log(`batch of ${PROMPTS.length} in ${secs}s — ${result.items.length} ok, ${result.failed.length} failed`)

  const hashes = new Map<string, number>()
  for (const it of result.items) {
    const { size } = await stat(it.path)
    const md5 = createHash('md5').update(await readFile(it.path)).digest('hex').slice(0, 10)
    console.log(`  [${it.index}] ${it.path} ${size}b ${it.width}x${it.height} md5=${md5}`)
    hashes.set(md5, (hashes.get(md5) ?? 0) + 1)
  }
  for (const f of result.failed) console.log(`  FAILED [${f.index}] ${f.code} :: ${f.prompt.slice(0, 60)}`)

  // The check the result object cannot make for itself.
  const dupes = [...hashes.entries()].filter(([, n]) => n > 1)
  if (dupes.length) throw new Error(`DUPLICATE IMAGES — the batch harvested the same canvas twice: ${JSON.stringify(dupes)}`)
  console.log(result.partial ? 'BATCH PARTIAL (see failures above)' : 'BATCH OK — all distinct')
} finally {
  await client.close()
}
