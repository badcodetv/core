import { expect } from 'chai'
import {
  TOKEN_2022_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
  getMint,
  getPermanentDelegate,
  getTokenMetadata,
} from '@solana/spl-token'
import * as anchor from '@coral-xyz/anchor'
import { readFileSync } from 'node:fs'
import {
  ASSET_COUNT,
  BN,
  GENESIS_M2,
  assetSpec,
  harness,
  initAssetAccounts,
  initParams,
  initializeAccounts,
  TERM_SECONDS,
  EPOCH_SECONDS,
  GRANTS_PER_EPOCH,
} from './enc-harness.js'

/**
 * Bootstrap: the mint, the vault, the rules, and the ten assets.
 *
 * **Written to be re-runnable against a persistent ledger.** `initialize` is
 * once-ever by construction, so this suite creates what is missing and then
 * asserts the invariants on whatever exists. Several tests can only be
 * meaningful on a fresh chain and mark themselves pending otherwise, rather
 * than passing for the wrong reason — `./stack reset` if you want them to run.
 */
describe('initialize + init_asset', () => {
  const h = harness()
  const K = BigInt(h.params.peg.k)
  const EXPECTED_SUPPLY = GENESIS_M2 * K

  const created = new Map<number, string>()

  /**
   * What a stranger got when they tried to bootstrap, attempted *before* the
   * asset existed.
   *
   * The timing is the point. Anchor evaluates `init` during account
   * construction but bare `constraint =` expressions only afterwards, so
   * attempting an index that already exists fails with "account already in use"
   * and never reaches the authority check. The transaction is atomic either
   * way, so the gate holds — but a test aimed at an existing index proves
   * nothing about it.
   */
  let strangerFailure: string | null = null

  before(async function () {
    this.timeout(300_000)

    if (!(await h.exists(h.configPda))) {
      await h.program.methods
        .initialize(initParams(h) as never)
        .accounts(initializeAccounts(h))
        .rpc()
    }

    for (let i = 0; i < ASSET_COUNT; i++) {
      if (await h.exists(h.assetPda(i))) continue
      const spec = assetSpec(i)

      if (strangerFailure === null) {
        const stranger = anchor.web3.Keypair.generate()
        const drop = await h.connection.requestAirdrop(stranger.publicKey, 1e9)
        await h.connection.confirmTransaction(drop)
        strangerFailure = await h.failureOf(() =>
          h.program.methods
            .initAsset(i, spec.name, spec.symbol, spec.uri, spec.price)
            .accounts(initAssetAccounts(h, i, stranger.publicKey))
            .signers([stranger])
            .rpc(),
        )
      }

      created.set(
        i,
        await h.program.methods
          .initAsset(i, spec.name, spec.symbol, spec.uri, spec.price)
          .accounts(initAssetAccounts(h, i))
          .rpc(),
      )
    }
  })

  // ── The rules ─────────────────────────────────────────────────────────────

  it('records the genesis parameters exactly as given', async () => {
    const config = await h.program.account.config.fetch(h.configPda)
    expect(config.k.toString()).to.equal(String(h.params.peg.k))
    expect(config.encDecimals).to.equal(6)
    expect(config.floorBps).to.equal(h.params.vault.floorBps)
    expect(config.faucetAlphaBps).to.equal(h.params.faucet.alphaBps)
    // Not the genesis 30 days: this ledger runs short terms so the auction's
    // settlement paths are reachable at all. See TERM_SECONDS.
    expect(Number(config.termSeconds)).to.equal(TERM_SECONDS)
    // Same substitution, same reasoning: at the shipped one-day epoch not one
    // faucet case is reachable. Asserted rather than assumed, so the swap is
    // visible in the record.
    expect(Number(config.epochSeconds)).to.equal(EPOCH_SECONDS)
    expect(config.grantsPerEpoch).to.equal(GRANTS_PER_EPOCH)
    expect(config.welcomeGrant.toString()).to.equal(String(h.params.faucet.welcomeGrant))
    expect(config.maxChangeBps).to.equal(h.params.sanity.maxChangeBps)
    expect(config.mint.toBase58()).to.equal(h.mintPda.toBase58())
    expect(config.vault.toBase58()).to.equal(h.vaultPda.toBase58())
  })

  it('is callable exactly once', async () => {
    const why = await h.failureOf(() =>
      h.program.methods
        .initialize(initParams(h) as never)
        .accounts(initializeAccounts(h))
        .rpc(),
    )
    expect(why, 'initialize ran a second time — the parameters are not immutable').to.not.equal('')
  })

  /**
   * The parameters are meant to be unchangeable, and the way to be sure is that
   * no instruction to change them exists — not that one exists and is gated.
   * This asserts the shape of the program, not its behaviour.
   */
  it('exposes no instruction that could rewrite the rules', () => {
    // An allowlist rather than a pattern: every new instruction has to be added
    // here deliberately, which is the moment to ask whether it touches Config.
    // (A regex is worse than useless — /set/ matches "initAsset".)
    const allowed = [
      'initialize', 'init_asset', 'initAsset',
      'sync_m2', 'syncM2',
      'place_bid', 'placeBid',
      'withdraw_bid', 'withdrawBid',
      'settle_auction', 'settleAuction',
      'roll_term', 'rollTerm',
      'mint_certificate', 'mintCertificate',
      'claim',
      'close_epoch', 'closeEpoch',
      // Mock builds only; absent from a real one, which the test below proves.
      'set_mock_m2', 'setMockM2',
      'mock_fund', 'mockFund',
    ]
    const unexpected = h.program.idl.instructions
      .map((i) => i.name)
      .filter((n) => !allowed.includes(n))
    expect(
      unexpected,
      `new instructions since this test was written — check none mutate Config: ${unexpected.join(', ')}`,
    ).to.be.empty
  })

  /**
   * Ruling A (2026-08-12) removed every holding cost, and the removal has to be
   * provable rather than merely untested. The allowlist above only catches
   * instructions being *added*; this catches them coming back.
   *
   * It matters beyond tidiness: both instructions existed to move ENC out of a
   * holder's wallet without their signature, which is the one power the design
   * now claims it does not have. The claim is checkable, so check it.
   */
  it('has no rent or foreclosure instruction, and no rent parameters', () => {
    const names = h.program.idl.instructions.map((i) => i.name)
    for (const gone of ['settle_rent', 'settleRent', 'foreclose']) {
      expect(names, `${gone} is back in the IDL`).to.not.include(gone)
    }
    // The parameters go too — a Config field with no instruction behind it is
    // a rule the coin cannot enforce and a sentence the README would owe.
    const fields = JSON.stringify(h.program.idl.accounts ?? []) + JSON.stringify(h.program.idl.types ?? [])
    for (const gone of ['rentRatePerDayBps', 'rent_rate_per_day_bps', 'graceSeconds', 'grace_seconds', 'forecloseBounty', 'foreclose_bounty', 'rentAccrued', 'rent_accrued']) {
      expect(fields, `${gone} is still in the published interface`).to.not.include(gone)
    }
  })

  /**
   * The mock instructions are a compile-time choice, not a gated one.
   *
   * `set_mock_m2` could set the money supply by hand and `mock_fund` could move
   * vault ENC to a chosen wallet — either would be fatal to the coin's only
   * real claim, which is that its supply is not ours to choose.
   *
   * **Reads the committed file on purpose.** `h.program.idl` is whatever
   * `anchor build` last wrote into `target/`, which under `./stack test` is a
   * *mock* build — so asserting against it would test the wrong artifact and
   * fail for the right-looking wrong reason. `chain/idl/` is what ships, and
   * only a default build publishes there.
   */
  it('ships an interface with no mock instruction in it', () => {
    const shipped = JSON.parse(
      readFileSync(new URL('../idl/emperors_new_coin.json', import.meta.url), 'utf8'),
    ) as { instructions: { name: string }[] }
    const names = shipped.instructions.map((i) => i.name)
    expect(names, 'the shipped IDL is empty — run `./stack build`').to.not.be.empty
    for (const gone of ['set_mock_m2', 'setMockM2', 'mock_fund', 'mockFund']) {
      expect(names, `${gone} is in the SHIPPED IDL — a default build must not carry it`).to.not.include(
        gone,
      )
    }
  })

  /** Only the upgrade authority may bootstrap, so nobody can front-run us. */
  it('refuses a stranger', function () {
    if (strangerFailure === null) this.skip()
    expect(strangerFailure, 'a stranger was allowed to bootstrap the coin').to.match(
      /NotUpgradeAuthority|upgrade authority/i,
    )
  })

  // ── The money ─────────────────────────────────────────────────────────────

  it('creates ENC with six decimals and NO freeze authority', async () => {
    const mint = await getMint(h.connection, h.mintPda, undefined, TOKEN_PROGRAM_ID)
    expect(mint.decimals).to.equal(6)
    // Not optional: a freeze authority is a live BadCode key over other
    // people's coins, and it can only be removed by never having set it.
    expect(mint.freezeAuthority, 'ENC has a freeze authority').to.be.null
    // The mint authority stays forever, and stays a PDA. Scanners will flag ENC
    // as arbitrarily inflatable — correctly, and that is the joke.
    expect(mint.mintAuthority?.toBase58()).to.equal(h.vaultPda.toBase58())
  })

  it('puts 100% of the genesis supply in the vault', async function () {
    // Only true before anything moves tokens: sync_m2 retargets the supply, and
    // the faucet will start paying it away at T13.
    const printer = await h.program.account.printer.fetch(h.printerPda)
    if (printer.m2ReleaseDate.toNumber() !== 0) this.skip()
    expect((await h.supply()).toString()).to.equal(EXPECTED_SUPPLY.toString())
    // BadCode takes no allocation. At genesis there is nobody else.
    expect((await h.vaultBalance()).toString()).to.equal((await h.supply()).toString())
  })

  it('records a genesis release date the first sync can beat', async function () {
    const printer = await h.program.account.printer.fetch(h.printerPda)
    if (printer.m2ReleaseDate.toNumber() !== 0) this.skip()
    expect(printer.m2Value.toString()).to.equal(GENESIS_M2.toString())
    expect(printer.targetSupply.toString()).to.equal(EXPECTED_SUPPLY.toString())
  })

  // ── The assets ────────────────────────────────────────────────────────────

  it('creates exactly ten, all held by the Emperor', async function () {
    const config = await h.program.account.config.fetch(h.configPda)
    expect(config.initializedAssets).to.equal(ASSET_COUNT)

    const assets = await Promise.all(
      Array.from({ length: ASSET_COUNT }, (_, i) => h.program.account.asset.fetch(h.assetPda(i))),
    )
    assets.forEach((a, i) => expect(a.index).to.equal(i))

    // "All held by the Emperor" is a statement about *genesis*, and the whole
    // point of the auction is to stop it being true. On a ledger the auction
    // suite has already played, skip rather than assert something the design
    // deliberately falsifies — `./stack reset` if you want this to run.
    if (assets.some((a) => a.holder.toBase58() !== h.vaultPda.toBase58())) this.skip()
    for (const [i, a] of assets.entries()) {
      expect(a.holder.toBase58(), `asset ${i} is not in the vault`).to.equal(h.vaultPda.toBase58())
    }
  })

  it('mints each as a true NFT: supply 1, no mint authority', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const mint = await getMint(h.connection, h.assetMintPda(i), undefined, TOKEN_2022_PROGRAM_ID)
      expect(mint.decimals, `asset ${i}`).to.equal(0)
      expect(mint.supply.toString(), `asset ${i}`).to.equal('1')
      // Dropped after minting the single unit, so no more can ever exist.
      expect(mint.mintAuthority, `asset ${i} can still be minted`).to.be.null
      const held = await h.connection.getTokenAccountBalance(
        h.vaultAta(h.assetMintPda(i), TOKEN_2022_PROGRAM_ID),
      )
      expect(held.value.amount, `asset ${i}`).to.equal('1')
    }
  })

  it('carries metadata a wallet can render', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const meta = await getTokenMetadata(
        h.connection,
        h.assetMintPda(i),
        undefined,
        TOKEN_2022_PROGRAM_ID,
      )
      expect(meta, `asset ${i} has no metadata`).to.not.be.null
      expect(meta!.name).to.equal(assetSpec(i).name)
      expect(meta!.uri).to.equal(assetSpec(i).uri)
    }
  })

  /**
   * The opposite of what T8 asserted, and deliberately so.
   *
   * The permanent delegate existed to make a forced sale possible. Ruling A
   * (2026-08-12) removed the forced sale, and the ten NFTs now never leave the
   * program's custody — so the power would have been dead weight while costing
   * the heaviest flag a risk scanner issues. Its absence is what makes "no
   * token leaves any wallet without its owner's signature" structural.
   */
  it('gives nobody permanent delegate over any asset', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const mint = await getMint(h.connection, h.assetMintPda(i), undefined, TOKEN_2022_PROGRAM_ID)
      expect(getPermanentDelegate(mint), `asset ${i} has a permanent delegate`).to.be.null
    }
  })

  it('refuses an eleventh asset, and a repeat of an existing one', async () => {
    for (const index of [10, 255, 0]) {
      const why = await h.failureOf(() =>
        h.program.methods
          .initAsset(index, 'x', 'x', 'x', new BN(1))
          .accounts(initAssetAccounts(h, index))
          .rpc(),
      )
      expect(why, `init_asset(${index}) was allowed`).to.not.equal('')
    }
  })

  /**
   * The reason `initialize` and `init_asset` are separate: all ten assets in one
   * call is roughly forty accounts, past both the compute and transaction-size
   * limits.
   */
  it('fits one asset in one transaction, well under the compute limit', async function () {
    // Only measurable when this run created it. solana-test-validator does not
    // index getSignaturesForAddress for these accounts, so on a warm ledger
    // there is nothing to look up — skip rather than pretend.
    const sig = created.get(ASSET_COUNT - 1)
    if (sig === undefined) this.skip()
    const tx = await h.history.getTransaction(sig, { maxSupportedTransactionVersion: 0 })
    const consumed = (tx?.meta?.logMessages ?? [])
      .map((l) => /consumed (\d+) of (\d+) compute units/.exec(l))
      .find(Boolean)
    expect(consumed, 'no compute-unit log found').to.not.be.undefined
    const used = Number(consumed![1])
    expect(used, `init_asset used ${used} CU`).to.be.lessThan(200_000)
  })
})
