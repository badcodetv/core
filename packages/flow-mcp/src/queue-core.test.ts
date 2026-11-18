import { describe, expect, it } from 'vitest'
import { MAX_TABS, firstOutput, jobKey, jobProblems, nextJob, shouldRetry, summarise, tabsFor, workLeftFor, type Job, type JobState } from './queue-core'

const img = (o: Partial<Job> = {}): Job => ({ kind: 'image', prompt: 'a shop at night', outPath: '/x/a.jpg', model: 'Nano Banana 2.1', ...o } as Job)
const vid = (o: Partial<Job> = {}): Job => ({ kind: 'video', motion: 'slow push in', outPath: '/x/a.mp4', model: 'Veo 3.1 Lite', aspect: '16:9', startImage: '/x/s.jpg', ...o } as Job)
const st = (...s: JobState[]) => s.map((state) => ({ state }))
const yes = () => true

describe('jobProblems', () => {
  it('passes a complete still', () => expect(jobProblems(img(), yes)).toEqual([]))
  it('needs a model (no default)', () => expect(jobProblems(img({ model: '' }), yes).join()).toMatch(/MODEL_REQUIRED/))
  it('needs an absolute outPath', () => expect(jobProblems(img({ outPath: 'a.jpg' }), yes).join()).toMatch(/absolute/))
  it('needs an edit reference that exists', () => {
    const e = { kind: 'edit', prompt: 'add a figure', referenceImages: ['/x/r.jpg'], outPath: '/x/e.jpg', model: 'Nano Banana 2.1' } as Job
    expect(jobProblems(e, () => false).join()).toMatch(/not found/)
    expect(jobProblems(e, yes)).toEqual([])
  })
  it('needs a video aspect (no default)', () => expect(jobProblems(vid({ aspect: undefined } as Partial<Job>), yes).join()).toMatch(/ASPECT_REQUIRED/))
  it('refuses an end frame with no start frame', () =>
    expect(jobProblems(vid({ startImage: undefined, endImage: '/x/e.jpg' } as Partial<Job>), yes).join()).toMatch(/END_ONLY/))
})

describe('tabsFor', () => {
  it('never more than the jobs', () => expect(tabsFor(3)).toBe(3))
  it(`never more than ${MAX_TABS}`, () => expect(tabsFor(20, 50)).toBe(MAX_TABS))
  it('what was asked otherwise', () => expect(tabsFor(20, 4)).toBe(4))
  it('at least one', () => expect(tabsFor(5, 0)).toBe(1))
})

describe('nextJob', () => {
  const specs = [img(), img({ character: 'Karen' }), img()]
  it('a helper tab skips Character jobs', () => expect(nextJob(st('done', 'pending', 'pending'), specs, false)).toBe(2))
  it('the home tab takes Character jobs first', () => expect(nextJob(st('pending', 'pending', 'pending'), specs, true)).toBe(1))
  it('the home tab takes ordinary jobs when no Character job is left', () => expect(nextJob(st('pending', 'done', 'pending'), specs, true)).toBe(0))
  it('-1 when nothing is left for this tab', () => {
    expect(nextJob(st('done', 'pending', 'running'), specs, false)).toBe(-1)
    expect(workLeftFor(st('done', 'pending', 'running'), specs, true)).toBe(true)
  })
})

describe('shouldRetry', () => {
  it('retries a flaky still', () => expect(shouldRetry('image', 'TIMEOUT: no new canvas', 1)).toBe(true))
  it('never retries a policy block', () => expect(shouldRetry('image', 'POLICY_BLOCKED', 1)).toBe(false))
  it('never retries the copy guard (look in the gallery first)', () => expect(shouldRetry('edit', 'REFERENCE_COPY_ONLY: ...', 1)).toBe(false))
  it('retries a video only when nothing was submitted', () => {
    expect(shouldRetry('video', 'UPLOAD_STUCK: x.jpg never appeared', 1)).toBe(true)
    expect(shouldRetry('video', 'TIMEOUT: waiting for video tiles', 1)).toBe(false) // may have rendered and been billed
  })
  it('stops after three attempts', () => expect(shouldRetry('image', 'TIMEOUT', 3)).toBe(false))
})

describe('the rest', () => {
  it('names a job by its key, else its file', () => {
    expect(jobKey(img({ key: 'beat 3' }), 0)).toBe('beat 3')
    expect(jobKey(img(), 0)).toBe('a.jpg')
  })
  it('knows the first file a job writes', () => {
    expect(firstOutput(img())).toBe('/x/a.jpg')
    expect(firstOutput({ kind: 'edit', prompt: 'p', referenceImages: ['/r.jpg'], outPath: '/x/e.jpg', model: 'm' } as Job)).toBe('/x/e-a.jpg')
  })
  it('summarises a run', () => {
    expect(summarise(st('done', 'failed', 'skipped'))).toMatchObject({ total: 3, finished: true })
    expect(summarise(st('done', 'running')).finished).toBe(false)
  })
})
