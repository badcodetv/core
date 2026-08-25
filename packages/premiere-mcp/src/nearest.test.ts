import { describe, expect, it } from 'vitest'
import { didYouMean, editDistance, nearestNames } from './nearest'

/** A slice of the real catalogue, so the ranking is judged against names we actually get back. */
const EFFECTS = [
  'AE.ADBE Gaussian Blur 2',
  'AE.ADBE Camera Blur',
  'AE.ADBE Motion',
  'AE.ADBE Opacity',
  'PR.ADBE Lumetri',
  'AE.ADBE Directional Blur',
  'PR.ADBE Crop',
]

const TRANSITIONS = [
  'AE.ADBE Cross Dissolve',
  'AE.ADBE Dip To Black',
  'AE.ADBE Dip To White',
  'AE.ADBE Film Dissolve',
]

describe('editDistance', () => {
  it('is zero for identical strings', () => {
    expect(editDistance('blur', 'blur')).toBe(0)
  })

  it('counts a substitution as one', () => {
    expect(editDistance('blur', 'blue')).toBe(1)
  })

  it('counts an insertion as one', () => {
    expect(editDistance('blur', 'blurs')).toBe(1)
  })

  it('falls back to length when one side is empty', () => {
    expect(editDistance('', 'lumetri')).toBe(7)
    expect(editDistance('lumetri', '')).toBe(7)
  })

  it('is symmetric', () => {
    expect(editDistance('kitten', 'sitting')).toBe(editDistance('sitting', 'kitten'))
    expect(editDistance('kitten', 'sitting')).toBe(3)
  })
})

describe('nearestNames', () => {
  it('puts an exact match first', () => {
    expect(nearestNames('AE.ADBE Motion', EFFECTS)[0]).toBe('AE.ADBE Motion')
  })

  it('ignores case and punctuation', () => {
    expect(nearestNames('ae adbe motion', EFFECTS)[0]).toBe('AE.ADBE Motion')
  })

  /** The point of the band ranking: a short word contained in a long name beats a name of
   * similar length that shares nothing. Raw edit distance gets this backwards. */
  it('ranks a contained substring above a merely similar-length name', () => {
    const hits = nearestNames('blur', EFFECTS)
    expect(hits.every((h) => h.toLowerCase().includes('blur'))).toBe(true)
  })

  it('finds a transition from its friendly name', () => {
    expect(nearestNames('cross dissolve', TRANSITIONS)[0]).toBe('AE.ADBE Cross Dissolve')
  })

  it('tolerates a typo', () => {
    expect(nearestNames('AE.ADBE Cross Disolve', TRANSITIONS)[0]).toBe('AE.ADBE Cross Dissolve')
  })

  it('returns at most `count`', () => {
    expect(nearestNames('blur', EFFECTS, 2)).toHaveLength(2)
    expect(nearestNames('blur', EFFECTS)).toHaveLength(3)
  })

  it('never returns more than there are candidates', () => {
    expect(nearestNames('blur', ['AE.ADBE Camera Blur'])).toEqual(['AE.ADBE Camera Blur'])
  })

  it('handles an empty needle without throwing', () => {
    expect(nearestNames('', EFFECTS)).toHaveLength(3)
    expect(nearestNames('   ', EFFECTS)).toHaveLength(3)
  })

  it('handles an empty candidate list', () => {
    expect(nearestNames('blur', [])).toEqual([])
  })

  it('is deterministic when two candidates tie', () => {
    const tied = ['B name', 'A name']
    expect(nearestNames('name', tied, 2)).toEqual(['A name', 'B name'])
  })
})

describe('didYouMean', () => {
  it('names the closest few and the size of the catalogue', () => {
    const msg = didYouMean('cross dissolve', TRANSITIONS)
    expect(msg).toContain('AE.ADBE Cross Dissolve')
    expect(msg).toContain(`the ${TRANSITIONS.length} available`)
  })

  it('says so plainly when Premiere reported nothing', () => {
    expect(didYouMean('anything', [])).toContain('none at all')
  })
})
