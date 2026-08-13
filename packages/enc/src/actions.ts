/**
 * What a connected wallet may do, and what the chain will say if it tries.
 *
 * Three separable things live here, and they are together because the page
 * needs all three at once for every button it draws:
 *
 * - **The account maps.** Every instruction's account list, derived from
 *   `EncAddresses`. Anchor can resolve some of these itself and cannot resolve
 *   the ones whose seeds come from an instruction argument, so all of them are
 *   named explicitly rather than half of them — a list that is sometimes
 *   complete is a list nobody can check.
 * - **The guards, mirrored.** Every `require!` in the program that a person
 *   could trip by clicking, re-derived here so the page can grey a button out
 *   and say why instead of charging a fee to be told no. The Rust is the source
 *   of truth; if the two disagree the Rust is right and this is the bug.
 * - **The refusals, in English.** The program's error names are its public
 *   interface, and a hex code in a wallet toast is not an explanation.
 *
 * The melting balance lives here too, because it is arithmetic and therefore
 * testable, and because a cosmetic number that nobody can check is exactly the
 * thing this coin is about.
 */
import { PublicKey, SystemProgram } from '@solana/web3.js'
import {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  type EncAddresses,
  type EncBid,
  type EncConfig,
  type EncFaucetEpoch,
  type EncPlayer,
  TOKEN_2022_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
  associatedTokenAddress,
} from './accounts.js'
import { ENC_IDL } from './idl/emperors_new_coin.js'
import { aboveFloor, faucetPot, faucetShare } from './math.js'
import { type AssetView, big } from './view.js'

// ── The account maps ────────────────────────────────────────────────────────
// Keys are Anchor's camelCase view of the Rust field names, which is what
// `.accounts()` wants. `chain/tests/actions.ts` drives every one of these
// against a live validator, so a name that drifts fails a suite rather than a
// user's transaction.

export function claimAccounts(
  a: EncAddresses,
  claimer: PublicKey,
  epoch: bigint,
  /** Null in the three cases the program accepts: epoch zero, an epoch nobody
   *  claimed in, and one already closed. It costs the caller their own share. */
  previousEpoch: PublicKey | null,
) {
  return {
    claimer,
    config: a.config,
    player: a.player(claimer),
    epochAccount: a.epoch(epoch),
    previousEpoch,
    mint: a.mint,
    vault: a.vault,
    vaultTokenAccount: a.vaultEncAta,
    claimerTokenAccount: associatedTokenAddress(claimer, a.mint),
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ASSOCIATED_TOKEN_PROGRAM_ID,
    systemProgram: SystemProgram.programId,
  }
}

export function placeBidAccounts(a: EncAddresses, index: number, bidder: PublicKey) {
  return {
    bidder,
    config: a.config,
    asset: a.asset(index),
    bid: a.bid(index, bidder),
    mint: a.mint,
    bidderTokenAccount: associatedTokenAddress(bidder, a.mint),
    escrow: a.escrow,
    escrowTokenAccount: a.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ASSOCIATED_TOKEN_PROGRAM_ID,
    systemProgram: SystemProgram.programId,
  }
}

/** No associated-token program and no system program: nothing is created here. */
export function withdrawBidAccounts(a: EncAddresses, index: number, bidder: PublicKey) {
  return {
    bidder,
    config: a.config,
    asset: a.asset(index),
    bid: a.bid(index, bidder),
    mint: a.mint,
    bidderTokenAccount: associatedTokenAddress(bidder, a.mint),
    escrow: a.escrow,
    escrowTokenAccount: a.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
  }
}

/**
 * Settlement, which any wallet may run.
 *
 * The caller is whoever bothered; the winner and the outgoing holder are read
 * off the asset, never off the person clicking. `outgoingHolderTokenAccount` is
 * created here if it is missing, at the caller's expense — that is rule 2 in
 * `settle_auction.rs`, and it is why nobody can veto their own eviction.
 */
export function settleAuctionAccounts(
  a: EncAddresses,
  index: number,
  winner: PublicKey,
  outgoingHolder: PublicKey,
  caller: PublicKey,
) {
  return {
    caller,
    config: a.config,
    asset: a.asset(index),
    winningBid: a.bid(index, winner),
    winner,
    outgoingHolder,
    mint: a.mint,
    outgoingHolderTokenAccount: associatedTokenAddress(outgoingHolder, a.mint),
    escrow: a.escrow,
    escrowTokenAccount: a.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ASSOCIATED_TOKEN_PROGRAM_ID,
    systemProgram: SystemProgram.programId,
  }
}

