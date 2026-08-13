import * as anchor from '@coral-xyz/anchor'
import anchorPkg from '@coral-xyz/anchor'
import { PublicKey } from '@solana/web3.js'
import { TOKEN_2022_PROGRAM_ID, TOKEN_PROGRAM_ID } from '@solana/spl-token'
import { readFileSync } from 'node:fs'
import type { EmperorsNewCoin } from '../idl/emperors_new_coin'

/**
 * Everything the ENC suites share: addresses, account maps, bootstrap, and the
 * two helpers that stop a test passing for the wrong reason.
 *
 * Exists because `initialize` is once-ever, so every suite after T8 needs the
 * same "create it if it isn't there" dance. Copying that four times is how the
 * copies drift apart.
 */

// BN lands in the namespace under CommonJS and on the default export under ESM.
export const BN = (anchorPkg as unknown as { BN?: typeof anchor.BN })?.BN ?? anchor.BN

/** This BN build has no `toBigInt`, and going via Number would lose precision. */
export const big = (n: { toString(): string }): bigint => BigInt(n.toString())

export const SYSTEM = anchor.web3.SystemProgram.programId
export const RENT = anchor.web3.SYSVAR_RENT_PUBKEY
export const ATA_PROGRAM = new PublicKey('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')
export const BPF_LOADER_UPGRADEABLE = new PublicKey('BPFLoaderUpgradeab1e11111111111111111111111')

/** Mirrors GENESIS_M2_VALUE in state.rs: $22,176.1bn at 6dp. */
export const GENESIS_M2 = 22_176_100_000n
export const ASSET_COUNT = 10
/** COPY_BYTES in state.rs. Bytes, not characters. */
export const COPY_BYTES = 280
/** SPIKE_MARKER in state.rs — the only thing the editor's pen can write. */
export const SPIKE_MARKER = '███████ SPIKED ███████'
/** PRICE_INTERPOLATION_SECONDS in state.rs. */
export const INTERPOLATION_SECONDS = 30 * 86_400

/**
 * The tenancy term this ledger runs, in seconds.
 *
 * **Deliberately not `params.genesis.json`'s 30 days.** A term is the clock the
 * auction turns on, so every settlement case — term end, the reserve re-check,
 * the stale-bid release — is unreachable without waiting one out. Twelve
 * seconds is long enough for a bid to land over RPC and short enough that a
 * suite can sit through several.
 *
 * The shipped value stays in `params.genesis.json` and is chosen at T15; what
 * is tested here is the *mechanism*, which does not care how long a term is.
 * `initialize.ts` asserts `Config` carries this number rather than the genesis
 * one, so the substitution is visible rather than silently assumed.
 */
export const TERM_SECONDS = 12

/**
 * The faucet epoch this ledger runs, in seconds.
 *
 * **Deliberately not `params.genesis.json`'s one day.** Every behaviour the
 * faucet has is cross-epoch — a pot divided among *yesterday's* registrants, a
 * second claim refused within one epoch, an epoch old enough to close — so at
 * the shipped length not one acceptance case is reachable without waiting out a
 * real day. Same substitution, and same reasoning, as `TERM_SECONDS`.
 *
 * Fifteen seconds: long enough that six claims land well inside one over local
 * RPC, short enough that a suite can sit through half a dozen.
 */
export const EPOCH_SECONDS = 15

/**
 * Welcome grants per epoch on this ledger, against the shipped 100.
 *
 * The headline bound is "payout during epoch N is at most pot(N−1) plus
 * grants_per_epoch × welcome_grant", so the cap is load-bearing — and at 100 it
 * would take 101 funded wallets to prove. Three takes four.
 */
export const GRANTS_PER_EPOCH = 3

/**
 * How long this ledger must go unsynced before `retire` will fire.
 *
 * The shipped value is a year, for the reason recorded in `params.genesis.json`
 * — the flag is irreversible on a non-upgradeable program. A suite cannot wait
 * one out, and unlike a term or an epoch this clock is **terminal**: once it
 * fires, `sync_m2` refuses on this ledger forever. So `retire.ts` is excluded
 * from the run-everything script and left to `./stack test test-retire`, after
 * which the ledger wants a `./stack reset`.
 *
 * Twenty-five seconds, comfortably longer than the auction's term and the
 * faucet's epoch, so nothing else in the suite can drift into it by accident.
 */
export const RETIREMENT_SILENCE_SECONDS = 25

