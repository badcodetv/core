/**
 * Which pool worker runs which clip (scripts/scene/pool.mts). Pure, so it is tested without a browser.
 *
 * Worker 0 drives the scene's own Flow project; workers 1..K-1 each drive a project of their own, so the
 * grid-diff harvest in run.mts only ever sees its own tiles. Flow Characters live inside a project
 * (/project/<id>/character), so a job that casts one MUST go to worker 0. Everything else is dealt out
 * to whichever worker has the fewest jobs, which keeps the waves level.
 */
export interface PoolJob { key: string; character: string | null }

export function planPool<J extends PoolJob>(jobs: J[], tabs: number): J[][] {
  const k = Math.max(1, Math.floor(tabs))
  const lanes: J[][] = Array.from({ length: k }, () => [])
  for (const j of jobs) if (j.character) lanes[0]!.push(j)
  for (const j of jobs) {
    if (j.character) continue
    let best = 0
    for (let i = 1; i < k; i++) if (lanes[i]!.length < lanes[best]!.length) best = i
    lanes[best]!.push(j)
  }
  return lanes
}
