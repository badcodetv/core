/**
 * Send `set_mock_m2` to the local validator.
 *
 * Run through `./stack enc mock-m2 <billions>`, which does the decimal
 * conversion. Lives in chain/ rather than in the CLI package because it needs
 * the Anchor provider and the generated IDL, both of which are set up here.
 */
import * as anchor from '@coral-xyz/anchor'
import anchorPkg from '@coral-xyz/anchor'

// BN lands in a different place depending on how this file is loaded, and both
// happen here: the test suites run as ES modules (where the namespace has no
// BN and the default export does), while tsx compiles this script to CommonJS
// (where the namespace *is* module.exports and there is no default). Taking
// whichever exists works under both.
const BN = (anchorPkg as unknown as { BN?: typeof anchor.BN })?.BN ?? anchor.BN
import { PublicKey } from '@solana/web3.js'

const [value, releaseDate] = process.argv.slice(2)
if (!value || !releaseDate) {
  throw new Error('usage: mock-m2.ts <m2-fixed-point> <release-date-unix>')
}

// `anchor test` sets these; a bare `npx tsx` does not, and the failure without
// them is an unhelpful "Provider local is not available".
process.env.ANCHOR_PROVIDER_URL ??= 'http://127.0.0.1:8899'
process.env.ANCHOR_WALLET ??= `${process.env.HOME}/.config/solana/id.json`

anchor.setProvider(anchor.AnchorProvider.env())
const provider = anchor.AnchorProvider.env()
const program = anchor.workspace.EmperorsNewCoin as anchor.Program

// Asking the client for the method rather than scanning IDL names: Anchor
// exposes instructions in camelCase but the IDL spells them snake_case, and
// which one you get has changed between versions.
if (typeof (program.methods as Record<string, unknown>).setMockM2 !== 'function') {
  throw new Error(
    'The deployed program has no set_mock_m2 instruction. Rebuild with the mock oracle:\n' +
      '  ./stack build --features mock emperors_new_coin && ./stack deploy',
  )
}

const [mockOracle] = PublicKey.findProgramAddressSync(
  [Buffer.from('mock_oracle')],
  program.programId,
)

// Wrapped rather than top-level await: chain/package.json declares no
// "type": "module", so tsx compiles this to CommonJS, where top-level await is
// a syntax error.
async function main(): Promise<void> {
  const sig = await program.methods
    .setMockM2(new BN(value), new BN(releaseDate))
    .accounts({
      payer: provider.wallet.publicKey,
      mockOracle,
      systemProgram: anchor.web3.SystemProgram.programId,
    })
    .rpc()

  const billions = (Number(value) / 1e6).toLocaleString('en-US')
  console.log(
    `M2 set to $${billions}bn, released ${new Date(Number(releaseDate) * 1000).toISOString()}`,
  )
  console.log(sig)
}

main().catch((err: unknown) => {
  console.error(err instanceof Error ? err.message : String(err))
  process.exitCode = 1
})
