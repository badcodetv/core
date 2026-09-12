/**
 * Read `.env` at the repo root into `process.env`.
 *
 * 🔴 Why this exists: an MCP server is launched by the CLIENT (`.mcp.json` → `npx tsx …`), not
 * from a shell that has sourced `.env`. So `GEMINI_API_KEY` was set for a hand-run proof and
 * absent for every real session — `listen_status` reported `apiKeySet: false` and every describe
 * would have fallen back to the browser, which cannot generate at all. Found by thread 08,
 * 2026-09-12, before it cost anyone a debugging session.
 *
 * 🔑 A real environment variable ALWAYS wins over the file. A key pinned in the shell is an
 * explicit instruction; silently overriding it with a stale file value is the kind of bug that
 * takes an afternoon. Same parsing conventions as `packages/cli/src/pull.ts`: an optional
 * `export ` prefix, and one matching pair of surrounding quotes removed.
 */
import { readFileSync } from 'node:fs'
import { join } from 'node:path'

export function parseEnvFile(content: string): Record<string, string> {
  const out: Record<string, string> = {}
  for (const raw of content.split('\n')) {
    const line = raw.replace(/^\s*export\s+/, '').trim()
    if (!line || line.startsWith('#')) continue
    const eq = line.indexOf('=')
    if (eq <= 0) continue
    const key = line.slice(0, eq).trim()
    if (!/^[A-Za-z_][A-Za-z0-9_]*$/.test(key)) continue
    let value = line.slice(eq + 1).trim()
    if (value.length >= 2 && (value[0] === '"' || value[0] === "'") && value.at(-1) === value[0]) {
      value = value.slice(1, -1)
    }
    out[key] = value
  }
  return out
}

/** Returns the names it set (never the values — these are secrets). */
export function loadEnvFile(repoRoot: string, env: NodeJS.ProcessEnv = process.env): string[] {
  let content: string
  try {
    content = readFileSync(join(repoRoot, '.env'), 'utf-8')
  } catch {
    return [] // no .env is normal; the caller reports a missing key on its own terms
  }
  const set: string[] = []
  for (const [k, v] of Object.entries(parseEnvFile(content))) {
    if (env[k] === undefined || env[k] === '') {
      env[k] = v
      set.push(k)
    }
  }
  return set
}
