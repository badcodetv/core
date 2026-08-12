import { describe, it, expect } from 'vitest'
import { isBoxCleared, modelAlreadySelected, videoModelAlreadySelected, aspectAlreadySelected } from './compose'

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

describe('videoModelAlreadySelected', () => {
  it('matches the trigger label ("<model> arrow_drop_down")', () => {
    expect(videoModelAlreadySelected('Veo 3.1 Quality arrow_drop_down', 'Veo 3.1 Quality')).toBe(true)
    expect(videoModelAlreadySelected('Omni Flash arrow_drop_down', 'Omni Flash')).toBe(true)
  })

  it('does not confuse a different tier for the target', () => {
    expect(videoModelAlreadySelected('Veo 3.1 Fast arrow_drop_down', 'Veo 3.1 Quality')).toBe(false)
  })

  it('does not let "Veo 3.1 Lite[Lower Priority]" satisfy a request for "Veo 3.1 Lite"', () => {
    // The bug this guards: "Veo 3.1 Lite" is a strict prefix of "Veo 3.1 Lite[Lower Priority]".
    // A naive substring check would report the Lower Priority tier as already-selected and
    // silently generate on it instead.
    expect(videoModelAlreadySelected('Veo 3.1 Lite[Lower Priority]', 'Veo 3.1 Lite')).toBe(false)
    expect(videoModelAlreadySelected('Veo 3.1 Lite[Lower Priority]', 'Veo 3.1 Lite[Lower Priority]')).toBe(true)
  })

  it('handles a missing label', () => {
    expect(videoModelAlreadySelected(null, 'Veo 3.1 Quality')).toBe(false)
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

  it('does not confuse 1:1 and 21:9 (task-flagged confusable pair)', () => {
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_21_91x', '1:1')).toBe(false)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_1_11x', '21:9')).toBe(false)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_1_11x', '1:1')).toBe(true)
    expect(aspectAlreadySelected('🍌 Nano Banana 2crop_21_91x', '21:9')).toBe(true)
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
