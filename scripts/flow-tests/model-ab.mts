/**
 * Re-run shots we already made on a different Flow video model: same start still, same prompt,
 * same length, one fresh project per shot (flow-automation law 19), count 1. Writes a recipe card
 * per clip. Built 2026-11-09 for the Omni 1.2 Flash test (Veo 3.1 Fast / Quality and Omni 1.1
 * leave Flow on 5 Dec 2026).
 *
 *   FLOW_CDP_PORT=<port> TMPDIR=$HOME/.cache/pw-tmp npx tsx scripts/flow-tests/model-ab.mts <jobs.json> [key …]
 *
 * jobs.json: { model, outDir, jobs: [{ key, start, motion, seconds, aspect, original, originalModel }] }
 * Skips a job whose output already exists, so re-running only pays for the holes.
 * Never run alongside another Flow call on the same browser.
 */
import { execFileSync } from 'node:child_process'
import { existsSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const cfg = JSON.parse(readFileSync(process.argv[2], 'utf8'))
const only = process.argv.slice(3)
const slug = (m: string) => m.toLowerCase().replace(/[^a-z0-9]+/g, '')

const c = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
for (const j of cfg.jobs) {
  if (only.length && !only.includes(j.key)) continue
  const out = join(cfg.outDir, `${j.key}-${slug(cfg.model)}.mp4`)
  if (existsSync(out)) { console.log(JSON.stringify({ key: j.key, skip: 'exists', out })); continue }
  const t0 = Date.now()
  try {
    const proj = await c.createProject(`ab-${j.key}`)
    const r = await c.generateVideo({ motion: j.motion, startImage: j.start, model: cfg.model, aspect: j.aspect, durationSeconds: j.seconds, count: 1, outPath: out } as any)
    execFileSync('python3', [join(REPO, 'scripts/provenance/prov.py'), 'card', out, '--kind', 'video', '--engine', 'google-flow',
      '--tool', 'scripts/flow-tests/model-ab.mts', '--model', cfg.model, '--prompt', j.motion, '--parent', j.start,
      '--source-id', (r as any).mediaId ?? '', '--why', `model A/B: same plate + prompt as ${j.original} (${j.originalModel})`,
      '--input', `start=${j.start}`, '--setting', `durationSeconds=${j.seconds}`, '--setting', `aspect=${j.aspect}`,
      '--setting', 'count=1', '--setting', `project=${proj.id}`], { stdio: 'inherit' })
    console.log(JSON.stringify({ key: j.key, ok: true, out, mediaId: (r as any).mediaId, via: (r as any).via, secs: Math.round((Date.now() - t0) / 1000) }))
  } catch (e) {
    console.log(JSON.stringify({ key: j.key, ok: false, error: String((e as Error).message).slice(0, 300), secs: Math.round((Date.now() - t0) / 1000) }))
  }
}
process.exit(0)
