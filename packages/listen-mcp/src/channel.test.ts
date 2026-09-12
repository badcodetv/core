import { describe, it, expect } from 'vitest'
import { isListenCandidate, LISTEN_MIN_CHANNEL } from './channel'

describe('isListenCandidate', () => {
  it('accepts a browser with an AI Studio tab', () => {
    expect(isListenCandidate(['https://aistudio.google.com/prompts/new_chat'])).toBe(true)
  })

  it('refuses a browser with no AI Studio tab', () => {
    expect(isListenCandidate(['https://suno.com/create'])).toBe(false)
    expect(isListenCandidate([])).toBe(false)
  })

  // 🔴 The regression this exists for: Flow moved to flow.google.com (2026-09-11), so a check
  // that only knew the old labs.google URL would have claimed Flow's signed-in browser.
  it('refuses a Flow browser even when AI Studio is also open there', () => {
    expect(isListenCandidate(['https://flow.google.com/', 'https://aistudio.google.com/'])).toBe(false)
    expect(isListenCandidate(['https://labs.google/fx/tools/flow', 'https://aistudio.google.com/'])).toBe(false)
  })

  it('never considers channel 1 — that is Flow and Suno', () => {
    expect(LISTEN_MIN_CHANNEL).toBe(2)
  })
})
