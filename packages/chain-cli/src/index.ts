import { existsSync, readFileSync, readdirSync } from 'node:fs'
import { join, resolve } from 'node:path'
import { Command } from 'commander'
import { build, deploy, deployProgram, exportIdl, generatedDir, syncIdl, test } from './anchor.js'
import { chosenRunner, composeCapture, composeRun, dockerAvailable, imageBuild, imageExists } from './docker.js'
import { VERSION_PROBE, checksFromCombined, formatReport, runChecks } from './doctor.js'
import { repoRoot } from './paths.js'
import { runInChain } from './runner.js'
import { airdrop, down, isUp, up } from './validator.js'
import { ensureWallet, walletAddress, walletBalance, walletPath } from './wallet.js'

export { repoRoot, chainDir, readVersions, type Versions } from './paths.js'
export { runChecks, formatReport, parseVersion, evaluate, checksFromCombined, VERSION_PROBE, type Check, type Probe } from './doctor.js'
export { toolPath, envWithTools, run, capture, runDetached } from './exec.js'
export { isUp, up, down, airdrop, readPid, ledgerDir, type UpOptions } from './validator.js'
export { runInChain, captureInChain } from './runner.js'
export {
  chosenRunner, dockerAvailable, composeFile, composeEnvFile, composeBase, writeComposeEnv,
  imageBuild, imageExists, composeRun, composeCapture, composeUpValidator, composeDown, type RunnerName,
} from './docker.js'
export { walletPath, ensureWallet, walletAddress, walletBalance } from './wallet.js'
export {
  build, deploy, deployProgram, test, testArgs, exportIdl, syncIdl, restoreKeys, idlDir, typesDir, generatedDir,
  keysDir, deployDir, LEGACY_VALIDATOR_ARGS, type DeployOptions, type TestOptions,
} from './anchor.js'

const CLUSTER_URLS: Record<string, string> = {
  localnet: 'http://127.0.0.1:8899',
  devnet: 'https://api.devnet.solana.com',
  'mainnet-beta': 'https://api.mainnet-beta.solana.com',
}

/** Enough SOL to deploy a program a few times over. */
const TARGET_SOL = 100
const LOW_SOL = 10

/**
 * Bytes reserved for each program on its first localnet deploy.
 *
 * Solana allocates exactly the program's current length by default, so the next
 * build that is one byte larger has to grow the account — and growing it is
 * currently broken: the CLI sends `ExtendProgram`, which the loader rejects as
 * "superseded by ExtendProgramChecked". Reserving headroom up front is what
 * keeps `redeploy` working after a change that makes the binary bigger, which is
 * most changes.
 *
 * Localnet only. It costs rent proportional to the size (~3.5 SOL here), which
 * is free where SOL is airdropped and rude where it is not.
 */
const LOCALNET_MAX_LEN = 500_000

function reportRunner(): void {
  const runner = chosenRunner()
  console.log(runner === 'docker' ? 'Runner: docker (chain-dev:local)' : 'Runner: host toolchain')
}

/**
 * Make sure the deploy wallet exists and can pay for a deploy.
 *
 * Called after every validator start, not just the first: wiping the ledger
 * wipes every balance on it, so a reset otherwise leaves the wallet at zero and
 * the next deploy fails with "found no record of a prior credit" — which reads
 * like a bug in your program.
 */
function ensureFundedWallet(url: string): void {
  if (ensureWallet()) console.log(`Created a deploy wallet at ${walletPath()}`)
  if ((walletBalance(url) ?? 0) >= LOW_SOL) return
  const address = walletAddress()
  if (!address) return
  airdrop(address, TARGET_SOL, url)
  console.log(`Funded the deploy wallet with ${TARGET_SOL} SOL`)
}

/** Everything needed before you can build against a local chain. */
async function bringUp(opts: { reset?: boolean } = {}): Promise<void> {
  reportRunner()
  if (chosenRunner() === 'docker' && !imageExists()) {
    console.log('Building the toolchain image (once, ~10 minutes)…')
    imageBuild()
  }
  await up({ reset: opts.reset })
  console.log(`Validator up at ${CLUSTER_URLS.localnet}`)
  ensureFundedWallet(CLUSTER_URLS.localnet)
  build()
  await deployLocalnet()
  console.log('\nDeployed:')
  for (const p of deployedPrograms()) console.log(`  ${p.name.padEnd(20)} ${p.address}`)
}

