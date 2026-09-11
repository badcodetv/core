/**
 * Every listen writes one markdown record under docs/listening/log/ — words in the repo, audio
 * outside it. The record carries the exact instruction sent, so any description can be re-run or
 * argued with later, and the lens hash, so it can be traced to the checklist that produced it.
 */
import { mkdir, writeFile } from 'node:fs/promises'
import { join } from 'node:path'
import { formatTime } from './remap'
import type { Lens, Measurements, Range } from './types'

export interface LedgerRecord {
  at: Date
  sourceName: string
  sha256: string
  range: Range | null
  lens: Lens
  modelRequested: string
  modelShown: string
  measurements: Measurements
  instruction: string
  description: string
  remapped: boolean
  question?: string
}

/** Lower-case name without its extension, non-alphanumerics → '-', collapsed, max 60 chars. */
function slug(sourceName: string): string {
  const s = sourceName
    .replace(/\.[^.]*$/, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 60)
    .replace(/-+$/, '')
  return s || 'audio'
}

const pad = (n: number): string => String(n).padStart(2, '0')

/** 'YYYY-MM-DD-HHMMSS-<slug>.md', in UTC. */
export function ledgerFileName(r: LedgerRecord): string {
  const d = r.at
  const date = `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())}`
  const time = `${pad(d.getUTCHours())}${pad(d.getUTCMinutes())}${pad(d.getUTCSeconds())}`
  return `${date}-${time}-${slug(r.sourceName)}.md`
}

export function rangeLabel(range: Range | null): string {
  return range ? `${formatTime(range.start)}–${formatTime(range.end)}` : 'full'
}

/**
 * Every string in the frontmatter is JSON-quoted, so a file or model name containing `: ` or `#`
 * cannot break the YAML — and every value round-trips through JSON.parse.
 */
export function renderLedger(r: LedgerRecord): string {
  const q = JSON.stringify
  const front = [
    '---',
    `at: ${q(r.at.toISOString())}`,
    `source: ${q(r.sourceName)}`,
    `sha256: ${q(r.sha256)}`,
    `range: ${q(rangeLabel(r.range))}`,
    `lens: ${q(`${r.lens.name}@${r.lens.hash}`)}`,
    `model_requested: ${q(r.modelRequested)}`,
    `model_shown: ${q(r.modelShown)}`,
    `remapped: ${r.remapped}`,
    `measurements: ${JSON.stringify(r.measurements)}`,
    '---',
  ]
  const body: string[] = []
  if (r.question) body.push('## Question', '', r.question.trim(), '')
  body.push('## Instruction sent', '', r.instruction.trim(), '')
  body.push('## Description', '', r.description.trim(), '')
  return `${front.join('\n')}\n\n${body.join('\n')}`
}

/** Write the record into `dir`; never overwrites (a clash gets -2, -3, …). Returns the absolute path. */
export async function writeLedger(dir: string, r: LedgerRecord): Promise<string> {
  await mkdir(dir, { recursive: true })
  const base = ledgerFileName(r).replace(/\.md$/, '')
  const text = renderLedger(r)
  for (let n = 1; n < 1000; n++) {
    const path = join(dir, n === 1 ? `${base}.md` : `${base}-${n}.md`)
    try {
      await writeFile(path, text, { encoding: 'utf8', flag: 'wx' })
      return path
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code !== 'EEXIST') throw e
    }
  }
  throw new Error(`LISTEN_ERROR: could not find a free ledger file name for ${base}`)
}
