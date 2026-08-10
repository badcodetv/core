import { existsSync, readFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

/**
 * Find the monorepo root by walking up for a package.json declaring `workspaces`.
 *
 * Do NOT reach for process.cwd() instead: `npm run --workspace <pkg>` sets the CWD
 * to the package directory, so anything resolved relative to it silently points at
 * the wrong place depending on how the command was invoked.
 */
export function repoRoot(from = dirname(fileURLToPath(import.meta.url))): string {
  let dir = resolve(from)
  for (;;) {
    const manifest = join(dir, 'package.json')
    if (existsSync(manifest)) {
      try {
        if ('workspaces' in JSON.parse(readFileSync(manifest, 'utf8'))) return dir
      } catch {
        // Unparseable package.json — keep walking rather than dying here.
      }
    }
    const parent = dirname(dir)
    if (parent === dir) throw new Error(`No workspace root above ${from}`)
    dir = parent
  }
}

/** Absolute path to the Anchor workspace. */
export const chainDir = (root = repoRoot()): string => join(root, 'chain')

/** The pinned toolchain versions. */
export interface Versions {
  rust: string
  agave: string
  anchor: string
  node: string
  crates: Record<string, string>
  npm: Record<string, string>
}

export function readVersions(root = repoRoot()): Versions {
  return JSON.parse(readFileSync(join(chainDir(root), 'versions.json'), 'utf8'))
}
