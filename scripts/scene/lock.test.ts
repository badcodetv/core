import { strict as assert } from 'node:assert'
import { spawn } from 'node:child_process'
import { existsSync, mkdirSync, mkdtempSync, readFileSync, utimesSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join } from 'node:path'
import { test } from 'vitest'
import { fileURLToPath } from 'node:url'
import { withLock } from './lock'

const HERE = dirname(fileURLToPath(import.meta.url))
const tmp = () => mkdtempSync(join(process.env.TMPDIR ?? tmpdir(), 'lock-'))

test('runs the function and releases the lock', () => {
  const l = join(tmp(), '.l')
  assert.equal(withLock(l, () => 7), 7)
  assert.equal(existsSync(l), false)
})

test('releases the lock when the function throws', () => {
  const l = join(tmp(), '.l')
  assert.throws(() => withLock(l, () => { throw new Error('boom') }), /boom/)
  assert.equal(existsSync(l), false)
})

test('breaks a stale lock left by a crashed worker', () => {
  const l = join(tmp(), '.l')
  mkdirSync(l)
  const old = new Date(Date.now() - 60_000)
  utimesSync(l, old, old)
  assert.equal(withLock(l, () => 'ok', 2000), 'ok')
})

test('times out on a live lock held by someone else', () => {
  const l = join(tmp(), '.l')
  mkdirSync(l)
  assert.throws(() => withLock(l, () => 1, 200), /LOCK_TIMEOUT/)
})

test('three processes doing read-modify-write never lose an update', async () => {
  const d = tmp()
  const f = join(d, 'n.json')
  writeFileSync(f, '{"n":0}')
  const child = join(d, 'child.mts')
  writeFileSync(child, `import { readFileSync, writeFileSync } from 'node:fs'
import { withLock } from ${JSON.stringify(join(HERE, 'lock.ts'))}
for (let i = 0; i < 100; i++) withLock(${JSON.stringify(join(d, '.l'))}, () => {
  const o = JSON.parse(readFileSync(${JSON.stringify(f)}, 'utf8')); o.n++; writeFileSync(${JSON.stringify(f)}, JSON.stringify(o))
})
`)
  const run = () => new Promise<void>((ok, bad) =>
    spawn('npx', ['tsx', child], { stdio: 'inherit' }).on('exit', (c) => (c ? bad(new Error(`exit ${c}`)) : ok())))
  await Promise.all([run(), run(), run()])
  assert.equal(JSON.parse(readFileSync(f, 'utf8')).n, 300)
})
