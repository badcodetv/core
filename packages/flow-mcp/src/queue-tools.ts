/**
 * flow_queue, flow_queue_status, flow_queue_stop (2026-11-18): the session's front door to the Flow queue.
 * The rule: ONE JOB PER TAB. One job → the ordinary flow_* tool, in the session's own tab. Two or more →
 * flow_queue, which runs them across up to 10 tabs (queue-runner.ts) and returns at once.
 */
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { z } from 'zod'
import { spawn } from 'node:child_process'
import { existsSync, mkdirSync, openSync, readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { QUEUE_HOME, REPO_ROOT, pidAlive } from './lock'
import { MAX_TABS, jobProblems, jobKey, summarise, tabsFor, type Job, type JobStatus } from './queue-core'
import { slotsInUse } from './queue-slots'
import type { RunSpec, RunStatus } from './queue-runner'
import { ok, fail, type ToolResult } from './result'

const RUNS = () => join(QUEUE_HOME, 'runs')
const IMAGE_ASPECTS = ['1:1', '3:2', '2:3', '3:4', '4:3', '4:5', '5:4', '9:16', '16:9', '21:9', '1:4', '4:1', '1:8', '8:1'] as const

const common = { key: z.string().min(1).optional(), why: z.string().min(1).optional(), outPath: z.string().min(1) }
const JOB = z.discriminatedUnion('kind', [
  z.object({
    kind: z.literal('image'), ...common, prompt: z.string().min(1), model: z.string().min(1),
    aspect: z.enum(IMAGE_ASPECTS).optional(), numOutputs: z.number().int().min(1).max(4).optional(), character: z.string().min(1).optional(),
  }),
  z.object({
    kind: z.literal('edit'), ...common, prompt: z.string().min(1), referenceImages: z.array(z.string().min(1)).min(1).max(3), model: z.string().min(1),
    aspect: z.enum(IMAGE_ASPECTS).optional(), numOutputs: z.number().int().min(1).max(4).optional(), character: z.string().min(1).optional(),
  }),
  z.object({
    kind: z.literal('video'), ...common, motion: z.string().min(1), model: z.string().min(1), aspect: z.enum(['16:9', '9:16']),
    startImage: z.string().min(1).optional(), endImage: z.string().min(1).optional(), count: z.number().int().min(1).max(4).optional(),
    durationSeconds: z.number().int().min(3).max(15).optional(), character: z.string().min(1).optional(),
  }),
])

const stamp = () => new Date().toISOString().replace(/[-:]/g, '').replace('T', '-').slice(0, 15)
const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40) || 'story'

function readStatus(runId: string): { spec: RunSpec; status: RunStatus | null } | null {
  const dir = join(RUNS(), runId)
  if (!existsSync(join(dir, 'run.json'))) return null
  const spec = JSON.parse(readFileSync(join(dir, 'run.json'), 'utf8')) as RunSpec
  let status: RunStatus | null = null
  try { status = JSON.parse(readFileSync(join(dir, 'status.json'), 'utf8')) } catch { /* not started yet */ }
  return { spec, status }
}

