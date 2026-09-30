// Camping mv2 re-cut stills (2026-09-29): every still in recut-stills.json, Nano Banana 2 · 16:9 · x2.
// Characters go in as reference images (the MCP cannot cast a Flow Character on the rebuilt Flow yet).
// Usage: npx tsx scripts/camping-mv2/recut-stills.mts [id …]   (existing outputs are skipped)
// Other sets: STILLS=breath STILLS_MODEL='Nano Banana Pro' reads breath-stills.json and writes clips/breath-stills/.
// Refs live in $CAST_REFS (default ~/.cache/badcode-cast): the committed world-cast plates + Bob's sheet crops.
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
import { readFileSync, existsSync, mkdirSync } from 'node:fs'
import { homedir } from 'node:os'
const SET = process.env.STILLS ?? 'recut'
const OUT = `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Camping Comic/music video/clips/${SET}-stills`
const REFS = process.env.CAST_REFS ?? `${homedir()}/.cache/badcode-cast`
const shots: { id: string; refs: string[]; prompt: string }[] = JSON.parse(readFileSync(new URL(`./${SET}-stills.json`, import.meta.url), 'utf8'))
const only = process.argv.slice(2)
mkdirSync(OUT, { recursive: true })
const log = (...a: any[]) => console.log(new Date().toISOString().slice(11, 19), ...a)
const c: any = await FlowClient.connect()
await c.openProject({ id: 'b93409d1-c1b9-4330-ae71-a07f65e2f780' })
const opts = { model: process.env.STILLS_MODEL ?? 'Nano Banana 2', aspect: '16:9', numOutputs: 2 }
for (const s of shots) {
  if (only.length && !only.includes(s.id)) continue
  const out = `${OUT}/${s.id}.jpg`
  if (existsSync(`${OUT}/${s.id}-a.jpg`)) { log(s.id, 'exists, skipped'); continue }
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      log(s.id, 'submit', attempt)
      const r = s.refs.length
        ? await c.editImage(s.prompt, s.refs.map((f) => `${REFS}/${f}`), out, opts)
        : await c.generateImage(s.prompt, out, opts)
      log(s.id, 'saved', JSON.stringify((r.candidates ?? [r]).map((x: any) => x.mediaId)), r.partial ? 'PARTIAL' : '')
      break
    } catch (e: any) {
      log(s.id, 'FAILED', attempt, String(e?.message ?? e).slice(0, 200))
      await c.page.keyboard.press('Escape').catch(() => {})
      await c.page.reload().catch(() => {}); await c.page.waitForTimeout(10_000)
      await c.openProject({ id: 'b93409d1-c1b9-4330-ae71-a07f65e2f780' }).catch(() => {})
    }
  }
}
log('done')
process.exit(0)
