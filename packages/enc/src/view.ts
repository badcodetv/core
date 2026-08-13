/**
 * What the chain says, turned into what the page shows.
 *
 * Everything here is a pure function of decoded accounts plus a timestamp, so
 * the page can re-derive the whole view every animation frame and watch prices
 * move — which is the point: an ENC price is a straight line between two
 * endpoints, so it ticks every slot rather than jumping once a month when the
 * Fed publishes.
 *
 * **The arithmetic is not reimplemented here.** `math.ts` mirrors `math.rs`
 * function for function and is tested against the same vectors; this file only
 * assembles those answers into the shapes a component wants. If a number is
 * computed rather than composed, it belongs in `math.ts`.
 *
 * Anchor hands back `BN` for every `u64`, which is a `Number`-shaped trap at
 * this scale — the supply passed 2^53 base units a long time ago — so every
 * quantity crossing into this file becomes a `bigint` at the boundary and stays
 * one.
 */
import { PublicKey } from '@solana/web3.js'
import type { EncAsset, EncConfig, EncFaucetEpoch, EncPrinter } from './accounts.js'
import { aboveFloor, epochOf, faucetPot, faucetShare, floorAmount, priceAt } from './math.js'

/** Anchor's `BN`, as much of it as anything here needs. */
interface Bn {
  toString(): string
}

/** `BN` → `bigint`. Via the decimal string: this BN build has no `toBigInt`. */
export const big = (n: Bn): bigint => BigInt(n.toString())

/** `BN` → `number`, for the `i64`s that are timestamps and fit comfortably. */
export const seconds = (n: Bn): number => Number(n.toString())

/** The all-zero key, which several fields use as "nobody". */
export const NOBODY = PublicKey.default

// ── One slot of the front page ──────────────────────────────────────────────

/** What anyone may call on a slot whose term has ended. */
export type TermAction = 'settle' | 'roll' | null

export interface AssetView {
  index: number
  /** Who holds the tenancy. The vault when the Emperor does. */
  holder: PublicKey
  /**
   * Whether that holder is the vault PDA.
   *
   * A sentinel rather than an `Option` on-chain, so the two cases cost the same
   * to read — and the page renders it as the Emperor, never as an address.
   */
  heldByEmperor: boolean
  /**
   * The price right now, in base units.
   *
   * **Both the displayed price and the auction reserve.** There is not a
   * separate number to bid against: `settle_auction` re-reads this same curve
   * at settlement time, which is why a bid that cleared the reserve when it was
   * placed can sit under it by term end.
   */
  price: bigint
  priceFrom: bigint
  priceTo: bigint
  interpStart: number
  interpEnd: number
  /** Whether the price has finished travelling to its target. */
  arrived: boolean
  termNumber: bigint
  termEndsAt: number
  /** Negative once the term has ended and nobody has settled it yet. */
  secondsToTermEnd: number
  termEnded: boolean
  /** The standing high bid in base units. Zero means nobody has bid. */
  highBid: bigint
  /** Null when there is no high bid — on-chain that is the all-zero key. */
  highBidder: PublicKey | null
  /** Whether the standing bid would clear the reserve if settled now. */
  bidClearsReserve: boolean
  /**
   * Which permissionless instruction the slot now qualifies for.
   *
   * The two guards are exact complements in the program, so an ended term is
   * always one or the other and never both.
   */
  nextAction: TermAction
  /** The filed copy, or null when nobody has ever written in this column. */
  copy: string | null
  /** Whether this term's one filing has been used. */
  copyFiled: boolean
  /** Whether the editor struck this column this term. */
  spiked: boolean
}

/**
 * A column's text.
 *
 * `copy_len` is carried on-chain rather than inferred, because "read to the
 * first zero byte" is a guess: nothing stops a tenant filing a NUL and the
 * array is zero-padded either way. Zero means nobody has ever written here,
 * which is a different thing from an empty column and renders differently.
 */