/**
 * Two accounts and **no signer at all**.
 *
 * The transaction's fee payer signs; this instruction asks nothing of anyone,
 * which is what "the clock is published" has to mean.
 */
export function rollTermAccounts(a: EncAddresses, index: number) {
  return { config: a.config, asset: a.asset(index) }
}

/** Anyone may pay. It lands in the holder's wallet regardless of who did. */
export function mintCertificateAccounts(
  a: EncAddresses,
  index: number,
  term: bigint,
  holder: PublicKey,
  payer: PublicKey,
) {
  const certMint = a.cert(index, term)
  return {
    payer,
    config: a.config,
    asset: a.asset(index),
    holder,
    vault: a.vault,
    // The all-zero key, which the token-metadata interface reads as "no update
    // authority". The System Program's id *is* that key.
    noneAuthority: SystemProgram.programId,
    certMint,
    holderCertAccount: associatedTokenAddress(holder, certMint, TOKEN_2022_PROGRAM_ID),
    tokenProgram: TOKEN_2022_PROGRAM_ID,
    associatedTokenProgram: ASSOCIATED_TOKEN_PROGRAM_ID,
    systemProgram: SystemProgram.programId,
  }
}

/**
 * Two accounts, and neither is a token account.
 *
 * That is the shape of the guarantee rather than a promise about it: the
 * Gazette cannot move money because the instruction has nothing to move it
 * with.
 */
export function fileCopyAccounts(a: EncAddresses, index: number, tenant: PublicKey) {
  return { tenant, asset: a.asset(index) }
}

// ── The faucet, from the asking wallet's side ───────────────────────────────

/**
 * Which of the faucet's outcomes this wallet is walking into.
 *
 * The shape is genuinely confusing — you register in one epoch and collect in
 * the next — and the page's job is to say which case somebody is in *before*
 * they pay a fee to discover it.
 */
export type ClaimCase =
  /** The vault is at or below its floor. Nothing pays out, to anyone. */
  | 'below-floor'
  /** Never claimed. Registers, takes the welcome grant, collects next epoch. */
  | 'first-ever'
  /** Registered last epoch, so there is a share waiting. */
  | 'share-due'
  /** Registered, but not last epoch — the missed pot stayed in the vault. */
  | 'no-share-due'
  /** Already registered this epoch. The program refuses a second. */
  | 'already-claimed'

export interface ClaimView {
  /** The epoch the chain is in. The instruction takes it as an argument. */
  epoch: bigint
  case: ClaimCase
  /** Whether the button does anything. False when refused or worthless. */
  claimable: boolean
  /** Yesterday's pot, divided by yesterday's registrants. */
  share: bigint
  /** The one-per-wallet-ever welcome grant, if this claim would carry one. */
  grant: bigint
  /** What would actually arrive: `share + grant`. Frequently zero, honestly. */
  total: bigint
  /**
   * What registering now would be worth on the next claim, at today's
   * headcount. It falls as more wallets register, which is the whole reason a
   * sybil farm dilutes itself instead of the vault.
   */
  shareNextEpoch: bigint
  /** Whether this wallet has ever taken the grant. */
  grantTaken: boolean
}

/**
 * Mirrors `claim.rs`'s handler, in the order the handler decides things.
 *
 * `player` is null before a wallet's first ever claim — the account is created
 * by that claim — and `current` is null before the epoch's first claimer opens
 * it, which is the normal state of every morning rather than an error.
 */
