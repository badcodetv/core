/**
 * The Flow queue's runner (2026-11-18). flow_queue writes a run folder and starts this detached, so a long
 * run outlives the tool call (and an MCP reconnect). One process per run; inside it, up to `tabs` worker
 * tabs, each in a Flow project of its own, each taking the next job the moment it is free.
 *
 *   tsx packages/flow-mcp/src/queue-runner.ts <run-dir>
 *
 * <run-dir>/run.json     what to do (written by flow_queue): story, home project, endpoint, tabs, jobs
 * <run-dir>/status.json  where it is (read by flow_queue_status): every job's state, files and error
 * <run-dir>/events.jsonl one line per thing that happened
 *
 * Rules it keeps, and why:
 * - One job per tab, a fresh attachment per job (a long-held Playwright attachment misfires clicks: server.ts).
 * - A tab works in one project, locked for its life: results are found by diffing that project's grid.
 * - Character jobs run in the story's HOME project (Characters live there); everything else in the story's
 *   helper projects, so the session's own tab (usually in the home project) is never crossed with a worker.
 * - At most 10 worker tabs on the machine (queue-slots.ts); the rest wait for a free one.
 * - Inputs under /mnt are copied into the WSL filesystem first (flow-automation law 20: /mnt uploads stick).
 * - Every file made gets its recipe card, like the flow_* tools (prov.ts).
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync, renameSync, statSync, writeFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { basename, join } from 'node:path'
import { FlowClient, POOL_TAB_PREFIX, isPoolTab } from './flow-client'
import { chromium } from 'playwright'
import { madeFiles, stampFlow } from './prov'
import { firstOutput, jobKey, needsHomeProject, nextJob, shouldRetry, summarise, workLeftFor, type Job, type JobStatus } from './queue-core'
import { release, takeHelper, takeProject, takeSlot, type Held } from './queue-slots'

export interface RunSpec {
  runId: string
  story: string
  /** The story's own Flow project (its badcode.md / scene.json flow_project). */
  home: string
  endpoint: string
  tabs: number
  staggerMs: number
  createdAt: string
  jobs: Job[]
}
export interface RunStatus {
  runId: string
  story: string
  home: string
  pid: number
  startedAt: string
  updatedAt: string
  finishedAt?: string
  stopped?: boolean
  note?: string
  tabs: { tab: number; project?: string; home: boolean; state: string; job?: string }[]
  jobs: JobStatus[]
}

const FLOW_URL = 'https://flow.google.com'
const DIR = process.argv[2]
if (!DIR || !existsSync(join(DIR, 'run.json'))) throw new Error('usage: queue-runner.ts <run-dir>')
const spec: RunSpec = JSON.parse(readFileSync(join(DIR, 'run.json'), 'utf8'))
const STAGE = join(homedir(), '.cache', 'badcode-flow-queue', 'stage', spec.runId)
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))
const now = () => new Date().toISOString()

const status: RunStatus = {
  runId: spec.runId,
  story: spec.story,
  home: spec.home,
  pid: process.pid,
  startedAt: now(),
  updatedAt: now(),
  tabs: [],
  jobs: spec.jobs.map((j, i) => ({ i, key: jobKey(j, i), kind: j.kind, outPath: j.outPath, state: 'pending', attempts: 0 })),
}
function save() {
  status.updatedAt = now()
  const tmp = join(DIR, `status.json.${process.pid}.tmp`)
  writeFileSync(tmp, JSON.stringify(status, null, 1))
  renameSync(tmp, join(DIR, 'status.json'))
}
function say(o: Record<string, unknown>) {
  appendFileSync(join(DIR, 'events.jsonl'), JSON.stringify({ at: now(), ...o }) + '\n')
}

let stopping = false
const holds = new Set<Held>()
const hold = (h: Held | null) => { if (h) holds.add(h); return h }
const drop = (h: Held | null | undefined) => { if (h) { release(h); holds.delete(h) } }
const tagOf = (tab: number) => `q:${spec.runId}:${tab}`

/** Inputs under /mnt are copied into the WSL filesystem under their own name (the picker matches the name). */
function stage(i: number, path: string): string {
  if (!path.startsWith('/mnt/')) return path
  const dst = join(STAGE, String(i), basename(path))
  if (!existsSync(dst)) {
    mkdirSync(join(STAGE, String(i)), { recursive: true })
    copyFileSync(path, `${dst}.tmp`)
    renameSync(`${dst}.tmp`, dst)
  }
  return dst
}

