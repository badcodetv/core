import { expect } from 'chai'
import {
  TOKEN_2022_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
  getMint,
  getTokenMetadata,
} from '@solana/spl-token'
import * as anchor from '@coral-xyz/anchor'
import {
  ASSET_COUNT,
  BN,
  GENESIS_M2,
  assetSpec,
  harness,
  initAssetAccounts,
  initParams,
  initializeAccounts,
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
    expect(config.rentRatePerDayBps).to.equal(h.params.rent.ratePerDayBps)
    expect(config.faucetAlphaBps).to.equal(h.params.faucet.alphaBps)
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
      'set_mock_m2', 'setMockM2', // mock builds only; absent from a real one
    ]
    const unexpected = h.program.idl.instructions
      .map((i) => i.name)
      .filter((n) => !allowed.includes(n))
    expect(
      unexpected,
      `new instructions since this test was written — check none mutate Config: ${unexpected.join(', ')}`,
    ).to.be.empty
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

  it('creates exactly ten, all held by the Emperor', async () => {
    const config = await h.program.account.config.fetch(h.configPda)
    expect(config.initializedAssets).to.equal(ASSET_COUNT)
    for (let i = 0; i < ASSET_COUNT; i++) {
      const a = await h.program.account.asset.fetch(h.assetPda(i))
      expect(a.index).to.equal(i)
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

  /** Permanent delegate is what makes the forced sale possible at T12. */
  it('gives the vault permanent delegate over every asset', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const info = await h.connection.getAccountInfo(h.assetMintPda(i))
      expect(info, `asset ${i} mint missing`).to.not.be.null
      // The delegate lives in the mint's extension data; finding the vault key
      // in there is enough to prove the extension was applied.
      expect(
        info!.data.includes(Buffer.from(h.vaultPda.toBytes())),
        `asset ${i} has no permanent delegate`,
      ).to.be.true
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
