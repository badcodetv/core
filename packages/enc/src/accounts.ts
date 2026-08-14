/**
 * Where ENC keeps its state, and how to read it.
 *
 * **The seeds are a cross-language contract.** Every address below is derived
 * the same way `chain/programs/emperors-new-coin/src/state.rs` derives it, and
 * both sides pin the same three base58 strings in their tests. A seed that
 * drifts does not throw: the client looks in a place nothing was ever written
 * to, every read comes back empty, and the page renders as though the coin has
 * no state at all. That is why the pins exist.
 *
 * Two decoding rules are load-bearing here.
 *
 * **Anchor accounts are decoded through a `Program`, never through a bare
 * coder.** Anchor emits two IDLs that disagree: the JSON uses the Rust field
 * names (`term_ends_at`), the generated `.ts` is its camelCase view
 * (`termEndsAt`). `Program` converts internally, so its coder matches the
 * types. A `BorshAccountsCoder` built from the raw JSON does not — TypeScript
 * says `termEndsAt`, the object has `term_ends_at`, the compiler is happy, and
 * every field reads `undefined` at runtime.
 *
 * **SPL accounts are not Anchor accounts.** The mint and the two token accounts
 * are plain SPL, so Anchor cannot decode them at all; their layouts are fixed
 * offsets, read here rather than pulled in as a dependency. `getTokenSupply`
 * and `getTokenAccountBalance` would answer the same questions, but they are
 * RPC calls rather than account subscriptions — and the page has to move when
 * the chain moves, not when someone refreshes.
 */
import type { BorshAccountsCoder, IdlAccounts, Program } from '@coral-xyz/anchor'
import { derive, deriveAddress, u8, u64le } from '@badcode/chain-kit'
import { PublicKey } from '@solana/web3.js'
import { ENC_PROGRAM_ID, type EmperorsNewCoin } from './idl/emperors_new_coin.js'

// ── Constants mirrored from the program ─────────────────────────────────────
// These are facts about the deployed artifact, not choices this file gets to
// make. Each one names the Rust constant it mirrors.

/** `ASSET_COUNT` in state.rs. Ten slots, fixed forever. */
export const ASSET_COUNT = 10

/** `COPY_BYTES` in state.rs. **Bytes, not characters** — an emoji costs four. */
export const COPY_BYTES = 280

/**
 * `SPIKE_MARKER` in state.rs — the only string the editor's pen can write, and
 * it does not get to choose it.
 */
export const SPIKE_MARKER = '███████ SPIKED ███████'

/** `ENC_DECIMALS` in state.rs. Six, because nine overflows u64 at this supply. */
export const ENC_DECIMALS = 6

/** `PRICE_INTERPOLATION_SECONDS` in state.rs: thirty days, in seconds. */
export const PRICE_INTERPOLATION_SECONDS = 30 * 86_400

/** The classic SPL Token program. ENC itself is a plain SPL token. */
export const TOKEN_PROGRAM_ID = new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA')

/**
 * Token-2022, which is **not** the program ENC itself uses.
 *
 * The two live side by side here on purpose: ENC is a plain classic SPL token,
 * and the tenancy NFTs and their certificates are Token-2022 because they need
 * the metadata extension. Passing one where the other belongs derives a
 * different associated-token address, which fails as "account not initialized"
 * and names nothing useful.
 */
export const TOKEN_2022_PROGRAM_ID = new PublicKey('TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb')

/** The associated-token program, which owns the vault's and escrow's accounts. */
export const ASSOCIATED_TOKEN_PROGRAM_ID = new PublicKey(
  'ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL',
)

// ── Account types ───────────────────────────────────────────────────────────
// Derived from the generated IDL, so a field deleted in Rust breaks `tsc` here
// rather than reading `undefined` in a browser. `u64`s arrive as Anchor `BN`s;
// see `view.ts` for the bigint conversion the page actually renders.

type Accounts = IdlAccounts<EmperorsNewCoin>
export type EncConfig = Accounts['config']
export type EncPrinter = Accounts['printer']
export type EncAsset = Accounts['asset']
export type EncFaucetEpoch = Accounts['faucetEpoch']
export type EncPlayer = Accounts['player']
export type EncBid = Accounts['bid']

// ── Addresses ───────────────────────────────────────────────────────────────

/**
 * An associated token account.
 *
 * `allowOwnerOffCurve` in the SPL client's vocabulary: the vault and the escrow
 * are PDAs, which are *chosen* to be off the ed25519 curve, so a derivation
 * that refused an off-curve owner would refuse exactly the two accounts this
 * page most needs to read. Deriving it directly has no such opinion.
 */
export function associatedTokenAddress(
  owner: PublicKey,
  mint: PublicKey,
  tokenProgram: PublicKey = TOKEN_PROGRAM_ID,
): PublicKey {
  return deriveAddress([owner, tokenProgram, mint], ASSOCIATED_TOKEN_PROGRAM_ID)
}

