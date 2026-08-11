import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import { chainDir } from './paths.js'
import { runInChain } from './runner.js'

/**
 * Anchor 1.x defaults its local validator to surfpool, which we do not install.
 * Every test invocation must ask for the legacy validator (solana-test-validator,
 * which ships with Agave) or it dies with "Failed to spawn `surfpool`".
 */
export const LEGACY_VALIDATOR_ARGS = ['--validator', 'legacy'] as const

export const idlDir = (root?: string): string => join(chainDir(root), 'target', 'idl')
export const typesDir = (root?: string): string => join(chainDir(root), 'target', 'types')

/** Committed home for generated interfaces. See syncIdl. */
export const generatedDir = (root?: string): string => join(chainDir(root), 'idl')

/** Where Anchor expects program keypairs, and where they get wiped from. */
export const deployDir = (root?: string): string => join(chainDir(root), 'target', 'deploy')

/** Program keypairs that survive `rm -rf target`. See chain/keys/README.md. */
export const keysDir = (root?: string): string => join(chainDir(root), 'keys')

/**
 * Put saved program keypairs back where Anchor looks for them.
 *
 * Anchor only reads keypairs from target/deploy, which is a build artifact — so
 * cleaning the build silently changes every program's address and breaks the
 * `declare_id!` in its source. Keeping the canonical copy in chain/keys and
 * restoring it before each build makes addresses stable across cleans, machines
 * and containers.
 */
export function restoreKeys(root?: string): string[] {
  const src = keysDir(root)
  if (!existsSync(src)) return []
  const dest = deployDir(root)
  mkdirSync(dest, { recursive: true })
  const restored: string[] = []
  for (const f of readdirSync(src).filter((f) => f.endsWith('-keypair.json'))) {
    const target = join(dest, f)
    // Never clobber: if a build already produced one, that is the live identity.
    if (!existsSync(target)) {
      copyFileSync(join(src, f), target)
      restored.push(f)
    }
  }
  return restored
}

/**
 * Build the workspace, or one program.
 *
 * Narrowing to one program matters more than it looks: Anchor rebuilds every
 * program *and* re-runs IDL generation for each, so a one-line edit to one
 * program costs the whole workspace. Naming it turns a 90-second loop into a
 * 25-second one.
 */
export function build(
  opts: { programName?: string; features?: string[]; root?: string } | string = {},
): void {
  // Accept a bare root for the original call shape.
  const { programName, features, root } =
    typeof opts === 'string' ? { programName: undefined, features: undefined, root: opts } : opts
  restoreKeys(root)
  runInChain('anchor', ['build', ...buildArgs({ programName, features })], root)
  syncIdl(root)
}

/**
 * Split out so the flag logic is testable without running Anchor.
 *
 * Cargo features go after `--`, which for `anchor build` really does forward
 * them (unlike `anchor deploy`, where everything after `--` is silently
 * dropped — see deployProgram).
 */
export function buildArgs(opts: { programName?: string; features?: string[] }): string[] {
  return [
    ...(opts.programName ? ['--program-name', opts.programName] : []),
    ...(opts.features?.length ? ['--', '--features', opts.features.join(',')] : []),
  ]
}

export interface DeployOptions {
  cluster: string
  programName?: string
  /**
   * Bytes to reserve for the program account.
   *
   * Only has any effect on a program's FIRST deploy, which is the only chance to
   * ask for headroom — see the caller for why you want some.
   */
  maxLen?: number
  root?: string
}

export function deploy({ cluster, programName, maxLen, root }: DeployOptions): void {
  restoreKeys(root)
  const args = [
    'deploy',
    '--provider.cluster', cluster,
    ...(programName ? ['--program-name', programName] : []),
    // Everything after `--` goes to `solana program deploy`.
    ...(maxLen === undefined ? [] : ['--', '--max-len', String(maxLen)]),
  ]
  try {
    runInChain('anchor', args, root)
  } catch (err) {
    // Upgrading in place only works while the new binary still fits the space
    // allocated at first deploy, and growing past it is currently unrecoverable:
    // the CLI sends ExtendProgram, which this loader rejects as "superseded by
    // ExtendProgramChecked". Hence the headroom reserved at first deploy.
    throw new Error(
      `${(err as Error).message}\n\n` +
        'If that mentioned "Auto-extend failed" or "ExtendProgram was superseded", the program ' +
        'outgrew the space reserved for it at first deploy, and this toolchain cannot extend it ' +
        'in place. On localnet: `chain reset`, which redeploys with fresh headroom. On devnet: ' +
        '`solana program extend <program-id> <bytes>`.',
    )
  }
}

