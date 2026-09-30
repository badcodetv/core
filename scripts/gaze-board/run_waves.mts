/**
 * Fill in whatever the cut is still missing, in WAVES — submit a few, collect, repeat.
 *
 * The one-big-batch attempt (run_parallel.mts) submitted forty prompts in thirteen minutes and
 * Flow accepted every one — the prompt box cleared each time, which is its own acknowledgement
 * — but only sixteen of the forty ever produced a clip, scattered right through the run rather
 * than stopping at some point. A second collection eleven minutes later found nothing new, so
 * they were not queued and slow, they were dropped. The most plausible reading is a cap on how
 * many generations one project may have in flight, silently enforced.
 *
 * So: waves. Small enough to stay under whatever the ceiling is, large enough that the waiting
 * still overlaps. Each wave recomputes what is missing FROM DISK, which makes the whole thing
 * self-correcting and safe to re-run — a clip already collected is never paid for twice, and a
 * wave that half-fails simply leaves a shorter list for the next one.
 *
 *   npx tsx scripts/gaze-board/run_waves.mts            # default wave size
 *   WAVE=4 npx tsx scripts/gaze-board/run_waves.mts     # smaller, if 6 still drops clips
 */
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const ENDPOINT = process.env.FLOW_CDP ?? 'http://localhost:9222'
const PROJECT = '5f273df4-2250-43bd-adc2-8c97f690b90e'
const STAGE = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/staged'
const LOG = join(REPO, 'scripts/gaze-board/run_videos.log')
const WAVE = Number(process.env.WAVE ?? 6)
/** Long enough for a wave to render (~90s each, overlapping), short enough not to idle. */
const SETTLE_MS = Number(process.env.SETTLE_MS ?? 240_000)

type Shot = { i: number; key: string; src: string; out: string; motion: string }
const shots: Shot[] = JSON.parse(
  execFileSync('python3', [join(REPO, 'scripts/gaze-board/motion.py'), 'json'], { encoding: 'utf8' }),
)
mkdirSync(STAGE, { recursive: true })

const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

/** Truth lives on disk, not in this process: re-read it every wave. */
const missing = () => shots.filter(s => !(existsSync(s.out) && statSync(s.out).size > 0))

/**
 * Collect everything Flow has finished, then let the picture matcher file it into cut order.
 *
 * `want` is how many clips this wave actually got submitted, and passing it is not an
 * optimisation — it is the harvester's stop condition. Flow lists newest first, so the clips a
 * wave produced are at the TOP of the gallery; without a target the harvest walks on past them
 * into everything we already own, and every one of those tiles has been recycled out of the
 * virtualised DOM, so each costs a 30s timeout to fail. Measured 2026-09-21: twenty minutes of
 * that, collecting nothing, looking from outside exactly like a hung browser.
 */
function collect(want: number) {
  const steps: [string, string[], NodeJS.ProcessEnv][] = [
    ['npx', ['tsx', join(REPO, 'scripts/gaze-board/harvest.mts')], { ...process.env, WANT: String(want) }],
    ['python3', [join(REPO, 'scripts/gaze-board/match_clips.py'), '--apply'], process.env],
  ]
  for (const [cmd, args, env] of steps) {
    try {
      // The per-step cap is a backstop for a step that hangs before its own guards can fire.
      execFileSync(cmd, args, { cwd: REPO, stdio: 'inherit', timeout: 12 * 60_000, env })
    } catch (err) {
      say({ event: 'collect-fail', cmd, why: (err as Error).message.slice(0, 160) })
    }
  }
}

let stuck = 0
for (let wave = 1; wave <= 20; wave++) {
  const todo = missing()
  if (!todo.length) {
    say({ event: 'all-present', wave })
    break
  }
  const batch = todo.slice(0, WAVE)
  say({ event: 'wave', wave, missing: todo.length, submitting: batch.map(s => s.key) })

  let submitted = 0
  const client = await FlowClient.connect(ENDPOINT)
  try {
    await client.openProject({ id: PROJECT })
    for (const s of batch) {
      // Uniquely-named copy: Flow's frame picker matches on BASENAME, and our stills share
      // only ten filenames between forty-six shots.
      const staged = join(STAGE, `gaze-${String(s.i).padStart(2, '0')}-${s.key}.jpg`)
      if (!existsSync(staged)) copyFileSync(s.src, staged)
      try {
        await client.submitVideo({
          motion: s.motion,
          outPath: s.out,
          startImage: staged,
          model: 'Veo 3.1 Fast',
          aspect: '16:9',
          count: 1,
          durationSeconds: 8,
        })
        submitted++
        say({ event: 'submitted', i: s.i, key: s.key, wave })
      } catch (err) {
        say({ event: 'submit-fail', i: s.i, key: s.key, wave, why: (err as Error).message.slice(0, 160) })
      }
    }
  } finally {
    await client.close().catch(() => {})
  }

  // Nothing went in, so there is nothing to come back for — collecting would only walk the
  // gallery we already own. A wave that submits nothing is a broken page, not a slow one.
  if (!submitted) {
    say({ event: 'nothing-submitted', wave })
    stuck++
    if (stuck >= 2) {
      say({ event: 'stalled', wave, remaining: missing().length })
      break
    }
    continue
  }

  await new Promise(r => setTimeout(r, SETTLE_MS))
  collect(submitted)

  const left = missing().length
  say({ event: 'wave-done', wave, remaining: left })
  // Two waves that change nothing means the cap theory is wrong and something else is broken;
  // stop rather than spend credits in a loop nobody is watching.
  stuck = left === todo.length ? stuck + 1 : 0
  if (stuck >= 2) {
    say({ event: 'stalled', wave, remaining: left })
    break
  }
}
say({ event: 'waves-done', remaining: missing().map(s => s.key) })
