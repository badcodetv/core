/**
 * The Flow queue (flow_queue, 2026-11-18): the pure parts — what a job is, which tab takes which job,
 * what is worth a retry, and the status a session reads. No browser here, so it is all unit-tested.
 *
 * The rule it implements (Kai, 2026-11-18): ONE JOB PER TAB. A single job runs in the session's own tab
 * (the ordinary flow_* tools). Two or more go in a queue that opens up to MAX_TABS tabs of the signed-in
 * browser, each in a Flow project of its own, and every tab takes the next job as soon as it is free.
 * More jobs than tabs simply wait. Two jobs in ONE tab fight over its prompt box, uploads and downloads
 * (law 16); separate tabs and separate projects do not.
 */
import { requireImageModel, requireVideoAspect, requireVideoModel, type VideoAspect } from './flow-client'
import { videoRequestError } from './video-mode'
import { candidateOutPath } from './candidates'

/** The most tabs the queue (and scripts/scene/pool.mts) may hold at once, across every run on this machine. */
export const MAX_TABS = 10

export interface ImageJob {
  kind: 'image'
  prompt: string
  outPath: string
  model: string
  aspect?: string
  numOutputs?: number
  character?: string
}
export interface EditJob {
  kind: 'edit'
  prompt: string
  referenceImages: string[]
  outPath: string
  model: string
  aspect?: string
  numOutputs?: number
  character?: string
}
export interface VideoJob {
  kind: 'video'
  motion: string
  outPath: string
  model: string
  aspect: VideoAspect
  startImage?: string
  endImage?: string
  count?: number
  durationSeconds?: number
  character?: string
}
/** `key` names the job in the status (default: the output file's name); `why` goes on the recipe card. */
export type Job = (ImageJob | EditJob | VideoJob) & { key?: string; why?: string }

export type JobState = 'pending' | 'running' | 'done' | 'failed' | 'skipped'
export interface JobStatus {
  i: number
  key: string
  kind: Job['kind']
  outPath: string
  state: JobState
  attempts: number
  tab?: number
  project?: string
  files?: string[]
  error?: string
  startedAt?: string
  endedAt?: string
}

const isAbs = (p: string) => p.startsWith('/')

/** Everything wrong with a job before a browser is touched. Empty means it can run. */
export function jobProblems(job: Job, exists: (p: string) => boolean): string[] {
  const out: string[] = []
  const tryIt = (f: () => unknown) => {
    try {
      f()
    } catch (err) {
      out.push((err as Error).message)
    }
  }
  if (!job.outPath || !isAbs(job.outPath)) out.push(`outPath must be an absolute path (got "${job.outPath}")`)
  const files: string[] = []
  if (job.kind === 'image') {
    tryIt(() => requireImageModel(job.model, 'flow_queue image'))
    if (!job.prompt?.trim()) out.push('prompt is empty')
  } else if (job.kind === 'edit') {
    tryIt(() => requireImageModel(job.model, 'flow_queue edit'))
    if (!job.prompt?.trim()) out.push('prompt is empty')
    if (!job.referenceImages?.length) out.push('an edit needs referenceImages')
    if ((job.referenceImages?.length ?? 0) > 3) out.push('an edit takes at most 3 referenceImages')
    files.push(...(job.referenceImages ?? []))
  } else if (job.kind === 'video') {
    tryIt(() => requireVideoModel(job.model, 'flow_queue video'))
    tryIt(() => requireVideoAspect(job.aspect, 'flow_queue video'))
    if (!job.motion?.trim()) out.push('motion is empty')
    const p = videoRequestError({ startImage: job.startImage, endImage: job.endImage, model: job.model, durationSeconds: job.durationSeconds ?? 8 })
    if (p) out.push(p)
    for (const f of [job.startImage, job.endImage]) if (f) files.push(f)
  } else {
    out.push(`unknown kind "${(job as { kind?: string }).kind}"`)
  }
  for (const f of files) {
    if (!isAbs(f)) out.push(`input must be an absolute path (got "${f}")`)
    else if (!exists(f)) out.push(`input not found: ${f}`)
  }
  return out
}