export interface Harness {
  provider: anchor.AnchorProvider
  program: anchor.Program<EmperorsNewCoin>
  connection: anchor.web3.Connection
  /** A `confirmed` connection: history RPCs refuse the provider's `processed`. */
  history: anchor.web3.Connection
  authority: PublicKey
  params: Params
  configPda: PublicKey
  printerPda: PublicKey
  vaultPda: PublicKey
  mintPda: PublicKey
  mockOraclePda: PublicKey
  programDataPda: PublicKey
  vaultEncAta: PublicKey
  assetPda: (i: number) => PublicKey
  assetMintPda: (i: number) => PublicKey
  escrowPda: PublicKey
  escrowEncAta: PublicKey
  bidPda: (i: number, bidder: PublicKey) => PublicKey
  certPda: (i: number, term: bigint) => PublicKey
  epochPda: (epoch: bigint) => PublicKey
  playerPda: (wallet: PublicKey) => PublicKey
  encAta: (owner: PublicKey) => PublicKey
  vaultAta: (mint: PublicKey, tokenProgram: PublicKey) => PublicKey
  exists: (key: PublicKey) => Promise<boolean>
  /** The **validator's** unix time. Never `Date.now()` — see the comment. */
  chainNow: () => Promise<number>
  failureOf: (run: () => Promise<unknown>) => Promise<string>
  supply: () => Promise<bigint>
  vaultBalance: () => Promise<bigint>
}

/**
 * Read once, at module scope, because `assetSpec` needs it too and two copies
 * of the price ladder is exactly the drift this project keeps stamping out.
 * Resolved from this file rather than the working directory: mocha loads these
 * as ES modules, where `__dirname` does not exist.
 */
const PARAMS = JSON.parse(
  readFileSync(new URL('../params.genesis.json', import.meta.url), 'utf8'),
) as Params

interface Params {
  peg: { k: number }
  vault: { floorBps: number }
  tenancy: { termSeconds: number }
  faucet: {
    epochSeconds: number
    alphaBps: number
    welcomeGrant: number
    grantsPerEpoch: number
  }
  retirement: { silenceSeconds: number }
  sanity: { maxChangeBps: number }
  assets: { count: number; genesisPricePpm: number[] }
}

export function harness(): Harness {
  anchor.setProvider(anchor.AnchorProvider.env())
  const provider = anchor.AnchorProvider.env()
  const program = anchor.workspace.EmperorsNewCoin as anchor.Program<EmperorsNewCoin>
  const connection = provider.connection

  const pda = (seeds: (Buffer | Uint8Array)[]) =>
    PublicKey.findProgramAddressSync(seeds, program.programId)[0]

  const vaultPda = pda([Buffer.from('vault')])
  const mintPda = pda([Buffer.from('mint')])
  const escrowPda = pda([Buffer.from('escrow')])
  const ataFor = (owner: PublicKey, mint: PublicKey, tokenProgram: PublicKey) =>
    PublicKey.findProgramAddressSync(
      [owner.toBuffer(), tokenProgram.toBuffer(), mint.toBuffer()],
      ATA_PROGRAM,
    )[0]
  const vaultAta = (mint: PublicKey, tokenProgram: PublicKey) =>
    ataFor(vaultPda, mint, tokenProgram)
  const encAta = (owner: PublicKey) => ataFor(owner, mintPda, TOKEN_PROGRAM_ID)

  /** Little-endian u64, matching `cert_seeds` and `epoch_seeds` in state.rs. */
  const u64Le = (n: bigint) => {
    const b = Buffer.alloc(8)
    b.writeBigUInt64LE(n)
    return b
  }

  const params = PARAMS

  // History RPCs (`getBlockTime`, `getTransaction`) refuse the provider's
  // `processed` commitment, so everything that reads the past goes through this.
  const history = new anchor.web3.Connection(connection.rpcEndpoint, 'confirmed')

  return {
    provider,
    program,
    connection,
    history,
    authority: provider.wallet.publicKey,
    params,
    configPda: pda([Buffer.from('config')]),
    printerPda: pda([Buffer.from('printer')]),
    vaultPda,
    mintPda,
    mockOraclePda: pda([Buffer.from('mock_oracle')]),
    programDataPda: PublicKey.findProgramAddressSync(
      [program.programId.toBuffer()],
      BPF_LOADER_UPGRADEABLE,
    )[0],
    vaultEncAta: vaultAta(mintPda, TOKEN_PROGRAM_ID),
    assetPda: (i) => pda([Buffer.from('asset'), Buffer.from([i])]),
    assetMintPda: (i) => pda([Buffer.from('asset_mint'), Buffer.from([i])]),
    escrowPda,
    escrowEncAta: ataFor(escrowPda, mintPda, TOKEN_PROGRAM_ID),
    bidPda: (i, bidder) =>
      pda([Buffer.from('bid'), Buffer.from([i]), bidder.toBuffer()]),
    certPda: (i, term) => pda([Buffer.from('cert'), Buffer.from([i]), u64Le(term)]),
    epochPda: (epoch) => pda([Buffer.from('epoch'), u64Le(epoch)]),
    playerPda: (wallet) => pda([Buffer.from('player'), wallet.toBuffer()]),
    encAta,
    vaultAta,
    exists: async (key) => (await connection.getAccountInfo(key)) !== null,

    /**
     * The **validator's** clock, not this machine's.
     *
     * `Clock::get()` is the only clock the program has, and a local validator's
     * unix time drifts behind wall time as slots slip. Deciding which epoch it
     * is from `Date.now()` gets `WrongEpoch` back from a chain that has not
     * caught up — which looks exactly like a program bug and is not one. Cost
     * an hour at T12; the same trap waits in T28.
     */
    chainNow: async () => {
      const slot = await history.getSlot()
      return (await history.getBlockTime(slot)) ?? Math.floor(Date.now() / 1000)
    },

    /**
     * Run something expected to fail and return everything the chain said about
     * why — the Anchor error name, the message, and the program logs.
     *
     * Returning the cause rather than a boolean matters: a test that only
     * asserts "something threw" passes just as happily when the failure is a
     * client-side typo, which is how a security check quietly stops being
     * tested.
     */
    failureOf: async (run) => {
      try {
        await run()
        return ''
      } catch (err) {
        const e = err as {
          error?: { errorCode?: { code?: string } }
          logs?: string[]
          getLogs?: (c: unknown) => Promise<string[]>
        }
        // web3.js leaves `logs` null on a preflight failure and makes you ask.
        const logs = e.logs ?? (await e.getLogs?.(connection).catch(() => [])) ?? []
        return [e.error?.errorCode?.code ?? '', String(err), ...logs].join('\n')
      }
    },

    supply: async () => BigInt((await connection.getTokenSupply(mintPda)).value.amount),
    vaultBalance: async () =>
      BigInt(
        (await connection.getTokenAccountBalance(vaultAta(mintPda, TOKEN_PROGRAM_ID))).value.amount,
      ),
  }
}

