/**
 * The program's own interface, re-exported from where `./stack build` puts it.
 *
 * **Nothing here is hand-written, and nothing here may be.** `anchor build`
 * generates the IDL and its TypeScript view into `chain/target/`, and `chain
 * build` copies both into `chain/idl/`, which is committed. This module exists
 * only so that the rest of the world imports ENC's interface from one place —
 * `@badcode/enc` — rather than reaching into the Anchor workspace itself.
 *
 * Two things it buys, both of which cost real time when they are missing:
 *
 * **No address is hardcoded anywhere.** The IDL carries `address` at the top,
 * so a redeploy to a different program id needs no code change on the page.
 *
 * **The types are the program's definition, not a description of it.** Delete a
 * field in the Rust struct and the next `chain build` breaks `tsc` here rather
 * than producing `undefined` in a browser six weeks later.
 *
 * The committed IDL is the **default build's**, which is the artifact that
 * ships — so `set_mock_m2` and `mock_fund` are absent from these types even
 * when a localnet ledger is running a `--features mock` build that has them.
 */
import { PublicKey } from '@solana/web3.js'
// Relative, not the repo's `@chain/*` alias, and deliberately so: that alias is
// a tsconfig path, which means every consumer has to declare it twice (once for
// the compiler, once for its bundler or test runner). This package is compiled
// by four of them — the web app, its own tests, the Anchor workspace's
// typecheck and the simulation's vitest — and a relative path is understood by
// all four with nothing to keep in step.
import idlJson from '../../../../chain/idl/emperors_new_coin.json'
import type { EmperorsNewCoin } from '../../../../chain/idl/emperors_new_coin'

export type { EmperorsNewCoin }

/**
 * The IDL, at the exact literal types Anchor wants.
 *
 * The JSON import widens every literal to `string`/`number[]`; the generated
 * `.ts` carries the narrow types. Same bytes, two views of them.
 */
export const ENC_IDL = idlJson as EmperorsNewCoin

/** Where the program is deployed, according to the program itself. */
export const ENC_PROGRAM_ID = new PublicKey(ENC_IDL.address)
