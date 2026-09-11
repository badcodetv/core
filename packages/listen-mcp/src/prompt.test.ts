import { describe, it, expect } from 'vitest'
import { buildPrompt } from './prompt'
import type { Lens, Measurements } from './types'

const lens: Lens = {
  name: 'music',
  description: 'd',
  body: 'Listen. Do not comment on stereo width.\n\n## Drums\nThe groove.\n\n## Bass\nThe low end.',
  headings: ['Drums', 'Bass'],
  hash: 'abcdef012345',
}

const m = (over: Partial<Measurements> = {}): Measurements => ({
  durationSec: 25,
  integratedLufs: -9.8,
  truePeakDbtp: -0.4,
  loudnessRangeLu: 5.1,
  channels: 2,
  stereoCorrelation: 0.6173,
  sideToMidDb: -11.42,
  spectralCentroidHz: 2140.5,
  tempo: { bpm: 174.2, confidence: 'high' },
  ...over,
})

/** Just the MEASURED FACTS block — up to the next blank line. */
const factsBlock = (p: string): string => {
  const i = p.indexOf('MEASURED FACTS')
  const end = p.indexOf('\n\n', i)
  return p.slice(i, end < 0 ? undefined : end)
}

describe('buildPrompt', () => {
  it('starts with the lens body and ends with the headings in lens order', () => {
    const p = buildPrompt({ lens, measurements: m() })
    expect(p.startsWith('Listen.')).toBe(true)
    expect(p.endsWith('Answer using exactly these headings, in order:\n## Drums\n## Bass')).toBe(true)
  })

  it('states duration, loudness and true peak as facts', () => {
    const f = factsBlock(buildPrompt({ lens, measurements: m() }))
    expect(f).toContain('MEASURED FACTS — do not contradict these:')
    expect(f).toContain('25.0 seconds')
    expect(f).toContain('-9.8 LUFS')
    expect(f).toContain('-0.4 dBTP')
  })

  it('omits loudness and peak when they were not measurable', () => {
    const f = factsBlock(buildPrompt({ lens, measurements: m({ integratedLufs: null, truePeakDbtp: null }) }))
    expect(f).not.toContain('LUFS')
    expect(f).not.toContain('dBTP')
  })

  it('includes tempo only when it is trusted', () => {
    expect(factsBlock(buildPrompt({ lens, measurements: m() }))).toContain('Tempo: 174 BPM')
    for (const confidence of ['none', 'unverified'] as const) {
      const f = factsBlock(buildPrompt({ lens, measurements: m({ tempo: { bpm: 174.2, confidence } }) }))
      expect(f).not.toContain('Tempo')
    }
  })

  it('never puts stereo numbers in the facts', () => {
    const f = factsBlock(buildPrompt({ lens, measurements: m() }))
    for (const s of ['stereoCorrelation', 'sideToMidDb', 'stereo', '0.6173', '0.62', '-11.42', '-11.4']) {
      expect(f).not.toContain(s)
    }
  })

  it('adds the range line only for a cut clip', () => {
    expect(buildPrompt({ lens, measurements: m() })).not.toContain('This clip is')
    expect(buildPrompt({ lens, measurements: m(), rangeLabel: '1:20–1:45' })).toContain(
      'This clip is 1:20–1:45 of a longer track; timestamps are relative to the clip start.',
    )
  })

  it('appends the question verbatim', () => {
    const question = 'Is the *bass* too loud at 0:30?\nBe blunt.'
    expect(buildPrompt({ lens, measurements: m(), question })).toContain(`EXTRA QUESTION:\n${question}`)
    expect(buildPrompt({ lens, measurements: m() })).not.toContain('EXTRA QUESTION')
  })

  it('is deterministic', () => {
    const args = { lens, measurements: m(), question: 'q', rangeLabel: '0:10–0:20' }
    expect(buildPrompt(args)).toBe(buildPrompt(args))
  })
})
