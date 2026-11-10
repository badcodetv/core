/**
 * Recipe cards (docs/provenance/README.md): every file a tool generates gets a small JSON card saying
 * how it was made — engine, model, exact prompt, inputs, settings — so the work can be re-run on a
 * better model later from the repo alone.
 *
 * A card is written TWICE: beside the file (`<file>.prov.json`, for whoever browses the drive) and
 * into the repo mirror (`docs/provenance/cards/<path under the media root>.prov.json`, which is the
 * one git keeps). GitHub holds the recipes, Google Drive backs up the media; together, everything.
 *
 * The Python twin is scripts/provenance/prov.py. Keep the two writing the same shape.
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, join, relative, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

export const SCHEMA = 'badcode.prov/1'
const REPO = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')

export interface Card {
  kind: 'image' | 'video' | 'voice' | 'music' | 'sfx' | 'cut' | 'other'
  engine: string // 'google-flow', 'gemini-tts', 'suno', 'ffmpeg', …
  tool: string // the tool or script that made it
  model?: string | null // as asked for; null = the engine's default at the time
  prompt?: string | null
  inputs?: Record<string, unknown> // reference images, start frame, character, transcript…
  settings?: Record<string, unknown> // aspect, duration, count, voice…
  source_id?: string | null // the engine's own id (Flow mediaId, Suno song id)
  parent?: string | null // the file this one was made from (a still a clip animated, a golden an edit changed)
  why?: string | null // the note that asked for it, in Kai's words where there is one
}

export const mediaRoot = () => process.env.BADCODE_MEDIA_ROOT ?? '/mnt/d/badcode-videos'
export const mirrorRoot = () => process.env.BADCODE_PROV_MIRROR ?? join(REPO, 'docs/provenance/cards')

const posix = (p: string) => {
  const m = /^([A-Za-z]):[\\/](.*)$/.exec(p)
  return (m ? `/mnt/${m[1].toLowerCase()}/${m[2].replace(/\\/g, '/')}` : p).replace(/\/+$/, '')
}
const under = (p: string, home: string) => {
  const [a, b] = p.startsWith('/mnt/') ? [p.toLowerCase(), home.toLowerCase()] : [p, home]
  return a === b || a.startsWith(b + '/')
}
const readJson = (f: string) => { try { return existsSync(f) ? JSON.parse(readFileSync(f, 'utf8')) : {} } catch { return {} } }

/** A file in a shared story on ANY machine -> the same file under the media root (Kai's D:), so one clip has
 * one card whichever machine made it. Twin of _canonical in scripts/provenance/prov.py; homes come from
 * scripts/drive/folders.json, this machine's folders from badcode.local.json (scripts/drive/localmap.py). */
function canonical(abs: string): string | null {
  const folders: Record<string, { homes?: string[] }> = readJson(join(REPO, 'scripts/drive/folders.json')).folders ?? {}
  const mine: Record<string, string> = readJson(join(REPO, 'badcode.local.json')).stories ?? {}
  const p = posix(abs)
  const cands: [string, string][] = []
  for (const [story, v] of Object.entries(folders)) for (const h of v.homes ?? []) cands.push([posix(h), story])
  for (const [story, h] of Object.entries(mine)) cands.push([posix(h), story])
  cands.sort((a, b) => b[0].length - a[0].length)
  const hit = cands.find(([h]) => under(p, h))
  if (!hit) return null
  const rest = p.slice(hit[0].length)
  const root = posix(mediaRoot())
  const home = (folders[hit[1]]?.homes ?? []).map(posix).find((h) => under(h, root) && h !== root)
  return home ? home + rest : null
}

/** Where a file's card lives in the repo: its path under the media root, else under _elsewhere/. */
export function mirrorPath(file: string): string {
  const abs = resolve(file)
  const inRoot = (p: string) => { const r = relative(mediaRoot(), p); return r && !r.startsWith('..') && !r.startsWith('/') ? r : null }
  const c = inRoot(abs) ? null : canonical(abs)
  const rel = inRoot(abs) ?? (c ? inRoot(c) : null)
  return join(mirrorRoot(), rel ?? join('_elsewhere', abs.replace(/^\/+/, ''))) + '.prov.json'
}

/** Write one card beside the file and into the repo mirror. Never throws: a card must not cost a generation. */
export function writeCard(file: string, card: Card): string[] {
  const body = JSON.stringify({ schema: SCHEMA, file: resolve(file), made: new Date().toISOString(), by: 'claude', ...card }, null, 1) + '\n'
  const wrote: string[] = []
  for (const p of [resolve(file) + '.prov.json', mirrorPath(file)]) {
    try {
      mkdirSync(dirname(p), { recursive: true })
      writeFileSync(p, body)
      wrote.push(p)
    } catch (err) {
      console.error(`prov: could not write ${p}: ${(err as Error).message}`)
    }
  }
  return wrote
}

type Made = { path?: string; mediaId?: string; prompt?: string; skipped?: boolean; candidates?: Made[]; items?: Made[] }

/** Every file a Flow tool result names (path, candidates[], batch items[] and their candidates). */
export function madeFiles(result: unknown): { path: string; mediaId?: string; prompt?: string }[] {
  const out: { path: string; mediaId?: string; prompt?: string }[] = []
  const walk = (r: Made | undefined, prompt?: string) => {
    // A batch resume skips files already on disk: their cards were written when they were made.
    if (!r || typeof r !== 'object' || r.skipped) return
    const p = r.prompt ?? prompt
    if (r.path && !out.some((o) => o.path === r.path)) out.push({ path: r.path, mediaId: r.mediaId, prompt: p })
    for (const c of r.candidates ?? []) walk(c, p)
    for (const i of r.items ?? []) walk(i, p)
  }
  walk(result as Made)
  return out
}

/** Stamp a card on every file a Flow tool returned, then hand the result back untouched. */
export function stampFlow<T>(result: T, card: Omit<Card, 'engine' | 'source_id'>): T {
  for (const f of madeFiles(result)) {
    writeCard(f.path, { engine: 'google-flow', ...card, prompt: f.prompt ?? card.prompt ?? null, source_id: f.mediaId || null })
  }
  return result
}
