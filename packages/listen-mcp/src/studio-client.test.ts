import { describe, it, expect } from 'vitest'
import { classifyPage } from './studio-client'
import { defaultModelName } from './studio-client'

describe('classifyPage', () => {
  const ok = { url: 'https://aistudio.google.com/prompts/new_chat', lastModelText: 'Here is the description.' }

  it('is ok for a normal reply', () => {
    expect(classifyPage(ok)).toBe('ok')
  })

  // Trap 3 — the signed-out page is on the SAME host, so a host match proves nothing.
  it('reads /welcome as signed out, and signed out beats everything else', () => {
    expect(classifyPage({ url: 'https://aistudio.google.com/welcome', lastModelText: '' })).toBe('signed-out')
    expect(classifyPage({ url: 'https://aistudio.google.com/welcome', lastModelText: 'quota exceeded' })).toBe('signed-out')
  })

  // Trap 4 — the 403 that blocked T3, in both the wordings we have actually seen.
  it('classifies the permission refusal as an error, not a timeout', () => {
    expect(classifyPage({ ...ok, lastModelText: 'error An internal error has occurred.' })).toBe('error')
    expect(classifyPage({ ...ok, lastModelText: 'The caller does not have permission' })).toBe('error')
    expect(classifyPage({ ...ok, lastModelText: 'Failed to create interaction: permission denied.' })).toBe('error')
  })

  it('classifies quota wording as rate-limited', () => {
    for (const t of ['Resource has been exhausted', 'you have hit a rate limit', 'Too many requests', 'Quota exceeded']) {
      expect(classifyPage({ ...ok, lastModelText: t })).toBe('rate-limited')
    }
  })

  it('prefers rate-limited over error when both could match', () => {
    expect(classifyPage({ ...ok, lastModelText: 'quota exceeded — something went wrong' })).toBe('rate-limited')
  })
})

describe('defaultModelName', () => {
  it('defaults to a Pro model and honours LISTEN_MODEL', () => {
    expect(defaultModelName({})).toBe('Gemini 3.1 Pro')
    expect(defaultModelName({ LISTEN_MODEL: 'Gemini 3.8 Flash' })).toBe('Gemini 3.8 Flash')
    expect(defaultModelName({ LISTEN_MODEL: '   ' })).toBe('Gemini 3.1 Pro')
  })
})
