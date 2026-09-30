/**
 * Collect every finished clip out of the Flow project, by SCROLLING the gallery.
 *
 * 🔴 Why this is not just "read the tiles and download them": Flow's media gallery is
 * VIRTUALISED. Only the tiles near the viewport exist in the DOM at all, so a count taken from
 * the page is a count of what is currently on screen — never of what the project holds.
 * Measured 2026-09-20: while forty clips were rendering, the visible tile count wobbled
 * 8 -> 6 -> 8 -> 7 as the list recycled, so `run_parallel`'s "wait until forty new tiles
 * appear" could never have come true no matter how long it waited. The user spotted the
 * symptom first, from the other side: stills in the gallery with no clip beside them.
 *
 * So: download what is visible, which scrolls each tile into view and pulls the next batch in,
 * and keep going until several passes in a row turn up nothing new. Everything lands in an
 * inbox under a throwaway name; match_clips.py then works out what each one actually IS from
 * its first frame, which is the only identification that survives a virtualised list.
 *
 *   npx tsx scripts/gaze-board/harvest.mts            # walk until the gallery goes quiet
 *   WANT=4 npx tsx scripts/gaze-board/harvest.mts     # stop after four clips land
 */
import { existsSync, mkdirSync, readdirSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { appendFileSync } from 'node:fs'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'

const REPO = new URL('../..', import.meta.url).pathname
const ENDPOINT = process.env.FLOW_CDP ?? 'http://localhost:9222'
const PROJECT = '5f273df4-2250-43bd-adc2-8c97f690b90e'
const INBOX = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/inbox'
const LOG = join(REPO, 'scripts/gaze-board/run_videos.log')

mkdirSync(INBOX, { recursive: true })
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line)
  appendFileSync(LOG, line + '\n')
}

const already = new Set(readdirSync(INBOX).filter(f => f.endsWith('.mp4')))

/**
 * How many NEW clips this harvest is here for, and the three ways it gives up.
 *
 * 🔴 Why the guards exist: on 2026-09-21 a harvest with none of them ran for twenty minutes and
 * collected nothing. It had already pulled the four clips it wanted — they sit at the TOP of the
 * gallery, because Flow lists newest first — and then kept walking backwards through forty-two
 * clips we already owned. Each of those tiles had been recycled out of the virtualised DOM, so
 * every one cost a full 30s locator timeout before failing. From outside it looked exactly like
 * a hang: a browser open on the right project, doing nothing, for as long as anyone watched.
 *
 * So a harvest now stops when it has what it came for (WANT), when the tiles stop resolving
 * (FAIL_STREAK), or when it has simply been too long (MAX_MS) — whichever comes first.
 */
const WANT = Number(process.env.WANT ?? 0) // 0 = no target, walk the gallery until it goes quiet
const FAIL_STREAK = Number(process.env.FAIL_STREAK ?? 3)
const MAX_MS = Number(process.env.HARVEST_MAX_MS ?? 8 * 60_000)

const client = await FlowClient.connect(ENDPOINT)
try {
  await client.openProject({ id: PROJECT })
  const seen = new Set<string>()
  const deadline = Date.now() + MAX_MS
  let order = already.size
  let idle = 0
  let got = 0
  let misses = 0
  let stop: string | null = null
  // `order` doubles as the filename counter AND the record of gallery position, which matters
  // when two clips share a first frame (a re-roll of a shot we already had): the gallery lists
  // newest first, so the lower-numbered file is the more recent generation.
  while (idle < 4 && !stop) {
    const keys = await client.videoTiles()
    const fresh = keys.filter(k => !seen.has(k))
    for (const k of fresh) {
      if (stop) break
      seen.add(k)
      const dst = join(INBOX, `raw-${String(order).padStart(3, '0')}.mp4`)
      order++
      try {
        // The download scrolls its own tile into view, which is also what pulls the NEXT batch
        // of virtualised tiles into the DOM — the scroll and the harvest are the same action.
        await client.harvestVideoTile(k, dst)
        got++
        misses = 0
        say({ event: 'harvested', file: dst, bytes: existsSync(dst) ? statSync(dst).size : 0, got, want: WANT })
      } catch (err) {
        // A recycled tile, not a broken clip. Cheap once; ruinous forty times in a row.
        misses++
        say({ event: 'harvest-fail', file: dst, misses, why: (err as Error).message.slice(0, 140) })
      }
      if (WANT && got >= WANT) stop = 'got-what-we-came-for'
      else if (misses >= FAIL_STREAK) stop = 'tiles-stopped-resolving'
      else if (Date.now() > deadline) stop = 'out-of-time'
    }
    if (stop) break
    idle = fresh.length ? 0 : idle + 1
    say({ event: 'scan', visible: keys.length, fresh: fresh.length, total: seen.size, idle })
    if (Date.now() > deadline) stop = 'out-of-time'
    await new Promise(r => setTimeout(r, 1_500))
  }
  say({ event: 'harvest-done', tiles: seen.size, got, want: WANT, stopped: stop ?? 'gallery-quiet', inbox: INBOX })
} finally {
  await client.close().catch(() => {})
}
