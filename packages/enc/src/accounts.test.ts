/**
 * Where the state lives, pinned.
 *
 * The three literal addresses below are asserted from the Rust side too, in
 * `state.rs`'s own unit tests, against the same program id. That is the point:
 * a seed encoding that drifts does not throw anywhere — the client simply looks
 * where nothing was ever written and the page renders as though the coin has no
 * state. Two languages, one set of strings, failing together.
 */
import { PublicKey } from '@solana/web3.js'
import { describe, expect, it } from 'vitest'
import {
  ASSET_COUNT,
  ENC_PROGRAM_ID,
  assetAddresses,
  associatedTokenAddress,
  decodeMintSupply,
  decodeTokenAmount,
  encAddresses,
} from './index.js'

const addresses = encAddresses(ENC_PROGRAM_ID)

describe('addresses', () => {
  it('derives what the program derives', () => {
    expect(addresses.config.toBase58()).toBe('DVrFUZxQNxLWM5Rwsk92sBQDmUNY4njHE4nri5d4cMdm')
    expect(addresses.printer.toBase58()).toBe('96PpBLCBHeWXUmCZ5YRdLFmBL75ZqJjMRWBoCarasJNY')
    expect(addresses.vault.toBase58()).toBe('BpAvBQGwMuVsPyaPmPUmSY4p1zrp3Wxd5P3SWsrEHZJH')
  })

  it('takes the program id from the IDL rather than a constant', () => {
    // A redeploy to a different address must need no code change anywhere.
    expect(addresses.programId.equals(ENC_PROGRAM_ID)).toBe(true)
    const elsewhere = encAddresses(new PublicKey('11111111111111111111111111111111'))
    expect(elsewhere.config.equals(addresses.config)).toBe(false)
  })

  it('gives every slot its own address, ten of them', () => {
    const slots = assetAddresses(addresses)
    expect(slots).toHaveLength(ASSET_COUNT)
    expect(new Set(slots.map((s) => s.toBase58())).size).toBe(ASSET_COUNT)
  })

  it('distinguishes a one-byte index from an eight-byte epoch', () => {
    // The classic way to derive a valid-looking address that points at nothing.
    expect(addresses.asset(1).equals(addresses.epoch(1n))).toBe(false)
  })

  it('derives the token accounts of two PDAs that are off the curve', () => {
    // The vault and the escrow are program addresses, chosen to be off the
    // ed25519 curve — a derivation that refused an off-curve owner would refuse
    // exactly the two accounts this page most needs.
    expect(addresses.vaultEncAta.equals(associatedTokenAddress(addresses.vault, addresses.mint))).toBe(true)
    expect(addresses.escrowEncAta.equals(addresses.vaultEncAta)).toBe(false)
  })
})

describe('the SPL accounts Anchor cannot decode', () => {
  /** An SPL mint: 36 bytes of COption authority, then the supply. */
  function mint(supply: bigint): Uint8Array {
    const data = new Uint8Array(82)
    new DataView(data.buffer).setBigUint64(36, supply, true)
    return data
  }

  /** An SPL token account: mint, owner, then the amount. */
  function tokenAccount(amount: bigint): Uint8Array {
    const data = new Uint8Array(165)
    new DataView(data.buffer).setBigUint64(64, amount, true)
    return data
  }

  it('reads a supply past what a Number can hold', () => {
    // ~2.2e16 base units, which is well past 2^53.
    expect(decodeMintSupply(mint(22_176_100_000_000_000n))).toBe(22_176_100_000_000_000n)
    expect(decodeMintSupply(mint(0n))).toBe(0n)
    expect(decodeMintSupply(mint(2n ** 64n - 1n))).toBe(18_446_744_073_709_551_615n)
  })

  it('reads a balance from the right offset', () => {
    expect(decodeTokenAmount(tokenAccount(1_000_000n))).toBe(1_000_000n)
  })

  it('refuses an account that is not one, rather than reading garbage', () => {
    // Pointing a decoder at the wrong address is a bug worth an exception: the
    // alternative is a plausible-looking number nobody can trace.
    expect(() => decodeMintSupply(tokenAccount(1n).slice(0, 40))).toThrow(/not an SPL mint/)
    expect(() => decodeTokenAmount(mint(1n))).toThrow(/not an SPL token account/)
  })
})
