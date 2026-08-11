import { expect } from 'chai'
import { TOKEN_PROGRAM_ID } from '@solana/spl-token'
import {
  ASSET_COUNT,
  GENESIS_M2,
  INTERPOLATION_SECONDS,
  assetMetas,
  big,
  bootstrap,
  harness,
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

  it('refuses a move larger than the sanity cap', async () => {
    const m2 = await currentM2()
    const beyond = m2 + (m2 * (MAX_CHANGE_BPS + 100n)) / 10_000n
    await setM2(beyond)
    expect(await h.failureOf(sync)).to.match(/ChangeTooLarge/)
  })

  it('refuses a mint larger than the per-sync cap even inside the change cap', async () => {
    // Exactly at the change cap, which at this supply is still a bigger mint
    // than max_single_mint allows — the second guard exists for precisely the
    // window the first one lets through.
    const m2 = await currentM2()
    const atCap = m2 + (m2 * MAX_CHANGE_BPS) / 10_000n
    const mintSize = targetFor(atCap) - (await h.supply())
    expect(
      mintSize > BigInt(h.params.sanity.maxSingleMint),
      `the placeholder params no longer put this case between the two caps (mint would be ${mintSize})`,
    ).to.be.true
    await setM2(atCap)
    expect(await h.failureOf(sync)).to.match(/MintTooLarge/)
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

  it('banks the rent clock on every asset', async () => {
    await setM2((await currentM2()) + 1_000_000n)
    const at = Math.floor(Date.now() / 1000)
    await sync()
    for (let i = 0; i < ASSET_COUNT; i++) {
      const a = await asset(i)
      // Rent owed is banked under the OLD curve and the clock restarted —
      // otherwise every unpaid day would be silently recomputed at the new
      // prices, charging people for a past that did not happen.
      expect(Math.abs(a.lastTouched.toNumber() - at), `asset ${i}`).to.be.lessThan(120)
    }
  })

  /**
   * The one acceptance case this suite cannot reach yet.
   *
   * A burn is `supply - target`, and the vault holds every token until
   * something moves them out. Nothing does until the faucet lands at T13, so
   * `supply - target <= vault balance` always holds here and the uncovered-burn
   * path is unreachable. The arithmetic is covered by the Rust unit tests
   * (`supply_move`, plus the `min` in the handler); the on-chain case is
   * enabled at T13.
   */
  it('leaves supply above target when the vault cannot cover a burn')
})
