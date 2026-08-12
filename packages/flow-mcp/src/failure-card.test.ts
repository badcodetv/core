import { describe, it, expect } from 'vitest'
import { classifyCard, ANY_CARD_RE } from './failure-card'

describe('classifyCard', () => {
  it('classifies null/empty as no card', () => {
    expect(classifyCard(null)).toBe(null)
    expect(classifyCard('')).toBe(null)
  })

  it('classifies unrecognised text as no card', () => {
    expect(classifyCard('Generating your image…')).toBe(null)
    expect(classifyCard('Add to Prompt')).toBe(null)
  })

  it('classifies the sentence-case policy-block string as blocked', () => {
    expect(
      classifyCard(
        'This generation might violate our policies. Please try a different prompt or send feedback',
      ),
    ).toBe('blocked')
  })

  it('classifies the Title Case "Prominent People" policy-block variant as blocked', () => {
    expect(
      classifyCard(
        'This Prompt Might Violate Our Policies About Generating Prominent People. Please Try a Different Prompt or Send Feedback.',
      ),
    ).toBe('blocked')
  })

  it('classifies the queue message as queued', () => {
    expect(
      classifyCard('Your video has been scheduled and is waiting in the queue due to high demand.'),
    ).toBe('queued')
  })

  it('classifies the transient-failure card as error', () => {
    expect(classifyCard('Oops, something went wrong!')).toBe('error')
  })

  it('is case-insensitive and tolerant of the comma after "Oops"', () => {
    expect(classifyCard('oops something went wrong!')).toBe('error')
    expect(classifyCard('OOPS, SOMETHING WENT WRONG!')).toBe('error')
  })

  describe('ambiguous combinations (a Flow chat transcript accumulates messages)', () => {
    it('prefers error over a co-occurring stale queue message', () => {
      // flow-video.md: the queue text persists in the transcript even after the clip
      // finishes or fails, so its presence alone proves nothing once a real error card
      // has also been posted.
      const transcript =
        'Your video has been scheduled and is waiting in the queue due to high demand. ' +
        'Oops, something went wrong!'
      expect(classifyCard(transcript)).toBe('error')
    })

    it('prefers error over a co-occurring queue message regardless of order', () => {
      const transcript =
        'Oops, something went wrong! ' +
        'Your video has been scheduled and is waiting in the queue due to high demand.'
      expect(classifyCard(transcript)).toBe('error')
    })

    it('prefers blocked over a co-occurring queue message', () => {
      const transcript =
        'Your video has been scheduled and is waiting in the queue due to high demand. ' +
        'This generation might violate our policies. Please try a different prompt or send feedback'
      expect(classifyCard(transcript)).toBe('blocked')
    })

    it('prefers blocked over a co-occurring error message', () => {
      const transcript =
        'Oops, something went wrong! ' +
        'This generation might violate our policies. Please try a different prompt or send feedback'
      expect(classifyCard(transcript)).toBe('blocked')
    })

    it('prefers blocked when all three are present', () => {
      const transcript = [
        'Your video has been scheduled and is waiting in the queue due to high demand.',
        'Oops, something went wrong!',
        'This generation might violate our policies. Please try a different prompt or send feedback',
      ].join(' ')
      expect(classifyCard(transcript)).toBe('blocked')
    })
  })

  it('classifies queued alone (no error, no block) as queued, not a failure', () => {
    // The "warning Failed"-looking icon can render WHILE queued — classifyCard must not
    // be fooled by that visual into reading this as an error or a block.
    expect(
      classifyCard('Your video has been scheduled and is waiting in the queue due to high demand.'),
    ).toBe('queued')
  })
})

describe('multiple cards joined from separate DOM nodes', () => {
  // detectFailureCard() reads ALL matching messages and joins them before classifying,
  // rather than taking the first hit. Flow's transcript accumulates (flow-video.md:61-62 —
  // the queue message survives after the clip finishes), so the stale message is frequently
  // the FIRST one in the DOM. These lock in that a stale queue line above a real block or
  // error cannot mask it.
  const QUEUED = 'Your video has been scheduled and is waiting in the queue due to high demand.'

  it('sees a block that appears below a stale queue message', () => {
    expect(classifyCard([QUEUED, 'This generation might violate our policies.'].join('\n'))).toBe('blocked')
  })

  it('sees an error that appears below a stale queue message', () => {
    expect(classifyCard([QUEUED, 'Oops, something went wrong!'].join('\n'))).toBe('error')
  })

  it('still reads a lone queue message as benign', () => {
    expect(classifyCard([QUEUED, QUEUED].join('\n'))).toBe('queued')
  })
})

describe('ANY_CARD_RE', () => {
  it('matches every known card string, so the DOM probe scopes to real cards only', () => {
    expect(ANY_CARD_RE.test('This generation might violate our policies.')).toBe(true)
    expect(ANY_CARD_RE.test('This Prompt Might Violate Our Policies About Generating Prominent People.')).toBe(true)
    expect(ANY_CARD_RE.test('Your video has been scheduled and is waiting in the queue due to high demand.')).toBe(true)
    expect(ANY_CARD_RE.test('Oops, something went wrong!')).toBe(true)
  })

  it('does not match unrelated compose-bar text', () => {
    expect(ANY_CARD_RE.test('What do you want to create?')).toBe(false)
  })
})
