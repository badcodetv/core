// Scratch runner: The Bank Robbery SHORT cut 7 clips (2026-10-19), Omni 1.1 Flash, 720p, 8s, Frames mode, from brs7-clips.json. Same as brs4-clips.mjs.
// One clip per entry in brs7-clips.json, through scripts/money-for-something/mfs-clip.mts (start frame + optional Character chips).
// Plates are copied into the WSL filesystem first (uploads from /mnt/c fail intermittently). Skips clips already on disk.
// usage: node brs-clips.mjs [id ...]
import { readFileSync, writeFileSync, existsSync, mkdirSync, copyFileSync, appendFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const IMG = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/images';
const OUT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/vids/short7';
const W = `${process.env.HOME}/.cache/badcode-bank-robbery/short7`;
for (const d of [OUT, W, `${W}/plates`, `${W}/prompts`, `${W}/uploaded`]) mkdirSync(d, { recursive: true });
const m = JSON.parse(readFileSync(join(here, 'brs7-clips.json'), 'utf8'));
const only = process.argv.slice(2);
const log = join(OUT, '00-run-log.txt');
const say = (s) => { const l = `${new Date().toISOString().slice(11, 19)} ${s}\n`; appendFileSync(log, l); process.stdout.write(l); };
for (const c of m.clips) {
  if (only.length && !only.includes(c.id)) continue;
  const out = join(OUT, c.id + '.mp4');
  if (existsSync(out)) { say(`skip ${c.id}`); continue; }
  const name = c.plate;
  const src = existsSync(join(IMG, 'short7', name + '.jpg')) ? join(IMG, 'short7', name + '.jpg') : join(IMG, 'short4', name + '.jpg');   // cut 7b: re-made talking clips start from the cut 4 plates
  const plateName = `brs7-${name}.jpg`;
  const plate = join(W, 'plates', plateName);
  if (!existsSync(plate)) copyFileSync(src, plate);
  const pf = join(W, 'prompts', c.id + '.txt');
  writeFileSync(pf, c.full);
  const mark = join(W, 'uploaded', plateName);
  let ok = false;
  for (let t = 1; t <= 3 && !ok; t++) {
    const args = ['tsx', join(here, '..', 'money-for-something', 'mfs-clip.mts'), plate, pf, out, ...c.chars.flatMap((x) => ['--char', x]), '--mode', c.mode];
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
