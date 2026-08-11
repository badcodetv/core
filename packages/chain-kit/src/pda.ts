// Imported, never assumed. `Buffer` is a Node global that does NOT exist in a
// browser, and Vite does not polyfill it — so relying on the global here throws
// "Buffer is not defined" the moment a wallet connects and the first PDA is
// derived. Importing it explicitly makes the bundler supply the shim in the
// browser while Node still uses its built-in, and means a project that copies
// this package needs no polyfill setup of its own.
import { Buffer } from 'buffer'
import { PublicKey } from '@solana/web3.js'

/** Anything usable as a PDA seed. */
export type Seed = string | Buffer | Uint8Array | PublicKey

/**
 * Encode a seed the way the Rust side will.
 *
 * Strings become UTF-8 bytes, matching Rust's `b"literal"`. Integers are NOT
 * handled here on purpose — their width and endianness must be stated explicitly
 * at the call site (see `u8`, `u64le`), because getting either wrong produces a
 * valid-looking address that simply points at nothing.
 */
export function encodeSeed(seed: Seed): Buffer {
  if (typeof seed === 'string') return Buffer.from(seed, 'utf8')
  if (seed instanceof PublicKey) return seed.toBuffer()
  return Buffer.from(seed)
}

/** One-byte seed. Mirrors Rust `index.to_le_bytes()` on a u8. */
export function u8(value: number): Buffer {
  if (!Number.isInteger(value) || value < 0 || value > 0xff) {
    throw new Error(`u8 seed out of range: ${value}`)
  }
  return Buffer.from([value])
}

/** Eight-byte little-endian seed. Mirrors Rust `value.to_le_bytes()` on a u64. */
export function u64le(value: bigint | number): Buffer {
  const v = BigInt(value)
  if (v < 0n || v > 0xffff_ffff_ffff_ffffn) throw new Error(`u64 seed out of range: ${value}`)
  const buf = Buffer.alloc(8)
  buf.writeBigUInt64LE(v)
  return buf
}

/** Derive a program address. Returns the address and its bump. */
export function derive(seeds: readonly Seed[], programId: PublicKey): [PublicKey, number] {
  return PublicKey.findProgramAddressSync(seeds.map(encodeSeed), programId)
}

/** Just the address, for the common case where the bump is stored on-chain. */
export function deriveAddress(seeds: readonly Seed[], programId: PublicKey): PublicKey {
  return derive(seeds, programId)[0]
}
