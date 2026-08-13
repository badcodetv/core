import {
  ASSET_COUNT,
  ENC_IDL,
  ENC_PROGRAM_ID,
  type EmperorsNewCoin,
  type EncBid,
  type EncPlayer,
  associatedTokenAddress,
  claimAccounts,
  decodeTokenAmount,
  encDecoders,
  encErrorMessage,
  fileCopyAccounts,
  mintCertificateAccounts,
  placeBidAccounts,
  rollTermAccounts,
  settleAuctionAccounts,
  withdrawBidAccounts,
} from '@badcode/enc'
import { humanizeError, useAccount, useProgram, useSendTransaction } from '@badcode/chain-react'
import { BN } from '@coral-xyz/anchor'
import { useWallet } from '@solana/wallet-adapter-react'
import { PublicKey } from '@solana/web3.js'
import { useCallback, useMemo, useState } from 'react'
import { useAccountList } from './useEncChain'
import type { EncChainState } from './useEncChain'

/**
 * The half of the page that needs a signature.
 *
 * Everything here is additive to `useEncChain`, which keeps working with no
 * wallet connected — that separation is the point of T19 and this file does not
 * get to undo it. When nothing is connected, every list below is empty, every
 * sender throws before it builds anything, and the page falls back to being a
 * document.
 *
 * **No `BN` reaches a component.** Anchor types every `u64` as `any`, so a `BN`
 * passed where a `bigint` is expected typechecks, builds, and throws "Cannot
 * mix BigInt and other types" in the browser. Accounts are decoded through
 * `@badcode/enc`, which converts at one boundary; instruction *arguments* go the
 * other way and are converted here, on the way out, in `bn()`.
 */

/**
 * `bigint` → the `BN` Anchor wants for a `u64` argument.
 *
 * Via the decimal string, exactly as `@badcode/enc` converts the other way:
 * this BN build has neither `toBigInt` nor `fromBigInt`, and going through
 * `Number` would lose precision on quantities that passed 2^53 years ago.
 *
 * `BN` comes from Anchor's own export rather than the `bn.js` package, so there
 * is one copy of the class in the bundle. Two is a real failure mode — the
 * coder's `instanceof` checks reject the stranger's.
 */
function bn(value: bigint): BN {
  return new BN(value.toString())
}

/** What just happened, so the page can say so and link to it. */
export interface ActionResult {
  kind: 'sent' | 'failed'
  /** Which button this was, for placing the message next to it. */
  action: string
  signature?: string
  message?: string
}

export interface EncActions {
  wallet: PublicKey | null
  /** The connected wallet's ENC, in base units. Zero when it has no account. */
  balance: bigint
  /** Null before this wallet's first ever claim. */
  player: EncPlayer | null
  /** This wallet's escrowed bid on each slot, by index. */
  bids: (EncBid | null)[]
  /** Whether the running term's certificate has already been minted, by index. */
  certificates: boolean[]
  pending: boolean
  /** The last thing that happened, successful or not. */
  result: ActionResult | null
  dismiss: () => void
  claim: () => Promise<void>
  placeBid: (index: number, amount: bigint) => Promise<void>
  withdrawBid: (index: number) => Promise<void>
  settleAuction: (index: number, winner: PublicKey, outgoingHolder: PublicKey) => Promise<void>
  rollTerm: (index: number) => Promise<void>
  mintCertificate: (index: number, term: bigint, holder: PublicKey) => Promise<void>
  fileCopy: (index: number, text: string) => Promise<void>
}

