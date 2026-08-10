import { resolve } from 'node:path'
import { Command } from 'commander'
import { build, deploy, exportIdl, test } from './anchor.js'
import { formatReport, runChecks } from './doctor.js'
import { repoRoot } from './paths.js'
import { airdrop, down, isUp, up } from './validator.js'

export { repoRoot, chainDir, readVersions, type Versions } from './paths.js'
export { runChecks, formatReport, parseVersion, evaluate, type Check, type Probe } from './doctor.js'
export { toolPath, envWithTools, run, capture, runDetached } from './exec.js'
export { isUp, up, down, airdrop, readPid, type UpOptions } from './validator.js'
export { build, deploy, test, exportIdl, idlDir, LEGACY_VALIDATOR_ARGS, type DeployOptions } from './anchor.js'

const CLUSTER_URLS: Record<string, string> = {
  localnet: 'http://127.0.0.1:8899',
  devnet: 'https://api.devnet.solana.com',
  'mainnet-beta': 'https://api.mainnet-beta.solana.com',
}

/**
 * The `chain` command group.
 *
 * Exported rather than run directly so a host CLI can mount it as a sub-command
 * (BadCode does: `badcode chain ...`) while `bin.ts` runs it standalone. Keep this
 * package free of any project-specific reference — it is meant to be lifted whole
 * into unrelated projects. See chain/README.md.
 */
export function chainCommand(): Command {
  const chain = new Command('chain').description('Solana dev-chain toolchain and local cluster.')

  chain
    .command('doctor')
    .description('Verify the installed toolchain matches chain/versions.json.')
    .action(() => {
      const checks = runChecks()
      console.log(formatReport(checks))
      if (checks.some((c) => !c.ok)) process.exitCode = 1
    })

  chain
    .command('up')
    .description('Start a local validator in the background and wait until it answers.')
    .option('--reset', 'wipe the ledger first, so tests start from an empty chain')
    .action(async (opts: { reset?: boolean }) => {
      const { started, pid } = await up({ reset: opts.reset })
      console.log(started ? `Validator up (pid ${pid}) at ${CLUSTER_URLS.localnet}` : 'Validator already running.')
    })

  chain
    .command('down')
    .description('Stop the local validator.')
    .action(async () => {
      console.log((await down()) ? 'Validator stopped.' : 'No validator was running.')
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
    .command('build')
    .description('Build the Anchor workspace.')
    .action(() => build())

  chain
    .command('deploy')
    .description('Deploy programs to a cluster.')
    .requiredOption('--cluster <cluster>', 'localnet | devnet | mainnet-beta')
    .option('--program-name <name>', 'deploy only this program')
    .action((opts: { cluster: string; programName?: string }) => {
      deploy({ cluster: opts.cluster, programName: opts.programName })
    })

  chain
    .command('test')
    .description('Run Anchor integration tests against a local validator.')
    .option('--script <name>', 'an Anchor.toml [scripts] entry, to run one suite')
    .option('--skip-build', 'reuse the existing build')
    .action((opts: { script?: string; skipBuild?: boolean }) => {
      test({ script: opts.script, skipBuild: opts.skipBuild })
    })

  chain
    .command('idl')
    .description('Copy generated IDLs somewhere a TypeScript package can import them.')
    .requiredOption('--out <dir>', 'destination directory, relative to the repo root')
    .action((opts: { out: string }) => {
      const dest = resolve(repoRoot(), opts.out)
      const copied = exportIdl(dest)
      console.log(`Copied ${copied.join(', ')} -> ${opts.out}`)
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

  return chain
}
