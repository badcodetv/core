import { describe, it, expect } from 'vitest'
import { isBoxCleared, modelAlreadySelected } from './compose'

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