async function runJob(c: FlowClient, job: Job, i: number): Promise<unknown> {
  const tool = `flow_queue (${job.kind})`
  const why = job.why ?? null
  if (job.kind === 'image') {
    const r = await c.generateImage(job.prompt, job.outPath, {
      model: job.model,
      ...(job.aspect ? { aspect: job.aspect } : {}),
      ...(job.numOutputs ? { numOutputs: job.numOutputs } : {}),
      ...(job.character ? { character: job.character } : {}),
    })
    return stampFlow(r, { kind: 'image', tool, prompt: job.prompt, model: job.model, why, inputs: { character: job.character ?? null }, settings: { aspect: job.aspect ?? null, numOutputs: job.numOutputs ?? 1 } })
  }
  if (job.kind === 'edit') {
    const refs = job.referenceImages.map((p) => stage(i, p))
    const r = await c.editImage(job.prompt, refs, job.outPath, {
      model: job.model,
      ...(job.aspect ? { aspect: job.aspect } : {}),
      ...(job.numOutputs ? { numOutputs: job.numOutputs } : {}),
      ...(job.character ? { character: job.character } : {}),
    })
    return stampFlow(r, { kind: 'image', tool, prompt: job.prompt, model: job.model, why, parent: job.referenceImages[0], inputs: { references: job.referenceImages, character: job.character ?? null }, settings: { aspect: job.aspect ?? null, numOutputs: job.numOutputs ?? 2 } })
  }
  const r = await c.generateVideo({
    motion: job.motion,
    outPath: job.outPath,
    model: job.model,
    aspect: job.aspect,
    ...(job.startImage ? { startImage: stage(i, job.startImage) } : {}),
    ...(job.endImage ? { endImage: stage(i, job.endImage) } : {}),
    ...(job.count ? { count: job.count } : {}),
    ...(job.durationSeconds ? { durationSeconds: job.durationSeconds } : {}),
    ...(job.character ? { character: job.character } : {}),
  })
  return stampFlow(r, { kind: 'video', tool, prompt: job.motion, model: job.model, why, parent: job.startImage ?? null, inputs: { start: job.startImage ?? null, end: job.endImage ?? null, character: job.character ?? null }, settings: { aspect: job.aspect, count: job.count ?? 1, durationSeconds: job.durationSeconds ?? null } })
}

/** Open this tab (again) and put it in `project`. Detaches after: every job attaches afresh. */
async function openIn(tab: number, project: string) {
  const c = await FlowClient.openTab(spec.endpoint, `${FLOW_URL}/project/${project}`, tagOf(tab))
  try { await c.openProject({ id: project }) } finally { await c.close() }
}

async function closeTab(tab: number) {
  const c = await FlowClient.attachTab(spec.endpoint, tagOf(tab)).catch(() => null)
  await c?.closeTab()
}

