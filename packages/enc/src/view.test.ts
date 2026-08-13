/**
 * The derived state, checked against the program's own rules.
 *
 * The cases that matter are the ones where the page could render something
 * false and look fine doing it: a slot the Emperor holds shown as an address, a
 * column nobody has written shown as empty, an ended term offered the wrong
 * permissionless call, and the supply drift shown as zero because the invariant
 * was assumed to be `=` when it is `≥`.
 */
import { PublicKey } from '@solana/web3.js'
import { describe, expect, it } from 'vitest'
import type { EncAsset, EncConfig, EncFaucetEpoch, EncPrinter } from './accounts.js'
import { SPIKE_MARKER } from './accounts.js'
import { assetView, decodeCopy, epochView, faucetView, retirementView, treasuryView } from './view.js'

const VAULT = new PublicKey('BpAvBQGwMuVsPyaPmPUmSY4p1zrp3Wxd5P3SWsrEHZJH')
const TENANT = new PublicKey('5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT')
const BIDDER = new PublicKey('96PpBLCBHeWXUmCZ5YRdLFmBL75ZqJjMRWBoCarasJNY')

/** Anchor hands `u64`/`i64` back as BN; only `toString` is ever used. */
const bn = (n: bigint | number) => ({ toString: () => String(n) }) as never

/** 280 zero bytes with `text` written into the front, as the program stores it. */
function column(text: string): { copy: number[]; copyLen: number } {
  const bytes = new TextEncoder().encode(text)
  const copy = Array.from({ length: 280 }, (_, i) => bytes[i] ?? 0)
  return { copy, copyLen: bytes.length }
}

function asset(overrides: Partial<Record<string, unknown>> = {}): EncAsset {
  const blank = column('')
  return {
    index: 0,
    holder: VAULT,
    priceFrom: bn(1_000n),
    priceTo: bn(2_000n),
    interpStart: bn(0),
    interpEnd: bn(100),
    termNumber: bn(3n),
    termEndsAt: bn(1_000),
    highBid: bn(0n),
    highBidder: PublicKey.default,
    copy: blank.copy,
    copyLen: 0,
    copyFiled: false,
    copySpiked: false,
    bump: 255,
    ...overrides,
  } as unknown as EncAsset
}

function config(overrides: Partial<Record<string, unknown>> = {}): EncConfig {
  return {
    k: bn(1_000_000n),
    encDecimals: 6,
    floorBps: 5_000,
    faucetAlphaBps: 1_000,
    epochSeconds: bn(86_400),
    retirementSilenceSeconds: bn(31_536_000),
    retired: false,
    ...overrides,
  } as unknown as EncConfig
}

const printer = (overrides: Partial<Record<string, unknown>> = {}): EncPrinter =>
  ({
    m2Value: bn(22_176_100_000n),
    m2ReleaseDate: bn(1_754_870_400),
    targetSupply: bn(1_000n),
    lastSyncAt: bn(0),
    ...overrides,
  }) as unknown as EncPrinter

const epochAccount = (pot: bigint, registrants: number): EncFaucetEpoch =>
  ({ pot: bn(pot), registrants }) as unknown as EncFaucetEpoch

describe('a slot', () => {
  it('prices itself off the curve, every second', () => {
    // Same vectors as the Rust interpolation tests: 1000 → 2000 over 100s.
    expect(assetView(asset(), VAULT, 0).price).toBe(1_000n)
    expect(assetView(asset(), VAULT, 25).price).toBe(1_250n)
    expect(assetView(asset(), VAULT, 100).price).toBe(2_000n)
    expect(assetView(asset(), VAULT, 10_000).price).toBe(2_000n)
  })

  it('says the Emperor holds it rather than naming a PDA', () => {
    expect(assetView(asset(), VAULT, 0).heldByEmperor).toBe(true)
    expect(assetView(asset({ holder: TENANT }), VAULT, 0).heldByEmperor).toBe(false)
  })

  it('reads the all-zero high bidder as nobody', () => {
    expect(assetView(asset(), VAULT, 0).highBidder).toBeNull()
    const bid = asset({ highBid: bn(5_000n), highBidder: BIDDER })
    expect(assetView(bid, VAULT, 0).highBidder?.equals(BIDDER)).toBe(true)
  })

  it('offers nothing while the term is still running', () => {
    const view = assetView(asset({ highBid: bn(9_000n), highBidder: BIDDER }), VAULT, 999)
    expect(view.termEnded).toBe(false)
    expect(view.nextAction).toBeNull()
    expect(view.secondsToTermEnd).toBe(1)
  })

  /**
   * The program's two guards are exact complements, so every ended term is
   * settleable or rollable and never both. Getting this backwards on the page
   * offers a button whose transaction is guaranteed to fail.
   */
  it('offers settle only when the standing bid still clears the reserve', () => {
    const at = 1_000 // the term has ended; the price has arrived at 2000
    const clears = asset({ highBid: bn(2_000n), highBidder: BIDDER })
    const under = asset({ highBid: bn(1_999n), highBidder: BIDDER })

    expect(assetView(clears, VAULT, at).nextAction).toBe('settle')
    expect(assetView(clears, VAULT, at).bidClearsReserve).toBe(true)
    // A bid that beat the reserve when placed can sit under it by term end,
    // because the reserve is re-read at settlement. That is a roll, not a sale.
    expect(assetView(under, VAULT, at).nextAction).toBe('roll')
    // And no bid at all is always a roll.
    expect(assetView(asset(), VAULT, at).nextAction).toBe('roll')
  })

  it('distinguishes a column nobody has written from an empty one', () => {
    // copy_len == 0 means never written — the page renders the Emperor's own
    // default copy there, which is not the same as a tenant filing nothing.
    expect(assetView(asset(), VAULT, 0).copy).toBeNull()
    expect(assetView(asset(column('the emperor has no clothes')), VAULT, 0).copy).toBe(
      'the emperor has no clothes',
    )
  })

  it('surfaces a spiked column as struck, marker and all', () => {
    const struck = asset({ ...column(SPIKE_MARKER), copySpiked: true, copyFiled: true })
    const view = assetView(struck, VAULT, 0)
    expect(view.spiked).toBe(true)
    expect(view.copy).toBe(SPIKE_MARKER)
  })
})