export function claimView(args: {
  epoch: bigint
  config: EncConfig
  player: EncPlayer | null
  current: EncFaucetEpoch | null
  previous: EncFaucetEpoch | null
  supply: bigint
  vaultBalance: bigint
}): ClaimView {
  const { epoch, config, player, current, previous, supply, vaultBalance } = args
  const above = aboveFloor(vaultBalance, supply, config.floorBps)

  // A `Player` whose wallet is the all-zero key has been created but never
  // written, which the program treats identically to one that does not exist.
  const known = player !== null && !player.wallet.equals(PublicKey.default)
  const lastRegistered = known ? big(player.lastRegisteredEpoch) : null
  const grantTaken = known ? player.welcomeGrantTaken : false

  const alreadyClaimed = lastRegistered === epoch
  const registeredLastEpoch = lastRegistered !== null && lastRegistered + 1n === epoch

  // The program checks the previous epoch account really is the previous one
  // rather than trusting whatever was passed, and so does this.
  const previousPot =
    previous !== null && big(previous.epoch) + 1n === epoch
      ? faucetShare(big(previous.pot), previous.registrants)
      : 0n
  const share =
    above && registeredLastEpoch && !alreadyClaimed
      ? // A pot snapshotted while the vault was fuller can exceed what is left.
        min(previousPot, vaultBalance)
      : 0n

  const grantsIssued = current?.grantsIssued ?? 0
  const grantDue =
    above && !grantTaken && !alreadyClaimed && grantsIssued < config.grantsPerEpoch
  const grant = grantDue ? min(big(config.welcomeGrant), vaultBalance - share) : 0n

  // The pot this claim would register against: today's if somebody has opened
  // it, otherwise what opening it right now would freeze.
  const potNow = current
    ? big(current.pot)
    : faucetPot(vaultBalance, supply, config.floorBps, config.faucetAlphaBps)
  const headcount = (current?.registrants ?? 0) + (alreadyClaimed ? 0 : 1)

  const kind: ClaimCase = !above
    ? 'below-floor'
    : alreadyClaimed
      ? 'already-claimed'
      : !known
        ? 'first-ever'
        : registeredLastEpoch
          ? 'share-due'
          : 'no-share-due'

  return {
    epoch,
    case: kind,
    // Below the floor the transaction would succeed and pay nothing, which is
    // worse than a refusal: it costs a fee to learn something the page knows.
    claimable: above && !alreadyClaimed,
    share,
    grant,
    total: share + grant,
    shareNextEpoch: faucetShare(potNow, headcount),
    grantTaken,
  }
}

// ── The auction, from the asking wallet's side ──────────────────────────────

/** Why `place_bid` would refuse before the amount is even considered. */
export type BidBlock =
  /** Past `term_ends_at`. Bidding reopens when somebody settles or rolls. */
  | 'term-ended'
  /** Escrow from an earlier term is still sitting here. Withdraw it first. */
  | 'stale-bid'
  | null

export interface BidView {
  /**
   * The least this wallet may offer: at or above the reserve, and **strictly**
   * above the standing bid. Ties lose, so the earlier bidder keeps the position
   * they paid a fee for.
   */
  minimum: bigint
  /** What this wallet already has escrowed on this slot, if anything. */
  escrowed: bigint
  /** Whether that escrow belongs to the live term, making a raise a top-up. */
  escrowIsCurrentTerm: boolean
  blocked: BidBlock
  /** Whether the wallet holds this slot right now. Bidding on it is allowed. */
  isHolder: boolean
  /** Whether this wallet is the standing high bidder. */
  isHighBidder: boolean
}

export function bidView(view: AssetView, wallet: PublicKey, bid: EncBid | null): BidView {
  const escrowed = bid ? big(bid.amount) : 0n
  const escrowIsCurrentTerm = bid !== null && big(bid.termNumber) === view.termNumber
  const stale = escrowed > 0n && !escrowIsCurrentTerm

  return {
    // `amount >= price` and `amount > high_bid`, so the binding floor is
    // whichever is higher — and one base unit above a bid that already clears.
    minimum: view.highBid + 1n > view.price ? view.highBid + 1n : view.price,
    escrowed,
    escrowIsCurrentTerm,
    blocked: view.termEnded ? 'term-ended' : stale ? 'stale-bid' : null,
    isHolder: view.holder.equals(wallet),
    isHighBidder: view.highBidder !== null && view.highBidder.equals(wallet),
  }
}

/** What a bid of `amount` actually transfers. Raising costs only the raise. */
export function bidCost(bid: BidView, amount: bigint): bigint {
  const already = bid.escrowIsCurrentTerm ? bid.escrowed : 0n
  return amount > already ? amount - already : 0n
}