/** What a session needs to read: counts, every job's state and files, and why anything failed. */
function report(runId: string) {
  const r = readStatus(runId)
  if (!r) return null
  const { spec, status } = r
  const jobs: JobStatus[] = status?.jobs ?? spec.jobs.map((j, i) => ({ i, key: jobKey(j, i), kind: j.kind, outPath: j.outPath, state: 'pending', attempts: 0 }))
  const sum = summarise(jobs)
  const finished = Boolean(status?.finishedAt)
  const alive = status ? pidAlive(status.pid) : false
  const runnerDied = Boolean(status) && !finished && !alive
  return {
    runId,
    story: spec.story,
    homeProject: spec.home,
    state: finished ? (status?.stopped ? 'stopped' : 'finished') : runnerDied ? 'runner died' : status ? 'running' : 'starting',
    ...sum,
    finished: finished || runnerDied,
    elapsedMin: status ? +((Date.parse(status.finishedAt ?? status.updatedAt) - Date.parse(status.startedAt)) / 60_000).toFixed(1) : 0,
    tabs: status?.tabs ?? [],
    jobs: jobs.map((j) => ({
      key: j.key, kind: j.kind, state: j.state, attempts: j.attempts,
      ...(j.tab !== undefined ? { tab: j.tab } : {}),
      ...(j.files?.length ? { files: j.files } : {}),
      ...(j.error ? { error: j.error } : {}),
    })),
    ...(status?.note ? { note: status.note } : {}),
    ...(runnerDied ? { hint: `The runner process is gone without finishing. Its log: ${join(RUNS(), runId, 'runner.log')}. Re-send the same jobs to flow_queue: files already on disk are skipped.` } : {}),
    runDir: join(RUNS(), runId),
  }
}