export function useEncActions(state: EncChainState): EncActions {
  const { publicKey } = useWallet()
  const program = useProgram<EmperorsNewCoin>(ENC_IDL, ENC_PROGRAM_ID)
  const { send, pending } = useSendTransaction()
  const [result, setResult] = useState<ActionResult | null>(null)
  const { addresses, assets, epochIndex } = state

  const reader = useMemo(() => (program ? encDecoders(program) : null), [program])

  // ── What the chain says about this wallet ─────────────────────────────────

  const encAta = useMemo(
    () => (publicKey ? associatedTokenAddress(publicKey, addresses.mint) : null),
    [addresses, publicKey],
  )
  const balance = useAccount(encAta, decodeTokenAmount)
  const playerPda = useMemo(
    () => (publicKey ? addresses.player(publicKey) : null),
    [addresses, publicKey],
  )
  const player = useAccount(playerPda, (data) => {
    if (!reader) throw new Error('no decoder yet')
    return reader.player(data)
  })

  // One bid account per slot. The addresses move with the wallet, so this is a
  // list rather than ten fixed subscriptions.
  const bidPdas = useMemo(
    () =>
      publicKey
        ? Array.from({ length: ASSET_COUNT }, (_, i) => addresses.bid(i, publicKey))
        : [],
    [addresses, publicKey],
  )
  const bids = useAccountList(bidPdas, (data) => {
    if (!reader) throw new Error('no decoder yet')
    return reader.bid(data)
  })

  // And one certificate mint per slot, at the term each slot is *currently*
  // running. Seeds are (asset, term), so a term issues exactly one ever — which
  // makes "has it been minted" answerable by the account existing, and saves
  // offering a button whose only possible outcome is "account already in use".
  //
  // Wallet-gated like the bids, and for a reason worth stating: these twenty
  // subscriptions exist only to decide whether to draw a button that needs a
  // signature. Leaving them on for a visitor who never connects would make
  // T19's read-only page pay for T20's, which is the wrong way round.
  const certPdas = useMemo(
    () =>
      publicKey
        ? assets.map((asset, i) =>
            asset ? addresses.cert(i, BigInt(asset.termNumber.toString())) : addresses.cert(i, 0n),
          )
        : [],
    [addresses, assets, publicKey],
  )
  const certs = useAccountList(certPdas, () => true)

  // ── Sending ───────────────────────────────────────────────────────────────

  /**
   * Build, send, and turn whatever comes back into one sentence.
   *
   * The mapping happens here rather than in `chain-react`, which is not allowed
   * to know this coin exists. What arrives is `useSendTransaction`'s own
   * rewritten `Error` with the original hanging off `cause`, and
   * `encErrorMessage` reads both — it has to, because the generic humaniser
   * runs first and its version of a refusal is a hex code.
   */
  const run = useCallback(
    async (action: string, build: () => Promise<{ instruction: unknown }>) => {
      setResult(null)
      try {
        const { instruction } = await build()
        const signature = await send([instruction as never])
        setResult({ kind: 'sent', action, signature })
      } catch (err) {
        setResult({ kind: 'failed', action, message: encErrorMessage(err) ?? humanizeError(err) })
      }
    },
    [send],
  )

  const need = useCallback(() => {
    if (!program || !publicKey) throw new Error('Connect a wallet first.')
    return { program, wallet: publicKey }
  }, [program, publicKey])

  const claim = useCallback(
    () =>
      run('claim', async () => {
        const { program: p, wallet } = need()
        // Null when yesterday's epoch account genuinely is not there — the
        // first epoch anyone claimed in, one nobody claimed in, or one already
        // closed. Passing an address that holds nothing would fail the whole
        // transaction; passing null costs only this caller's own share.
        const previous =
          state.previousEpoch !== null && epochIndex > 0n ? addresses.epoch(epochIndex - 1n) : null
        return {
          instruction: await p.methods
            .claim(bn(epochIndex) as never)
            .accounts(claimAccounts(addresses, wallet, epochIndex, previous))
            .instruction(),
        }
      }),
    [addresses, epochIndex, need, run, state.previousEpoch],
  )

  const placeBid = useCallback(
    (index: number, amount: bigint) =>
      run('bid', async () => {
        const { program: p, wallet } = need()
        return {
          instruction: await p.methods
            .placeBid(index, bn(amount) as never)
            .accounts(placeBidAccounts(addresses, index, wallet))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  const withdrawBid = useCallback(
    (index: number) =>
      run('withdraw', async () => {
        const { program: p, wallet } = need()
        return {
          instruction: await p.methods
            .withdrawBid(index)
            .accounts(withdrawBidAccounts(addresses, index, wallet))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  const settleAuction = useCallback(
    (index: number, winner: PublicKey, outgoingHolder: PublicKey) =>
      run('settle', async () => {
        const { program: p, wallet } = need()
        return {
          instruction: await p.methods
            .settleAuction(index)
            // The caller is whoever bothered. The winner and the outgoing
            // holder come off the asset, never off the person clicking.
            .accounts(settleAuctionAccounts(addresses, index, winner, outgoingHolder, wallet))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  const rollTerm = useCallback(
    (index: number) =>
      run('roll', async () => {
        // `roll_term` has no signer at all; the fee payer signs the transaction
        // and the instruction asks nothing of anyone. A wallet is still needed
        // to pay that fee, which is a different thing and worth not conflating.
        const { program: p } = need()
        return {
          instruction: await p.methods
            .rollTerm(index)
            .accounts(rollTermAccounts(addresses, index))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  const mintCertificate = useCallback(
    (index: number, term: bigint, holder: PublicKey) =>
      run('certificate', async () => {
        const { program: p, wallet } = need()
        return {
          instruction: await p.methods
            .mintCertificate(index, bn(term) as never)
            // Anyone may pay for it; it lands in the holder's wallet either way.
            .accounts(mintCertificateAccounts(addresses, index, term, holder, wallet))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  const fileCopy = useCallback(
    (index: number, text: string) =>
      run('file', async () => {
        const { program: p, wallet } = need()
        return {
          instruction: await p.methods
            .fileCopy(index, text)
            .accounts(fileCopyAccounts(addresses, index, wallet))
            .instruction(),
        }
      }),
    [addresses, need, run],
  )

  return {
    wallet: publicKey ?? null,
    balance: balance.data ?? 0n,
    player: player.data,
    bids,
    certificates: certs.map((c) => c === true),
    pending,
    result,
    dismiss: useCallback(() => setResult(null), []),
    claim,
    placeBid,
    withdrawBid,
    settleAuction,
    rollTerm,
    mintCertificate,
    fileCopy,
  }
}
