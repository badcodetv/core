import { Command } from 'commander'
import { formatReport, runChecks } from './doctor.js'

export { repoRoot, chainDir, readVersions, type Versions } from './paths.js'
export { runChecks, formatReport, parseVersion, evaluate, type Check } from './doctor.js'

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

  return chain
}
