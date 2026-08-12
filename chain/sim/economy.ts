/**
 * The ENC economy, in TypeScript, running on the program's own arithmetic.
 *
 * **Every number here comes from `@badcode/enc`, which mirrors `math.rs`.**
 * Nothing is re-derived, approximated or floated: if this file disagreed with
 * the program by one truncation, it would pick parameters for a coin that does
 * not exist.
 *
 * ## What is modelled, and what is not
 *
 * Modelled, because the parameters depend on it: the peg (`sync_m2`, including
 * T29's catch-up walk), the vault, total supply, the ten asset price curves and
 * their reserves, and the faucet in full — pots, snapshots, registration,
 * welcome grants, the floor.
 *
 * **Not** modelled: bidding wars, certificates, term lengths, who wins what.
 * Ruling A removed turnover as a goal, so asset turnover is explicitly *not* a
 * criterion — T15 judges vault solvency and whether a patient claimant can ever
 * afford the cheapest reserve, and neither of those needs an auction simulated
 * around it. What *is* modelled is the money moving when a purchase happens,
 * because a purchase from the Emperor refills the vault and that changes the
 * faucet.
 */
import {
  aboveFloor,
  cappedStep,
  faucetPot,
  faucetShare,
  priceAt,
  rescale,
  supplyMove,
  targetSupply,
  type PriceCurve,
} from '@badcode/enc'

export interface SimParams {
  k: bigint
  floorBps: number
  alphaBps: number
  welcomeGrant: bigint
  grantsPerEpoch: number
  epochSeconds: number
  maxChangeBps: number
  interpolationSeconds: number
  /** One genesis price per asset, cheapest first. */
  genesisPrices: bigint[]
}

export interface SyncResult {
  /** How many `sync_m2` calls the release needed. One, unless the walk engaged. */
  steps: number
  /** Whether the release date was finally committed. False means a deadlock. */
  committed: boolean
  minted: bigint
  burned: bigint
  /** How much of a burn the vault could not cover. */
  uncovered: bigint
}

export interface ClaimResult {
  share: bigint
  grant: bigint
}

interface EpochRecord {
  pot: bigint
  registrants: number
  grantsIssued: number
}

interface PlayerRecord {
  lastRegisteredEpoch: number
  grantTaken: boolean
}

/** How far a walk may run before the harness calls it a deadlock. */
const WALK_LIMIT = 10_000

export class Economy {
  readonly params: SimParams
  now: number
  m2: bigint
  releaseDate: number
  supply: bigint
  vault: bigint
  assets: PriceCurve[]
  wallets = new Map<string, bigint>()

  private epochs = new Map<number, EpochRecord>()
  private players = new Map<string, PlayerRecord>()

  constructor(
    params: SimParams,
    genesisM2: bigint,
    startedAt: number,
    genesisReleaseDate = 0,
  ) {
    this.params = params
    this.now = startedAt
    this.m2 = genesisM2
    // The program writes **zero** here, on the reasoning that any real Fed
    // release is later than the unix epoch. True of a coin deployed in 2026,
    // and false of a counterfactual replay that starts in 1959: pre-1970
    // observations have *negative* timestamps, so every release before
    // 1970-01 fails the anti-double-mint guard and the peg sits frozen for
    // eleven years — 133 refusals, then one enormous catch-up walk. That is a
    // fact about the harness, not about the program, so a historical run says
    // when the coin was notionally deployed instead.
    this.releaseDate = genesisReleaseDate
    this.supply = targetSupply(genesisM2, params.k)
    // Every token in the vault. BadCode takes no allocation; there is nobody
    // else at genesis.
    this.vault = this.supply
    this.assets = params.genesisPrices.map((p) => ({
      from: p,
      to: p,
      start: startedAt,
      end: startedAt,
    }))
  }

  epoch(): number {
    return Math.floor(this.now / this.params.epochSeconds)
  }

  balanceOf(wallet: string): bigint {
    return this.wallets.get(wallet) ?? 0n
  }

  /** The reserve on the cheapest asset: what "afford one" costs right now. */
  cheapestReserve(): bigint {
    return this.assets.map((c) => priceAt(c, this.now)).reduce((a, b) => (a < b ? a : b))
  }

  vaultShareBps(): number {
    if (this.supply === 0n) return 0
    return Number((this.vault * 10_000n) / this.supply)
  }

  // ── The peg ───────────────────────────────────────────────────────────────

