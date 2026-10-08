// Scratch runner: The Bank Robbery sixth-pass clips (2026-10-08, Jack's notes on cut 4). Omni 1.1 Flash, Frames, 16:9, 720p, 8s, x1.
// One clip per entry in br-clips-v6.json, through scripts/money-for-something/mfs-clip.mts (start frame + optional Character chips).
// Plates are copied into the WSL filesystem first (uploads from /mnt/c fail intermittently). Skips clips already on disk.
// usage: node br-clips-v3.mjs [id ...]
import { readFileSync, writeFileSync, existsSync, mkdirSync, copyFileSync, appendFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const IMG = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/images';
const OUT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/vids/v6';
const W = `${process.env.HOME}/.cache/badcode-bank-robbery/v6c`;
for (const d of [OUT, W, `${W}/plates`, `${W}/prompts`, `${W}/uploaded`]) mkdirSync(d, { recursive: true });
const m = JSON.parse(readFileSync(join(here, 'br-clips-v6.json'), 'utf8'));
const only = process.argv.slice(2);
const log = join(OUT, '00-run-log.txt');
const say = (s) => { const l = `${new Date().toISOString().slice(11, 19)} ${s}\n`; appendFileSync(log, l); process.stdout.write(l); };
for (const c of m.clips) {
  if (only.length && !only.includes(c.id)) continue;
  const out = join(OUT, c.id + '.mp4');
  if (existsSync(out)) { say(`skip ${c.id}`); continue; }
  const [pass, name] = c.plate.split('/');
  const src = join(IMG, 'scenes-' + pass, name + '.jpg');
  const plateName = `br6-${pass}-${name}.jpg`;
  const plate = join(W, 'plates', plateName);
  if (!existsSync(plate)) copyFileSync(src, plate);
  const pf = join(W, 'prompts', c.id + '.txt');
  writeFileSync(pf, c.full ?? (m.open + c.text + m.close));
  const mark = join(W, 'uploaded', plateName);
  let ok = false;
  for (let t = 1; t <= 3 && !ok; t++) {
    const args = ['tsx', join(here, '..', 'money-for-something', 'mfs-clip.mts'), plate, pf, out, ...c.chars.flatMap((x) => ['--char', x])];
    const r = spawnSync('npx', args, { encoding: 'utf8', timeout: 16 * 60000, cwd: join(here, '..', 'money-for-something'), env: { ...process.env, MFS_SKIP_UPLOAD: existsSync(mark) ? '1' : '' } });
    const tail = ((r.stdout || '') + (r.stderr || '')).trim().split('\n').slice(-2).join(' | ').slice(0, 220);
    ok = existsSync(out);
    if (/attached|submitted|box:/.test(r.stdout || '') || ok) writeFileSync(mark, '');
    say(`${c.id} try ${t} ${ok ? 'OK' : 'FAIL'} ${tail}`);
    if (!ok && /TIMEOUT|FLOW_FAILED/.test(tail)) break; // a block or a refusal: rewrite, do not retry
    if (!ok) spawnSync('sleep', ['10']);
  }
}
say('ALL_DONE');
