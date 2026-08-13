/**
 * The guards, checked against the program's own.
 *
 * Every case here is one a person can reach by clicking, and the ones that
 * matter are where the page could confidently say the wrong thing: a claim that
 * would silently pay nothing, escrow described as stuck when it is one
 * transaction from coming back, a minimum bid that is a base unit too low, and
 * a refusal rendered as a hex code.
 *
 * The account maps are checked here for shape and derivation; that they are
 * *accepted by the program* is proved against a live validator in
 * `chain/tests/actions.ts`, because only a validator can prove that.
 */
import { PublicKey } from '@solana/web3.js'
import { describe, expect, it } from 'vitest'
import type { EncBid, EncConfig, EncFaucetEpoch, EncPlayer } from './accounts.js'
import { TOKEN_2022_PROGRAM_ID, TOKEN_PROGRAM_ID, encAddresses } from './accounts.js'
import {
  MELT_ANNUAL_BPS,
  MELT_SCALE,
  SECONDS_PER_YEAR,
  bidCost,
  bidView,
  certificateIssuable,
  claimAccounts,
  claimView,
  encErrorMessage,
  encErrorName,
  fileCopyAccounts,
  filingBlock,
  meltFactor,
  meltedBalance,
  mintCertificateAccounts,
  placeBidAccounts,
  rollTermAccounts,
  settleAuctionAccounts,
  withdrawBidAccounts,
  withdrawView,
} from './actions.js'
import { ENC_IDL, ENC_PROGRAM_ID } from './idl/emperors_new_coin.js'
import type { AssetView } from './view.js'

const addresses = encAddresses(ENC_PROGRAM_ID)
const VAULT = addresses.vault
const ALICE = new PublicKey('96PpBLCBHeWXUmCZ5YRdLFmBL75ZqJjMRWBoCarasJNY')
const BOB = new PublicKey('5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT')

/** Anchor hands `u64`/`i64` back as BN; only `toString` is ever used. */
const bn = (n: bigint | number) => ({ toString: () => String(n) }) as never

function view(overrides: Partial<AssetView> = {}): AssetView {
  return {
    index: 3,
    holder: VAULT,
    heldByEmperor: true,
    price: 1_000n,
    priceFrom: 1_000n,
    priceTo: 1_000n,
    interpStart: 0,
    interpEnd: 0,
    arrived: true,
    termNumber: 5n,
    termEndsAt: 2_000,
    secondsToTermEnd: 500,
    termEnded: false,
    highBid: 0n,
    highBidder: null,
    bidClearsReserve: false,
    nextAction: null,
    copy: null,
    copyFiled: false,
    spiked: false,
    ...overrides,
  }
}

function config(overrides: Partial<Record<string, unknown>> = {}): EncConfig {
  return {
    floorBps: 5_000,
    faucetAlphaBps: 1_000,
    welcomeGrant: bn(1_000_000_000n),
    grantsPerEpoch: 3,
    ...overrides,
  } as unknown as EncConfig
}

function player(overrides: Partial<Record<string, unknown>> = {}): EncPlayer {
  return {
    wallet: ALICE,
    lastRegisteredEpoch: bn(0n),
    welcomeGrantTaken: true,
    bump: 255,
    ...overrides,
  } as unknown as EncPlayer
}

function epoch(index: bigint, pot: bigint, registrants: number, grantsIssued = 0): EncFaucetEpoch {
  return {
    epoch: bn(index),
    pot: bn(pot),
    registrants,
    grantsIssued,
    bump: 255,
  } as unknown as EncFaucetEpoch
}

function bid(amount: bigint, term: bigint, bidder = ALICE): EncBid {
  return {
    assetIndex: 3,
    bidder,
    amount: bn(amount),
    termNumber: bn(term),
    bump: 255,
  } as unknown as EncBid
}

// A vault comfortably above a 50% floor, so the faucet is open by default.
const SUPPLY = 1_000_000_000_000n
const RICH_VAULT = 800_000_000_000n