describe('decoding a column', () => {
  it('respects the recorded length rather than hunting for a zero byte', () => {
    // A tenant may file a NUL. Scanning for one would truncate their column.
    const withNul = column('a\0b')
    expect(decodeCopy(withNul.copy, withNul.copyLen)).toBe('a\0b')
  })

  it('does not read the zero padding', () => {
    const short = column('no')
    expect(decodeCopy(short.copy, short.copyLen)).toBe('no')
  })

  it('decodes multi-byte characters by bytes, not characters', () => {
    // COPY_BYTES is bytes: the spike marker's blocks are three bytes each.
    const marker = column(SPIKE_MARKER)
    expect(marker.copyLen).toBeGreaterThan(SPIKE_MARKER.length)
    expect(decodeCopy(marker.copy, marker.copyLen)).toBe(SPIKE_MARKER)
  })
})

describe('the money', () => {
  /**
   * Anchor types every `u64` as `any` in this build, so a `BN` handed straight
   * to a component compiles and then throws "cannot mix BigInt and other types"
   * in a browser — which is exactly how this page first failed to render. The
   * conversion happens once, in the view, and this is the test that says so.
   */
  it('hands out bigints, never the BNs it was given', () => {
    const view = treasuryView({
      config: config(),
      printer: printer(),
      supply: 1_000n,
      vaultBalance: 800n,
      escrowBalance: 0n,
    })
    expect(view.m2Value).toBe(22_176_100_000n)
    expect(typeof view.m2Value).toBe('bigint')
    expect(typeof view.k).toBe('bigint')
    expect(view.m2ReleaseDate).toBe(1_754_870_400)
    expect(typeof view.m2ReleaseDate).toBe('number')
  })

  it('shows the drift when supply sits above its target', () => {
    // The honest invariant is supply ≥ k × M2. A burn the vault could not cover
    // leaves the excess outstanding, and this is the only place it shows.
    const view = treasuryView({
      config: config(),
      printer: printer({ targetSupply: bn(1_000n) }),
      supply: 1_050n,
      vaultBalance: 600n,
      escrowBalance: 0n,
    })
    expect(view.drift).toBe(50n)
    expect(view.targetSupply).toBe(1_000n)
  })

  it('measures the floor and the pot against supply, not against the target', () => {
    const view = treasuryView({
      config: config(),
      printer: printer(),
      supply: 1_000n,
      vaultBalance: 800n,
      escrowBalance: 25n,
    })
    // Floor 50% of 1000 = 500; surplus 300; α 10% → 30. Same vector as math.rs.
    expect(view.floor).toBe(500n)
    expect(view.potIfOpenedNow).toBe(30n)
    expect(view.vaultShareBps).toBe(8_000)
    expect(view.aboveFloor).toBe(true)
    expect(view.escrowBalance).toBe(25n)
  })

  it('pays nothing at or below the floor', () => {
    const view = treasuryView({
      config: config(),
      printer: printer(),
      supply: 1_000n,
      vaultBalance: 500n,
      escrowBalance: 0n,
    })
    expect(view.aboveFloor).toBe(false)
    expect(view.potIfOpenedNow).toBe(0n)
  })
})

describe('the faucet', () => {
  it('treats a missing epoch account as an empty pot, not an error', () => {
    // The account is created lazily by the first claimer of the day, so before
    // then there is genuinely nothing there.
    const view = faucetView({ now: 86_400, config: config(), current: null, previous: null })
    expect(view.opened).toBe(false)
    expect(view.pot).toBe(0n)
    expect(view.registrants).toBe(0)
    expect(view.shareToday).toBe(0n)
  })

  it('divides yesterday pot among yesterday registrants', () => {
    const view = faucetView({
      now: 86_400,
      config: config(),
      current: epochAccount(400n, 2),
      previous: epochAccount(100n, 3),
    })
    // Truncation stays in the vault; it never overpays.
    expect(view.shareToday).toBe(33n)
    expect(view.shareTomorrow).toBe(200n)
    expect(view.current.index).toBe(1n)
  })
})

describe('the clocks', () => {
  it('bounds the epoch a timestamp falls in', () => {
    const view = epochView(86_400 + 3_600, 86_400)
    expect(view.index).toBe(1n)
    expect(view.startsAt).toBe(86_400)
    expect(view.endsAt).toBe(172_800)
    expect(view.secondsRemaining).toBe(82_800)
  })

  it('counts silence from our own clock, not the Fed release date', () => {
    const view = retirementView(config(), printer({ lastSyncAt: bn(1_000) }), 1_000 + 86_400)
    expect(view.dueAt).toBe(1_000 + 31_536_000)
    expect(view.ready).toBe(false)
    expect(view.retired).toBe(false)
  })

  it('knows when anyone could end it', () => {
    const view = retirementView(config(), printer({ lastSyncAt: bn(0) }), 31_536_000)
    expect(view.ready).toBe(true)
    expect(view.secondsRemaining).toBe(0)
  })
})
