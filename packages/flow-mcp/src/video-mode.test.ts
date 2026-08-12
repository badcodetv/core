import { describe, it, expect } from 'vitest'
import { chooseVideoMode, refineRequestError, videoRequestError } from './video-mode'

const req = (over: Partial<Parameters<typeof videoRequestError>[0]> = {}) => ({
  model: 'Veo 3.1 - Fast',
  durationSeconds: 8,
  ...over,
})

describe('chooseVideoMode', () => {
  it('sends a lone start frame down the proven Animate path', () => {
    expect(chooseVideoMode('a.jpg', undefined)).toBe('animate')
  })

  it('sends start+end, and no frames at all, through the Frames slots', () => {
    expect(chooseVideoMode('a.jpg', 'b.jpg')).toBe('frames')
    expect(chooseVideoMode(undefined, undefined)).toBe('frames')
  })
})

describe('videoRequestError', () => {
  it('accepts the ordinary requests', () => {
    expect(videoRequestError(req({ startImage: 'a.jpg' }))).toBe(null)
    expect(videoRequestError(req({ startImage: 'a.jpg', endImage: 'b.jpg' }))).toBe(null)
    expect(videoRequestError(req())).toBe(null) // text to video
  })

  it('rejects a duration Flow does not offer', () => {
    // There is no slider — 5s is not "rounded", it does not exist.
    expect(videoRequestError(req({ durationSeconds: 5 }))).toMatch(/^VIDEO_DURATION_INVALID/)
    expect(videoRequestError(req({ durationSeconds: 0 }))).toMatch(/^VIDEO_DURATION_INVALID/)
  })

  it('rejects 10s on every Veo tier and allows it on Omni Flash', () => {
    for (const model of ['Veo 3.1 - Lite', 'Veo 3.1 - Fast', 'Veo 3.1 - Quality', 'Veo 3.1 - Lite [Lower Priority]']) {
      expect(videoRequestError(req({ model, durationSeconds: 10 }))).toMatch(/^VIDEO_DURATION_UNAVAILABLE/)
    }
    expect(videoRequestError(req({ model: 'Omni Flash', durationSeconds: 10 }))).toBe(null)
  })

  it('rejects a last frame with no first frame', () => {
    expect(videoRequestError(req({ endImage: 'b.jpg' }))).toMatch(/^VIDEO_END_ONLY_UNSUPPORTED/)
  })

  it('rejects a last frame on Omni Flash, which takes a first frame but not a last', () => {
    expect(videoRequestError(req({ startImage: 'a.jpg', endImage: 'b.jpg', model: 'Omni Flash' }))).toMatch(
      /^VIDEO_FRAMES_UNAVAILABLE/,
    )
    // …and the same model is fine for a start frame alone.
    expect(videoRequestError(req({ startImage: 'a.jpg', model: 'Omni Flash' }))).toBe(null)
  })

  it('accepts the loose model spellings callers write', () => {
    expect(videoRequestError(req({ startImage: 'a.jpg', endImage: 'b.jpg', model: 'omni flash' }))).toMatch(
      /^VIDEO_FRAMES_UNAVAILABLE/,
    )
    expect(videoRequestError(req({ model: 'Veo 3.1 Quality', durationSeconds: 10 }))).toMatch(
      /^VIDEO_DURATION_UNAVAILABLE/,
    )
  })

  it('checks duration before frames, so a doubly-wrong request names the simpler fix first', () => {
    const err = videoRequestError(req({ endImage: 'b.jpg', model: 'Omni Flash', durationSeconds: 5 }))
    expect(err).toMatch(/^VIDEO_DURATION_INVALID/)
  })
})

describe('refineRequestError', () => {
  const ref = (over: Partial<Parameters<typeof refineRequestError>[0]> = {}) => ({
    mediaId: '390b5431-d1c1-4371-aa6b-4fd49f6166ac',
    motion: 'Same shot, slower push in.',
    model: 'Veo 3.1 - Fast',
    ...over,
  })

  it('accepts a media id with no duration at all — the normal case', () => {
    // Omitting duration is not an oversight: Reuse prompt restores the original turn's length.
    expect(refineRequestError(ref())).toBe(null)
  })

  it('names the path mistake instead of letting it surface as "clip not found"', () => {
    expect(refineRequestError(ref({ mediaId: 'out/clip.mp4' }))).toMatch(/^VIDEO_REFINE_NOT_A_MEDIA_ID/)
    expect(refineRequestError(ref({ mediaId: '/home/kai/clip.mp4' }))).toMatch(/^VIDEO_REFINE_NOT_A_MEDIA_ID/)
    expect(refineRequestError(ref({ mediaId: 'panel-03.jpg' }))).toMatch(/^VIDEO_REFINE_NOT_A_MEDIA_ID/)
  })

  it('rejects a missing source or a blank prompt', () => {
    expect(refineRequestError(ref({ mediaId: '  ' }))).toMatch(/^VIDEO_REFINE_NO_SOURCE/)
    expect(refineRequestError(ref({ motion: '   ' }))).toMatch(/^VIDEO_REFINE_NO_PROMPT/)
  })

  it('applies the duration rules only when a duration is actually requested', () => {
    expect(refineRequestError(ref({ durationSeconds: 5 }))).toMatch(/^VIDEO_DURATION_INVALID/)
    expect(refineRequestError(ref({ durationSeconds: 10 }))).toMatch(/^VIDEO_DURATION_UNAVAILABLE/)
    expect(refineRequestError(ref({ durationSeconds: 10, model: 'omni flash' }))).toBe(null)
    expect(refineRequestError(ref({ durationSeconds: 4 }))).toBe(null)
  })
})
