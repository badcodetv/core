/**
 * Live proof that `resume` actually resumes.
 *
 * ⚠️ Spends credits for exactly ONE image — that is the point of the test. It re-runs the same
 * three prompts into a directory that already holds their output, having deleted the middle
 * one. A correct run regenerates index 1 only, and the two survivors must come back BYTE-FOR-
 * BYTE unchanged (a "skip" that silently re-generated would still return three healthy items).
 *
 * Run smoke-batch-live.ts into the same outDir first.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-batch-resume.ts <projectId> <outDir>
 */
import { readFile, unlink, stat } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { FlowClient } from './flow-client'

const [projectId, outDir] = process.argv.slice(2)
if (!projectId || !outDir) throw new Error('usage: smoke-batch-resume.ts <projectId> <outDir>')

const PROMPTS = [
  'A single plain metal disc resting on a dark wooden table, one thin light from above. Grounded, cinematic.',
  'A long empty corridor of server racks, one thin vertical light at the far end. Grounded, cinematic.',
  'A folding camp chair knocked over on wet grass at dawn. Grounded, cinematic.',
]

const md5 = async (p: string) => createHash('md5').update(await readFile(p)).digest('hex').slice(0, 10)

const before = { 0: await md5(`${outDir}/00.jpg`), 2: await md5(`${outDir}/02.jpg`) }
console.log('before:', JSON.stringify(before))
await unlink(`${outDir}/01.jpg`)
console.log('deleted 01.jpg — a resumed run must regenerate exactly this one')

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const started = Date.now()
  const result = await client.generateBatch(PROMPTS, outDir, { model: 'Nano Banana 2 Lite', resume: true })
  console.log(`resumed run in ${((Date.now() - started) / 1000).toFixed(1)}s`)
  for (const it of result.items) {
    console.log(`  [${it.index}] ${it.skipped ? 'SKIPPED' : 'generated'} ${it.width}x${it.height} ${it.path}`)
  }
  for (const f of result.failed) console.log(`  FAILED [${f.index}] ${f.code}`)

  const skipped = result.items.filter((i) => i.skipped).map((i) => i.index)
  if (JSON.stringify(skipped) !== '[0,2]') throw new Error(`expected 0 and 2 skipped, got ${JSON.stringify(skipped)}`)
  // The survivors must be untouched, not merely present.
  if ((await md5(`${outDir}/00.jpg`)) !== before[0]) throw new Error('00.jpg CHANGED — it was regenerated, not skipped')
  if ((await md5(`${outDir}/02.jpg`)) !== before[2]) throw new Error('02.jpg CHANGED — it was regenerated, not skipped')
  const regenerated = await stat(`${outDir}/01.jpg`)
  if (regenerated.size < 10_000) throw new Error('01.jpg was not regenerated properly')
  // Skipped items must carry real dimensions, not 0x0 — a manifest built from a resumed run
  // would otherwise record nothing and look fine doing it.
  for (const it of result.items.filter((i) => i.skipped)) {
    if (!it.width || !it.height) throw new Error(`skipped item ${it.index} reported ${it.width}x${it.height}`)
  }
  console.log('RESUME OK — one regenerated, two untouched, dimensions intact')
} finally {
  await client.close()
}
