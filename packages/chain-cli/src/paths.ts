import { existsSync, readFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = (): string => dirname(fileURLToPath(import.meta.url))

/** Walk up from `from`, returning the first directory `match` accepts. */
function walkUp(from: string, match: (dir: string) => boolean): string | null {
  let dir = resolve(from)
  for (;;) {
    if (match(dir)) return dir
    const parent = dirname(dir)
    if (parent === dir) return null
    dir = parent
  }
}

function isWorkspaceRoot(dir: string): boolean {
  const manifest = join(dir, 'package.json')
  if (!existsSync(manifest)) return false
  try {
    return 'workspaces' in JSON.parse(readFileSync(manifest, 'utf8'))
  } catch {
    // Unparseable package.json — keep walking rather than dying here.
    return false
  }
}

/**
 * Locate the Anchor workspace.
 *
 * Found by looking for `Anchor.toml`, not by assuming a layout — this package is
 * meant to be lifted into projects that are not npm monorepos, where it may sit
 * inside `chain/` rather than beside it, and where there is no workspace root to
 * measure from at all. `CHAIN_DIR` overrides for anything stranger.
 *
 * Passing `root` keeps the original meaning: `<root>/chain`.
 */
export function chainDir(root?: string): string {
  if (root !== undefined) return join(root, 'chain')
  if (process.env.CHAIN_DIR) return resolve(process.env.CHAIN_DIR)

  const found = walkUp(here(), (dir) =>
    existsSync(join(dir, 'Anchor.toml')) || existsSync(join(dir, 'chain', 'Anchor.toml')),
  )
  if (found === null) {
    throw new Error(
      `Could not find an Anchor workspace above ${here()}. ` +
        'Expected an Anchor.toml here or in a chain/ directory; set CHAIN_DIR to override.',
    )
  }
  return existsSync(join(found, 'Anchor.toml')) ? found : join(found, 'chain')
}

/**
 * The project root.
 *
 * The npm workspace root when there is one, since that is where `--out` paths
 * and node_modules are anchored. Otherwise the directory containing the Anchor
 * workspace, because a project is not obliged to be an npm monorepo — requiring
 * one was the first thing to break when this was copied into a Go project.
 *
 * Do NOT reach for process.cwd() instead: `npm run --workspace <pkg>` sets the
 * CWD to the package directory, so anything resolved relative to it silently
 * points at the wrong place depending on how the command was invoked.
 */
export function repoRoot(from: string = here()): string {
  const workspace = walkUp(from, isWorkspaceRoot)
  if (workspace !== null) return workspace
  // Only fall back for the default caller; an explicit `from` is asking a
  // question about that path, and answering with an unrelated directory would
  // be worse than saying no.
  if (from === here()) return dirname(chainDir())
  throw new Error(`No workspace root above ${from}`)
}

/** The pinned toolchain versions. */
export interface Versions {
  rust: string
  agave: string
  anchor: string
  node: string
  crates: Record<string, string>
  npm: Record<string, string>
}

export function readVersions(root?: string): Versions {
  return JSON.parse(readFileSync(join(chainDir(root), 'versions.json'), 'utf8'))
}