export function decodeCopy(copy: ArrayLike<number>, copyLen: number): string | null {
  if (copyLen === 0) return null
  const bytes = Uint8Array.from(Array.prototype.slice.call(copy, 0, copyLen))
  return new TextDecoder('utf-8').decode(bytes)
}

export function assetView(asset: EncAsset, vault: PublicKey, now: number): AssetView {
  const curve = {
    from: big(asset.priceFrom),
    to: big(asset.priceTo),
    start: seconds(asset.interpStart),
    end: seconds(asset.interpEnd),
  }
  const price = priceAt(curve, now)
  const highBid = big(asset.highBid)
  const termEndsAt = seconds(asset.termEndsAt)
  const termEnded = now >= termEndsAt
  // `settle_auction` requires a bid that is both non-zero and at or above the
  // reserve; `roll_term` requires the negation of exactly that.
  const bidClearsReserve = highBid > 0n && highBid >= price

  return {
    index: asset.index,
    holder: asset.holder,
    heldByEmperor: asset.holder.equals(vault),
    price,
    priceFrom: curve.from,
    priceTo: curve.to,
    interpStart: curve.start,
    interpEnd: curve.end,
    arrived: now >= Math.max(curve.end, curve.start),
    termNumber: big(asset.termNumber),
    termEndsAt,
    secondsToTermEnd: termEndsAt - now,
    termEnded,
    highBid,
    highBidder: asset.highBidder.equals(NOBODY) ? null : asset.highBidder,
    bidClearsReserve,
    nextAction: !termEnded ? null : bidClearsReserve ? 'settle' : 'roll',
    copy: decodeCopy(asset.copy, asset.copyLen),
    copyFiled: asset.copyFiled,
    spiked: asset.copySpiked,
  }
}

// ── The money ───────────────────────────────────────────────────────────────

export interface TreasuryView {
  /**
   * M2 as the Fed last published it: **billions of USD, six decimal places**.
   *
   * `22176.1` is stored as `22_176_100_000`, and getting that by a factor of a
   * thousand is the easiest catastrophic mistake available on this page.
   */
  m2Value: bigint
  /** Unix seconds of the **Fed's release**, not of our sync. */
  m2ReleaseDate: number
  /** Base units of ENC per unit of `m2_value` — that is, per $1,000 of M2. */
  k: bigint
  /** Decimals on the mint. Six. */
  encDecimals: number
  /** Every ENC in existence, from the mint. */
  supply: bigint
  /** `k × M2` at the last sync — what supply was *aimed* at. */
  targetSupply: bigint
  /**
   * `supply − target`. The invariant is `supply ≥ k × M2`, never `=`.
   *
   * A burn larger than the vault could cover leaves the excess outstanding
   * until the next release retargets absolutely. Nothing records that debt,
   * because the next target is a level rather than a delta — so the only place
   * it is visible is right here, as the gap between the two numbers.
   */
  drift: bigint
  /** The vault's floor: `floor_bps` of total supply. Half, as shipped. */
  floor: bigint
  vaultBalance: bigint
  /** The Emperor's share of all the money, in basis points. */
  vaultShareBps: number
  /** Above the floor the faucet pays; at or below it, nothing pays at all. */
  aboveFloor: boolean
  /** Every live bid on every slot, pooled — deliberately not in the vault. */
  escrowBalance: bigint
  /** What an epoch opening right now would snapshot as its pot. */
  potIfOpenedNow: bigint
}

export function treasuryView(args: {
  config: EncConfig
  printer: EncPrinter
  supply: bigint
  vaultBalance: bigint
  escrowBalance: bigint
}): TreasuryView {
  const { config, printer, supply, vaultBalance, escrowBalance } = args
  const floorBps = config.floorBps
  return {
    // Anchor hands every `u64` back as a `BN`, and a `BN` reaching a component
    // is how a number silently becomes `[object Object]` or a mixed-BigInt
    // throw. The conversion happens here, once, and nothing downstream sees one.
    m2Value: big(printer.m2Value),
    m2ReleaseDate: seconds(printer.m2ReleaseDate),
    k: big(config.k),
    encDecimals: config.encDecimals,
    supply,
    targetSupply: big(printer.targetSupply),
    drift: supply - big(printer.targetSupply),
    floor: floorAmount(supply, floorBps),
    vaultBalance,
    vaultShareBps: supply === 0n ? 0 : Number((vaultBalance * 10_000n) / supply),
    aboveFloor: aboveFloor(vaultBalance, supply, floorBps),
    escrowBalance,
    potIfOpenedNow: faucetPot(vaultBalance, supply, floorBps, config.faucetAlphaBps),
  }
}