/** The genesis parameters as the instruction wants them. */
export function initParams(h: Harness) {
  return {
    // Zeroes until T17 stands the real feed up on devnet. The mock ignores it.
    expectedFeedId: Array(32).fill(0),
    k: new BN(h.params.peg.k),
    faucetAlphaBps: h.params.faucet.alphaBps,
    floorBps: h.params.vault.floorBps,
    welcomeGrant: new BN(h.params.faucet.welcomeGrant),
    // See GRANTS_PER_EPOCH: the shipped 100 would need 101 wallets to prove the
    // cap, and the cap is half of the payout bound.
    grantsPerEpoch: GRANTS_PER_EPOCH,
    // See TERM_SECONDS: the genesis 30 days would make every settlement case
    // untestable, and the mechanism is indifferent to the number.
    termSeconds: new BN(TERM_SECONDS),
    // See EPOCH_SECONDS: at the shipped day, every faucet case would need one.
    epochSeconds: new BN(EPOCH_SECONDS),
    // See RETIREMENT_SILENCE_SECONDS: the shipped year is unwaitable, and this
    // clock is the one whose firing cannot be undone.
    retirementSilenceSeconds: new BN(RETIREMENT_SILENCE_SECONDS),
    maxChangeBps: h.params.sanity.maxChangeBps,
    // The genesis editor. **This ledger's deploy wallet**, which is the only key
    // every suite already has and which survives a re-run — `initialize` is
    // once-ever, so a freshly generated keypair here would leave the pen in the
    // hands of a key that vanished when the process exited.
    //
    // Not in `params.genesis.json`: that file holds economic parameters, chosen
    // by the simulation, and the pen is neither.
    editor: h.authority,
  }
}

/**
 * PLACEHOLDER NAMES, REAL PRICES.
 *
 * The ten slots' names and images are still Jack's call (T31); nothing in the
 * program hardcodes them, so naming them for real costs one bootstrap call
 * rather than a redeploy.
 *
 * The **prices are the shipped ladder**, not a stand-in. T15 chose it as parts
 * per million of the genesis supply — never as a fixed number of tokens, which
 * would be a constant measured against an exponentially growing M2 and is the
 * exact shape T29 had to delete from the sanity caps. `init_asset` takes
 * absolute base units, so the multiplication happens here and at deployment,
 * from the same one number.
 */