export interface EncAddresses {
  programId: PublicKey
  /** The rules. Written once at `initialize`, never changed. */
  config: PublicKey
  /** What the Fed last told us, and what we did about it. */
  printer: PublicKey
  /** Mint authority, landlord, and the Emperor's pocket. */
  vault: PublicKey
  /** The ENC mint, itself a PDA — findable without reading `Config` first. */
  mint: PublicKey
  /** Every bidder's escrowed ENC, deliberately not pooled in the vault. */
  escrow: PublicKey
  /** The vault's ENC. What "the Emperor's share" is measured from. */
  vaultEncAta: PublicKey
  /** The escrow's ENC: every live bid on every slot, in one number. */
  escrowEncAta: PublicKey
  asset: (index: number) => PublicKey
  assetMint: (index: number) => PublicKey
  epoch: (epoch: bigint) => PublicKey
  player: (wallet: PublicKey) => PublicKey
  bid: (index: number, bidder: PublicKey) => PublicKey
  cert: (index: number, term: bigint) => PublicKey
}

/** Every address the coin has, from one program id. */
export function encAddresses(programId: PublicKey = ENC_PROGRAM_ID): EncAddresses {
  const at = (seeds: Parameters<typeof deriveAddress>[0]) => deriveAddress(seeds, programId)

  const vault = at(['vault'])
  const mint = at(['mint'])
  const escrow = at(['escrow'])

  return {
    programId,
    config: at(['config']),
    printer: at(['printer']),
    vault,
    mint,
    escrow,
    vaultEncAta: associatedTokenAddress(vault, mint),
    escrowEncAta: associatedTokenAddress(escrow, mint),
    // The asset index is ONE byte and the epoch is EIGHT, little-endian. The
    // two look alike and are not: confusing them derives a valid address that
    // points at nothing, which reads as "no state" rather than as an error.
    asset: (index) => at(['asset', u8(index)]),
    assetMint: (index) => at(['asset_mint', u8(index)]),
    epoch: (epoch) => at(['epoch', u64le(epoch)]),
    player: (wallet) => at(['player', wallet]),
    bid: (index, bidder) => at(['bid', u8(index), bidder]),
    cert: (index, term) => at(['cert', u8(index), u64le(term)]),
  }
}

/** The ten slot addresses, in index order — one `getMultipleAccounts`. */
export function assetAddresses(addresses: EncAddresses): PublicKey[] {
  return Array.from({ length: ASSET_COUNT }, (_, i) => addresses.asset(i))
}

/** The bump too, for the rare caller that needs to sign with a seed. */
export function deriveEnc(
  seeds: Parameters<typeof derive>[0],
  programId: PublicKey = ENC_PROGRAM_ID,
): [PublicKey, number] {
  return derive(seeds, programId)
}

// ── Decoding ────────────────────────────────────────────────────────────────

/**
 * Decoders for the program's own accounts, bound to a `Program` handle.
 *
 * `decodeAny` matches on the eight-byte discriminator, so pointing one of these
 * at the wrong address throws rather than returning a plausible-looking struct
 * of the wrong type. Renaming a Rust struct cannot silently break them either.
 */
export function encDecoders(program: Program<EmperorsNewCoin>) {
  // The cast reaches `decodeAny`, which the generic `AccountsCoder` interface
  // does not declare; the instance is always the borsh one.
  const coder = program.coder.accounts as BorshAccountsCoder
  return {
    config: (data: Buffer): EncConfig => coder.decodeAny(data),
    printer: (data: Buffer): EncPrinter => coder.decodeAny(data),
    asset: (data: Buffer): EncAsset => coder.decodeAny(data),
    faucetEpoch: (data: Buffer): EncFaucetEpoch => coder.decodeAny(data),
    player: (data: Buffer): EncPlayer => coder.decodeAny(data),
    bid: (data: Buffer): EncBid => coder.decodeAny(data),
  }
}

/** Offset of `supply` in an SPL mint: after a 36-byte COption<Pubkey> authority. */
const MINT_SUPPLY_OFFSET = 36
/** The fixed size of an SPL mint account, before any Token-2022 extension. */
const MINT_SIZE = 82

/** Offset of `amount` in an SPL token account: after the mint and the owner. */
const TOKEN_AMOUNT_OFFSET = 64
/** The fixed size of an SPL token account. */
const TOKEN_ACCOUNT_SIZE = 165

function readU64Le(data: Uint8Array, offset: number, what: string): bigint {
  if (data.length < offset + 8) {
    throw new Error(`${what}: ${data.length} bytes is too short to be one`)
  }
  return new DataView(data.buffer, data.byteOffset, data.byteLength).getBigUint64(offset, true)
}

/**
 * Total ENC in existence, from the mint account.
 *
 * This is the number the peg is about, and the honest invariant is
 * `supply ≥ k × M2` — never `=`, because a burn larger than the vault could
 * cover leaves the excess outstanding until the next release retargets.
 */
export function decodeMintSupply(data: Uint8Array): bigint {
  if (data.length < MINT_SIZE) {
    throw new Error(`not an SPL mint: ${data.length} bytes, expected at least ${MINT_SIZE}`)
  }
  return readU64Le(data, MINT_SUPPLY_OFFSET, 'mint')
}

/** The balance of an SPL token account, in base units. */
export function decodeTokenAmount(data: Uint8Array): bigint {
  if (data.length < TOKEN_ACCOUNT_SIZE) {
    throw new Error(
      `not an SPL token account: ${data.length} bytes, expected at least ${TOKEN_ACCOUNT_SIZE}`,
    )
  }
  return readU64Le(data, TOKEN_AMOUNT_OFFSET, 'token account')
}
