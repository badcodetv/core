// Run a list of Flow stills and clips unattended, with recipe cards, a log, and a fresh project every few jobs
// (a project goes bad after a few prompts: hangs at 99%, or an empty composer).
// jobs.json: [{ id, kind: "still"|"clip", prompt, out, count?, model, aspect?, startImage?, seconds?, character? }]
// usage: npx tsx scripts/flow/run-shots.mts <jobs.json> <log.jsonl> [--every 3] [--only id,id]
// A job with its output already on disk is skipped. A refusal is logged and not retried. Everything else gets 3 tries.
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
import { stampFlow } from '../../packages/flow-mcp/src/prov.ts'
import { readFileSync, existsSync, appendFileSync, mkdirSync, copyFileSync } from 'node:fs'
import { dirname, basename, join } from 'node:path'
import { homedir } from 'node:os'

const a = process.argv.slice(2)
const [jobsPath, logPath] = a
const opt = (k: string) => { const i = a.indexOf(k); return i > 0 ? a[i + 1] : undefined }
const every = Number(opt('--every') ?? 3)
const only = opt('--only')?.split(',')
const jobs: any[] = JSON.parse(readFileSync(jobsPath, 'utf8')).filter((j: any) => !only || only.includes(j.id))
const say = (s: string) => console.log(new Date().toISOString().slice(11, 19), s)
const log = (row: object) => appendFileSync(logPath, JSON.stringify({ at: new Date().toISOString(), ...row }) + '\n')
const suffixed = (out: string, s: string) => out.replace(/(\.[a-z0-9]+)$/i, `-${s}$1`)
const done = (j: any) => existsSync(j.out) || existsSync(suffixed(j.out, 'a'))
const plateDir = join(homedir(), '.cache/badcode-flow-plates')
mkdirSync(plateDir, { recursive: true })
const local = (p: string) => { const d = join(plateDir, basename(p)); if (!existsSync(d)) copyFileSync(p, d); return d }
const refused = (m: string) => /POLICY|reputational|prominent|unable to generate|violat/i.test(m)

const c: any = await FlowClient.connect()
let sinceFresh = Infinity
for (const j of jobs) {
  if (done(j)) { say(`skip ${j.id}`); continue }
  mkdirSync(dirname(j.out), { recursive: true })
  let finished = false
  for (let t = 1; t <= 3 && !finished; t++) {
    try {
      if (sinceFresh >= every) { const p = await c.createProject(); say(`project ${p.id}`); sinceFresh = 0 }
      sinceFresh++
      let r: any
      if (j.kind === 'still') {
        r = stampFlow(await c.generateImage(j.prompt, j.out, { numOutputs: j.count ?? 2, model: j.model, aspect: j.aspect, ...(j.character ? { character: j.character } : {}) }),
          { kind: 'image', tool: 'flow_generate_image', prompt: j.prompt, model: j.model, parent: null, inputs: {} } as any)
      } else {
        r = stampFlow(await c.generateVideo({ motion: j.prompt, outPath: j.out, startImage: local(j.startImage), model: j.model, aspect: j.aspect, count: j.count ?? 1, durationSeconds: j.seconds ?? 4 }),
          { kind: 'video', tool: 'flow_generate_video', prompt: j.prompt, model: j.model, parent: j.startImage, inputs: { start: j.startImage } } as any)
      }
      log({ id: j.id, status: 'ok', try: t, path: r.path, mediaId: r.mediaId, via: r.via ?? null, partial: r.partial ?? false })
      say(`${j.id} ok (try ${t})`)
      finished = true
    } catch (e: any) {
      let m = String(e?.message ?? e).slice(0, 400)
      // A refusal often surfaces as a timeout whose dump holds the real text.
      const dump = m.match(/\/tmp\/flow-timeout-[^ /]+?\.txt/)?.[0]
      if (dump && existsSync(dump) && /unable to generate|reputational/i.test(readFileSync(dump, 'utf8'))) m = 'POLICY in dump: ' + m
      say(`${j.id} try ${t} FAILED ${m.slice(0, 160)}`)
      sinceFresh = Infinity
      if (refused(m)) { log({ id: j.id, status: 'refused', error: m }); break }
      if (t === 3) log({ id: j.id, status: 'failed', error: m })
      await new Promise((r) => setTimeout(r, 10000))
    }
  }
}
say('ALL_DONE')
await c.close().catch(() => {})
process.exit(0)
