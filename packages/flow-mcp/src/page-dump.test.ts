import { describe, it, expect } from 'vitest'
import { dumpLines } from './page-dump'

describe('dumpLines', () => {
  it('keeps a real message and drops the chrome around it', () => {
    expect(
      dumpLines([
        'arrow_backGo Back',
        'more_vertMore options',
        "You've run out of credits for this month.",
        'addAdd Media',
        'Agent',
      ]),
    ).toEqual(["You've run out of credits for this month."])
  })

  it('drops a bare Material icon name, which leaf-node scraping splits off on its own', () => {
    expect(dumpLines(['dashboard', 'swap_horiz', 'crop_16_9', 'Out of credits'])).toEqual(['Out of credits'])
  })

  it('keeps unknown wording, which is the entire point', () => {
    // If this filter ever gets clever enough to only keep text it recognises, the dump stops
    // being able to tell us about the failure states we have never seen.
    const odd = 'Verify you are human to continue'
    expect(dumpLines([odd])).toEqual([odd])
  })

  it('collapses whitespace and dedupes repeats', () => {
    expect(dumpLines(['Something  broke\n  badly', 'Something broke badly'])).toEqual(['Something broke badly'])
  })

  it('drops icon ligatures and whole-subtree concatenations', () => {
    const subtree = 'x'.repeat(401)
    expect(dumpLines(['ok', '  ', subtree, 'a real line'])).toEqual(['a real line'])
  })

  it('caps the output so a wedged page cannot write an unreadable file', () => {
    const many = Array.from({ length: 200 }, (_, i) => `message number ${i}`)
    expect(dumpLines(many)).toHaveLength(60)
    expect(dumpLines(many, 5)).toEqual([
      'message number 0',
      'message number 1',
      'message number 2',
      'message number 3',
      'message number 4',
    ])
  })

  it('preserves page order, so the newest transcript line is findable by position', () => {
    expect(dumpLines(['first thing', 'second thing'])).toEqual(['first thing', 'second thing'])
  })
})
