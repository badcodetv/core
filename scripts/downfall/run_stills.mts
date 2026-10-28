/**
 * Generate the downfall pack's option stills, shot by shot, into the scene's scratch folder.
 *
 * Eleven shots × four written treatments = 44 plates. W3 is deliberately NOT here: its four
 * prompts are reference-led and need the SELECTED W2 plate attached, so it cannot run until
 * Kai has picked. Anchors (T3, N3, W2) run first, because the rest of the pack has to match
 * their light, materials and field geography.
 *
 * Resume is on: a plate already on disk is never paid for twice, so a died run restarts with
 * the same command and deleting one bad image regenerates exactly that one.
 *
 *   npx tsx scripts/downfall/run_stills.mts                 # everything still missing
 *   npx tsx scripts/downfall/run_stills.mts T3 N3 W2        # just these shots
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const ENDPOINT = process.env.FLOW_CDP ?? 'http://localhost:9222'
const PROJECT = process.env.FLOW_PROJECT ?? '81bcb94f-7545-47a7-b13f-3b1f22dfb09f'
const STILLS = '/mnt/d/badcode-videos/gitpush-origin-master/clips/downfall/stills'
const LOG = join(REPO, 'scripts/downfall/run_stills.log')

/** Anchors first (they settle light, materials and geography), then the shots that match them. */
const ORDER = ['T3', 'N3', 'W2', 'T1', 'T2', 'N1', 'N2', 'SG', 'NY', 'LN', 'W1']

type Still = { key: string; shot: string; variant: string; title: string; prompt: string }
const stills: Still[] = JSON.parse(
  execFileSync('python3', [join(REPO, 'scripts/downfall/prompts.py'), 'stills'], { encoding: 'utf8', maxBuffer: 1 << 24 }),
)

const want = process.argv.slice(2).filter(a => !a.startsWith('-'))
const shots = (want.length ? want : ORDER).filter(s => ORDER.includes(s))

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

const client = await FlowClient.connect(ENDPOINT)
try {
  await client.openProject({ id: PROJECT })
  say({ ev: 'open', project: PROJECT, shots })
  for (const shot of shots) {
    const group = stills.filter(s => s.shot === shot).sort((a, b) => a.variant.localeCompare(b.variant))
    const outDir = join(STILLS, shot)
    mkdirSync(outDir, { recursive: true })
    say({ ev: 'shot.start', shot, n: group.length, outDir })
    const t0 = Date.now()
    try {
      const res = await client.generateBatch(group.map(s => s.prompt), outDir, {
        model: 'Nano Banana Pro', aspect: '16:9', numOutputs: 1, resume: true,
      })
      say({ ev: 'shot.done', shot, secs: Math.round((Date.now() - t0) / 1000),
            done: res.items.length, failed: res.failed, partial: res.partial })
    } catch (err) {
      say({ ev: 'shot.error', shot, error: String(err) })
    }
  }
} finally {
  await client.close?.()
}
say({ ev: 'end' })
