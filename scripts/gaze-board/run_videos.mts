/**
 * Render every clip in the gaze running order, unattended, with no model in the loop.
 *
 * Why this exists: 46 Veo clips is roughly an hour of FLOW's time, and none of it needs
 * judgement — the prompts were designed and frozen in motion.py, and the three ways a Flow
 * video call fails are all documented recoveries. Driving that from a chat loop spends tokens
 * on 46 rounds of "call, look, call again" to do what a `for` loop does for free. So this
 * script talks to the same FlowClient the MCP server uses (and therefore gets its fixes),
 * and writes one JSON line per clip to a log a human or an agent can read at any point.
 *
 *   npx tsx scripts/gaze-board/run_videos.mts            # everything not already on disk
 *   npx tsx scripts/gaze-board/run_videos.mts 12 21      # just #12..#21 (1-based, inclusive)
 *   FORCE=1 npx tsx scripts/gaze-board/run_videos.mts 1  # re-roll #1 even though it exists
 *
 * It is RESUMABLE by design: an existing non-empty .mp4 is skipped, so a crash, a browser
 * restart or a stopped run costs nothing but the clip that was in flight. Never delete a clip
 * to "start clean" — every one of them is paid for.
 */
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, statSync, unlinkSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const ENDPOINT = process.env.FLOW_CDP ?? 'http://localhost:9222'
const PROJECT = '5f273df4-2250-43bd-adc2-8c97f690b90e'
const LOG = join(REPO, 'scripts/gaze-board/run_videos.log')
const DOWNLOADS = join(homedir(), 'Downloads')

type Shot = { i: number; key: string; src: string; out: string; motion: string }

const shots: Shot[] = JSON.parse(
  execFileSync('python3', [join(REPO, 'scripts/gaze-board/motion.py'), 'json'], { encoding: 'utf8' }),
)

const [fromArg, toArg] = process.argv.slice(2)
const from = fromArg ? Number(fromArg) : 1
const to = toArg ? Number(toArg) : fromArg ? Number(fromArg) : shots.length
const force = process.env.FORCE === '1'

const STAGE = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/staged'
mkdirSync(STAGE, { recursive: true })

/**
 * The uniquely-named copy Flow will see, because its frame picker matches on BASENAME.
 *
 * 🔴 Our 46 stills live as `<shot-folder>/00-b.jpg` and share only TEN filenames between them —
 * `00-b.jpg` alone belongs to eight different shots. Upload the original and Flow animates
 * whichever `00-b.jpg` it finds first, producing a clip of the wrong photograph with the right
 * prompt. Measured twice on 2026-09-20; both times only the picture matcher noticed.
 */
function staged(shot: Shot): string {
  const dst = join(STAGE, `gaze-${String(shot.i).padStart(2, '0')}-${shot.key}.jpg`)
  if (!existsSync(dst)) copyFileSync(shot.src, dst)
  return dst
}

const md5 = (p: string) => createHash('md5').update(readFileSync(p)).digest('hex')
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

/**
 * Every clip we already hold, by checksum.
 *
 * The duplicate guard this feeds is the reason it exists: on 2026-09-19 the bridge harvested
 * the same pre-existing clip for two different prompts, and the ONLY signal that anything was
 * wrong was that the two files were byte-identical. The bridge bug is fixed, but a silent
 * wrong-clip is expensive enough (a whole run of plausible-looking garbage) to keep checking.
 */
const seen = new Map<string, string>()
for (const s of shots) if (existsSync(s.out) && statSync(s.out).size > 0) seen.set(md5(s.out), s.key)

/**
 * Recover a clip whose download threw ENOENT.
 *
 * Chrome still saved it, under Flow's own auto-title, in ~/Downloads — the clip is rendered
 * and BILLED, so re-running the generation to "get it back" pays twice for one clip. The age
 * check is what stops this grabbing an unrelated file from a previous session.
 */
function rescue(out: string): boolean {
  const cands = readdirSync(DOWNLOADS)
    .filter(f => f.endsWith('.mp4'))
    .map(f => ({ f: join(DOWNLOADS, f), t: statSync(join(DOWNLOADS, f)).mtimeMs }))
    .sort((a, b) => b.t - a.t)
  const newest = cands[0]
  if (!newest || Date.now() - newest.t > 10 * 60_000) return false
  // copy-then-unlink, never rename: ~/Downloads is on the WSL disk and the clips live on /mnt/d,
  // so a rename is a cross-device move and throws EXDEV — which crashed a run mid-way with a
  // perfectly good clip already downloaded and sitting there.
  copyFileSync(newest.f, out)
  unlinkSync(newest.f)
  return true
}

async function once(shot: Shot): Promise<{ ok: true } | { ok: false; why: string; retry: boolean }> {
  const client = await FlowClient.connect(ENDPOINT)
  try {
    await client.openProject({ id: PROJECT })
    await client.generateVideo({
      motion: shot.motion,
      outPath: shot.out,
      startImage: staged(shot),
      model: 'Veo 3.1 Fast',
      aspect: '16:9',
      count: 1,
      durationSeconds: 8,
    })
    return { ok: true }
  } catch (err) {
    const why = err instanceof Error ? err.message : String(err)
    // ENOENT: rendered, billed, and sitting in ~/Downloads. Recovering is not a retry.
    if (/ENOENT|saveAs/.test(why) && rescue(shot.out)) return { ok: true }
    // Flow gave up and says it did not charge us, so trying again is free and often works.
    if (/GENERATION_REFUSED/.test(why)) return { ok: false, why, retry: true }
    // A timeout may still have produced a clip; a rescue is worth one look before retrying.
    if (/TIMEOUT/.test(why) && rescue(shot.out)) return { ok: true }
    if (/TIMEOUT|DISCONNECT|Target closed|Execution context/.test(why)) return { ok: false, why, retry: true }
    // POLICY_BLOCKED needs a human or a model to soften the prompt — never retry it verbatim.
    return { ok: false, why, retry: false }
  } finally {
    await client.close().catch(() => {})
  }
}

say({ event: 'start', from, to, total: shots.length, endpoint: ENDPOINT })

let made = 0
let skipped = 0
const failed: { key: string; why: string }[] = []

for (const shot of shots) {
  if (shot.i < from || shot.i > to) continue
  if (!force && existsSync(shot.out) && statSync(shot.out).size > 0) {
    skipped++
    continue
  }
  let done = false
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    const r = await once(shot)
    if (!r.ok) {
      say({ event: 'fail', i: shot.i, key: shot.key, attempt, retry: r.retry, why: r.why.slice(0, 300) })
      if (!r.retry) break
      continue
    }
    const sum = md5(shot.out)
    const clash = seen.get(sum)
    if (clash) {
      // Identical bytes to a clip we already have: the harvest grabbed the wrong tile.
      // Bin it and try once more rather than keeping a file we know is the wrong picture.
      unlinkSync(shot.out)
      say({ event: 'duplicate', i: shot.i, key: shot.key, sameAs: clash, attempt })
      continue
    }
    seen.set(sum, shot.key)
    made++
    done = true
    say({ event: 'ok', i: shot.i, key: shot.key, bytes: statSync(shot.out).size, md5: sum, attempt })
  }
  if (!done && !failed.some(f => f.key === shot.key)) failed.push({ key: shot.key, why: 'see log' })
}

say({ event: 'done', made, skipped, failed })
if (failed.length) process.exitCode = 1