describe('claimView', () => {
  const base = { config: config(), supply: SUPPLY, vaultBalance: RICH_VAULT }

  it('pays a first-ever claimant the grant and nothing else', () => {
    const v = claimView({ ...base, epoch: 9n, player: null, current: null, previous: null })
    expect(v.case).toBe('first-ever')
    expect(v.share).toBe(0n)
    expect(v.grant).toBe(1_000_000_000n)
    expect(v.total).toBe(1_000_000_000n)
    expect(v.claimable).toBe(true)
  })

  it('treats an unwritten Player exactly as a missing one', () => {
    // `init_if_needed` can leave a zeroed account behind; the program keys
    // "first visit" on the wallet field, not on the account existing.
    const zeroed = player({ wallet: PublicKey.default, welcomeGrantTaken: false })
    const v = claimView({ ...base, epoch: 9n, player: zeroed, current: null, previous: null })
    expect(v.case).toBe('first-ever')
    expect(v.grant).toBe(1_000_000_000n)
  })

  it('pays yesterday’s share to somebody who registered yesterday', () => {
    const v = claimView({
      ...base,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(9n) }),
      current: null,
      previous: epoch(9n, 400n, 4),
    })
    expect(v.case).toBe('share-due')
    expect(v.share).toBe(100n)
    expect(v.grant).toBe(0n)
  })

  it('pays nothing to somebody who missed a day', () => {
    // Eligibility is "registered in exactly the previous epoch". The share you
    // did not take stays in the vault.
    const v = claimView({
      ...base,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(7n) }),
      current: null,
      previous: epoch(9n, 400n, 4),
    })
    expect(v.case).toBe('no-share-due')
    expect(v.share).toBe(0n)
    expect(v.claimable).toBe(true)
  })

  it('ignores a previous-epoch account that is not the previous epoch', () => {
    const v = claimView({
      ...base,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(9n) }),
      current: null,
      previous: epoch(4n, 400n, 4),
    })
    expect(v.share).toBe(0n)
  })

  it('refuses a second claim in one epoch', () => {
    const v = claimView({
      ...base,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(10n) }),
      current: epoch(10n, 400n, 4),
      previous: epoch(9n, 400n, 4),
    })
    expect(v.case).toBe('already-claimed')
    expect(v.claimable).toBe(false)
    expect(v.total).toBe(0n)
  })

  it('pays nothing at all below the floor — not a share, not a grant', () => {
    const v = claimView({
      ...base,
      // At or below half of supply, `above_floor` is false and the whole
      // handler pays zero. Arriving during the tightening is the lesson.
      vaultBalance: 500_000_000_000n,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(9n), welcomeGrantTaken: false }),
      current: null,
      previous: epoch(9n, 400n, 4),
    })
    expect(v.case).toBe('below-floor')
    expect(v.share).toBe(0n)
    expect(v.grant).toBe(0n)
    expect(v.claimable).toBe(false)
  })

  it('withholds the grant once the epoch’s allotment has run out', () => {
    const v = claimView({
      ...base,
      epoch: 10n,
      player: null,
      current: epoch(10n, 400n, 3, 3),
      previous: null,
    })
    expect(v.grant).toBe(0n)
    // Still worth claiming: it registers you for tomorrow, and the grant is
    // owed to the wallet rather than to the minute it first turned up.
    expect(v.claimable).toBe(true)
  })

  it('caps a share at what the vault actually still holds', () => {
    const v = claimView({
      ...base,
      vaultBalance: 500_000_000_001n,
      epoch: 10n,
      player: player({ lastRegisteredEpoch: bn(9n) }),
      current: null,
      previous: epoch(9n, 900_000_000_000n, 1),
    })
    expect(v.share).toBe(500_000_000_001n)
  })

  it('counts the asking wallet into tomorrow’s divisor', () => {
    // The number that falls as more wallets register — which is why a sybil
    // farm dilutes itself rather than the vault.
    const alone = claimView({ ...base, epoch: 10n, player: null, current: null, previous: null })
    const crowded = claimView({
      ...base,
      epoch: 10n,
      player: null,
      current: epoch(10n, 1_000n, 9),
      previous: null,
    })
    expect(crowded.shareNextEpoch).toBe(100n)
    expect(alone.shareNextEpoch).toBeGreaterThan(crowded.shareNextEpoch)
  })
})

