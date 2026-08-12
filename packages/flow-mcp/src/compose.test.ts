import { describe, it, expect } from 'vitest'
import {
  isBoxCleared,
  modelAlreadySelected,
  videoModelAlreadySelected,
  canonicalVideoModel,
  VIDEO_MODELS,
  aspectAlreadySelected,
  maxDurationForModel,
  parseVideoDuration,
  videoDurationAlreadySelected,
  VIDEO_DURATIONS,
} from './compose'

describe('isBoxCleared', () => {
  it('treats a truly empty box as cleared', () => {
    expect(isBoxCleared('')).toBe(true)
    expect(isBoxCleared(null)).toBe(true)
  })

  it('treats each surface placeholder as cleared', () => {
    for (const p of [
      'What do you want to create?',
      'What do you want to change?',
      'Describe body and outfit....',
      'Describe your character…',
    ]) {
      expect(isBoxCleared(p)).toBe(true)
    }
  })

  it('ignores zero-width leftovers', () => {
    expect(isBoxCleared('​What do you want to create?﻿')).toBe(true)
  })

  it('reports real user text as not cleared', () => {
    expect(isBoxCleared('A single plain metal disc spinning on a dark tabletop')).toBe(false)
  })
})

describe('modelAlreadySelected', () => {
  it('matches inside a concatenated config label', () => {
    expect(modelAlreadySelected('🍌 Nano Banana Pro crop_16_9 x2', 'Nano Banana Pro')).toBe(true)
    expect(modelAlreadySelected('🍌 Nano Banana 2crop_16_91x', 'Nano Banana 2')).toBe(true)
  })

  it('does not confuse a different tier for the target', () => {
    expect(modelAlreadySelected('🍌 Nano Banana 2 crop_16_9 x2', 'Nano Banana Pro')).toBe(false)
  })

  it('does not let the Lite label satisfy its own prefix', () => {
    // The bug this guards: "Nano Banana 2" is a prefix of "Nano Banana 2 Lite".
    expect(modelAlreadySelected('🍌 Nano Banana 2 Lite', 'Nano Banana 2')).toBe(false)
    expect(modelAlreadySelected('🍌 Nano Banana 2 Lite', 'Nano Banana 2 Lite')).toBe(true)
  })

  it('handles a missing label', () => {
    expect(modelAlreadySelected(null, 'Nano Banana Pro')).toBe(false)
  })
})

describe('canonicalVideoModel', () => {
  // The live menu labels, captured 2026-08-12. Everything else in the codebase writes these
  // names without the " - ", which is why an exact click target has to be resolved.
  it('resolves the spelling we use to the spelling Flow renders', () => {
    expect(canonicalVideoModel('Veo 3.1 Fast')).toBe('Veo 3.1 - Fast')
    expect(canonicalVideoModel('Veo 3.1 Quality')).toBe('Veo 3.1 - Quality')
    expect(canonicalVideoModel('veo 3.1 lite')).toBe('Veo 3.1 - Lite')
  })

  it('leaves an already-canonical name alone', () => {
    for (const m of VIDEO_MODELS) expect(canonicalVideoModel(m)).toBe(m)
  })

  it('keeps the Lower Priority tier distinct from plain Lite', () => {
    expect(canonicalVideoModel('Veo 3.1 Lite [Lower Priority]')).toBe('Veo 3.1 - Lite [Lower Priority]')
    expect(canonicalVideoModel('Veo 3.1 Lite')).toBe('Veo 3.1 - Lite')
  })

  it('passes an unknown name through untouched, so a new Flow model still works', () => {
    expect(canonicalVideoModel('Veo 4 - Ultra')).toBe('Veo 4 - Ultra')
  })
})

describe('videoModelAlreadySelected', () => {
  // The trigger glues the caret straight onto the name, with NO space: "Omni Flasharrow_drop_down".
  it('matches the real trigger label, whose caret text is not separated by a space', () => {
    expect(videoModelAlreadySelected('Omni Flasharrow_drop_down', 'Omni Flash')).toBe(true)
    expect(videoModelAlreadySelected('Veo 3.1 - Qualityarrow_drop_down', 'Veo 3.1 - Quality')).toBe(true)
  })

  it('accepts a loosely-spelled request against the rendered label', () => {
    expect(videoModelAlreadySelected('Veo 3.1 - Fastarrow_drop_down', 'Veo 3.1 Fast')).toBe(true)
  })

  it('does not confuse a different tier for the target', () => {
    expect(videoModelAlreadySelected('Veo 3.1 - Fastarrow_drop_down', 'Veo 3.1 - Quality')).toBe(false)
  })

  it('does not let "Lite [Lower Priority]" satisfy a request for plain "Lite"', () => {
    // The suffix has a LEADING SPACE — the earlier lookahead guard assumed it did not, and
    // let this exact case through.
    expect(videoModelAlreadySelected('Veo 3.1 - Lite [Lower Priority]arrow_drop_down', 'Veo 3.1 - Lite')).toBe(false)
    expect(
      videoModelAlreadySelected('Veo 3.1 - Lite [Lower Priority]arrow_drop_down', 'Veo 3.1 - Lite [Lower Priority]'),
    ).toBe(true)
  })

  it('handles a missing label', () => {
    expect(videoModelAlreadySelected(null, 'Veo 3.1 - Quality')).toBe(false)
  })
})

