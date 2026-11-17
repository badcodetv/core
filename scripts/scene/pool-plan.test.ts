import { strict as assert } from 'node:assert'
import { test } from 'vitest'
import { planPool } from './pool-plan'

const j = (key: string, character: string | null = null) => ({ key, character })
const keys = (lanes: { key: string }[][]) => lanes.map((l) => l.map((x) => x.key))

test('deals plain jobs out evenly across the tabs', () => {
  const lanes = planPool(['01', '02', '03', '04', '05', '06', '07'].map((k) => j(k)), 3)
  assert.deepEqual(keys(lanes), [['01', '04', '07'], ['02', '05'], ['03', '06']])
})

test('a job that casts a Character always goes to worker 0 (the scene project)', () => {
  const lanes = planPool([j('01', 'Her'), j('02'), j('03', 'Her'), j('04'), j('05')], 3)
  assert.deepEqual(keys(lanes)[0]!.slice(0, 2), ['01', '03'])
  for (const l of lanes.slice(1)) for (const x of l) assert.equal(x.character, null)
})

test('worker 0 takes no plain jobs until the others have caught up with its cast jobs', () => {
  const lanes = planPool([j('a', 'X'), j('b', 'X'), j('c'), j('d')], 3)
  assert.deepEqual(keys(lanes), [['a', 'b'], ['c'], ['d']])
})

test('more tabs than jobs leaves the spare tabs empty', () => {
  assert.deepEqual(keys(planPool([j('01'), j('02')], 5)), [['01'], ['02'], [], [], []])
})

test('one tab (or nonsense) is the plain single runner', () => {
  assert.deepEqual(keys(planPool([j('01'), j('02', 'X')], 1)), [['02', '01']])
  assert.deepEqual(keys(planPool([j('01')], 0)), [['01']])
})

test('every job lands exactly once', () => {
  const jobs = Array.from({ length: 30 }, (_, i) => j(String(i), i % 7 === 0 ? 'C' : null))
  const flat = planPool(jobs, 6).flat().map((x) => x.key).sort()
  assert.deepEqual(flat, jobs.map((x) => x.key).sort())
})
