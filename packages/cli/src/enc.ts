import { Command } from 'commander'
import { readFileSync } from 'node:fs'
import { join } from 'node:path'
import { PublicKey } from '@solana/web3.js'
import { chainDir, repoRoot, runInChain } from '@badcode/chain-cli'

/**
 * Emperor's New Coin, from the command line.
 *
 * **This file is why `@badcode/chain-cli` stays generic.** Everything here
 * names ENC — its program, its accounts, its M2 units — and none of it may
 * migrate down into the toolchain, which is meant to be lifted whole into
 * unrelated projects. See the portability contract in chain/README.md.
 */

/** Same fixed-point as the program: billions of USD with 6 decimals. */
export const M2_DECIMALS = 6

/**
 * `22176.1` (billions) -> `22_176_100_000`.
 *
 * Parsed as a decimal string rather than through a float: `22176.1 * 1e6` is
 * 22176099999.999996 in IEEE-754, and rounding a money supply because of a
 * binary fraction is exactly the kind of quiet wrongness this coin cannot
 * afford.
 */
export function toFixedPoint(value: string, decimals = M2_DECIMALS): bigint {
  const trimmed = value.trim()
  if (!/^\d+(\.\d+)?$/.test(trimmed)) {
    throw new Error(`Not a positive decimal number: "${value}"`)
  }
  const [whole, fraction = ''] = trimmed.split('.')
  if (fraction.length > decimals) {
    throw new Error(`More than ${decimals} decimal places in "${value}"`)
  }
  return BigInt(whole + fraction.padEnd(decimals, '0'))
}

/** The ENC program id, read from the generated IDL rather than hardcoded. */
export function programId(): PublicKey {
  const idl = JSON.parse(
    readFileSync(join(chainDir(), 'idl', 'emperors_new_coin.json'), 'utf8'),
  ) as { address: string }
  return new PublicKey(idl.address)
}

export function encCommand(): Command {
  const enc = new Command('enc').description("Emperor's New Coin.")

  enc
    .command('mock-m2')
    .description('Set M2 by hand on localnet. Requires a build with --features mock.')
    .argument('<value>', 'M2 in billions of USD, e.g. 22176.1')
    .option('--release-date <unix>', 'the Fed release timestamp; defaults to now')
    .option('--cluster <cluster>', 'localnet only', 'localnet')
    .action((value: string, opts: { releaseDate?: string; cluster: string }) => {
      // Refused rather than merely discouraged. The instruction only exists in
      // a mock build, so pointing this at devnet could not work — but the error
      // it would produce ("instruction not found") sends people looking in the
      // wrong place entirely.
      if (opts.cluster !== 'localnet') {
        throw new Error(
          'mock-m2 is localnet-only by construction: set_mock_m2 is compiled out of every ' +
            'other build. On devnet, advance the real feed with `./stack enc crank`.',
        )
      }
      const fixed = toFixedPoint(value)
      const releaseDate = opts.releaseDate ?? String(Math.floor(Date.now() / 1000))
      runInChain(
        'npx',
        ['tsx', 'scripts/mock-m2.ts', String(fixed), releaseDate],
        repoRoot(),
      )
    })

  return enc
}