describe('bidView', () => {
  it('asks for the reserve when nobody has bid', () => {
    expect(bidView(view({ price: 1_000n }), ALICE, null).minimum).toBe(1_000n)
  })

  it('asks for one base unit over a standing bid that already clears', () => {
    // `amount > high_bid` is strict: ties lose, so the earlier bidder keeps the
    // position they paid a fee for.
    const v = view({ price: 1_000n, highBid: 1_500n, highBidder: BOB })
    expect(bidView(v, ALICE, null).minimum).toBe(1_501n)
  })

  it('asks for the reserve when the standing bid has fallen under it', () => {
    const v = view({ price: 2_000n, highBid: 1_500n, highBidder: BOB })
    expect(bidView(v, ALICE, null).minimum).toBe(2_000n)
  })

  it('blocks bidding once the term has ended', () => {
    const v = view({ termEnded: true, secondsToTermEnd: -5 })
    expect(bidView(v, ALICE, null).blocked).toBe('term-ended')
  })

  it('blocks bidding while escrow from an earlier term is outstanding', () => {
    const v = view({ termNumber: 6n })
    expect(bidView(v, ALICE, bid(900n, 5n)).blocked).toBe('stale-bid')
  })

  it('does not call a same-term bid stale', () => {
    const v = view({ termNumber: 6n, highBid: 900n, highBidder: ALICE })
    const b = bidView(v, ALICE, bid(900n, 6n))
    expect(b.blocked).toBe(null)
    expect(b.escrowIsCurrentTerm).toBe(true)
    expect(b.isHighBidder).toBe(true)
  })

  it('charges only the difference when raising a live bid', () => {
    const v = view({ termNumber: 6n, highBid: 900n, highBidder: ALICE })
    expect(bidCost(bidView(v, ALICE, bid(900n, 6n)), 1_500n)).toBe(600n)
  })

  it('charges the whole amount when the escrow belongs to an old term', () => {
    const v = view({ termNumber: 6n })
    expect(bidCost(bidView(v, ALICE, bid(900n, 5n)), 1_500n)).toBe(1_500n)
  })
})

describe('withdrawView', () => {
  it('locks the standing bid of the live term, and only that', () => {
    const v = view({ termNumber: 6n, highBid: 900n, highBidder: ALICE })
    const w = withdrawView(v, ALICE, bid(900n, 6n))
    expect(w.withdrawable).toBe(false)
    expect(w.fromEarlierTerm).toBe(false)
  })

  it('releases a bid that has been outbid in the same term', () => {
    const v = view({ termNumber: 6n, highBid: 2_000n, highBidder: BOB })
    expect(withdrawView(v, ALICE, bid(900n, 6n)).withdrawable).toBe(true)
  })

  it('always releases a bid from an earlier term, standing or not', () => {
    // The answer to "my money is stuck" is usually "it isn't": once the term
    // rolls, the bid is dead whatever it once was.
    const v = view({ termNumber: 7n, highBid: 0n, highBidder: null })
    const w = withdrawView(v, ALICE, bid(900n, 6n))
    expect(w.withdrawable).toBe(true)
    expect(w.fromEarlierTerm).toBe(true)
    expect(w.amount).toBe(900n)
  })

  it('has nothing to say when there is no bid account', () => {
    expect(withdrawView(view(), ALICE, null)).toEqual({
      amount: 0n,
      withdrawable: false,
      fromEarlierTerm: false,
    })
  })
})

describe('the Gazette’s guards', () => {
  it('refuses a stranger, in the handler’s own order', () => {
    expect(filingBlock(view({ holder: VAULT }), ALICE)).toBe('not-the-tenant')
  })

  it('tells a struck tenant they were struck, not that they already filed', () => {
    // `copy_spiked` is checked before `copy_filed` in the program precisely so
    // the tenant is told the true thing.
    const v = view({ holder: ALICE, heldByEmperor: false, spiked: true, copyFiled: false })
    expect(filingBlock(v, ALICE)).toBe('spiked')
  })

  it('allows exactly one filing a term', () => {
    const fresh = view({ holder: ALICE, heldByEmperor: false })
    expect(filingBlock(fresh, ALICE)).toBe(null)
    expect(filingBlock(view({ ...fresh, copyFiled: true }), ALICE)).toBe('already-filed')
  })

  it('issues no certificate for a column the Emperor holds', () => {
    expect(certificateIssuable(view({ heldByEmperor: true }), false)).toBe(false)
    expect(certificateIssuable(view({ heldByEmperor: false }), false)).toBe(true)
    expect(certificateIssuable(view({ heldByEmperor: false }), true)).toBe(false)
  })
})

