/**
 * Lenses — the listening checklists in docs/listening/lenses/<name>.md. Changing what Gemini is
 * asked to listen for is a doc edit, not a code change (decision 6). A lens's `## ` headings are
 * the headings the answer must use, in order; its hash goes in the ledger so a description can
 * always be traced to the exact checklist that produced it.
 */
import { createHash } from 'node:crypto'
import { existsSync, readdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import type { Lens } from './types'

/** Split `---\nkey: value\n---\nbody`. A file with no frontmatter is all body. */
function splitFrontmatter(text: string): { meta: Record<string, string>; body: string } {
  const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(text)
  if (!m) return { meta: {}, body: text }
  const meta: Record<string, string> = {}
  for (const line of m[1]!.split(/\r?\n/)) {
    const kv = /^([A-Za-z_][\w-]*):\s*(.*)$/.exec(line)
    if (kv) meta[kv[1]!] = kv[2]!.trim().replace(/^(['"])(.*)\1$/, '$2')
  }
  return { meta, body: m[2]! }
}

export function parseLens(name: string, fileText: string): Lens {
  const { meta, body } = splitFrontmatter(fileText)
  const headings = body
    .split(/\r?\n/)
    .filter((l) => l.startsWith('## '))
    .map((l) => l.slice(3).trim())
  return {
    name: meta.name || name,
    description: meta.description ?? '',
    body: body.trim(),
    headings,
    hash: createHash('sha256').update(fileText).digest('hex').slice(0, 12),
  }
}

/** Lens names available in `dir`: '*.md' only, extension stripped, sorted. */
export function listLenses(dir: string): string[] {
  if (!existsSync(dir)) return []
  return readdirSync(dir)
    .filter((f) => f.endsWith('.md'))
    .map((f) => f.slice(0, -3))
    .sort()
}

export function loadLens(dir: string, name: string): Lens {
  const available = listLenses(dir)
  // Names come from the caller, so never let one walk out of the lens directory.
  if (!available.includes(name)) {
    throw new Error(`LENS_NOT_FOUND: no lens "${name}". Available: ${available.join(', ') || '(none)'}`)
  }
  return parseLens(name, readFileSync(join(dir, `${name}.md`), 'utf8'))
}