/**
 * Deploy one program straight through `solana program deploy`.
 *
 * Exists because `anchor deploy -- --max-len N` silently DROPS everything after
 * the `--`, despite advertising it as "arguments to pass to the underlying
 * `solana program deploy`". Verified: via Anchor the account is allocated at the
 * binary's exact size; called directly, the requested size is honoured. Without
 * this there is no way to reserve headroom, and no way to redeploy a program
 * that grew.
 *
 * Paths are relative to the Anchor workspace so they mean the same thing on the
 * host and inside the container.
 */
export function deployProgram(opts: {
  name: string
  url: string
  maxLen?: number
  root?: string
}): void {
  restoreKeys(opts.root)
  runInChain(
    'solana',
    [
      'program', 'deploy',
      '--url', opts.url,
      '--program-id', `target/deploy/${opts.name}-keypair.json`,
      ...(opts.maxLen === undefined ? [] : ['--max-len', String(opts.maxLen)]),
      `target/deploy/${opts.name}.so`,
    ],
    opts.root,
  )
}

/**
 * Run a test suite against the already-running validator.
 *
 * `--skip-local-validator` is not an optimisation, it is the only thing that
 * works here: `anchor test` otherwise starts a second validator on the same port
 * as the one `chain up` is running. It also makes the suite several seconds
 * faster and means tests see the same chain the browser does. The cost is that
 * state persists between runs, so tests must assert on movement rather than on
 * absolute values.
 *
 * `script` selects an Anchor.toml [scripts] entry.
 */
export interface TestOptions {
  script?: string
  skipBuild?: boolean
  /** Let Anchor start its own validator instead of reusing the running one. */
  ownValidator?: boolean
  /** Cargo features for the build this test run performs. */
  features?: string[]
  root?: string
}

/** Split out so the flag logic is testable without running Anchor. */
export function testArgs(opts: TestOptions): string[] {
  return [
    'test',
    ...(opts.ownValidator ? LEGACY_VALIDATOR_ARGS : ['--skip-local-validator']),
    ...(opts.script ? ['--script', opts.script] : []),
    ...(opts.skipBuild ? ['--skip-build'] : []),
    ...(opts.features?.length ? ['--', '--features', opts.features.join(',')] : []),
  ]
}

export function test(opts: TestOptions = {}): void {
  restoreKeys(opts.root)
  runInChain('anchor', testArgs(opts), opts.root)
}

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

/**
 * Publish the generated interface — IDL *and* TypeScript types — to chain/idl.
 *
 * This is the seam that makes the dev loop work: change a Rust struct, rebuild,
 * and the frontend's types change with it, because it imports from here rather
 * than from the gitignored build output. The IDL also carries the program's
 * deployed address, so nothing downstream hardcodes one.
 *
 * Runs automatically after every build; committed so a fresh clone typechecks
 * without a Rust toolchain.
 */
export function syncIdl(root?: string): string[] {
  const dest = generatedDir(root)
  mkdirSync(dest, { recursive: true })
  const written: string[] = []

  for (const [src, ext] of [[idlDir(root), '.json'], [typesDir(root), '.ts']] as const) {
    if (!existsSync(src)) continue
    for (const f of readdirSync(src).filter((f) => f.endsWith(ext))) {
      copyFileSync(join(src, f), join(dest, f))
      written.push(f)
    }
  }

  if (written.length === 0) {
    throw new Error(`Nothing to publish from ${idlDir(root)}. Did the build fail?`)
  }
  return written
}