export function registerQueueTools(server: McpServer, endpoint: () => Promise<string>, toToolError: (e: unknown) => ToolResult) {
  server.registerTool(
    'flow_queue',
    {
      title: 'Queue several Flow jobs across tabs',
      description:
        'Run TWO OR MORE Flow jobs at once — stills, edits and video clips, mixed freely — each in its own browser tab, ' +
        `up to ${MAX_TABS} tabs (the most on this machine at once, across every run). More jobs than tabs simply wait for a ` +
        'free tab. For ONE job, use the ordinary flow_generate_image / flow_edit_image / flow_generate_video in the ' +
        'session\'s own tab. Returns AT ONCE with a runId; follow it with flow_queue_status (pass waitSeconds to wait).\n' +
        'Each job takes the same fields as its single tool: kind "image" = flow_generate_image (prompt, model, aspect?, ' +
        'numOutputs?, character?), "edit" = flow_edit_image (prompt, referenceImages, model, aspect?, numOutputs? default 2, ' +
        'character?), "video" = flow_generate_video (motion, model, aspect, startImage?, endImage?, count?, durationSeconds?, ' +
        'character?). Every job needs an absolute outPath; key (a short name) and why (the note that asked for it, for the ' +
        'recipe card) are optional. Model and aspect come from the story\'s badcode.md: there is no default.\n' +
        'project is the story\'s OWN Flow project id (its badcode.md, or scene.json flow_project) and story its slug. Jobs ' +
        'run in that story\'s helper projects ("<story> queue N", made on first use and reused), so a worker never shares a ' +
        'project grid with another tab. A job with a character runs in the story\'s own project, because Characters live ' +
        'there: while such a run is going, make no flow_* calls of your own in that project.\n' +
        'A job whose output file is already on disk is skipped, so re-sending a run only pays for what is missing. Stills ' +
        'and edits are retried up to 3 times on a flaky failure; a video only when the failure came before anything was ' +
        'submitted (a timed-out video may have been billed). Policy blocks and refused uploads are never retried: rewrite.',
      inputSchema: {
        project: z.string().min(1),
        story: z.string().min(1),
        tabs: z.number().int().min(1).max(MAX_TABS).optional(),
        jobs: z.array(JOB).min(1).max(200),
      },
    },
    async ({ project, story, tabs, jobs }) => {
      try {
        const problems = (jobs as Job[]).flatMap((j, i) => jobProblems(j, existsSync).map((p) => `job ${i + 1} (${jobKey(j, i)}): ${p}`))
        const outs = new Map<string, number>()
        for (const [i, j] of (jobs as Job[]).entries()) {
          if (outs.has(j.outPath)) problems.push(`job ${i + 1}: outPath is the same as job ${outs.get(j.outPath)! + 1}'s (${j.outPath})`)
          outs.set(j.outPath, i)
        }
        if (problems.length) return fail('INVALID_ARGS', problems.join('\n'), 'Nothing was queued. Fix these and send the whole list again.')
        const runId = `${stamp()}-${slug(story)}-${Math.random().toString(36).slice(2, 6)}`
        const dir = join(RUNS(), runId)
        mkdirSync(dir, { recursive: true })
        const spec: RunSpec = {
          runId, story: slug(story), home: project, endpoint: await endpoint(), tabs: tabsFor(jobs.length, tabs),
          staggerMs: Number(process.env.FLOW_QUEUE_STAGGER_MS ?? 8_000), createdAt: new Date().toISOString(), jobs: jobs as Job[],
        }
        writeFileSync(join(dir, 'run.json'), JSON.stringify(spec, null, 1))
        const log = openSync(join(dir, 'runner.log'), 'a')
        const child = spawn(join(REPO_ROOT, 'node_modules', '.bin', 'tsx'), [join(REPO_ROOT, 'packages/flow-mcp/src/queue-runner.ts'), dir], {
          cwd: REPO_ROOT, detached: true, stdio: ['ignore', log, log], env: process.env,
        })
        child.unref()
        return ok({
          runId,
          jobs: jobs.length,
          tabs: spec.tabs,
          slotsInUseNow: slotsInUse(),
          runDir: dir,
          next: `flow_queue_status { runId: "${runId}", waitSeconds: 300 } waits for it (call again until finished). Check each file as it lands, as you would after a single call.`,
        })
      } catch (err) {
        return toToolError(err)
      }
    },
  )

  server.registerTool(
    'flow_queue_status',
    {
      title: 'Flow queue status',
      description:
        'Where a flow_queue run is: every job\'s state (pending, running, done, failed, skipped), the files it made, and why ' +
        'anything failed; plus each tab and the project it works in. waitSeconds (up to 540) waits until the run finishes ' +
        'or the time is up, whichever is first — call it again to keep waiting. With no runId, lists the recent runs.',
      inputSchema: { runId: z.string().min(1).optional(), waitSeconds: z.number().int().min(0).max(540).optional() },
    },
    async ({ runId, waitSeconds }) => {
      try {
        if (!runId) {
          const ids = existsSync(RUNS()) ? readdirSync(RUNS()).sort().reverse().slice(0, 10) : []
          return ok({
            slotsInUse: slotsInUse(),
            runs: ids.map((id) => report(id)).filter(Boolean).map((r) => ({ runId: r!.runId, story: r!.story, state: r!.state, total: r!.total, done: r!.done, failed: r!.failed, pending: r!.pending, running: r!.running })),
          })
        }
        const end = Date.now() + (waitSeconds ?? 0) * 1000
        let r = report(runId)
        if (!r) return fail('RUN_NOT_FOUND', `No queue run ${runId}.`, 'flow_queue_status with no runId lists the recent runs.')
        while (!r!.finished && Date.now() < end) {
          await new Promise((res) => setTimeout(res, 5_000))
          r = report(runId)
        }
        return ok(r)
      } catch (err) {
        return toToolError(err)
      }
    },
  )

  server.registerTool(
    'flow_queue_stop',
    {
      title: 'Stop a Flow queue run',
      description:
        'Stop a flow_queue run now: jobs not started stay unstarted, jobs mid-render are marked failed (check the Flow ' +
        'gallery before re-running them: a clip may still finish there), and the run\'s tabs are closed.',
      inputSchema: { runId: z.string().min(1) },
    },
    async ({ runId }) => {
      try {
        const r = readStatus(runId)
        if (!r) return fail('RUN_NOT_FOUND', `No queue run ${runId}.`)
        if (!r.status || r.status.finishedAt || !pidAlive(r.status.pid)) return ok({ runId, note: 'not running' })
        process.kill(r.status.pid, 'SIGTERM')
        await new Promise((res) => setTimeout(res, 4_000))
        return ok(report(runId))
      } catch (err) {
        return toToolError(err)
      }
    },
  )
}