export interface WithdrawView {
  /** What is sitting in escrow for this wallet on this slot. */
  amount: bigint
  withdrawable: boolean
  /**
   * Whether the escrow is from a term that has already rolled.
   *
   * **The distinction the page must not bury.** A bid is locked in exactly one
   * situation — standing *and* current-term — and a bid from any earlier term
   * is always withdrawable, however long it has sat there.
   */
  fromEarlierTerm: boolean
}

export function withdrawView(view: AssetView, wallet: PublicKey, bid: EncBid | null): WithdrawView {
  if (!bid) return { amount: 0n, withdrawable: false, fromEarlierTerm: false }
  const sameTerm = big(bid.termNumber) === view.termNumber
  const standing = sameTerm && view.highBidder !== null && view.highBidder.equals(wallet)
  return {
    amount: big(bid.amount),
    withdrawable: !standing,
    fromEarlierTerm: !sameTerm,
  }
}

// ── The Gazette, from the asking wallet's side ──────────────────────────────

/** Why `file_copy` would refuse. Checked in the handler's own order. */
export type FilingBlock = 'not-the-tenant' | 'spiked' | 'already-filed' | null

export function filingBlock(view: AssetView, wallet: PublicKey): FilingBlock {
  if (!view.holder.equals(wallet)) return 'not-the-tenant'
  if (view.spiked) return 'spiked'
  if (view.copyFiled) return 'already-filed'
  return null
}

/**
 * Whether a certificate can still be minted for the running tenancy.
 *
 * `minted` is the existence of the certificate mint PDA, which the caller
 * reads: the seeds are `(asset, term)`, so a term issues exactly one, ever.
 */
export function certificateIssuable(view: AssetView, minted: boolean): boolean {
  return !view.heldByEmperor && !minted
}

// ── The melting balance ─────────────────────────────────────────────────────

/**
 * How fast the displayed balance falls: **6% a year**.
 *
 * Not invented, and not a decay of anything on-chain — nothing on this coin
 * decays, there is no demurrage, and the number in your wallet will be the same
 * number tomorrow. It is roughly the rate the money supply grows at, so it is
 * what a balance sitting still loses in purchasing power against everything
 * priced against M2 — which on this page is literally every price.
 *
 * **Measured, not borrowed** (corrected 2026-08-13). This was 5%, taken from
 * `design/research/2026-08-12-enc-tokenomics/README.md`, which says M2 grows
 * "on the order of 5% per year". That is an order-of-magnitude figure doing an
 * order-of-magnitude job there — it was comparing against rent at *150% a
 * month*, where a point either way changes nothing. Stated on the page as what
 * the money supply actually does, it was simply too low. Compound growth of
 * M2SL straight from the Fed's own series:
 *
 * | window | CAGR |
 * | --- | --- |
 * | 1959-01 → 2026-06 (the whole record) | **6.73%** |
 * | 1990-01 → 2026-06 | 5.62% |
 * | 2000-01 → 2026-06 | 6.25% |
 * | 2010-01 → 2026-06 | 6.32% |
 * | 2015-01 → 2026-06 | 6.08% |
 *
 * **Every window is above 5%**, so 6% is the conservative round number rather
 * than a flattering one — the full-record figure is worse, and the joke is
 * better for it. Re-run it against `chain/sim/m2-history.csv` if you want to
 * move it; do not re-import the research's 5% without reading why it says 5%.
 *
 * The page says all of this out loud. A number that lies has to admit it.
 */
export const MELT_ANNUAL_BPS = 600

/** A Gregorian year, so a countdown and a decay agree about how long one is. */
export const SECONDS_PER_YEAR = 31_556_952

/** The decay factor's fixed-point scale: parts per trillion. */
export const MELT_SCALE = 1_000_000_000_000n

/**
 * `(1 − rate) ^ (seconds / year)`, as parts per trillion.
 *
 * A `number` on the way through, because the exponent is genuinely fractional —
 * but only ever for the *factor*, never for the balance. The balance is a `u64`
 * of base units well past 2^53, so it stays a `bigint` and is scaled by this
 * integer, which is the whole reason the factor is expressed this way.
 */
export function meltFactor(secondsHeld: number, annualBps: number = MELT_ANNUAL_BPS): bigint {
  if (!Number.isFinite(secondsHeld) || secondsHeld <= 0) return MELT_SCALE
  const remaining = 1 - annualBps / 10_000
  if (remaining <= 0) return 0n
  const factor = Math.pow(remaining, secondsHeld / SECONDS_PER_YEAR)
  return BigInt(Math.round(factor * Number(MELT_SCALE)))
}

