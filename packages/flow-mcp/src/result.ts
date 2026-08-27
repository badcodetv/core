/** MCP tool return shape (subset of the SDK's CallToolResult). */
export interface ToolResult {
  [key: string]: unknown
  content: { type: 'text'; text: string }[]
  structuredContent?: Record<string, unknown>
  isError?: boolean
}

export const NOT_RUNNING_HINT =
  'No browser on this session\'s channel. Run `./scripts/browser-channel.sh claim` — it picks a free ' +
  'channel (a CDP port + its own Chrome profile), launches it if needed, and prints which one you got. ' +
  'Do NOT pick a port by hand. If it comes up logged out, ask the user to sign in to Google/Flow in ' +
  'that window; the login persists in that channel\'s profile. `flow_channels` shows what is running.'

/**
 * Success: encode data as JSON text, and additionally as structuredContent when — and only
 * when — the data is a plain object.
 *
 * MCP validates structuredContent as a record and REJECTS the whole tool call if it is an
 * array, so a list-returning tool (flow_list_media/_projects/_characters) that set it would
 * fail with an opaque "expected record, received array" before its result ever reached the
 * caller. The array is not wrapped in a synthetic key here because `content.text` already
 * carries the payload verbatim; inventing `{ items: [...] }` would make the two encodings of
 * the same result disagree.
 */
export function ok(data: unknown): ToolResult {
  const result: ToolResult = { content: [{ type: 'text', text: JSON.stringify(data) }] }
  if (isPlainObject(data)) result.structuredContent = data
  return result
}

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v)
}

/** Failure: a structured error the caller (skill) can branch on. */
export function fail(code: string, message: string, hint?: string): ToolResult {
  const body = hint
    ? { error: true, code, message, hint }
    : { error: true, code, message }
  return { content: [{ type: 'text', text: JSON.stringify(body) }], isError: true }
}
