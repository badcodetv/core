#!/usr/bin/env node
// Makes the simulated citizen pool from real published distributions.
//   node scripts/government/sim/make-pool.mjs [--size 1000] [--seed pool-2026-11-23]
// Reads docs/government/simulation/citizens/distributions.json (each figure carries its source)
// and writes pool.json next to it. Same seed, same pool: anyone can rebuild and check it.
//
// Every attribute is drawn from its own real marginal share. Three plausibility rules then stop
// impossible people (they are GUESSES, not data, and the pool file says so):
//   1. SNP voters live in Scotland and Plaid Cymru voters in Wales: elsewhere those weights are 0.
//   2. Over-65s are mostly retired: economic activity for 65+ uses retired 0.85, employed 0.12, other 0.03.
//   3. Under-65s are rarely retired (retired weight x0.05); 18-24s are students three times as often.
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { rng, pick } from './lot.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const dir = join(here, '../../../docs/government/simulation/citizens');
const args = process.argv.slice(2);
const flag = (n, d) => { const i = args.indexOf(`--${n}`); return i < 0 ? d : args[i + 1]; };
const size = Number(flag('size', 1000));
const seed = flag('seed', 'pool-2026-11-23');

const dist = JSON.parse(readFileSync(join(dir, 'distributions.json'), 'utf8'));
const A = dist.attributes;
const r = rng(seed);
const AGE_SPAN = { '18-24': [18, 24], '25-34': [25, 34], '35-44': [35, 44], '45-54': [45, 54], '55-64': [55, 64], '65-74': [65, 74], '75+': [75, 92] };

export function makePerson(i) {
  const age_band = pick(A.age_band.values, r());
  const [lo, hi] = AGE_SPAN[age_band];
  const age = lo + Math.floor(r() * (hi - lo + 1));
  const region = pick(A.region.values, r());
  let work;
  if (age >= 65) work = pick({ retired: 0.85, employed: 0.12, other: 0.03 }, r());
  else {
    const w = { ...A.economic_activity.values };
    w.retired *= 0.05;
    if (age <= 24) w.student *= 3;
    work = pick(w, r());
  }
  const vote = { ...A.vote_2024.values };
  if (region !== 'Scotland') vote.snp = 0;
  if (region !== 'Wales') vote.plaid_cymru = 0;
  return {
    id: `c${String(i).padStart(4, '0')}`,
    age, age_band,
    sex: pick(A.sex.values, r()),
    region,
    tenure: pick(A.tenure.values, r()),
    work,
    qualification: pick(A.qualification.values, r()),
    ethnicity: pick(A.ethnicity.values, r()),
    vote_2024: pick(vote, r()),
  };
}

const people = Array.from({ length: size }, (_, i) => makePerson(i));
const share = (k, v) => people.filter((p) => p[k] === v).length / size;
const pool = {
  schema: 'fp-sim-pool/1',
  version: seed,
  stamp: 'SIMULATED',
  what: 'Simulated UK adults. Not real people, and never "the public".',
  built: dist.built,
  size,
  seed,
  method: 'Each attribute drawn independently from its real marginal share (distributions.json, every figure sourced). Three plausibility rules are guesses, not data: SNP only in Scotland, Plaid Cymru only in Wales; over-65s mostly retired (0.85/0.12/0.03); under-65s rarely retired (x0.05) and 18-24s students x3.',
  limits: 'Marginals only, no joint distributions; tenure, work, qualification and ethnicity are England and Wales figures used UK-wide; vote shares are of registered electors.',
  check: { london: share('region', 'London'), over_65: people.filter((p) => p.age >= 65).length / size, did_not_vote: share('vote_2024', 'did_not_vote') },
  sources: Object.fromEntries(Object.entries(A).map(([k, v]) => [k, v.source])),
  people,
};
writeFileSync(join(dir, 'pool.json'), JSON.stringify(pool, null, 0).replace(/\},\{"id"/g, '},\n{"id"') + '\n');
console.log(`pool ${seed}: ${size} people; London ${pool.check.london.toFixed(3)}, 65+ ${pool.check.over_65.toFixed(3)}, didn't vote ${pool.check.did_not_vote.toFixed(3)}`);
