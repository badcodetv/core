import { describe, it, expect } from 'vitest'
import { chooseVideoMode, videoRequestError } from './video-mode'

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
