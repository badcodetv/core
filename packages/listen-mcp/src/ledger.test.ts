import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { mkdtempSync, readFileSync, readdirSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { ledgerFileName, renderLedger, writeLedger, type LedgerRecord } from './ledger'
import type { Lens } from './types'

const lens: Lens = { name: 'music', description: 'd', body: 'b', headings: ['A'], hash: 'abcdef012345' }

const record = (over: Partial<LedgerRecord> = {}): LedgerRecord => ({
  at: new Date('2026-09-11T14:03:22.000Z'),
  sourceName: 'Camping R17: take #2.mp3',
  sha256: 'f'.repeat(64),
  range: { start: 80, end: 105 },
  lens,
  modelRequested: 'Gemini 3.1 Pro',
  modelShown: 'Gemini 3.1 Pro Preview: #1',
  measurements: {
    durationSec: 25, integratedLufs: -9.8, truePeakDbtp: -0.4, loudnessRangeLu: 5.1, channels: 2,
    stereoCorrelation: 0.6, sideToMidDb: -11, spectralCentroidHz: 2000, tempo: { bpm: 174, confidence: 'high' },
  },
  instruction: 'Listen.\n\n## Drums',
  description: '## Drums\nTight.',
  remapped: true,
  ...over,
})

function frontmatter(text: string): Record<string, unknown> {
  const m = /^---\n([\s\S]*?)\n---\n/.exec(text)
  if (!m) throw new Error('no frontmatter')
  const out: Record<string, unknown> = {}
  for (const line of m[1]!.split('\n')) {
    const i = line.indexOf(': ')
    out[line.slice(0, i)] = JSON.parse(line.slice(i + 2))
  }
  return out
}

describe('ledgerFileName', () => {
  it('is a UTC timestamp plus a slug of the source name', () => {
    expect(ledgerFileName(record())).toBe('2026-09-11-140322-camping-r17-take-2.md')
  })
  it('caps the slug at 60 characters', () => {
    const name = ledgerFileName(record({ sourceName: `${'a'.repeat(100)}.wav` }))
    expect(name).toBe(`2026-09-11-140322-${'a'.repeat(60)}.md`)
  })
})

describe('renderLedger', () => {
  it('JSON-quotes every frontmatter value so each round-trips', () => {
    const f = frontmatter(renderLedger(record()))
    expect(f).toEqual({
      at: '2026-09-11T14:03:22.000Z',
      source: 'Camping R17: take #2.mp3',
      sha256: 'f'.repeat(64),
      range: '1:20–1:45',
      lens: 'music@abcdef012345',
      model_requested: 'Gemini 3.1 Pro',
      model_shown: 'Gemini 3.1 Pro Preview: #1',
      remapped: true,
      measurements: record().measurements,
    })
  })
  it('says "full" when there is no range', () => {
    expect(frontmatter(renderLedger(record({ range: null }))).range).toBe('full')
  })
  it('writes the body sections in order, Question only when asked', () => {
    const without = renderLedger(record())
    expect(without).not.toContain('## Question')
    expect(without.indexOf('## Instruction sent')).toBeLessThan(without.indexOf('## Description'))
    const withQ = renderLedger(record({ question: 'Is the bass too loud?' }))
    const qi = withQ.indexOf('## Question')
    expect(qi).toBeGreaterThan(0)
    expect(qi).toBeLessThan(withQ.indexOf('## Instruction sent'))
    expect(withQ).toContain('Is the bass too loud?')
  })
})

describe('writeLedger', () => {
  let dir: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'listen-ledger-test-'))
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  it('never overwrites: the same timestamp twice gives two files', async () => {
    const a = await writeLedger(dir, record())
    const b = await writeLedger(dir, record({ description: 'second' }))
    expect(a).not.toBe(b)
    expect(b.endsWith('-2.md')).toBe(true)
    expect(readdirSync(dir)).toHaveLength(2)
    expect(readFileSync(a, 'utf8')).toContain('Tight.')
    expect(readFileSync(b, 'utf8')).toContain('second')
  })
})