describe('the account maps', () => {
  it('derives claim’s accounts, previous epoch optional', () => {
    const a = claimAccounts(addresses, ALICE, 12n, null)
    expect(a.player.equals(addresses.player(ALICE))).toBe(true)
    expect(a.epochAccount.equals(addresses.epoch(12n))).toBe(true)
    expect(a.previousEpoch).toBe(null)
    expect(a.tokenProgram.equals(TOKEN_PROGRAM_ID)).toBe(true)
  })

  it('sends a bid to the escrow pool, never the vault', () => {
    // The Emperor's money is burned by a contraction; a bidder's never was.
    const a = placeBidAccounts(addresses, 3, ALICE)
    expect(a.escrowTokenAccount.equals(addresses.escrowEncAta)).toBe(true)
    expect(a.escrowTokenAccount.equals(addresses.vaultEncAta)).toBe(false)
    expect(a.bid.equals(addresses.bid(3, ALICE))).toBe(true)
  })

  it('gives withdraw no way to create anything', () => {
    const a = withdrawBidAccounts(addresses, 3, ALICE)
    expect('systemProgram' in a).toBe(false)
    expect('associatedTokenProgram' in a).toBe(false)
  })

  it('pays settlement to the outgoing holder and refunds rent to the winner', () => {
    const a = settleAuctionAccounts(addresses, 3, ALICE, BOB, VAULT)
    expect(a.winner.equals(ALICE)).toBe(true)
    expect(a.outgoingHolder.equals(BOB)).toBe(true)
    expect(a.winningBid.equals(addresses.bid(3, ALICE))).toBe(true)
    expect(a.caller.equals(VAULT)).toBe(true)
  })

  it('gives roll_term two accounts and no signer', () => {
    expect(Object.keys(rollTermAccounts(addresses, 3))).toEqual(['config', 'asset'])
  })

  it('lands a certificate in the holder’s wallet, on Token-2022', () => {
    // Anyone may pay; it is never the payer's.
    const a = mintCertificateAccounts(addresses, 3, 7n, ALICE, BOB)
    expect(a.certMint.equals(addresses.cert(3, 7n))).toBe(true)
    expect(a.tokenProgram.equals(TOKEN_2022_PROGRAM_ID)).toBe(true)
    expect(a.holder.equals(ALICE)).toBe(true)
    expect(a.payer.equals(BOB)).toBe(true)
  })

  it('gives file_copy no token account at all', () => {
    expect(Object.keys(fileCopyAccounts(addresses, 3, ALICE))).toEqual(['tenant', 'asset'])
  })
})

describe('the melting balance', () => {
  it('does not move at zero seconds', () => {
    expect(meltFactor(0)).toBe(MELT_SCALE)
    expect(meltedBalance(123_456_789n, 0)).toBe(123_456_789n)
  })

  it('loses exactly the annual rate over a year', () => {
    const balance = 1_000_000_000_000n
    const after = meltedBalance(balance, SECONDS_PER_YEAR)
    expect(after).toBe((balance * BigInt(10_000 - MELT_ANNUAL_BPS)) / 10_000n)
  })

  it('compounds rather than accumulating linearly', () => {
    const balance = 1_000_000_000_000n
    const two = meltedBalance(balance, SECONDS_PER_YEAR * 2)
    // 0.95² = 0.9025, which is above the 0.90 a linear fall would give.
    expect(two).toBe(902_500_000_000n)
  })

  it('keeps every base unit of a balance past 2^53', () => {
    // The supply is around 2.2e16 base units, so a factor applied through
    // `Number` would start skipping integers. Nothing here is a float but the
    // factor itself.
    const supply = 22_176_100_000_000_000n
    expect(meltedBalance(supply, 0)).toBe(supply)
    expect(meltedBalance(supply, 1)).toBeLessThan(supply)
  })

  it('moves visibly within a second on a wallet-sized balance', () => {
    // The tell only works if the last digits actually tick. A thousand ENC
    // loses a couple of micro-ENC a second, which is the whole effect.
    const thousand = 1_000_000_000n
    expect(thousand - meltedBalance(thousand, 1)).toBeGreaterThan(0n)
  })

  it('never goes negative or past zero', () => {
    expect(meltedBalance(1_000n, SECONDS_PER_YEAR * 500)).toBeGreaterThanOrEqual(0n)
    expect(meltFactor(-5)).toBe(MELT_SCALE)
  })
})

