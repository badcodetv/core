import * as anchor from '@coral-xyz/anchor'
import anchorPkg from '@coral-xyz/anchor'
// BN is a CommonJS export, so it is not available as a named ESM import.
const { BN } = anchorPkg
import { PublicKey } from '@solana/web3.js'
import {
  TOKEN_2022_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
  getMint,
  getTokenMetadata,
} from '@solana/spl-token'
import { expect } from 'chai'
import { readFileSync } from 'node:fs'
import type { EmperorsNewCoin } from '../idl/emperors_new_coin'

/**
 * Bootstrap: the mint, the vault, the rules, and the ten assets.
 *
 * **Written to be re-runnable against a persistent ledger.** `initialize` is
 * once-ever by construction, so this suite creates what is missing and then
 * asserts the invariants on whatever exists — rather than assuming an empty
 * chain and passing exactly once. Run `./stack reset` if you want a virgin one.
 */
describe('initialize + init_asset', () => {
  anchor.setProvider(anchor.AnchorProvider.env())
  const provider = anchor.AnchorProvider.env()
  const program = anchor.workspace.EmperorsNewCoin as anchor.Program<EmperorsNewCoin>
  const authority = provider.wallet.publicKey
  const connection = provider.connection

  const BPF_LOADER_UPGRADEABLE = new PublicKey('BPFLoaderUpgradeab1e11111111111111111111111')
  const pda = (seeds: (Buffer | Uint8Array)[]) =>
    PublicKey.findProgramAddressSync(seeds, program.programId)[0]

  const configPda = pda([Buffer.from('config')])
  const printerPda = pda([Buffer.from('printer')])
  const vaultPda = pda([Buffer.from('vault')])
  const mintPda = pda([Buffer.from('mint')])
  const assetPda = (i: number) => pda([Buffer.from('asset'), Buffer.from([i])])
  const assetMintPda = (i: number) => pda([Buffer.from('asset_mint'), Buffer.from([i])])
  const [programDataPda] = PublicKey.findProgramAddressSync(
    [program.programId.toBuffer()],
    BPF_LOADER_UPGRADEABLE,
  )

  // The genesis parameters, from the file that is their single source of truth.
  // Placeholders until T15 replaces them; this suite asserts they arrive
  // on-chain intact, not that they are good numbers.
  // Resolved from this file, not from the working directory: mocha runs these
  // as ES modules, where __dirname does not exist.
  const params = JSON.parse(
    readFileSync(new URL('../params.genesis.json', import.meta.url), 'utf8'),
  )
  const K = BigInt(params.peg.k)
  const GENESIS_M2 = 22_176_100_000n // mirrors GENESIS_M2_VALUE in state.rs
  const EXPECTED_SUPPLY = GENESIS_M2 * K

  const initParams = {
    // Zeroes until T17 stands the real feed up on devnet. Nothing reads it yet.
    expectedFeedId: Array(32).fill(0),
    k: new BN(params.peg.k),
    rentRatePerDayBps: params.rent.ratePerDayBps,
    faucetAlphaBps: params.faucet.alphaBps,
    floorBps: params.vault.floorBps,
    welcomeGrant: new BN(params.faucet.welcomeGrant),
    grantsPerEpoch: params.faucet.grantsPerEpoch,
    graceSeconds: new BN(params.rent.graceSeconds),
    forecloseBounty: new BN(params.rent.forecloseBounty),
    maxChangeBps: params.sanity.maxChangeBps,
    maxSingleMint: new BN(params.sanity.maxSingleMint),
  }

  // PLACEHOLDER NAMES. The ten parody assets are a creative decision that has
  // not been made yet — see docs/stories/magic-money-tree/. Nothing in the
  // program hardcodes them: they are instruction arguments, so naming them for
  // real later costs one bootstrap call, not a redeploy.
  const asset = (i: number) => ({
    name: `Placeholder Asset ${i}`,
    symbol: `ENCA${i}`,
    uri: `https://badcode.dev/enc/assets/${i}.json`,
    price: new BN(1_000_000_000_000).muln(i + 1),
  })

  const vaultAta = (mint: PublicKey, tokenProgram: PublicKey) =>
    PublicKey.findProgramAddressSync(
      [vaultPda.toBuffer(), tokenProgram.toBuffer(), mint.toBuffer()],
      new PublicKey('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL'),
    )[0]

  const exists = async (key: PublicKey) => (await connection.getAccountInfo(key)) !== null

  /**
   * Run something expected to fail and return everything the chain said about
   * why — the Anchor error name if there is one, otherwise the message plus the
   * program logs.
   *
   * Returning the *cause* rather than a boolean matters: a test that only
   * asserts "something threw" passes just as happily when the failure is a
   * client-side typo, which is exactly how a security check quietly stops being
   * tested.
   */
  const failureOf = async (run: () => Promise<unknown>): Promise<string> => {
    try {
      await run()
      return ''
    } catch (err) {
      const e = err as {
        error?: { errorCode?: { code?: string } }
        logs?: string[]
        getLogs?: (c: unknown) => Promise<string[]>
      }
      // web3.js leaves `logs` null on a preflight failure and makes you ask for
      // them, so the reason the transaction was rejected is only one await away
      // — but it is not in the string form of the error.
      const logs = e.logs ?? (await e.getLogs?.(connection).catch(() => [])) ?? []
      return [e.error?.errorCode?.code ?? '', String(err), ...logs].join('\n')
    }
  }

  // getSignaturesForAddress and getTransaction refuse the provider's default
  // `processed` commitment, so history needs its own connection.
  const history = new anchor.web3.Connection(connection.rpcEndpoint, 'confirmed')

  const SYSTEM = anchor.web3.SystemProgram.programId
  const RENT = anchor.web3.SYSVAR_RENT_PUBKEY
  const ATA_PROGRAM = new PublicKey('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')

  // Every account, named. Anchor's resolver cannot derive the asset PDAs (their
  // seeds come from an instruction argument) and will not guess a Token-2022
  // associated-token account, so nothing here is left to inference.
  const initializeAccounts = {
    authority,
    program: program.programId,
    programData: programDataPda,
    config: configPda,
    printer: printerPda,
    vault: vaultPda,
    mint: mintPda,
    vaultTokenAccount: vaultAta(mintPda, TOKEN_PROGRAM_ID),
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
    rent: RENT,
  }

  const initAssetAccounts = (i: number, signer: PublicKey = authority) => ({
    authority: signer,
    program: program.programId,
    programData: programDataPda,
    config: configPda,
    vault: vaultPda,
    asset: assetPda(i),
    assetMint: assetMintPda(i),
    vaultNftAccount: vaultAta(assetMintPda(i), TOKEN_2022_PROGRAM_ID),
    tokenProgram: TOKEN_2022_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
    rent: RENT,
  })

  // Signatures of the assets this run actually created, so the compute-unit
  // test can inspect a transaction it knows exists.
  const created = new Map<number, string>()

  /**
   * What a stranger got when they tried to bootstrap, attempted *before* the
   * asset exists.
   *
   * The timing is the point. Anchor evaluates `init` during account
   * construction but bare `constraint =` expressions only afterwards, so
   * attempting an index that already exists fails with "account already in
   * use" and never reaches the authority check at all. The transaction is
   * atomic either way, so the gate holds — but a test aimed at an existing
   * index proves nothing about it.
   */
  let strangerFailure: string | null = null

  before(async function () {
    this.timeout(300_000)
    if (!(await exists(configPda))) {
      await program.methods
        .initialize(initParams as never)
        .accounts(initializeAccounts)
        .rpc()
    }
    for (let i = 0; i < 10; i++) {
      if (!(await exists(assetPda(i)))) {
        if (strangerFailure === null) {
          const stranger = anchor.web3.Keypair.generate()
          const drop = await connection.requestAirdrop(stranger.publicKey, 1e9)
          await connection.confirmTransaction(drop)
          const a0 = asset(i)
          strangerFailure = await failureOf(() =>
            program.methods
              .initAsset(i, a0.name, a0.symbol, a0.uri, a0.price)
              .accounts(initAssetAccounts(i, stranger.publicKey))
              .signers([stranger])
              .rpc(),
          )
        }
        const a = asset(i)
        const sig = await program.methods
          .initAsset(i, a.name, a.symbol, a.uri, a.price)
          .accounts(initAssetAccounts(i))
          .rpc()
        created.set(i, sig)
      }
    }
  })

  // ── The rules ─────────────────────────────────────────────────────────────

  it('records the genesis parameters exactly as given', async () => {
    const config = await program.account.config.fetch(configPda)
    expect(config.k.toString()).to.equal(params.peg.k.toString())
    expect(config.encDecimals).to.equal(6)
    expect(config.floorBps).to.equal(params.vault.floorBps)
    expect(config.rentRatePerDayBps).to.equal(params.rent.ratePerDayBps)
    expect(config.faucetAlphaBps).to.equal(params.faucet.alphaBps)
    expect(config.maxChangeBps).to.equal(params.sanity.maxChangeBps)
    expect(config.mint.toBase58()).to.equal(mintPda.toBase58())
    expect(config.vault.toBase58()).to.equal(vaultPda.toBase58())
  })

  it('is callable exactly once', async () => {
    let threw = false
    try {
      await program.methods
        .initialize(initParams as never)
        .accounts(initializeAccounts)
        .rpc()
    } catch {
      threw = true
    }
    expect(threw, 'initialize ran a second time — the parameters are not immutable').to.be.true
  })

  /**
   * The parameters are meant to be unchangeable, and the way to be sure is that
   * no instruction to change them exists at all — not that one exists and is
   * gated. This asserts the shape of the program, not its behaviour.
   */
  it('exposes no instruction that could rewrite the rules', () => {
    // An allowlist rather than a pattern: every new instruction has to be added
    // here deliberately, which is the moment to ask whether it touches Config.
    // (A regex is worse than useless — /set/ matches "initAsset".)
    const allowed = ['initialize', 'init_asset', 'initAsset']
    const unexpected = program.idl.instructions
      .map((i) => i.name)
      .filter((n) => !allowed.includes(n))
    expect(
      unexpected,
      `new instructions since this test was written — check none of them mutate Config: ${unexpected.join(', ')}`,
    ).to.be.empty
  })

  /** Only the upgrade authority may bootstrap, so nobody can front-run us. */
  it('refuses a stranger', function () {
    if (strangerFailure === null) {
      // Nothing was created this run, so the attempt could not be made against
      // a fresh account and would have failed for the wrong reason.
      this.skip()
    }
    expect(strangerFailure, 'a stranger was allowed to bootstrap the coin').to.match(
      /NotUpgradeAuthority|upgrade authority/i,
    )
  })

  // ── The money ─────────────────────────────────────────────────────────────

  it('creates ENC with six decimals and NO freeze authority', async () => {
    const mint = await getMint(connection, mintPda, undefined, TOKEN_PROGRAM_ID)
    expect(mint.decimals).to.equal(6)
    // Not optional: a freeze authority is a live BadCode key over other
    // people's coins, and it can only be removed by never having set it.
    expect(mint.freezeAuthority, 'ENC has a freeze authority').to.be.null
    // The mint authority stays forever, and stays a PDA. Scanners will flag
    // ENC as arbitrarily inflatable — correctly, and that is the joke.
    expect(mint.mintAuthority?.toBase58()).to.equal(vaultPda.toBase58())
  })

  it('puts 100% of the genesis supply in the vault', async () => {
    const mint = await getMint(connection, mintPda, undefined, TOKEN_PROGRAM_ID)
    const vault = await connection.getTokenAccountBalance(vaultAta(mintPda, TOKEN_PROGRAM_ID))
    expect(mint.supply.toString()).to.equal(EXPECTED_SUPPLY.toString())
    // BadCode takes no allocation. Before the faucet runs there is nobody else.
    expect(vault.value.amount).to.equal(mint.supply.toString())
  })

  it('records the genesis target and a release date the first sync can beat', async () => {
    const printer = await program.account.printer.fetch(printerPda)
    expect(printer.m2Value.toString()).to.equal(GENESIS_M2.toString())
    expect(printer.targetSupply.toString()).to.equal(EXPECTED_SUPPLY.toString())
    // Zero, so any real Fed release strictly advances it.
    expect(printer.m2ReleaseDate.toNumber()).to.equal(0)
  })

  // ── The assets ────────────────────────────────────────────────────────────

  it('creates exactly ten, all held by the Emperor', async () => {
    const config = await program.account.config.fetch(configPda)
    expect(config.initializedAssets).to.equal(10)
    for (let i = 0; i < 10; i++) {
      const a = await program.account.asset.fetch(assetPda(i))
      expect(a.index).to.equal(i)
      expect(a.holder.toBase58(), `asset ${i} is not in the vault`).to.equal(vaultPda.toBase58())
      expect(a.priceFrom.toString()).to.equal(a.priceTo.toString())
    }
  })

  it('mints each as a true NFT: supply 1, no mint authority', async () => {
    for (let i = 0; i < 10; i++) {
      const mint = await getMint(connection, assetMintPda(i), undefined, TOKEN_2022_PROGRAM_ID)
      expect(mint.decimals, `asset ${i}`).to.equal(0)
      expect(mint.supply.toString(), `asset ${i}`).to.equal('1')
      // Dropped after minting the single unit, so no more can ever exist.
      expect(mint.mintAuthority, `asset ${i} can still be minted`).to.be.null
      const held = await connection.getTokenAccountBalance(
        vaultAta(assetMintPda(i), TOKEN_2022_PROGRAM_ID),
      )
      expect(held.value.amount, `asset ${i}`).to.equal('1')
    }
  })

  it('carries metadata a wallet can render', async () => {
    for (let i = 0; i < 10; i++) {
      const meta = await getTokenMetadata(connection, assetMintPda(i), undefined, TOKEN_2022_PROGRAM_ID)
      expect(meta, `asset ${i} has no metadata`).to.not.be.null
      expect(meta!.name).to.equal(asset(i).name)
      expect(meta!.uri).to.equal(asset(i).uri)
    }
  })

  /** Permanent delegate is what makes the forced sale possible at T12. */
  it('gives the vault permanent delegate over every asset', async () => {
    for (let i = 0; i < 10; i++) {
      const info = await connection.getAccountInfo(assetMintPda(i))
      expect(info, `asset ${i} mint missing`).to.not.be.null
      // The delegate is stored in the mint's extension data; finding the vault
      // key in there is enough to prove the extension was applied.
      const hasVault = info!.data.includes(Buffer.from(vaultPda.toBytes()))
      expect(hasVault, `asset ${i} has no permanent delegate`).to.be.true
    }
  })

  it('refuses an eleventh asset, and a repeat of an existing one', async () => {
    for (const index of [10, 255, 0]) {
      const why = await failureOf(() =>
        program.methods
          .initAsset(index, 'x', 'x', 'x', new BN(1))
          .accounts(initAssetAccounts(index))
          .rpc(),
      )
      expect(why, `init_asset(${index}) was allowed`).to.not.equal('')
    }
  })

  /**
   * The reason `initialize` and `init_asset` are separate instructions: all ten
   * assets in one call is roughly forty accounts, past both the compute and the
   * transaction-size limits.
   */
  it('fits one asset in one transaction, well under the compute limit', async function () {
    // Only measurable when this run created it. solana-test-validator does not
    // index getSignaturesForAddress for these accounts, so on a warm ledger
    // there is nothing to look up — skip rather than pretend.
    const sig = created.get(9)
    if (sig === undefined) this.skip()
    // No confirmTransaction here: `.rpc()` already confirmed the one we sent,
    // and a signature recovered from history is confirmed by definition — but
    // its blockhash has long expired, so confirming it again blocks for the
    // full 30-second timeout and then fails.
    const tx = await history.getTransaction(sig, {
      maxSupportedTransactionVersion: 0,
    })
    const consumed = (tx?.meta?.logMessages ?? [])
      .map((l) => /consumed (\d+) of (\d+) compute units/.exec(l))
      .find(Boolean)
    expect(consumed, 'no compute-unit log found').to.not.be.undefined
    const used = Number(consumed![1])
    expect(used, `init_asset used ${used} CU`).to.be.lessThan(200_000)
  })
})
