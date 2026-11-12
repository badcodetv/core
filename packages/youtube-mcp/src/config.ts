/**
 * Where the YouTube server finds its secrets, and small pure helpers shared by the server and the
 * login script.
 *
 * 🔑 Two secrets, kept in two places, neither in git:
 *   - the OAuth CLIENT (which Google Cloud app is asking): YOUTUBE_CLIENT_ID + YOUTUBE_CLIENT_SECRET
 *     in `.env` at the repo root (git-ignored), or the real environment.
 *   - the REFRESH TOKEN (the BadCode channel's "yes, this app may manage me"): a JSON file outside
 *     the repo, `~/.config/badcode/youtube-token.json` (mode 600), or YOUTUBE_TOKEN_FILE.
 * The client can be shared between Kai and Jack; the token is per machine and per sign-in.
 */
import { readFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'

/**
 * One scope for everything: upload, edit, thumbnails, playlists, captions.
 * `youtube.force-ssl` is accepted by videos.insert/update, thumbnails.set, playlists.* and
 * captions.*; asking for several narrower scopes would only make the consent screen longer.
 */
export const SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

export function tokenFile(env: NodeJS.ProcessEnv = process.env): string {
  return env.YOUTUBE_TOKEN_FILE?.trim() || join(homedir(), '.config', 'badcode', 'youtube-token.json')
}

export interface ClientCreds {
  clientId: string
  clientSecret: string
}

export function clientCreds(env: NodeJS.ProcessEnv = process.env): ClientCreds | null {
  const clientId = env.YOUTUBE_CLIENT_ID?.trim() ?? ''
  const clientSecret = env.YOUTUBE_CLIENT_SECRET?.trim() ?? ''
  return clientId && clientSecret ? { clientId, clientSecret } : null
}

/**
 * Read `.env` at the repo root into `process.env` (a copy of listen-mcp's env-file.ts, kept local
 * so this server doesn't pull in Playwright).
 *
 * 🔴 An MCP server is launched by the client (`.mcp.json`), not from a shell that sourced `.env`,
 * so without this the client id is absent in every real session. A real env var always wins.
 */
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

/**
 * Client credentials read FRESH each time: a real environment variable (set before this process
 * read .env) wins, otherwise the current contents of .env.
 *
 * 🔴 Why: the server is started when Claude starts. On 2026-11-12 Kai fixed .env after that, and
 * every call failed with `unauthorized_client` because the server still held the old client id
 * (a different Cloud project) from startup. Reading .env on each refresh removes the restart.
 */
export function freshClientCreds(repoRoot: string, realEnv: Record<string, string | undefined>): ClientCreds | null {
  let file: Record<string, string> = {}
  try {
    file = parseEnvFile(readFileSync(join(repoRoot, '.env'), 'utf-8'))
  } catch {
    /* no .env */
  }
  const pick = (k: string) => (realEnv[k]?.trim() || file[k]?.trim() || '')
  return clientCreds({ YOUTUBE_CLIENT_ID: pick('YOUTUBE_CLIENT_ID'), YOUTUBE_CLIENT_SECRET: pick('YOUTUBE_CLIENT_SECRET') })
}

export function loadEnvFile(repoRoot: string, env: NodeJS.ProcessEnv = process.env): string[] {
  let content: string
  try {
    content = readFileSync(join(repoRoot, '.env'), 'utf-8')
  } catch {
    return []
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

/**
 * Accept a Windows path (`D:\badcode-videos\x.mp4`, `D:/…`) or a WSL path and return the WSL one.
 * Finished cuts live on D:, and Kai and Jack paste Windows paths.
 */
export function toLocalPath(p: string): string {
  const s = p.trim().replace(/^"(.*)"$/, '$1')
  const m = /^([A-Za-z]):[\\/](.*)$/.exec(s)
  if (!m) return s
  return `/mnt/${m[1]!.toLowerCase()}/${m[2]!.replace(/\\/g, '/')}`
}

const VIDEO_TYPES: Record<string, string> = {
  mp4: 'video/mp4',
  m4v: 'video/mp4',
  mov: 'video/quicktime',
  webm: 'video/webm',
  mkv: 'video/x-matroska',
  avi: 'video/x-msvideo',
}
const IMAGE_TYPES: Record<string, string> = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg' }

const ext = (p: string) => p.split('.').pop()?.toLowerCase() ?? ''
export const videoMime = (p: string) => VIDEO_TYPES[ext(p)] ?? 'application/octet-stream'
export const imageMime = (p: string): string | null => IMAGE_TYPES[ext(p)] ?? null

/** Accept a bare id, youtu.be/<id>, watch?v=<id>, shorts/<id> or a Studio link. */
export function parseId(s: string): string {
  const t = s.trim()
  const m =
    /(?:youtu\.be\/|[?&]v=|\/shorts\/|\/video\/|\/live\/)([A-Za-z0-9_-]{11})/.exec(t) ?? /^([A-Za-z0-9_-]{11})$/.exec(t)
  if (!m) throw new Error(`Not a YouTube video id or link: ${s}`)
  return m[1]!
}
