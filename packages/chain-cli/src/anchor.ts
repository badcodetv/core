import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import { chainDir } from './paths.js'
import { run } from './exec.js'

/**
 * Anchor 1.x defaults its local validator to surfpool, which we do not install.
 * Every test invocation must ask for the legacy validator (solana-test-validator,
 * which ships with Agave) or it dies with "Failed to spawn `surfpool`".
 */
export const LEGACY_VALIDATOR_ARGS = ['--validator', 'legacy'] as const

export function build(root?: string): void {
  run('anchor', ['build'], { cwd: chainDir(root) })
}

export interface DeployOptions {
  cluster: string
  programName?: string
  root?: string
}

export function deploy({ cluster, programName, root }: DeployOptions): void {
  run(
    'anchor',
    ['deploy', '--provider.cluster', cluster, ...(programName ? ['--program-name', programName] : [])],
    { cwd: chainDir(root) },
  )
}

/** Run a test suite. `script` selects an Anchor.toml [scripts] entry. */
export function test(opts: { script?: string; skipBuild?: boolean; root?: string } = {}): void {
  run(
    'anchor',
    [
      'test',
      ...LEGACY_VALIDATOR_ARGS,
      ...(opts.script ? ['--script', opts.script] : []),
      ...(opts.skipBuild ? ['--skip-build'] : []),
    ],
    { cwd: chainDir(opts.root) },
  )
}

export const idlDir = (root?: string): string => join(chainDir(root), 'target', 'idl')

/**
 * Copy generated IDLs somewhere a TypeScript package can import them.
 *
 * chain/target is gitignored, so anything that needs an IDL at build time needs
 * its own committed copy. Takes an explicit destination — this package must not
 * know the name of any consuming package.
 */
export function exportIdl(destination: string, root?: string): string[] {
  const src = idlDir(root)
  if (!existsSync(src)) {
    throw new Error(`No IDL at ${src}. Run \`chain build\` first.`)
  }
  const files = readdirSync(src).filter((f) => f.endsWith('.json'))
  if (files.length === 0) throw new Error(`No .json IDL files in ${src}. Did the build fail?`)

  mkdirSync(destination, { recursive: true })
  for (const f of files) copyFileSync(join(src, f), join(destination, f))
  return files
}
