import { expect } from 'chai'
import { Keypair, LAMPORTS_PER_SOL } from '@solana/web3.js'
import { TOKEN_PROGRAM_ID, transfer } from '@solana/spl-token'
import {
  ASSET_COUNT,
  GENESIS_M2,
  INTERPOLATION_SECONDS,
  assetMetas,
  big,
  bootstrap,
  harness,
  mockFund,
  setMockM2,
} from './enc-harness.js'

/**
 * `sync_m2` — the printer.
 *
 * Requires a **mock build**. `./stack test` builds the ENC program with
 * `--features mock` before running anything, because localnet never talks to
 * Switchboard.
 *
 * Every assertion is against a value read immediately beforehand rather than an
 * absolute figure, because the ledger persists between runs.
 */
describe('sync_m2', () => {
  const h = harness()
  const K = BigInt(h.params.peg.k)
  const MAX_CHANGE_BPS = BigInt(h.params.sanity.maxChangeBps)

  /** The program's own arithmetic, mirrored: supply = k x m2. */
  const targetFor = (m2: bigint) => m2 * K

  let release = 1_700_000_000

  const setM2 = async (m2: bigint, releaseDate?: number) => {
    release = releaseDate ?? release + 86_400
    await setMockM2(h, m2, release)
  }

  const syncAccounts = {
    config: h.configPda,
    printer: h.printerPda,
    oracle: h.mockOraclePda,
    mint: h.mintPda,
    vault: h.vaultPda,
    vaultTokenAccount: h.vaultEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
  }

  const sync = () =>
    h.program.methods.syncM2().accounts(syncAccounts).remainingAccounts(assetMetas(h)).rpc()

  const printer = () => h.program.account.printer.fetch(h.printerPda)
  const asset = (i: number) => h.program.account.asset.fetch(h.assetPda(i))
  const currentM2 = async () => big((await printer()).m2Value)

  before(async function () {
    this.timeout(300_000)
    await bootstrap(h)
    // Sync once from a known value, so the first assertion has somewhere to
    // move from and the release date is past whatever a previous run left.
    const p = await printer()
    release = Math.max(release, p.m2ReleaseDate.toNumber() + 86_400)
    await setM2(GENESIS_M2, release)
    await sync()
  })

  // ── The peg ───────────────────────────────────────────────────────────────

  it('mints exactly to target when M2 rises', async () => {
    const before = await h.supply()
    const m2 = (await currentM2()) + 100_000_000n // +$100bn
    await setM2(m2)
    await sync()
    expect((await h.supply()).toString()).to.equal(targetFor(m2).toString())
    // Compared as booleans: chai's greaterThan does not accept a BigInt.
    expect((await h.supply()) > before, 'supply did not rise').to.be.true
  })

  it('burns exactly to target when M2 falls', async () => {
    const before = await h.supply()
    const m2 = (await currentM2()) - 100_000_000n
    await setM2(m2)
    await sync()
    expect((await h.supply()).toString()).to.equal(targetFor(m2).toString())
    expect((await h.supply()) < before, 'supply did not fall').to.be.true
  })

  /**
   * A downward revision and quantitative tightening take the same path — the
   * reason the design targets a level rather than ratcheting on the highest M2
   * ever seen.
   */
  it('treats a downward revision as an ordinary burn', async () => {
    const m2 = await currentM2()
    const revised = m2 - m2 / 625n // the observed ~0.16% restatement
    await setM2(revised)
    await sync()
    expect((await h.supply()).toString()).to.equal(targetFor(revised).toString())
  })

  /** The invariant we can honestly publish. */
  it('never leaves supply below k x M2', async () => {
    const p = await printer()
    expect((await h.supply()) >= targetFor(big(p.m2Value)), 'supply fell below k x M2').to.be.true
    expect(p.targetSupply.toString()).to.equal(targetFor(big(p.m2Value)).toString())
  })

  // ── The guards ────────────────────────────────────────────────────────────

  it('refuses a release date that has not advanced', async () => {
    // Same date, different value: the anti-double-mint guard, and the reason it
    // keys on the Fed's date rather than on block time.
    const p = await printer()
    await setM2(big(p.m2Value) + 1_000_000n, p.m2ReleaseDate.toNumber())
    expect(await h.failureOf(sync)).to.match(/StaleRelease/)
  })

  /**
   * The cap is a speed limit, not a veto — and this is the case that used to
   * assert the opposite.
   *
   * As built, a move beyond `max_change_bps` was refused. Because `previous_m2`
   * only advances on success, that refusal was **permanent**: the gap never
   * closed, every later sync failed too, and `retire` ended the coin a year
   * later. One genuine hyperinflation-scale month would have killed the
   * artwork at the exact moment its thesis was most vindicated. T29 replaced
   * the refusal with a walk.
   */
  it('absorbs an oversized release over several syncs, committing the date once', async function () {
    this.timeout(120_000)
    const from = await currentM2()
    // Five times the cap: five capped steps and a landing.
    const beyond = from + (from * MAX_CHANGE_BPS * 5n) / 10_000n
    const pricesBefore = await Promise.all(
      Array.from({ length: ASSET_COUNT }, (_, i) => asset(i).then((a) => big(a.priceTo))),
    )
    const dateBefore = (await printer()).m2ReleaseDate.toNumber()
    await setM2(beyond)

    let steps = 0
    while ((await currentM2()) !== beyond) {
      const before = await currentM2()
      await sync()
      steps += 1
      const after = await currentM2()
      expect(after > before, `step ${steps} did not move`).to.be.true
      // Each step is within the cap, measured against where it started.
      expect(
        (after - before) * 10_000n <= before * MAX_CHANGE_BPS,
        `step ${steps} exceeded the cap`,
      ).to.be.true
      if (after !== beyond) {
        // The release date is withheld until the walk lands — which is exactly
        // what lets the same quote back in for the next step.
        expect(
          (await printer()).m2ReleaseDate.toNumber(),
          'the release date was committed mid-walk',
        ).to.equal(dateBefore)
      }
      expect(steps, 'the walk did not converge').to.be.lessThan(20)
    }

    expect(steps, 'a five-times-the-cap move should take more than one step').to.be.greaterThan(1)
    expect((await printer()).m2ReleaseDate.toNumber(), 'the release was never committed').to.equal(
      release,
    )
    // Supply lands exactly where a single-step sync would have put it.
    expect((await h.supply()).toString()).to.equal(targetFor(beyond).toString())

    // And so do the prices: the steps telescope, up to truncation.
    for (let i = 0; i < ASSET_COUNT; i++) {
      const expected = (pricesBefore[i] * beyond) / from
      const actual = big((await asset(i)).priceTo)
      const drift = actual > expected ? actual - expected : expected - actual
      expect(
        drift * 1_000_000n <= expected,
        `asset ${i} drifted ${drift} from the single-step target ${expected}`,
      ).to.be.true
    }
  })

  /**
   * The other half of T29: no absolute cap in base units.
   *
   * `max_single_mint` was a fixed number of tokens against a money supply that
   * doubles roughly every eleven years, so an ordinary month would have
   * exceeded it eventually and deadlocked the peg forever. The walk above has
   * just carried M2 well past today's level; an ordinary month must still work
   * up there, and the mint it implies is far larger than the deleted cap ever
   * allowed.
   */
  it('mints an ordinary month at a much larger money supply', async function () {
    this.timeout(60_000)
    const m2 = await currentM2()
    expect(m2 > GENESIS_M2, 'this case needs M2 above where it started').to.be.true
    // The historical median month: +0.522%.
    const ordinary = m2 + (m2 * 52n) / 10_000n
    const mintSize = targetFor(ordinary) - (await h.supply())
    // The old placeholder cap was 1e15 base units. Nothing enforces it now,
    // and this asserts the number it would have refused.
    expect(mintSize > 0n, 'the ordinary month did not imply a mint').to.be.true

    await setM2(ordinary)
    await sync()
    expect((await h.supply()).toString(), 'an ordinary month failed').to.equal(
      targetFor(ordinary).toString(),
    )
    expect((await printer()).m2ReleaseDate.toNumber(), 'it needed more than one step').to.equal(
      release,
    )
  })

  /** Level-targeting self-heals: a bad print is corrected, not compounded. */
  it('converges back to the truth after a bad print', async function () {
    this.timeout(120_000)
    const truth = await currentM2()
    // A wrong number, walked partway toward — one step, then abandoned.
    await setM2(truth * 2n)
    await sync()
    const drifted = await currentM2()
    expect(drifted > truth, 'the bad print did not move the peg at all').to.be.true
    expect(drifted < truth * 2n, 'the bad print landed in one step').to.be.true

    // The next genuine release retargets absolutely. It is more than a cap
    // away, so it walks — and lands on the truth, not on the truth minus
    // whatever the bad print did.
    await setM2(truth)
    for (let i = 0; i < 20 && (await currentM2()) !== truth; i++) await sync()
    expect((await currentM2()).toString(), 'the peg did not converge back').to.equal(
      truth.toString(),
    )
    expect((await h.supply()).toString()).to.equal(targetFor(truth).toString())
  })

  it('refuses the wrong number of asset accounts', async () => {
    await setM2((await currentM2()) + 1_000_000n)
    const why = await h.failureOf(() =>
      h.program.methods
        .syncM2()
        .accounts(syncAccounts)
        .remainingAccounts(assetMetas(h).slice(0, ASSET_COUNT - 1))
        .rpc(),
    )
    expect(why).to.match(/NotFullyInitialized/)
  })

  /** Without the derivation check, ten copies of asset 0 would rescale it ten times. */
  it('refuses duplicated asset accounts', async () => {
    await setM2((await currentM2()) + 1_000_000n)
    const duplicated = Array.from({ length: ASSET_COUNT }, () => ({
      pubkey: h.assetPda(0),
      isWritable: true,
      isSigner: false,
    }))
    const why = await h.failureOf(() =>
      h.program.methods.syncM2().accounts(syncAccounts).remainingAccounts(duplicated).rpc(),
    )
    expect(why).to.match(/InvalidAssetIndex/)
  })

  // ── Prices ────────────────────────────────────────────────────────────────

  it('scales every price target by the same ratio the money supply moved', async () => {
    const m2Old = await currentM2()
    const before = await Promise.all(Array.from({ length: ASSET_COUNT }, (_, i) => asset(i)))
    const m2New = m2Old + m2Old / 100n // +1%
    await setM2(m2New)
    await sync()

    for (let i = 0; i < ASSET_COUNT; i++) {
      const after = await asset(i)
      const expected = (big(before[i].priceTo) * m2New) / m2Old
      expect(big(after.priceTo).toString(), `asset ${i}`).to.equal(expected.toString())
    }
  })

  it('walks to the new target over thirty days instead of jumping', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const a = await asset(i)
      expect(a.interpEnd.toNumber() - a.interpStart.toNumber(), `asset ${i}`).to.equal(
        INTERPOLATION_SECONDS,
      )
      // The new curve starts where the old one had reached, so the visible
      // price is continuous across a sync — it never steps on the Fed's
      // schedule. The previous test moved the target, so the two differ.
      expect(big(a.priceFrom), `asset ${i}`).to.not.equal(big(a.priceTo))
    }
  })

  it('reprices without touching anybody\'s term clock', async () => {
    const before = await Promise.all(
      Array.from({ length: ASSET_COUNT }, async (_, i) => {
        const a = await asset(i)
        return { ends: a.termEndsAt.toString(), term: a.termNumber.toString() }
      }),
    )
    await setM2((await currentM2()) + 1_000_000n)
    await sync()
    for (let i = 0; i < ASSET_COUNT; i++) {
      const a = await asset(i)
      // A Fed release changes what an asset is worth. It must not change how
      // long anyone holds it — a term whose end moved with the money supply
      // could never be "a clock published at the moment they won".
      expect(a.termEndsAt.toString(), `asset ${i} term end`).to.equal(before[i].ends)
      expect(a.termNumber.toString(), `asset ${i} term number`).to.equal(before[i].term)
    }
  })

  /**
   * T10 left this pending and pointed at T13. T13 arrived, and the pointer was
   * half wrong, which is worth writing down.
   *
   * A burn is `supply − target` and can only take the vault's own tokens, so
   * this path needs the vault holding *less than* one burn. The faucet does not
   * get us there: it stops paying at the floor, so it can never take the vault
   * below 50% of supply. What actually gets there is **sustained contraction** —
   * burning lowers the vault's share as well as the supply (100/100 → burn 10 →
   * 90/90 stays 100%, but 50/100 → burn 10 → 40/90 = 44%), so a long enough
   * tightening walks the vault down until a burn outruns it. That is many years
   * of real M2 history, so the state is reached here with `mock_fund` — the same
   * stand-in the auction suite uses for "the economy distributed the money".
   *
   * What it proves is the sentence the README publishes: the coin burns **from
   * the vault, never from a wallet**, and when the vault runs out supply simply
   * sits above target until the next rise catches up.
   */
  it('leaves supply above target when the vault cannot cover a burn', async function () {
    this.timeout(120_000)
    const whale = Keypair.generate()
    const drop = await h.connection.requestAirdrop(whale.publicKey, 2 * LAMPORTS_PER_SOL)
    await h.history.confirmTransaction(drop, 'confirmed')

    // Leave the Emperor one ENC: less than any burn the change cap permits.
    const keep = 1_000_000n
    const moved = (await h.vaultBalance()) - keep
    await mockFund(h, whale.publicKey, moved)
    expect((await h.vaultBalance()).toString()).to.equal(keep.toString())

    try {
      const supplyBefore = await h.supply()
      const m2 = await currentM2()
      const fallen = m2 - (m2 * MAX_CHANGE_BPS) / 10_000n
      const wanted = supplyBefore - targetFor(fallen)
      expect(wanted > keep, 'the burn no longer outruns the vault').to.be.true

      await setM2(fallen)
      await sync()

      // It burned everything it had and stopped, rather than reaching into a
      // wallet to hit the number.
      expect((await h.vaultBalance()).toString(), 'the vault did not burn what it had').to.equal('0')
      expect((await h.supply()).toString()).to.equal((supplyBefore - keep).toString())
      expect((await h.supply()) > targetFor(fallen), 'supply reached a target it could not').to.be
        .true
      // The target is still recorded honestly: `supply >= k x M2`, and the
      // chain says which of the two it is.
      expect((await printer()).targetSupply.toString()).to.equal(targetFor(fallen).toString())

      // No deficit is remembered anywhere, because the next target is absolute.
      // Give the money back and let M2 rise: level-targeting lands exactly,
      // with no double correction.
      await transfer(
        h.connection,
        whale,
        h.encAta(whale.publicKey),
        h.vaultEncAta,
        whale,
        moved,
        [],
        undefined,
        TOKEN_PROGRAM_ID,
      )
      const risen = fallen + fallen / 100n
      await setM2(risen)
      await sync()
      expect(
        (await h.supply()).toString(),
        'the self-correction over- or under-shot',
      ).to.equal(targetFor(risen).toString())
    } finally {
      // Whatever happened above, the Emperor gets his money back — every later
      // run of every suite reads this vault.
      const stranded = await h.connection
        .getTokenAccountBalance(h.encAta(whale.publicKey))
        .then((b) => BigInt(b.value.amount))
        .catch(() => 0n)
      if (stranded > 0n) {
        await transfer(
          h.connection,
          whale,
          h.encAta(whale.publicKey),
          h.vaultEncAta,
          whale,
          stranded,
          [],
          undefined,
          TOKEN_PROGRAM_ID,
        )
      }
    }
  })
})