export function assetSpec(i: number) {
  const bootstrapSupply = GENESIS_M2 * BigInt(PARAMS.peg.k)
  const price = (bootstrapSupply * BigInt(PARAMS.assets.genesisPricePpm[i])) / 1_000_000n
  return {
    name: `Placeholder Asset ${i}`,
    symbol: `ENCA${i}`,
    uri: `https://badcode.dev/enc/assets/${i}.json`,
    price: new BN(price.toString()),
  }
}

export function initializeAccounts(h: Harness) {
  return {
    authority: h.authority,
    program: h.program.programId,
    programData: h.programDataPda,
    config: h.configPda,
    printer: h.printerPda,
    vault: h.vaultPda,
    mint: h.mintPda,
    vaultTokenAccount: h.vaultEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
    rent: RENT,
  }
}

/**
 * Every account, named. Anchor's resolver cannot derive the asset PDAs (their
 * seeds come from an instruction argument) and will not guess a Token-2022
 * associated-token account.
 */
export function initAssetAccounts(h: Harness, i: number, signer: PublicKey = h.authority) {
  return {
    authority: signer,
    program: h.program.programId,
    programData: h.programDataPda,
    config: h.configPda,
    vault: h.vaultPda,
    asset: h.assetPda(i),
    assetMint: h.assetMintPda(i),
    vaultNftAccount: h.vaultAta(h.assetMintPda(i), TOKEN_2022_PROGRAM_ID),
    tokenProgram: TOKEN_2022_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
    rent: RENT,
  }
}

export interface BootstrapResult {
  /** Signatures for whatever this run actually created. Empty on a warm ledger. */
  created: Map<number, string>
  /** Whether `initialize` ran in this process. */
  initialized: boolean
}

/** Create anything missing. Safe to call against a warm ledger. */
export async function bootstrap(h: Harness): Promise<BootstrapResult> {
  const created = new Map<number, string>()
  let initialized = false

  if (!(await h.exists(h.configPda))) {
    await h.program.methods
      .initialize(initParams(h) as never)
      .accounts(initializeAccounts(h))
      .rpc()
    initialized = true
  }

  for (let i = 0; i < ASSET_COUNT; i++) {
    if (!(await h.exists(h.assetPda(i)))) {
      const spec = assetSpec(i)
      const sig = await h.program.methods
        .initAsset(i, spec.name, spec.symbol, spec.uri, spec.price)
        .accounts(initAssetAccounts(h, i))
        .rpc()
      created.set(i, sig)
    }
  }

  return { created, initialized }
}

/**
 * Set M2 by hand. Mock builds only.
 *
 * Cast because the **committed IDL is the default build's** — the artifact that
 * actually ships — so `set_mock_m2` is absent from the generated types even
 * though the deployed localnet program has it. Committing the mock IDL instead
 * would mean the checked-in interface described a build we never release.
 */
export function setMockM2(h: Harness, m2Value: bigint, releaseDate: number): Promise<string> {
  const methods = h.program.methods as unknown as Record<
    string,
    (...args: unknown[]) => { accounts(a: unknown): { rpc(): Promise<string> } }
  >
  if (typeof methods.setMockM2 !== 'function') {
    throw new Error(
      'This suite needs a mock build. Use `./stack test`, which builds the ENC program with --features mock.',
    )
  }
  return methods
    .setMockM2(new BN(m2Value.toString()), new BN(releaseDate))
    .accounts({ payer: h.authority })
    .rpc()
}

/** Move vault ENC to a wallet. Mock builds only — see `mock_fund.rs`. */
export function mockFund(h: Harness, recipient: PublicKey, amount: bigint): Promise<string> {
  const methods = h.program.methods as unknown as Record<
    string,
    (...args: unknown[]) => { accounts(a: unknown): { rpc(): Promise<string> } }
  >
  if (typeof methods.mockFund !== 'function') {
    throw new Error(
      'This suite needs a mock build. Use `./stack test`, which builds the ENC program with --features mock.',
    )
  }
  return methods
    .mockFund(new BN(amount.toString()))
    .accounts({
      payer: h.authority,
      config: h.configPda,
      recipient,
      vault: h.vaultPda,
      mint: h.mintPda,
      vaultTokenAccount: h.vaultEncAta,
      recipientTokenAccount: h.encAta(recipient),
      tokenProgram: TOKEN_PROGRAM_ID,
      associatedTokenProgram: ATA_PROGRAM,
      systemProgram: SYSTEM,
    })
    .rpc()
}