/**
 * What the page shows instead of the balance.
 *
 * Truncating rather than rounding, like every other number here: showing a
 * balance nobody has is the wrong direction to be wrong in, even when the
 * number is admittedly cosmetic.
 */
export function meltedBalance(
  balance: bigint,
  secondsHeld: number,
  annualBps: number = MELT_ANNUAL_BPS,
): bigint {
  return (balance * meltFactor(secondsHeld, annualBps)) / MELT_SCALE
}

// ── The refusals, in English ────────────────────────────────────────────────

/**
 * Every error the program can return, by its Anchor code.
 *
 * Built from the IDL rather than hand-numbered, so inserting a variant in the
 * Rust enum cannot silently renumber this table into saying the wrong thing —
 * which is the failure mode that makes error mapping worth doing carefully at
 * all.
 *
 * **Anchor's two IDLs disagree about error names, and the JSON is the one that
 * is true at runtime.** `chain/idl/emperors_new_coin.json` carries the Rust
 * variant name (`MathOverflow`), the generated `.ts` view carries its camelCase
 * rendering (`mathOverflow`), and `ENC_IDL` is the JSON wearing the `.ts`
 * file's types. The name a running program actually puts in its logs — and
 * therefore in `errorCode.code` — is the Rust one. Taking the compiler's word
 * for it here would build a lookup table that never matches anything, and would
 * do so silently: every refusal would fall through to a hex code.
 */
const ENC_ERRORS = ENC_IDL.errors as unknown as { code: number; name: string; msg: string }[]

const BY_CODE = new Map<number, { name: string; msg: string }>(
  ENC_ERRORS.map((e) => [e.code, { name: e.name, msg: e.msg }]),
)

/**
 * What the refusal actually means to the person who clicked.
 *
 * The program's `#[msg]` strings are written for an explorer and are correct
 * but terse; these are written for someone who is about to conclude their money
 * is gone. Anything not listed falls back to the IDL's own message, so a new
 * error is merely blunt rather than a hex code.
 */
const IN_ENGLISH: Record<string, string> = {
  // ── The auction ──
  BidBelowReserve:
    'That is under the reserve. The reserve is what M2 says this column is worth and it climbs every second, so it has probably moved since the page drew it — read the price again and bid at least that.',
  BidNotHighEnough:
    'Somebody is already bidding that much or more. Ties lose here, so beat the standing bid by at least one micro-ENC.',
  BidIsStanding:
    'You are winning, and the winning bid of a live term is the only locked money in this program. It unlocks the moment the term settles — which anyone may do once the clock runs out, including you.',
  StaleBidOutstanding:
    'You still have escrow on this column from an earlier term. It is not stuck: withdraw it and it comes straight back. It is simply not re-entered into an auction you never chose to join.',
  TermEnded:
    'This term is over and bidding has closed. It reopens the moment somebody settles or rolls it, and that somebody can be you.',
  TermNotEnded: 'The term has not ended yet. Nobody gets to end one early, including us.',
  NoQualifyingBid:
    'No bid cleared the reserve, so there is nothing to settle. Roll the term instead — the incumbent keeps the column, which is what a quiet market looks like.',
  QualifyingBidExists:
    'A bid did clear the reserve, so this term settles rather than rolls. Settle it and the column changes hands.',
  WrongBidAccount:
    'That is no longer the standing bid — somebody moved while this was in flight. The page has caught up; look again.',
  NoCertificateDue:
    'No certificate is due. Either that term has already rolled, or the Emperor holds the column — and the Emperor gets no receipt, because he never won anything.',
  WrongHolderAccount:
    'That account does not belong to the holder. A certificate only ever lands in the tenant’s wallet, never the payer’s.',

  // ── The Gazette ──
  NotTheTenant:
    'You do not hold this column. Win it at auction and the page is yours for a term.',
  AlreadyFiled:
    'This column has already been filed this term. One filing per term — you used yours, and the next term gets a fresh page.',
  ColumnSpiked:
    'The editor struck this column. Nothing more goes in it this term; the next term starts clean.',
  CopyTooLong: 'Longer than a column. 280 bytes, and an emoji costs four of them.',
  NotTheEditor: 'Only the editor may do that, and you are not holding the pen.',
  PenBroken: 'The pen was broken. This paper has no editor and never will again.',

  // ── The faucet ──
  AlreadyClaimedThisEpoch:
    'You have already claimed this epoch. Come back in the next one — register today, collect tomorrow is the whole shape of it.',
  WrongEpoch:
    'The epoch turned over while this transaction was in flight. Send it again and it will name the new one.',
  EpochNotSettled: 'That epoch can still be collected against. It is not finished yet.',

  // ── Lifecycle ──
  NotFullyInitialized:
    'The coin is not switched on here — the ten columns do not all exist yet.',
  InvalidAssetIndex: 'There is no column with that number. There are ten, 0 through 9.',
  Retired:
    'This coin has retired. Somebody observed that the Fed had stopped speaking and said so on-chain; the peg will never move again.',
  NotSilentEnough: 'It has heard about money too recently to be retired.',
  MathOverflow:
    'The arithmetic refused. Nothing wraps in this program — a wrapped number is the one failure this coin could not survive.',
}