async function worker(tab: number, home: boolean) {
  const row = { tab, home, state: 'waiting' as string, project: undefined as string | undefined, job: undefined as string | undefined }
  status.tabs.push(row)
  await sleep(tab * spec.staggerMs)
  if (stopping || !workLeftFor(status.jobs, spec.jobs, home)) { row.state = 'not needed'; save(); return }
  const who = `queue ${spec.runId} tab ${tab}`
  const slot = hold(await takeSlot(who, () => { row.state = 'waiting for a free tab slot (10 in use)'; save(); say({ event: 'slot-wait', tab }) }, () => stopping))
  if (!slot) return
  let project: Held | null = null
  let opened = false
  try {
    if (!workLeftFor(status.jobs, spec.jobs, home)) { row.state = 'not needed'; return }
    if (home) {
      row.state = 'waiting for the home project'
      save()
      project = hold(await takeProject(spec.home, who, () => stopping))
      if (!project) return
      row.project = spec.home
      await openIn(tab, spec.home)
    } else {
      // Open on the projects page; takeHelper either opens an existing helper or makes a new one in this tab.
      const c = await FlowClient.openTab(spec.endpoint, FLOW_URL, tagOf(tab))
      try {
        const h = await takeHelper(spec.home, spec.story, who, async (name) => (await c.createProject(name)).id)
        project = hold(h.held)
        row.project = h.id
        if (h.made) say({ event: 'helper-made', tab, project: h.id })
        else await c.openProject({ id: h.id })
      } finally { await c.close() }
    }
    opened = true
    say({ event: 'tab-open', tab, home, project: row.project })
    for (;;) {
      if (stopping) break
      const i = nextJob(status.jobs, spec.jobs, home)
      if (i < 0) break
      const js = status.jobs[i]!
      const job = spec.jobs[i]!
      Object.assign(js, { state: 'running', tab, project: row.project, startedAt: now(), attempts: js.attempts + 1 })
      delete js.error
      row.state = 'running'
      row.job = js.key
      save()
      say({ event: 'job-start', tab, i, key: js.key, attempt: js.attempts })
      let c: FlowClient | null = null
      try {
        c = await FlowClient.attachTab(spec.endpoint, tagOf(tab))
        if (!(await c.status()).url.includes(`/project/${row.project}`)) await c.openProject({ id: row.project! })
        const result = await runJob(c, job, i)
        Object.assign(js, { state: 'done', files: madeFiles(result).map((f) => f.path), endedAt: now() })
        say({ event: 'job-done', tab, i, key: js.key, files: js.files })
      } catch (err) {
        const msg = ((err as Error)?.message ?? String(err)).split('\n')[0]!.slice(0, 500)
        const again = !stopping && shouldRetry(job.kind, msg, js.attempts)
        Object.assign(js, { state: again ? 'pending' : 'failed', error: msg, endedAt: now() })
        say({ event: again ? 'job-retry' : 'job-failed', tab, i, key: js.key, attempt: js.attempts, error: msg })
        // A closed or wedged tab: open it again before the next job.
        if (/TAB_GONE|Target closed|has been closed/i.test(msg)) await openIn(tab, row.project!).catch(() => {})
      } finally {
        await c?.close().catch(() => {})
        row.job = undefined
        save()
      }
    }
  } catch (err) {
    say({ event: 'tab-error', tab, error: ((err as Error)?.message ?? String(err)).slice(0, 500) })
    row.state = `error: ${((err as Error)?.message ?? String(err)).split('\n')[0]!.slice(0, 200)}`
  } finally {
    if (opened || !stopping) await closeTab(tab).catch(() => {})
    drop(project)
    drop(slot)
    if (!row.state.startsWith('error') && row.state !== 'not needed') row.state = 'closed'
    save()
    say({ event: 'tab-closed', tab })
  }
}

/** Close every tab this run opened (a killed worker never reaches its own closeTab). */
async function sweep() {
  const b = await chromium.connectOverCDP(spec.endpoint).catch(() => null)
  if (!b) return
  for (const p of b.contexts()[0]?.pages() ?? []) {
    if (!(await isPoolTab(p))) continue
    const name = await p.evaluate(() => window.name).catch(() => '')
    if (name.startsWith(`${POOL_TAB_PREFIX}q:${spec.runId}:`)) await p.close().catch(() => {})
  }
  await b.close().catch(() => {})
}

async function stop(sig: string) {
  if (stopping) return
  stopping = true
  for (const js of status.jobs) if (js.state === 'running') Object.assign(js, { state: 'failed', error: `stopped (${sig}) mid-job: check the Flow gallery of ${js.project} before re-running it`, endedAt: now() })
  status.stopped = true
  status.finishedAt = now()
  save()
  say({ event: 'stopped', sig })
  await sweep().catch(() => {})
  for (const h of [...holds]) drop(h)
  process.exit(130)
}
process.on('SIGTERM', () => void stop('SIGTERM'))
process.on('SIGINT', () => void stop('SIGINT'))
process.on('exit', () => { for (const h of holds) release(h) })

// Already on disk = already made (re-running a run only pays for what is missing).
for (const [i, js] of status.jobs.entries()) {
  const f = firstOutput(spec.jobs[i]!)
  if (existsSync(f) && statSync(f).size > 0) Object.assign(js, { state: 'skipped', files: [f], error: 'already on disk' })
}
const pending = status.jobs.filter((j) => j.state === 'pending')
const homeJobs = pending.filter((j) => needsHomeProject(spec.jobs[j.i]!)).length
const helperJobs = pending.length - homeJobs
const homeTabs = homeJobs ? 1 : 0
const helperTabs = Math.min(helperJobs, Math.max(homeTabs ? 0 : 1, spec.tabs - homeTabs))
save()
say({ event: 'start', jobs: spec.jobs.length, pending: pending.length, homeTabs, helperTabs })
const workers: Promise<void>[] = []
for (let t = 0; t < homeTabs + helperTabs; t++) workers.push(worker(t, t < homeTabs))
await Promise.all(workers)
await sweep().catch(() => {})
const s = summarise(status.jobs)
status.finishedAt = now()
if (s.pending) status.note = `${s.pending} job(s) never ran: no tab could take them`
save()
say({ event: 'done', ...s })
process.exit(0)