/** Is there an account at this address? Null when the cluster is unreachable. */
async function accountExists(url: string, address: string): Promise<boolean | null> {
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'getAccountInfo', params: [address, { encoding: 'base64' }] }),
      signal: AbortSignal.timeout(5000),
    })
    const body = (await res.json()) as { result?: { value: unknown } }
    return body.result?.value != null
  } catch {
    return null
  }
}

/**
 * How much space to ask for, or undefined to let Solana decide.
 *
 * Only on a first deploy: `--max-len` is rejected on an upgrade, and an upgrade
 * is exactly when we no longer have a say.
 */
async function localnetHeadroom(cluster: string): Promise<number | undefined> {
  if (cluster !== 'localnet') return undefined
  const url = CLUSTER_URLS.localnet
  const programs = deployedPrograms()
  if (programs.length === 0) return LOCALNET_MAX_LEN
  const present = await Promise.all(programs.map((p) => accountExists(url, p.address)))
  return present.some((p) => p === true) ? undefined : LOCALNET_MAX_LEN
}

/**
 * Deploy to localnet, reserving headroom the first time.
 *
 * The first deploy is the only chance to ask for space, so it goes through
 * `solana program deploy` directly; upgrades go through Anchor as usual.
 */
async function deployLocalnet(programName?: string): Promise<void> {
  const maxLen = await localnetHeadroom('localnet')
  if (maxLen === undefined) {
    deploy({ cluster: 'localnet', programName })
    return
  }
  const url = CLUSTER_URLS.localnet
  const programs = deployedPrograms().filter((p) => !programName || p.name === programName)
  for (const p of programs) {
    console.log(`Deploying ${p.name} with ${maxLen} bytes reserved…`)
    deployProgram({ name: p.name, url, maxLen })
  }
}

/** Program name -> address, read from the published IDLs. */
function deployedPrograms(): Array<{ name: string; address: string }> {
  const dir = generatedDir()
  if (!existsSync(dir)) return []
  return readdirSync(dir)
    .filter((f) => f.endsWith('.json'))
    .map((f) => {
      const idl = JSON.parse(readFileSync(join(dir, f), 'utf8')) as { address?: string; metadata?: { name?: string } }
      return { name: idl.metadata?.name ?? f.replace(/\.json$/, ''), address: idl.address ?? '(none)' }
    })
}

/** `--features a,b` -> ['a','b']. Undefined stays undefined so no `--` is added. */
export function splitFeatures(list?: string): string[] | undefined {
  if (list === undefined) return undefined
  const parts = list.split(',').map((f) => f.trim()).filter((f) => f.length > 0)
  return parts.length > 0 ? parts : undefined
}

/**
 * The `chain` command group.
 *
 * Exported rather than run directly so a host CLI can mount it as a sub-command
 * (BadCode mounts it under `badcode`, then wraps that again in ./stack), while
 * `bin.ts` runs it standalone for a project with no CLI of its own. Keep this
 * package free of any project-specific reference — it is meant to be lifted whole
 * into unrelated projects. See chain/README.md.
 */
