import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
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

// ── Build provenance ────────────────────────────────────────────────────────
// A cargo feature build is a *different program*. It compiles in code the
// default build does not have, and that code exists precisely because it must
// never reach a real cluster. But `deploy` uploads whatever `.so` is on disk
// and has no way to tell the two apart — a binary carries no record of the
// flags that made it. So the build writes one down beside the artifact, and the
// deploy refuses to send a flagged artifact anywhere but a local validator.
//
// Nothing here knows what any feature means; a feature build is simply not the
// thing that ships.

/** Written beside `<name>.so`, and removed by the next default build of it. */
const FEATURE_MARKER = '.features.json'

export const featureMarkerPath = (programName: string, root?: string): string =>
  join(deployDir(root), `${programName}${FEATURE_MARKER}`)

/** Every program with a built artifact on disk. */
export function builtArtifacts(root?: string): string[] {
  const dir = deployDir(root)
  if (!existsSync(dir)) return []
  return readdirSync(dir).filter((f) => f.endsWith('.so')).map((f) => f.slice(0, -3))
}

/**
 * Record — or clear — which cargo features produced the artifacts just built.
 *
 * Clearing on a default build is the half that keeps this honest: a marker that
 * outlived the binary it described would refuse a deploy that is actually fine,
 * which is the fastest way to teach someone to delete the guard.
 */
export function recordBuildFeatures(opts: {
  programName?: string
  features?: string[]
  root?: string
}): string[] {
  const names = opts.programName ? [opts.programName] : builtArtifacts(opts.root)
  const touched: string[] = []
  for (const name of names) {
    const path = featureMarkerPath(name, opts.root)
    if (opts.features?.length) {
      mkdirSync(deployDir(opts.root), { recursive: true })
      writeFileSync(path, `${JSON.stringify({ features: opts.features, builtAt: new Date().toISOString() }, null, 2)}\n`)
      touched.push(name)
    } else if (existsSync(path)) {
      rmSync(path)
      touched.push(name)
    }
  }
  return touched
}

/**
 * The features that built this artifact: `[]` for a default build, `null` when
 * nothing was recorded.
 *
 * **Null is not suspicion.** A fresh checkout has no `target/` at all, so a
 * missing marker is the ordinary case and must not stand between anyone and a
 * legitimate deploy — there the deploy fails for the honest reason that there is
 * no binary. An unreadable marker is different: something wrote it and we cannot
 * tell what, so it is reported rather than assumed innocent.
 */
export function buildFeatures(programName: string, root?: string): string[] | null {
  const path = featureMarkerPath(programName, root)
  if (!existsSync(path)) return null
  try {
    const parsed = JSON.parse(readFileSync(path, 'utf8')) as { features?: unknown }
    if (!Array.isArray(parsed.features)) throw new Error('no features array')
    return parsed.features.map(String)
  } catch {
    return ['(unreadable build marker)']
  }
}

/** Localnet, by name or by URL. Everything else is somebody's real chain. */
export function isLocalCluster(clusterOrUrl: string): boolean {
  if (clusterOrUrl === 'localnet') return true
  try {
    const { hostname } = new URL(clusterOrUrl)
    return hostname === '127.0.0.1' || hostname === 'localhost' || hostname === '0.0.0.0'
  } catch {
    return false
  }
}

/**
 * Refuse to send a feature-built artifact to a cluster that is not local.
 *
 * Localnet keeps working exactly as before — that is where a feature build
 * belongs, and where the test suites need it.
 */
export function assertDefaultBuild(opts: {
  cluster: string
  programName?: string
  root?: string
}): void {
  if (isLocalCluster(opts.cluster)) return
  const names = opts.programName ? [opts.programName] : builtArtifacts(opts.root)
  for (const name of names) {
    const features = buildFeatures(name, opts.root)
    if (!features?.length) continue
    throw new Error(
      `Refusing to deploy ${name} to ${opts.cluster}: this binary was not built from the default sources.\n\n` +
        `target/deploy/${name}.so was produced by a build with cargo features [${features.join(', ')}], ` +
        'according to the marker written beside it. A feature build compiles in code the shipping build ' +
        'does not have, so it is for a local validator only.\n\n' +
        'Rebuild without features, then deploy again:\n' +
        `  chain build --program-name ${name}\n` +
        `  chain deploy --cluster ${opts.cluster} --program-name ${name}\n\n` +
        `(The marker is ${name}${FEATURE_MARKER}, written by the build that made this binary and ` +
        'removed by the next default build of it.)',
    )
  }
}