describe('the refusals', () => {
  it('reads the name off a structured Anchor error', () => {
    const err = { error: { errorCode: { code: 'BidBelowReserve', number: 6019 } } }
    expect(encErrorName(err)).toBe('BidBelowReserve')
    expect(encErrorMessage(err)).toMatch(/under the reserve/)
  })

  it('reads it back out of a re-thrown message', () => {
    // `useSendTransaction` humanises and re-throws, so the object is gone by
    // the time the page sees it and only the text survives.
    const err = new Error('AnchorError occurred. Error Code: BidIsStanding. Error Number: 6023.')
    expect(encErrorName(err)).toBe('BidIsStanding')
    expect(encErrorMessage(err)).toMatch(/You are winning/)
  })

  it('recovers a name from a bare hex code', () => {
    const code = codeOf('AlreadyClaimedThisEpoch')
    const err = new Error(`custom program error: 0x${code.toString(16)}`)
    expect(encErrorName(err)).toBe('AlreadyClaimedThisEpoch')
    expect(encErrorMessage(err)).toMatch(/register today, collect tomorrow/)
  })

  it('recovers one from a simulation’s JSON', () => {
    const code = codeOf('TermNotEnded')
    const err = new Error(`failed: {"InstructionError":[0,{"Custom":${code}}]}`)
    expect(encErrorName(err)).toBe('TermNotEnded')
  })

  it('has a sentence for every error the ticket named', () => {
    for (const name of [
      'BidBelowReserve',
      'BidNotHighEnough',
      'BidIsStanding',
      'StaleBidOutstanding',
      'TermNotEnded',
      'NoQualifyingBid',
      'AlreadyClaimedThisEpoch',
      'WrongEpoch',
      'NotTheTenant',
      'AlreadyFiled',
      'ColumnSpiked',
    ]) {
      const message = encErrorMessage({ error: { errorCode: { code: name } } })
      expect(message, name).toBeTruthy()
      // Never a code, never a name: the point is that neither reaches a person.
      expect(message, name).not.toContain(name)
      expect(message!.length, name).toBeGreaterThan(30)
    }
  })

  it('falls back to the program’s own message rather than inventing one', () => {
    // Every error has *something* to say, so a variant added in Rust is blunt
    // rather than a hex code.
    for (const name of ['InvalidRate', 'AssetOutOfOrder', 'StaleRelease']) {
      expect(encErrorMessage({ error: { errorCode: { code: name } } })).toBeTruthy()
    }
  })

  it('recovers one from a message a generic humaniser already rewrote', () => {
    // The shape the page actually receives: `chain-react` catches the failure,
    // turns it into its own sentence, and rethrows. The code survives inside
    // that text, and this is the case that reached a browser as a hex code
    // before it was covered.
    const code = codeOf('TermNotEnded')
    const err = new Error(`The program rejected this (error 0x${code.toString(16)}).`)
    expect(encErrorName(err)).toBe('TermNotEnded')
    expect(encErrorMessage(err)).toMatch(/not ended yet/i)
  })

  it('follows the cause when the rethrow kept the original', () => {
    const inner = { error: { errorCode: { code: 'StaleBidOutstanding' } } }
    const err = new Error('The program rejected this.', { cause: inner })
    expect(encErrorName(err)).toBe('StaleBidOutstanding')
    expect(encErrorMessage(err)).toMatch(/earlier term/i)
  })

  it('says nothing about failures that are not the program refusing', () => {
    expect(encErrorMessage(new Error('User rejected the request.'))).toBe(null)
    expect(encErrorMessage(new Error('Blockhash not found'))).toBe(null)
    // 0x1 is the token program's, not this program's — ENC's codes start at
    // 6000, and claiming a stranger's error would be a confident lie about
    // whose fault something is.
    expect(encErrorName(new Error('custom program error: 0x1'))).toBe(null)
  })

  it('names the one refusal that comes from the token program instead', () => {
    expect(encErrorMessage(new Error('Transfer: insufficient funds'))).toMatch(/that much ENC/)
  })
})

/**
 * The code the program would actually return, read from the IDL.
 *
 * Hardcoding `6019` here would make this suite pass while the mapping was
 * wrong: both would be wrong in the same direction the day somebody inserts a
 * variant into the middle of the Rust enum.
 */
function codeOf(name: string): number {
  // Read through `unknown`: the generated `.ts` types claim these names are
  // camelCase, and the JSON `ENC_IDL` actually is carries the Rust ones. The
  // runtime value is what a program's logs contain, so the runtime value wins.
  const errors = ENC_IDL.errors as unknown as { code: number; name: string }[]
  const error = errors.find((e) => e.name === name)
  if (!error) throw new Error(`no such error: ${name}`)
  return error.code
}