export function chainCommand(): Command {
  const chain = new Command('chain').description('Solana dev-chain toolchain and local cluster.')

  chain
    .command('doctor')
    .description('Verify the toolchain matches chain/versions.json.')
    .action(() => {
      reportRunner()
      if (chosenRunner() === 'docker') {
        if (!dockerAvailable()) {
          console.log('  ✗ docker           not available — install Docker, or use CHAIN_RUNNER=host')
          process.exitCode = 1
          return
        }
        if (!imageExists()) {
          console.log('  ✗ chain-dev:local  image not built yet\n\nTo fix:\n  chain image')
          process.exitCode = 1
          return
        }
        const out = composeCapture('bash', ['-lc', VERSION_PROBE])
        if (out === null) {
          console.log('  ✗ container        could not run — try: chain image --no-cache')
          process.exitCode = 1
          return
        }
        const checks = checksFromCombined(out)
        console.log(formatReport(checks))
        if (checks.some((c) => !c.ok)) process.exitCode = 1
        return
      }
      const checks = runChecks()
      console.log(formatReport(checks))
      if (checks.some((c) => !c.ok)) process.exitCode = 1
    })

  chain
    .command('image')
    .description('Build the pinned toolchain image (Docker runner only).')
    .option('--no-cache', 'rebuild every layer from scratch')
    .action((opts: { cache?: boolean }) => {
      if (chosenRunner() !== 'docker') throw new Error('CHAIN_RUNNER=host — there is no image to build.')
      imageBuild({ noCache: opts.cache === false })
    })

  chain
    .command('shell')
    .description('Open a shell in the toolchain container.')
    .action(() => {
      if (chosenRunner() !== 'docker') throw new Error('CHAIN_RUNNER=host — you are already in the shell.')
      composeRun('bash', [])
    })

  chain
    .command('up')
    .description('Start a local validator and wait until it answers.')
    .option('--reset', 'wipe the ledger first, so you start from an empty chain')
    .action(async (opts: { reset?: boolean }) => {
      reportRunner()
      const { started } = await up({ reset: opts.reset })
      console.log(started ? `Validator up at ${CLUSTER_URLS.localnet}` : 'Validator already running.')
    })

  chain
    .command('down')
    .description('Stop the local validator.')
    .action(async () => {
      console.log((await down()) ? 'Validator stopped.' : 'No validator was running.')
    })

  chain
    .command('reset')
    .description('Wipe the ledger and redeploy. Do this after changing an account layout.')
    .action(async () => {
      // Accounts written with the old struct no longer deserialize, and the
      // failure surfaces as a raw byte-range error pointing at the frontend
      // rather than at the layout change that caused it. Wiping is the fix, and
      // it has to redeploy too — an empty ledger has no programs on it.
      await bringUp({ reset: true })
      console.log('\nFresh ledger, programs redeployed. Browser wallets will need another airdrop.')
    })

  chain
    .command('status')
    .description('Report whether the local validator is answering.')
    .action(async () => {
      const running = await isUp()
      console.log(running ? 'Validator is up.' : 'Validator is not running.')
      if (!running) process.exitCode = 1
    })

  chain
    .command('wallet')
    .description('Show the deploy wallet, creating and funding it if needed.')
    .option('--cluster <cluster>', 'localnet | devnet', 'localnet')
    .action((opts: { cluster: string }) => {
      const url = CLUSTER_URLS[opts.cluster]
      if (!url) throw new Error(`Unknown cluster "${opts.cluster}"`)
      if (opts.cluster === 'localnet') ensureFundedWallet(url)
      else if (ensureWallet()) console.log(`Created a deploy wallet at ${walletPath()}`)
      const balance = walletBalance(url)
      console.log(`Deploy wallet: ${walletAddress() ?? '(unknown)'}`)
      console.log(`Balance:       ${balance === null ? '(cluster unreachable)' : `${balance} SOL on ${opts.cluster}`}`)
    })

  chain
    .command('build')
    .description('Build the Anchor workspace and publish its IDL + TypeScript types.')
    .option('--program-name <name>', 'build only this program — much faster in a workspace')
    .option('--features <list>', 'comma-separated cargo features, e.g. mock')
    .action((opts: { programName?: string; features?: string }) => {
      build({ programName: opts.programName, features: splitFeatures(opts.features) })
      console.log(`Published interfaces to chain/idl:`)
      for (const p of deployedPrograms()) console.log(`  ${p.name.padEnd(20)} ${p.address}`)
    })

  chain
    .command('deploy')
    .description('Deploy programs to a cluster.')
    .requiredOption('--cluster <cluster>', 'localnet | devnet | mainnet-beta')
    .option('--program-name <name>', 'deploy only this program')
    .option('--max-len <bytes>', 'space to reserve; first deploy only')
    .action(async (opts: { cluster: string; programName?: string; maxLen?: string }) => {
      if (opts.cluster === 'localnet' && !opts.maxLen) {
        await deployLocalnet(opts.programName)
        return
      }
      deploy({ cluster: opts.cluster, programName: opts.programName, maxLen: opts.maxLen ? Number(opts.maxLen) : undefined })
    })

  chain
    .command('test')
    .description('Run Anchor integration tests against the local validator.')
    .option('--script <name>', 'an Anchor.toml [scripts] entry, to run one suite')
    .option('--skip-build', 'reuse the existing build')
    .option('--own-validator', 'let Anchor start its own validator instead of reusing ours')
    .option('--features <list>', 'comma-separated cargo features for the build it runs')
    .action(
      async (opts: {
        script?: string
        skipBuild?: boolean
        ownValidator?: boolean
        features?: string
      }) => {
        if (!opts.ownValidator) await up()
        test({
          script: opts.script,
          skipBuild: opts.skipBuild,
          ownValidator: opts.ownValidator,
          features: splitFeatures(opts.features),
        })
      },
    )

  chain
    .command('cargo')
    // Rust unit tests (`cargo test -p <program> --lib`) need the pinned Rust
    // toolchain, which under Docker only exists in the container. Without this
    // there is no way to run them at all on a machine with no host Rust.
    .description('Run cargo inside the toolchain, from the Anchor workspace.')
    .argument('[args...]', 'arguments for cargo, e.g. test -p emperors-new-coin --lib')
    // Read raw argv rather than commander's parse: cargo's flags (--lib, -p) are
    // ours to forward, not ours to interpret, and commander's own pass-through
    // mode would force positional-option parsing on the entire CLI.
    .allowUnknownOption()
    .helpOption(false)
    .action(() => {
      const at = process.argv.indexOf('cargo')
      runInChain('cargo', at === -1 ? [] : process.argv.slice(at + 1))
    })

  chain
    .command('idl')
    .description('Publish generated IDLs and types. Defaults to chain/idl; --out copies elsewhere too.')
    .option('--out <dir>', 'extra destination for the .json IDLs, relative to the repo root')
    .action((opts: { out?: string }) => {
      const written = syncIdl()
      console.log(`Published ${written.join(', ')} -> chain/idl`)
      if (opts.out) {
        const dest = resolve(repoRoot(), opts.out)
        console.log(`Copied ${exportIdl(dest).join(', ')} -> ${opts.out}`)
      }
    })

  chain
    .command('airdrop')
    .description('Fund a wallet on a non-mainnet cluster.')
    .argument('<address>', 'recipient public key')
    .option('--sol <amount>', 'how much SOL', '10')
    .option('--cluster <cluster>', 'localnet | devnet', 'localnet')
    .action((address: string, opts: { sol: string; cluster: string }) => {
      const url = CLUSTER_URLS[opts.cluster]
      if (!url) throw new Error(`Unknown cluster "${opts.cluster}"`)
      if (opts.cluster === 'mainnet-beta') throw new Error('There is no airdrop on mainnet.')
      airdrop(address, Number(opts.sol), url)
      console.log(`Airdropped ${opts.sol} SOL to ${address} on ${opts.cluster}`)
    })

  chain
    .command('dev')
    .description('Everything needed to develop: image, validator, funded wallet, build, deploy.')
    .option('--reset', 'wipe the ledger first')
    .action(async (opts: { reset?: boolean }) => {
      await bringUp({ reset: opts.reset })
      console.log('\nPoint a wallet at http://127.0.0.1:8899 and run the web app.')
    })

  return chain
}

/**
 * The same commands, as a standalone program.
 *
 * Not just `addCommand(chainCommand())` — that nests the group under its own
 * name and you have to type `chain chain doctor`. A project with no host CLI to
 * mount this on runs `chain doctor`, so the subcommands are re-hosted at the top
 * level here.
 */
export function standaloneProgram(): Command {
  const group = chainCommand()
  const program = new Command('chain').description(group.description())
  for (const command of group.commands) program.addCommand(command)
  return program
}