  /**
   * Apply one Fed release, walking if it is bigger than the cap allows.
   *
   * Returns the number of `sync_m2` calls it took. `committed: false` means the
   * walk never landed — which is the deadlock T29 exists to make impossible, so
   * the tests assert it never happens rather than handling it.
   */
  sync(m2Value: bigint, releaseDate: number): SyncResult {
    if (releaseDate <= this.releaseDate) {
      return { steps: 0, committed: false, minted: 0n, burned: 0n, uncovered: 0n }
    }
    let steps = 0
    let minted = 0n
    let burned = 0n
    let uncovered = 0n

    while (steps < WALK_LIMIT) {
      const previous = this.m2
      const applied = cappedStep(previous, m2Value, this.params.maxChangeBps)
      const target = targetSupply(applied, this.params.k)
      const move = supplyMove(this.supply, target)

      if (move.kind === 'mint') {
        this.supply += move.amount
        this.vault += move.amount
        minted += move.amount
      } else if (move.kind === 'burn') {
        // Only the vault's own tokens can be burned. A burn it cannot cover
        // simply burns everything it has and leaves supply above target.
        const burning = move.amount < this.vault ? move.amount : this.vault
        this.supply -= burning
        this.vault -= burning
        burned += burning
        uncovered += move.amount - burning
      }

      // Rescaled by *this step's* ratio. The steps telescope.
      for (const curve of this.assets) {
        const shown = priceAt(curve, this.now)
        curve.from = shown
        curve.to = rescale(curve.to, previous, applied)
        curve.start = this.now
        curve.end = this.now + this.params.interpolationSeconds
      }

      this.m2 = applied
      steps += 1
      if (applied === m2Value) {
        this.releaseDate = releaseDate
        return { steps, committed: true, minted, burned, uncovered }
      }
    }
    return { steps, committed: false, minted, burned, uncovered }
  }

  // ── The faucet ────────────────────────────────────────────────────────────

  /**
   * `claim()`, exactly as the program does it: open the epoch (snapshotting its
   * pot from the vault *before* this caller is paid), pay the previous epoch's
   * share, pay a welcome grant if one is owed, register.
   */
  claim(wallet: string): ClaimResult {
    const n = this.epoch()
    const player = this.players.get(wallet)
    if (player && player.lastRegisteredEpoch === n) return { share: 0n, grant: 0n }

    const above = aboveFloor(this.vault, this.supply, this.params.floorBps)

    let current = this.epochs.get(n)
    if (!current) {
      current = {
        pot: faucetPot(this.vault, this.supply, this.params.floorBps, this.params.alphaBps),
        registrants: 0,
        grantsIssued: 0,
      }
      this.epochs.set(n, current)
    }

    const previous = this.epochs.get(n - 1)
    const eligible = player !== undefined && player.lastRegisteredEpoch === n - 1
    let share = above && eligible && previous ? faucetShare(previous.pot, previous.registrants) : 0n
    if (share > this.vault) share = this.vault

    const grantDue =
      above && !(player?.grantTaken ?? false) && current.grantsIssued < this.params.grantsPerEpoch
    let grant = grantDue ? this.params.welcomeGrant : 0n
    const left = this.vault - share
    if (grant > left) grant = left

    const paid = share + grant
    this.vault -= paid
    this.wallets.set(wallet, this.balanceOf(wallet) + paid)

    if (grantDue) current.grantsIssued += 1
    current.registrants += 1
    this.players.set(wallet, {
      lastRegisteredEpoch: n,
      grantTaken: (player?.grantTaken ?? false) || grantDue,
    })

    return { share, grant }
  }

  /** What one epoch's pot was, for the outflow-bound assertions. */
  potOf(epoch: number): bigint {
    return this.epochs.get(epoch)?.pot ?? 0n
  }

  registrantsOf(epoch: number): number {
    return this.epochs.get(epoch)?.registrants ?? 0
  }

  // ── Buying a tenancy ──────────────────────────────────────────────────────

  /**
   * Win the cheapest asset at its reserve, paying the Emperor.
   *
   * The auction itself is not modelled (see the header); what matters to the
   * parameters is the *money*, and the money is: the winner pays the current
   * price, and while the Emperor is the outgoing holder it lands in the vault.
   * That is the second way the vault refills, and it is why a faucet that pays
   * out is not simply a leak.
   */
  buyCheapest(wallet: string): bigint | null {
    const price = this.cheapestReserve()
    const held = this.balanceOf(wallet)
    if (held < price) return null
    this.wallets.set(wallet, held - price)
    this.vault += price
    return price
  }

  advance(seconds: number) {
    this.now += seconds
  }
}