describe('aspectAlreadySelected', () => {
  it('matches the confirmed 16:9 icon inside a concatenated trigger label', () => {
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_16_91x', '16:9')).toBe(true)
  })

  it('matches the confirmed 4:3 icon, which is a descriptive name (crop_landscape), not a derived one', () => {
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_landscape1x', '4:3')).toBe(true)
  })

  it('tolerates count digits immediately after the icon name (no separator, e.g. x2)', () => {
    // Proves the "no lookahead guard needed" reasoning in compose.ts: the count tab's word
    // characters sit directly against the icon name and must not block the match.
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_16_9x2', '16:9')).toBe(true)
  })

  it('uses the live-confirmed descriptive icons for 1:1 and 3:4, not derived numeric ones', () => {
    // Mapped live 2026-08-12 (smoke-compose-popover.ts): Flow's five image ratios render as
    // crop_16_9 / crop_9_16 / crop_landscape / crop_portrait / crop_square. This test used to
    // assert crop_1_1 for 1:1 — the same guess the code made, which is exactly why the wrong
    // ligature survived: a unit test that encodes the implementation's assumption proves nothing.
    expect(aspectAlreadySelected('🍌 Nano Banana Procrop_squarex1', '1:1')).toBe(true)
    expect(aspectAlreadySelected('🍌 Nano Banana Procrop_portraitx1', '3:4')).toBe(true)
    expect(aspectAlreadySelected('🍌 Nano Banana Procrop_1_1x1', '1:1')).toBe(false)
  })

  it('does not confuse 1:1 with a hypothetical 21:9 (both fall outside the descriptive set)', () => {
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_21_91x', '1:1')).toBe(false)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_squarex1', '21:9')).toBe(false)
  })

  it('does not confuse 16:9 and 9:16 (task-flagged confusable pair)', () => {
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_9_161x', '16:9')).toBe(false)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_16_91x', '9:16')).toBe(false)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_9_161x', '9:16')).toBe(true)
  })

  it('handles a missing label', () => {
    expect(aspectAlreadySelected(null, '16:9')).toBe(false)
  })
})

describe('video clip duration', () => {
  // Every label below was READ OFF THE LIVE TRIGGER on 2026-08-12 (smoke-duration.ts /
  // smoke-duration-model.ts), not derived from the parser. That distinction matters: the
  // aspect helper's tests once asserted `crop_1_1` because the code guessed `crop_1_1`, and
  // two green suites hid a selector that matched nothing.
  const LIVE = {
    four: 'Video · 4scrop_9_16x1',
    six: 'Video · 6scrop_9_16x1',
    eight: 'Video · 8scrop_9_16x1',
    ten: 'Video · 10scrop_9_16x1',
    image: '🍌 Nano Banana Procrop_16_9x1',
  }

  it('offers exactly the four lengths Flow shows', () => {
    expect([...VIDEO_DURATIONS]).toEqual([4, 6, 8, 10])
  })

  it('parses each live trigger label', () => {
    expect(parseVideoDuration(LIVE.four)).toBe(4)
    expect(parseVideoDuration(LIVE.six)).toBe(6)
    expect(parseVideoDuration(LIVE.eight)).toBe(8)
    expect(parseVideoDuration(LIVE.ten)).toBe(10)
  })

  it('reads 10s as ten, not as one or zero', () => {
    // The digit-by-digit failure a substring matcher invites: "10s" contains "0s", and a
    // matcher anchored on the leading digit would call it "1".
    expect(videoDurationAlreadySelected(LIVE.ten, 10)).toBe(true)
    expect(videoDurationAlreadySelected(LIVE.ten, 1)).toBe(false)
    expect(videoDurationAlreadySelected(LIVE.ten, 0)).toBe(false)
  })

  it('is not fooled by the aspect ligature or count digits sharing the label', () => {
    // "crop_9_16" and "x1" are the neighbours; nothing in them may read as a duration.
    expect(videoDurationAlreadySelected(LIVE.four, 9)).toBe(false)
    expect(videoDurationAlreadySelected(LIVE.four, 16)).toBe(false)
    expect(videoDurationAlreadySelected(LIVE.four, 1)).toBe(false)
    expect(videoDurationAlreadySelected(LIVE.four, 4)).toBe(true)
  })

  it('refuses to read a duration off an image-mode label', () => {
    // An image-mode trigger carries no duration at all; returning a number here would let the
    // guard pass without the popover ever being in Video mode.
    expect(parseVideoDuration(LIVE.image)).toBe(null)
    expect(videoDurationAlreadySelected(LIVE.image, 8)).toBe(false)
    expect(parseVideoDuration(null)).toBe(null)
  })

  it('caps every Veo tier at 8s and only Omni Flash at 10s', () => {
    // Confirmed by opening the popover on each tier: the 10s tab is absent on Veo.
    expect(maxDurationForModel('Omni Flash')).toBe(10)
    expect(maxDurationForModel('Veo 3.1 - Lite')).toBe(8)
    expect(maxDurationForModel('Veo 3.1 - Fast')).toBe(8)
    expect(maxDurationForModel('Veo 3.1 - Quality')).toBe(8)
    expect(maxDurationForModel('Veo 3.1 - Lite [Lower Priority]')).toBe(8)
  })

  it('accepts the loose spellings callers actually write', () => {
    // Same canonicalisation the model click uses — "Veo 3.1 Fast" never appears in the menu.
    expect(maxDurationForModel('veo 3.1 fast')).toBe(8)
    expect(maxDurationForModel('omni flash')).toBe(10)
    expect(maxDurationForModel('OmniFlash')).toBe(10)
  })

  it('caps an unrecognised model at 8s', () => {
    // Conservative on purpose: a model Flow adds tomorrow gets the safe limit, and asking for
    // 10s on it fails loudly rather than silently returning an 8s clip.
    expect(maxDurationForModel('Veo 4')).toBe(8)
  })
})
