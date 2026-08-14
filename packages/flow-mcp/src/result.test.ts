import { describe, it, expect } from 'vitest'
import { ok, fail, NOT_RUNNING_HINT } from './result'

describe('tool results', () => {
  it('wraps success data in text + structuredContent', () => {
    const r = ok({ path: '/tmp/p05.jpg', mediaId: 'uuid' })
    expect(r.isError).toBeUndefined()
    expect(r.structuredContent).toEqual({ path: '/tmp/p05.jpg', mediaId: 'uuid' })
    expect(JSON.parse(r.content[0].text)).toEqual({ path: '/tmp/p05.jpg', mediaId: 'uuid' })
  })

  // Live 2026-08-12: flow_list_characters failed the MCP client's own validation with
  // "expected record, received array" — structuredContent is spec'd as a record, and the
  // old blind `data as Record<...>` cast let every list tool ship an array into it. The
  // array still reaches the caller via content.text.
  it('omits structuredContent for arrays, keeping the payload in text', () => {
    const rows = [{ name: 'Economist', id: 'abc' }]
    const r = ok(rows)
    expect(r.isError).toBeUndefined()
    expect('structuredContent' in r).toBe(false)
    expect(JSON.parse(r.content[0].text)).toEqual(rows)
  })

  it('omits structuredContent for an empty array', () => {
    const r = ok([])
    expect('structuredContent' in r).toBe(false)
    expect(JSON.parse(r.content[0].text)).toEqual([])
  })

  it('omits structuredContent for primitives and null', () => {
    for (const v of ['a string', 42, true, null]) {
      const r = ok(v)
      expect('structuredContent' in r).toBe(false)
      expect(JSON.parse(r.content[0].text)).toEqual(v)
    }
  })

  it('marks failures and carries code/message/hint', () => {
    const r = fail('NOT_RUNNING', 'Chrome is not reachable on :9222', NOT_RUNNING_HINT)
    expect(r.isError).toBe(true)
    expect(JSON.parse(r.content[0].text)).toEqual({
      error: true,
      code: 'NOT_RUNNING',
      message: 'Chrome is not reachable on :9222',
      hint: NOT_RUNNING_HINT,
    })
  })

  it('omits hint when not provided', () => {
    const r = fail('TIMEOUT', 'generation timed out')
    expect(JSON.parse(r.content[0].text)).toEqual({
      error: true,
      code: 'TIMEOUT',
      message: 'generation timed out',
    })
  })
})
