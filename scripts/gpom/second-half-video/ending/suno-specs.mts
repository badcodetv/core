/**
 * Build the Suno specs for the GPOM ending (scenes C, D, E) from the live sheet.
 *   npx tsx scripts/gpom/second-half-video/ending/suno-specs.mts <outDir> [round=A]
 * Writes one <atom>.json per take, ready for `suno.mts pair`. Spends nothing.
 */
import { execFileSync } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'

const SHEET = 'docs/stories/gitpush-origin-master/songs/second-half-ending-music.md'
const [outDir, round = 'A'] = process.argv.slice(2)
if (!outDir) throw new Error('usage: suno-specs.mts <outDir> [round]')
mkdirSync(outDir, { recursive: true })

const voice = { voice: 'badcode newsreader', styleInfluence: 50, audioInfluence: 65, weirdness: [25, 10] }
const music = { styleInfluence: 75, weirdness: [30, 60] }
const atoms: [string, number, object][] = [
  ['gpom-sh-end-ai-C', 30, voice],
  ['gpom-sh-end-ai-D', 60, voice],
  ['gpom-sh-end-ai-E', 40, voice],
  ['gpom-sh-c-walk', 60, music],
  ['gpom-sh-d-room', 70, music],
  ['gpom-sh-d-cross', 45, music],
  ['gpom-sh-e-coda', 40, music],
]
for (const [id, durationSec, extra] of atoms) {
  const boxes = JSON.parse(
    execFileSync('npx', ['tsx', 'scripts/suno/suno.mts', 'extract', SHEET, '### `' + id + '`'], { encoding: 'utf8' }),
  )
  const spec = {
    style: boxes.style,
    exclude: boxes.exclude,
    lyrics: boxes.lyrics,
    model: 'v6',
    variety: 'off',
    maxMode: false,
    vocalGender: null,
    personalize: false,
    durationSec,
    title: `${id}-${round}`,
    workspace: 'gpom-story',
    ...extra,
  }
  writeFileSync(join(outDir, `${id}.json`), JSON.stringify(spec, null, 2))
  console.log(`${id}.json  dur=${durationSec}  w=${(extra as { weirdness: number[] }).weirdness}`)
}
