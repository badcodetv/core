/**
 * Render the gaze's clips in PARALLEL: submit every prompt without waiting, then collect.
 *
 * The serial runner (run_videos.mts) spends its whole life waiting — submit, wait ~90s for
 * Flow to render, download, repeat. But Flow renders server-side and queues happily, so the
 * waiting is pure dead time: 46 clips cost an hour when the submitting itself is fifteen
 * minutes. This script splits the job into three phases that each do one thing well.
 *
 *   A. SUBMIT   every shot, back to back, never waiting for a result.
 *   B. HARVEST  once the gallery has as many new finished tiles as we submitted.
 *   C. MATCH    each downloaded clip back to the still that made it, BY PICTURE.
 *
 * Phase C is what makes phase A safe. With one generation in flight you always know which
 * clip is yours; with forty in flight you do not, and Flow's own titles collide badly (four
 * playground shots, three power stations). But image-to-video means a clip's FIRST FRAME is
 * its source still, so the mapping is recoverable from the pixels — no ordering assumption,
 * no title parsing, no DOM guesswork. match_clips.py does that and renames into cut order.
 *
 * 🔴 STAGING IS NOT OPTIONAL. Flow's frame picker matches the uploaded file's BASENAME, and
 * our 46 stills share just 10 filenames between them (eight different shots are `00-b.jpg`).
 * Measured 2026-09-20: a clip came back animated from the wrong photograph with the right
 * prompt, and nothing but the picture matcher noticed. So every still is copied to a
 * uniquely-named staging file first, and that copy is what gets uploaded.
 *
 *   npx tsx scripts/gaze-board/run_parallel.mts              # everything not on disk
 *   npx tsx scripts/gaze-board/run_parallel.mts 5 20         # just #5..#20
 *   npx tsx scripts/gaze-board/run_parallel.mts --harvest    # skip submitting, collect only
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readdirSync, statSync, unlinkSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const ENDPOINT = process.env.FLOW_CDP ?? 'http://localhost:9222'
const PROJECT = '5f273df4-2250-43bd-adc2-8c97f690b90e'
const ROOT = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze'
const STAGE = join(ROOT, 'staged')
const INBOX = join(ROOT, 'inbox')
const OUT = join(ROOT, 'video')
const LOG = join(REPO, 'scripts/gaze-board/run_videos.log')

type Shot = { i: number; key: string; src: string; out: string; motion: string }

const shots: Shot[] = JSON.parse(
  execFileSync('python3', [join(REPO, 'scripts/gaze-board/motion.py'), 'json'], { encoding: 'utf8' }),
)

const args = process.argv.slice(2)
const harvestOnly = args.includes('--harvest')
const nums = args.filter(a => /^\d+$/.test(a)).map(Number)
const from = nums[0] ?? 1
const to = nums[1] ?? (nums.length === 1 ? nums[0]! : shots.length)

for (const d of [STAGE, INBOX, OUT]) mkdirSync(d, { recursive: true })

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

/** Shots we still owe a clip for — an existing output is proof we already have one. */
const todo = shots.filter(s => s.i >= from && s.i <= to && !(existsSync(s.out) && statSync(s.out).size > 0))

/** The uniquely-named copy Flow will see. Its basename is the whole point. */
const stagedPath = (s: Shot) => join(STAGE, `gaze-${String(s.i).padStart(2, '0')}-${s.key}.jpg`)

const client = await FlowClient.connect(ENDPOINT)
try {
  await client.openProject({ id: PROJECT })
  const before = new Set(await client.videoTiles())
  say({ event: 'phase', phase: harvestOnly ? 'harvest-only' : 'submit', todo: todo.length, tilesBefore: before.size })

  let submitted = 0
  if (!harvestOnly) {
    for (const s of todo) {
      const staged = stagedPath(s)
      if (!existsSync(staged)) copyFileSync(s.src, staged)
      try {
        await client.submitVideo({
          motion: s.motion,
          outPath: s.out, // unused by submitVideo; kept so the request reads the same as generateVideo's
          startImage: staged,
          model: 'Veo 3.1 Fast',
          aspect: '16:9',
          count: 1,
          durationSeconds: 8,
        })
        submitted++
        say({ event: 'submitted', i: s.i, key: s.key, n: submitted, of: todo.length })
      } catch (err) {
        say({ event: 'submit-fail', i: s.i, key: s.key, why: (err as Error).message.slice(0, 200) })
      }
    }
  }

  // Phase B. Wait for the gallery to grow by however many we actually got in, then take
  // everything new in one pass — the keys are signed URLs and rotate, so they are read and
  // used immediately rather than held.
  const want = harvestOnly ? 1 : submitted
  const deadline = Date.now() + 25 * 60_000
  let fresh: string[] = []
  while (Date.now() < deadline) {
    fresh = (await client.videoTiles()).filter(k => !before.has(k))
    say({ event: 'waiting', have: fresh.length, want })
    if (fresh.length >= want) break
    await new Promise(r => setTimeout(r, 20_000))
  }

  say({ event: 'phase', phase: 'download', tiles: fresh.length })
  let got = 0
  for (const [n, key] of fresh.entries()) {
    const dst = join(INBOX, `raw-${Date.now()}-${n}.mp4`)
    try {
      await client.harvestVideoTile(key, dst)
      got++
    } catch (err) {
      say({ event: 'harvest-fail', n, why: (err as Error).message.slice(0, 160) })
      // The clip is rendered and BILLED; Chrome may still have saved it under Flow's own name.
      const cands = readdirSync(join(process.env.HOME!, 'Downloads'))
        .filter(f => f.endsWith('.mp4'))
        .map(f => join(process.env.HOME!, 'Downloads', f))
        .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)
      if (cands[0] && Date.now() - statSync(cands[0]).mtimeMs < 10 * 60_000) {
        copyFileSync(cands[0], dst)
        unlinkSync(cands[0])
        got++
      }
    }
  }
  say({ event: 'done', submitted, harvested: got, inbox: INBOX })
} finally {
  await client.close().catch(() => {})
}
