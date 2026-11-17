/**
 * new-scene stage 3, in PARALLEL: run a scene's missing Flow clips across K tabs of the signed-in browser at once
 * (Kai + Jack, 2026-11-17: "make more efficient use of Flow with concurrency").
 *
 * Why tabs work where two calls did not: law 16 (flow-automation) is two jobs sharing ONE compose bar. Every tab has
 * its own bar, and every worker here has its own tab AND its own Flow project, so its grid-diff harvest only ever sees
 * its own tiles. Tabs share the browser's Google login, so unlike a second channel there is nothing to sign in to.
 *
 *   FLOW_CDP_PORT=<port> TABS=3 npx tsx scripts/scene/pool.mts <scene-dir> [key …]
 *
 * - Worker w0 drives the scene's own project (scene.json flow_project) and takes every job that casts a Flow
 *   Character, because Characters live inside a project. Workers w1..w(K-1) get projects of their own, made once and
 *   remembered in <media>/video/inbox/pool.json, so a re-run reuses them instead of making new ones.
 * - Each worker is a plain run.mts (WORKER, OPEN_TAB=1, FLOW_PROJECT): same waves, refusal retries, settings record and
 *   match.py naming, so a clip lands exactly where the single runner would put it. Re-running only pays for what is missing.
 * - It opens its own tabs and closes them at the end. It never drives a tab that was already open, and the flow MCP
 *   (FlowClient.connect) skips pool tabs, so a session's MCP call cannot land in a worker's compose bar.
 * - Workers start STAGGER_MS apart (default 20 s) so their first uploads don't all hit Flow in the same second.
 *
 * 🔴 Credits and Google's rate limits are per ACCOUNT. More tabs is not free throughput past Google's own limit, which
 * is unmeasured: start at TABS=3, read the pool log, then try more.
 */
import { execFileSync, spawn } from 'node:child_process'
import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../packages/flow-mcp/src/flow-client'
import { planPool } from './pool-plan'

const REPO = new URL('../..', import.meta.url).pathname
const HERE = join(REPO, 'scripts/scene')
const SCENE = process.argv[2]
if (!SCENE || !existsSync(join(SCENE, 'scene.json'))) throw new Error('usage: pool.mts <scene-dir> [key …]')
const CFG = JSON.parse(readFileSync(join(SCENE, 'scene.json'), 'utf8'))
const MEDIA = execFileSync('python3', [join(HERE, '../drive/localmap.py'), 'path', CFG.media], { encoding: 'utf8' }).trim()
if (!CFG.flow_project) throw new Error('scene.json has no flow_project')
const INBOX = join(MEDIA, 'video/inbox')
mkdirSync(INBOX, { recursive: true })
const TABS = Math.max(1, Number(process.env.TABS ?? 3))
const STAGGER_MS = Number(process.env.STAGGER_MS ?? 20_000)
const ENDPOINT = process.env.FLOW_CDP ?? `http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`
const LOG = join(MEDIA, 'video/pool.log')
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), pool: true, ...o })
  console.log(line)
  writeFileSync(LOG, line + '\n', { flag: 'a' })
}

type Shot = { key: string; plate: string | null; out: string; character: string | null }
const shots = (): Shot[] =>
  JSON.parse(execFileSync('python3', [join(HERE, 'shots.py'), SCENE], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'inherit'] }))
const only = process.argv.slice(3)
const missing = () => shots().filter((s) => s.plate && (!only.length || only.includes(s.key)) && !(existsSync(s.out) && statSync(s.out).size > 0))

const todo = missing()
if (!todo.length) { say({ event: 'all-present' }); process.exit(0) }
const lanes = planPool(todo, Math.min(TABS, todo.length)).filter((l, i) => i === 0 || l.length)

// Projects: w0 = the scene's; the rest from pool.json, made (and saved) when there are not enough yet.
const POOL = join(INBOX, 'pool.json')
const saved: string[] = existsSync(POOL) ? JSON.parse(readFileSync(POOL, 'utf8')).projects ?? [] : []
while (saved.length < lanes.length - 1) {
  const c = await FlowClient.openTab(ENDPOINT, 'https://flow.google.com', 'setup')
  try {
    const p = await c.createProject(`${CFG.scene} pool ${saved.length + 1}`)
    saved.push(p.id)
    writeFileSync(POOL, JSON.stringify({ projects: saved, why: 'pool.mts worker projects (w1, w2, …), reused on every run' }, null, 1))
    say({ event: 'project-made', worker: `w${saved.length}`, id: p.id, name: p.name })
  } finally { await c.closeTab() }
}
const projects = [CFG.flow_project as string, ...saved]

say({ event: 'start', tabs: lanes.length, jobs: todo.length, lanes: lanes.map((l, i) => ({ worker: `w${i}`, project: projects[i], keys: l.map((s) => s.key) })) })

const started = Date.now()
const runs = lanes.map((lane, i) => new Promise<number>((done) => {
  if (!lane.length) return done(0)
  setTimeout(() => {
    const child = spawn('npx', ['tsx', join(HERE, 'run.mts'), SCENE, ...lane.map((s) => s.key)], {
      env: { ...process.env, WORKER: `w${i}`, OPEN_TAB: '1', FLOW_PROJECT: projects[i]!, FLOW_CDP: ENDPOINT },
      stdio: ['ignore', 'inherit', 'inherit'],
    })
    say({ event: 'worker-start', worker: `w${i}`, pid: child.pid, keys: lane.map((s) => s.key) })
    child.on('exit', (code) => { say({ event: 'worker-exit', worker: `w${i}`, code }); done(code ?? 1) })
  }, i * STAGGER_MS)
}))
const codes = await Promise.all(runs)
const left = missing().map((s) => s.key)
say({ event: 'done', minutes: +((Date.now() - started) / 60_000).toFixed(1), made: todo.length - left.length, remaining: left, codes })
process.exit(left.length ? 1 : 0)
