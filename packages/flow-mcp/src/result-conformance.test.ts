import { describe, it, expect } from 'vitest'
import { CallToolResultSchema } from '@modelcontextprotocol/sdk/types.js'
import { ok, fail, NOT_RUNNING_HINT } from './result'

/**
 * Validate what our tools actually return against the MCP SDK's OWN result schema — the
 * same zod validator the client runs on every tool response.
 *
 * This exists because of a live failure on 2026-08-12: three tools returned arrays, `ok()`
 * blindly cast them into `structuredContent`, and every call died at the protocol boundary
 * with "expected record, received array" before the result reached the caller. Nothing in
 * the unit suite could see it — the parsers were all correct — and it took a browser, a
 * logged-in session and an MCP reconnect to discover something the schema knew statically.
 *
 * Catching this class of bug here costs milliseconds and no Chrome. Any new result shape
 * should get a line in `RESULTS` below.
 */
const RESULTS: Record<string, unknown> = {
  'object payload': ok({ path: '/tmp/p05.jpg', mediaId: 'uuid' }),
  'array payload (flow_list_media / _projects / _characters)': ok([
    { title: 'Man in suit holding papers', kind: 'Image', index: 0 },
  ]),
  'empty array payload': ok([]),
  'nested arrays inside an object': ok({ items: [1, 2, 3], meta: { count: 3 } }),
  'string payload': ok('done'),
  'null payload': ok(null),
  'error with hint': fail('NOT_RUNNING', 'Chrome is not reachable on :9222', NOT_RUNNING_HINT),
  'error without hint': fail('TIMEOUT', 'generation timed out'),
}

describe('MCP protocol conformance', () => {
  for (const [name, result] of Object.entries(RESULTS)) {
    it(`accepts ${name}`, () => {
      const parsed = CallToolResultSchema.safeParse(result)
      expect(parsed.success ? null : parsed.error.issues).toBe(null)
    })
  }

  // Guard the guard: if a future SDK stopped rejecting an array here, every test above would
  // still pass while proving nothing. This asserts the validator can actually fail.
  it('still rejects the exact shape that broke us, so these tests retain their teeth', () => {
    const regression = {
      content: [{ type: 'text', text: '[]' }],
      structuredContent: [{ name: 'Untitled Character' }],
    }
    expect(CallToolResultSchema.safeParse(regression).success).toBe(false)
  })
})