export function placeBidAccounts(h: Harness, i: number, bidder: PublicKey) {
  return {
    bidder,
    config: h.configPda,
    asset: h.assetPda(i),
    bid: h.bidPda(i, bidder),
    mint: h.mintPda,
    bidderTokenAccount: h.encAta(bidder),
    escrow: h.escrowPda,
    escrowTokenAccount: h.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
  }
}

export function withdrawBidAccounts(h: Harness, i: number, bidder: PublicKey) {
  return {
    bidder,
    config: h.configPda,
    asset: h.assetPda(i),
    bid: h.bidPda(i, bidder),
    mint: h.mintPda,
    bidderTokenAccount: h.encAta(bidder),
    escrow: h.escrowPda,
    escrowTokenAccount: h.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
  }
}

export function settleAccounts(
  h: Harness,
  i: number,
  winner: PublicKey,
  outgoingHolder: PublicKey,
  caller: PublicKey = h.authority,
) {
  return {
    caller,
    config: h.configPda,
    asset: h.assetPda(i),
    winningBid: h.bidPda(i, winner),
    winner,
    outgoingHolder,
    mint: h.mintPda,
    outgoingHolderTokenAccount: h.encAta(outgoingHolder),
    escrow: h.escrowPda,
    escrowTokenAccount: h.escrowEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
  }
}

export function certAccounts(h: Harness, i: number, term: bigint, holder: PublicKey) {
  return {
    payer: h.authority,
    config: h.configPda,
    asset: h.assetPda(i),
    holder,
    vault: h.vaultPda,
    noneAuthority: SYSTEM,
    certMint: h.certPda(i, term),
    holderCertAccount: PublicKey.findProgramAddressSync(
      [holder.toBuffer(), TOKEN_2022_PROGRAM_ID.toBuffer(), h.certPda(i, term).toBuffer()],
      ATA_PROGRAM,
    )[0],
    tokenProgram: TOKEN_2022_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
  }
}

/**
 * `previousEpoch` is Anchor-optional: `null` when that epoch account does not
 * exist (the first epoch anyone claimed in, one nobody claimed in, or one
 * already closed). Passing null costs the caller their own share and nothing
 * else, which is why the program can accept it without a fight.
 */
export function claimAccounts(
  h: Harness,
  claimer: PublicKey,
  epoch: bigint,
  previousEpoch: PublicKey | null,
) {
  return {
    claimer,
    config: h.configPda,
    player: h.playerPda(claimer),
    epochAccount: h.epochPda(epoch),
    previousEpoch,
    mint: h.mintPda,
    vault: h.vaultPda,
    vaultTokenAccount: h.vaultEncAta,
    claimerTokenAccount: h.encAta(claimer),
    tokenProgram: TOKEN_PROGRAM_ID,
    associatedTokenProgram: ATA_PROGRAM,
    systemProgram: SYSTEM,
  }
}

export function closeEpochAccounts(h: Harness, epoch: bigint, closer: PublicKey) {
  return {
    closer,
    config: h.configPda,
    epochAccount: h.epochPda(epoch),
  }
}

export function fileCopyAccounts(h: Harness, i: number, tenant: PublicKey) {
  return { tenant, asset: h.assetPda(i) }
}

export function spikeAccounts(h: Harness, i: number, editor: PublicKey) {
  return { editor, config: h.configPda, asset: h.assetPda(i) }
}

/** Shared by `pass_the_pen` and `break_the_pen` — they need the same two. */
export function penAccounts(h: Harness, editor: PublicKey) {
  return { editor, config: h.configPda }
}

/**
 * The readable part of a column: `copy` is a fixed 280-byte array, zero-padded,
 * and `copyLen` says how much of it is real. Reading to the first zero byte
 * would be a guess — nothing stops a tenant filing a NUL.
 */
export function readCopy(asset: { copy: number[]; copyLen: number }): string {
  return Buffer.from(asset.copy.slice(0, asset.copyLen)).toString('utf8')
}

export function syncAccounts(h: Harness) {
  return {
    config: h.configPda,
    printer: h.printerPda,
    oracle: h.mockOraclePda,
    mint: h.mintPda,
    vault: h.vaultPda,
    vaultTokenAccount: h.vaultEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
  }
}

/** The ten Asset PDAs as writable remaining-accounts, in index order. */
export function assetMetas(h: Harness) {
  return Array.from({ length: ASSET_COUNT }, (_, i) => ({
    pubkey: h.assetPda(i),
    isWritable: true,
    isSigner: false,
  }))
}