export interface BuildOptions {
  programName?: string
  features?: string[]
  /**
   * Publish the generated interface into chain/idl. Default true.
   *
   * **A command whose job is to run or to test passes `false`.** chain/idl is
   * tracked, and publishing it is a deliberate act with a diff to read — not a
   * side effect of starting a validator. See `publishOrReport`.
   */
  publish?: boolean
  root?: string
}

/**
 * Build the workspace, or one program.
 *
 * Narrowing to one program matters more than it looks: Anchor rebuilds every
 * program *and* re-runs IDL generation for each, so a one-line edit to one
 * program costs the whole workspace. Naming it turns a 90-second loop into a
 * 25-second one.
 */
export function build(opts: BuildOptions | string = {}): void {
  // Accept a bare root for the original call shape.
  const { programName, features, publish, root } =
    typeof opts === 'string' ? ({ root: opts } as BuildOptions) : opts
  restoreKeys(root)
  runInChain('anchor', ['build', ...buildArgs({ programName, features })], root)
  recordBuildFeatures({ programName, features, root })

  // A feature build is a variant, not the artifact that ships, so it does not
  // overwrite the committed interface. Without this the checked-in IDL would
  // flip depending on which build you happened to run last, and a local test
  // run would leave the repo describing a program nobody releases.
  if (features?.length) {
    console.log(`Built with features [${features.join(', ')}] — committed IDL left unchanged.`)
    return
  }
  if (publish === false) {
    publishOrReport(root)
    return
  }
  syncIdl(root)
}

/**
 * Publish only if there is nothing published yet; otherwise say what drifted.
 *
 * The exception matters as much as the rule. On a checkout that has never
 * published an interface — a fresh copy of this toolchain into another project
 * — writing chain/idl creates files rather than rewriting tracked ones, and
 * without it `dev` would have no interface to deploy from or import. Once the
 * directory has contents, the working tree belongs to whoever is reading the
 * diff, so this reports and leaves it alone.
 */
function publishOrReport(root?: string): void {
  if (publishedInterfaces(root).length === 0) {
    syncIdl(root)
    return
  }
  const drifted = idlDrift(root)
  if (drifted.length === 0) return
  console.log(
    `\nchain/idl is out of date with this build: ${drifted.join(', ')}.\n` +
      'This command does not publish it — run `chain build` when you mean to.\n',
  )
}

/** Interfaces already published into chain/idl. */
export function publishedInterfaces(root?: string): string[] {
  const dir = generatedDir(root)
  if (!existsSync(dir)) return []
  return readdirSync(dir).filter((f) => f.endsWith('.json') || f.endsWith('.ts'))
}

/** Generated files that the committed copies no longer match. */
export function idlDrift(root?: string): string[] {
  const drifted: string[] = []
  for (const [src, ext] of [[idlDir(root), '.json'], [typesDir(root), '.ts']] as const) {
    if (!existsSync(src)) continue
    for (const f of readdirSync(src).filter((f) => f.endsWith(ext))) {
      const published = join(generatedDir(root), f)
      if (!existsSync(published) || readFileSync(published, 'utf8') !== readFileSync(join(src, f), 'utf8')) {
        drifted.push(f)
      }
    }
  }
  return drifted
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
  assertDefaultBuild({ cluster, programName, root })
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
  // Same provenance gate as `deploy`, reached through the URL: this path takes
  // a cluster URL rather than a cluster name, and it is the one localnet
  // actually uses.
  assertDefaultBuild({ cluster: opts.url, programName: opts.name, root: opts.root })
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