// ── The faucet's clock ──────────────────────────────────────────────────────

export interface EpochView {
  /** The epoch a timestamp falls in. Also its PDA seed. */
  index: bigint
  startsAt: number
  endsAt: number
  secondsRemaining: number
}

export function epochView(now: number, epochSeconds: number): EpochView {
  const index = epochOf(now, epochSeconds)
  const startsAt = index * epochSeconds
  return {
    index: BigInt(index),
    startsAt,
    endsAt: startsAt + epochSeconds,
    secondsRemaining: startsAt + epochSeconds - now,
  }
}

export interface FaucetView {
  /** Today's epoch: what you register in. */
  current: EpochView
  /** Today's snapshotted pot, or zero if nobody has claimed yet today. */
  pot: bigint
  /** How many wallets have registered today. Tomorrow's divisor. */
  registrants: number
  /**
   * Whether today's epoch account exists yet.
   *
   * **A missing epoch is the normal morning state, not an error.** The account
   * is created lazily by whoever claims first, which is also what snapshots the
   * pot — so before the first claimer of the day there is genuinely nothing
   * there, and the honest reading is a pot of zero rather than a spinner.
   */
  opened: boolean
  /** Yesterday's pot, which is what today's claimants divide. */
  previousPot: bigint
  previousRegistrants: number
  /** One registrant's share of yesterday's pot, if they registered yesterday. */
  shareToday: bigint
  /** What today's pot would pay each of today's registrants, tomorrow. */
  shareTomorrow: bigint
}

/**
 * The faucet, from the two epoch accounts that decide it.
 *
 * Register in N, collect in N+1: a pot divided by a headcount that is still
 * growing could be drawn many times over, so today's claimants divide
 * *yesterday's* frozen pot among *yesterday's* frozen registrant count.
 */
export function faucetView(args: {
  now: number
  config: EncConfig
  current: EncFaucetEpoch | null
  previous: EncFaucetEpoch | null
}): FaucetView {
  const { now, config, current, previous } = args
  const epochSeconds = seconds(config.epochSeconds)
  const pot = current ? big(current.pot) : 0n
  const registrants = current?.registrants ?? 0
  const previousPot = previous ? big(previous.pot) : 0n
  const previousRegistrants = previous?.registrants ?? 0

  return {
    current: epochView(now, epochSeconds),
    pot,
    registrants,
    opened: current !== null,
    previousPot,
    previousRegistrants,
    shareToday: faucetShare(previousPot, previousRegistrants),
    shareTomorrow: faucetShare(pot, registrants),
  }
}

// ── The end, if it ever comes ───────────────────────────────────────────────

export interface RetirementView {
  /** Our clock at the last successful sync — silence is measured from here. */
  lastSyncAt: number
  silenceSeconds: number
  /** When anyone could call `retire`, if nothing is heard before then. */
  dueAt: number
  secondsRemaining: number
  /** Whether the silence condition is already met. */
  ready: boolean
  /** Whether someone has already called it. One-way, and nobody's decision. */
  retired: boolean
}

export function retirementView(config: EncConfig, printer: EncPrinter, now: number): RetirementView {
  const lastSyncAt = seconds(printer.lastSyncAt)
  const silenceSeconds = seconds(config.retirementSilenceSeconds)
  const dueAt = lastSyncAt + silenceSeconds
  return {
    lastSyncAt,
    silenceSeconds,
    dueAt,
    secondsRemaining: dueAt - now,
    ready: now >= dueAt,
    retired: config.retired,
  }
}