export const jobKey = (job: Job, i: number): string =>
  job.key || job.outPath.split('/').pop() || `job-${i + 1}`

/** True when a job pins its tab to the story's OWN project: Flow Characters live inside one project. */
export const needsHomeProject = (job: Job): boolean => Boolean(job.character)

/** How many tabs a run opens: what was asked, never more than the jobs, never more than MAX_TABS. */
export function tabsFor(jobs: number, asked?: number): number {
  return Math.max(1, Math.min(MAX_TABS, jobs, Math.floor(asked ?? MAX_TABS)))
}

/**
 * The next job a free tab should take, or -1. The HOME tab (the story's own project) takes Character jobs
 * first, then anything; every other tab (a helper project) takes only jobs without a Character.
 */
export function nextJob(jobs: Pick<JobStatus, 'state'>[], specs: Job[], home: boolean): number {
  if (home) {
    const c = jobs.findIndex((j, i) => j.state === 'pending' && needsHomeProject(specs[i]!))
    if (c >= 0) return c
  }
  return jobs.findIndex((j, i) => j.state === 'pending' && !needsHomeProject(specs[i]!))
}

/** True while some pending job can still be taken by a tab of this kind. */
export const workLeftFor = (jobs: Pick<JobStatus, 'state'>[], specs: Job[], home: boolean): boolean =>
  nextJob(jobs, specs, home) >= 0

/**
 * Errors where nothing was generated or paid for, so the same job can simply run again (on any tab).
 * Videos are retried ONLY on these: a video that timed out may have rendered and been billed.
 */
const BEFORE_SPEND =
  /UPLOAD_STUCK|FRAME_NOT_ATTACHED|FRAME_SLOTS_NOT_FOUND|SUBMIT_FAILED|TAB_GONE|NO_CONTEXT|ECONNRESET|ECONNREFUSED|Target closed|Target page, context or browser has been closed|browser has been closed|LOCK_TIMEOUT|NOT_IN_PROJECT|unusual activity/i
/** Errors that a retry can never fix: the prompt, the picture or the request itself is the problem. */
const PERMANENT =
  /POLICY_BLOCKED|UPLOAD_REFUSED|MODEL_REQUIRED|ASPECT_REQUIRED|VIDEO_DURATION_|VIDEO_END_ONLY|VIDEO_FRAMES_UNAVAILABLE|CHARACTER_NOT_FOUND|CHARACTER_CAST_UNAVAILABLE|REFERENCE_COPY_ONLY|INVALID|IMAGE_MODEL|VIDEO_MODEL/i

export const MAX_ATTEMPTS = 3

/** Should a job that failed with `message` on attempt `attempts` (1-based) go back in the queue? */
export function shouldRetry(kind: Job['kind'], message: string, attempts: number): boolean {
  if (attempts >= MAX_ATTEMPTS) return false
  if (PERMANENT.test(message)) return false
  if (kind === 'video') return BEFORE_SPEND.test(message)
  return true // stills and edits are free: a timeout or a flaky download is worth one more go
}

/** The first file a job writes (candidates get -a/-b… suffixes, as candidates.ts names them): on disk = done. */
export function firstOutput(job: Job): string {
  const n = job.kind === 'video' ? job.count ?? 1 : job.kind === 'edit' ? job.numOutputs ?? 2 : job.numOutputs ?? 1
  return candidateOutPath(job.outPath, 0, n)
}

export interface RunSummary {
  total: number
  pending: number
  running: number
  done: number
  failed: number
  skipped: number
  finished: boolean
}

export function summarise(jobs: Pick<JobStatus, 'state'>[]): RunSummary {
  const n = (s: JobState) => jobs.filter((j) => j.state === s).length
  const s = { total: jobs.length, pending: n('pending'), running: n('running'), done: n('done'), failed: n('failed'), skipped: n('skipped') }
  return { ...s, finished: s.pending === 0 && s.running === 0 }
}