/**
 * Pull an Anchor error name out of whatever shape the failure arrived in.
 *
 * There are four shapes and all of them turn up in practice, which is why this
 * is a chain of attempts rather than one lookup:
 *
 * 1. **The structured Anchor error**, when the failure was decoded for us.
 * 2. **Anchor's own text**, which survives being re-thrown as a plain `Error`.
 * 3. **A bare code**, from a preflight failure where the name never existed —
 *    including the form `chain-react` prints once it has humanised the message
 *    itself, which is the shape the ENC page actually receives most often.
 * 4. **A simulation's JSON**, where the code arrives in decimal.
 *
 * It also follows `cause`, because a rethrow that keeps the original is the
 * whole reason this can be better than "the program rejected this".
 */
export function encErrorName(err: unknown): string | null {
  const structured = (err as { error?: { errorCode?: { code?: string } } })?.error?.errorCode?.code
  if (typeof structured === 'string' && BY_CODE_NAME.has(structured)) return structured

  const raw = err instanceof Error ? err.message : typeof err === 'string' ? err : ''
  const named = raw.match(/Error Code: (\w+)/)
  if (named && BY_CODE_NAME.has(named[1])) return named[1]
  // `custom program error: 0x1780` raw, and `(error 0x1780)` once a generic
  // humaniser has had a go at it first.
  const hex = raw.match(/error:? \(?(0x[0-9a-f]+)\)?/i)
  if (hex) return BY_CODE.get(Number.parseInt(hex[1], 16))?.name ?? null
  const decimal = raw.match(/"Custom"\s*:\s*(\d+)/)
  if (decimal) return BY_CODE.get(Number.parseInt(decimal[1], 10))?.name ?? null

  const cause = (err as { cause?: unknown })?.cause
  return cause !== undefined && cause !== null && cause !== err ? encErrorName(cause) : null
}

const BY_CODE_NAME = new Set(ENC_ERRORS.map((e) => e.name))

/**
 * The refusal as a sentence, or null when this is not the program refusing.
 *
 * Null rather than a guess: a wallet cancellation and a dead RPC are the
 * caller's to phrase, and pretending they came from the program would be a
 * confident lie about whose fault something is.
 */
export function encErrorMessage(err: unknown): string | null {
  const name = encErrorName(err)
  if (name) return IN_ENGLISH[name] ?? BY_CODE_NAME_MSG.get(name) ?? null

  // The SPL token program's own refusal, which is not in ENC's error table and
  // is by far the likeliest thing a bidder will hit.
  const raw = [
    err instanceof Error ? err.message : typeof err === 'string' ? err : '',
    (err as { cause?: { message?: string } })?.cause?.message ?? '',
  ].join('\n')
  if (/insufficient funds|Insufficient Funds/.test(raw)) {
    return 'You do not have that much ENC. The faucet is the only route in that we control, and it pays once an epoch.'
  }
  return null
}

const BY_CODE_NAME_MSG = new Map(ENC_ERRORS.map((e) => [e.name, e.msg]))

function min(a: bigint, b: bigint): bigint {
  return a < b ? a : b
}
