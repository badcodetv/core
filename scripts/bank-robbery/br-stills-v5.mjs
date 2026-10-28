// Scratch runner: makes the fifth-pass (2026-10-08, Jack's notes on cut 3) Bank Robbery stills from br-stills-v5.json, one at a time,
// casting Characters by hand through scripts/flow/.tmp/cast-many-v4.mjs. Skips files already on disk.
// usage: node br-stills-v3.mjs <port> <outDir> [id ...]
import { readFileSync, writeFileSync, existsSync, mkdirSync, appendFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const [port, outDir, ...only] = process.argv.slice(2);
const m = JSON.parse(readFileSync(join(here, 'br-stills-v5.json'), 'utf8'));
const tmp = join(here, '.tmp'); mkdirSync(tmp, { recursive: true });
const log = join(outDir, '00-run-log.txt');
for (const s of [...m.shots, ...(m.later || [])]) {
  if (only.length && !only.includes(s.id)) continue;
  const out = join(outDir, s.id + '.jpg');
  if (existsSync(out)) { console.log('skip', s.id); continue; }
  const prompt = s.full ?? ((s.cast.length ? m.pre : '') + s.body + m[s.endKey]);
  const pf = join(tmp, s.id + '.txt'); writeFileSync(pf, prompt);
  const r = spawnSync('node', [join(here, '..', 'flow', '.tmp', 'cast-many-v4.mjs'), port, pf, out, ...(s.refs || []), ...s.cast], { encoding: 'utf8', timeout: 420000 });
  const ok = existsSync(out);
  const line = `${new Date().toISOString()} ${s.id} ${ok ? 'OK' : 'FAIL'} ${(r.stdout || '').replace(/\s+/g, ' ').slice(-160)} ${(r.stderr || '').replace(/\s+/g, ' ').slice(-200)}\n`;
  appendFileSync(log, line); process.stdout.write(line);
}
console.log('DONE');
