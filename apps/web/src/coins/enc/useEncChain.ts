import {
  ASSET_COUNT,
  ENC_IDL,
  ENC_PROGRAM_ID,
  type EmperorsNewCoin,
  type EncAsset,
  type EncConfig,
  type EncFaucetEpoch,
  type EncPrinter,
  assetAddresses,
  decodeMintSupply,
  decodeTokenAmount,
  encAddresses,
  encDecoders,
  epochOf,
  seconds,
} from '@badcode/enc'
import { useAccount, useProgramReader } from '@badcode/chain-react'
import { useConnection } from '@solana/wallet-adapter-react'
import type { PublicKey } from '@solana/web3.js'
import { useEffect, useMemo, useRef, useState } from 'react'

/**
 * Everything the coin knows about itself, kept live.
 *
 * Reading needs no wallet. That is not an accident of the implementation — a
 * page whose entire subject is a number nobody can change should be legible to
 * someone who never connects anything, and every hook below goes through the
 * read-only program handle for exactly that reason.
 *
 * Nothing here polls. Every account is subscribed to over the websocket, so a
 * sync, a bid or a filing arrives in the browser when it lands on the chain
 * rather than when someone reloads.
 */

/**
 * The chain's clock, not this machine's.
 *
 * `Clock::get()` is the only clock the program has, and a local validator's
 * unix time drifts behind wall time as slots slip. Every price on this page is
 * interpolated against that clock and every epoch index is derived from it, so
 * deriving them from `Date.now()` would render a page subtly about a different
 * moment than the one the program is living in. Read the chain's time once,
 * keep the offset, and tick locally from there.
 */
export function useChainClock(tickMs = 1_000): number {
  const { connection } = useConnection()
  const [offset, setOffset] = useState(0)
  const [now, setNow] = useState(() => Math.floor(Date.now() / 1_000))

  useEffect(() => {
    let live = true
    const sync = async () => {
      try {
        const slot = await connection.getSlot('confirmed')
        const chainTime = await connection.getBlockTime(slot)
        if (live && chainTime !== null) setOffset(chainTime - Math.floor(Date.now() / 1_000))
      } catch {
        // A clock we cannot read is not worth an error on the page; wall time is
        // the honest fallback and is right on any cluster that keeps up.
      }
    }
    void sync()
    // Slot time drifts, so re-anchor occasionally rather than trusting one read.
    const resync = setInterval(sync, 60_000)
    return () => {
      live = false
      clearInterval(resync)
    }
  }, [connection])

  useEffect(() => {
    const tick = setInterval(() => setNow(Math.floor(Date.now() / 1_000)), tickMs)
    return () => clearInterval(tick)
  }, [tickMs])

  return now + offset
}

/**
 * The ten slots, in index order.
 *
 * One `getMultipleAccounts` for the first read — ten round trips to draw one
 * front page would be visible — then a subscription each, because a bid or a
 * filing touches exactly one column and re-reading all ten to notice would
 * throw away the reason for subscribing at all.
 */
function useAssets(
  addresses: PublicKey[],
  decode: (data: Buffer) => EncAsset,
): (EncAsset | null)[] {
  const { connection } = useConnection()
  const decodeRef = useRef(decode)
  decodeRef.current = decode
  const [assets, setAssets] = useState<(EncAsset | null)[]>(() =>
    Array.from({ length: ASSET_COUNT }, () => null),
  )
  const key = addresses.map((a) => a.toBase58()).join(',')

  useEffect(() => {
    let live = true
    const put = (index: number, data: Buffer | null) => {
      if (!live) return
      setAssets((previous) => {
        const next = [...previous]
        try {
          next[index] = data ? decodeRef.current(data) : null
        } catch {
          // A slot that will not decode is a layout change, not a bad slot —
          // the page says so once, globally, rather than ten times.
          next[index] = null
        }
        return next
      })
    }

    connection
      .getMultipleAccountsInfo(addresses)
      .then((infos) => infos.forEach((info, i) => put(i, info?.data ?? null)))
      .catch(() => {
        /* the config read surfaces a dead RPC; ten copies of it helps nobody */
      })

    const subs = addresses.map((address, i) =>
      connection.onAccountChange(address, (info) => put(i, info.data)),
    )
    return () => {
      live = false
      subs.forEach((sub) => void connection.removeAccountChangeListener(sub))
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- decode is held in a ref
  }, [connection, key])

  return assets
}

export interface EncChainState {
  now: number
  addresses: ReturnType<typeof encAddresses>
  config: EncConfig | null
  printer: EncPrinter | null
  supply: bigint
  vaultBalance: bigint
  escrowBalance: bigint
  assets: (EncAsset | null)[]
  /** Today's faucet epoch. Null until the day's first claimer creates it. */
  currentEpoch: EncFaucetEpoch | null
  /** Yesterday's, which is the pot today's claimants divide. */
  previousEpoch: EncFaucetEpoch | null
  loading: boolean
  /** True when the program is deployed here but has never been initialised. */
  uninitialised: boolean
  error: Error | null
}

export function useEncChain(): EncChainState {
  const reader = useProgramReader<EmperorsNewCoin>(ENC_IDL, ENC_PROGRAM_ID)
  const decoders = useMemo(() => encDecoders(reader), [reader])
  const addresses = useMemo(() => encAddresses(ENC_PROGRAM_ID), [])
  const assetPdas = useMemo(() => assetAddresses(addresses), [addresses])
  const now = useChainClock()

  const config = useAccount(addresses.config, decoders.config)
  const printer = useAccount(addresses.printer, decoders.printer)
  const mint = useAccount(addresses.mint, decodeMintSupply)
  const vault = useAccount(addresses.vaultEncAta, decodeTokenAmount)
  const escrow = useAccount(addresses.escrowEncAta, decodeTokenAmount)
  const assets = useAssets(assetPdas, decoders.asset)

  // The epoch index changes once a day, not once a second, so the PDAs are
  // memoised on the index itself — otherwise every tick would resubscribe.
  const epochSeconds = config.data ? seconds(config.data.epochSeconds) : 0
  const epochIndex = epochSeconds > 0 ? epochOf(now, epochSeconds) : 0
  const currentEpochPda = useMemo(
    () => (epochSeconds > 0 ? addresses.epoch(BigInt(epochIndex)) : null),
    [addresses, epochIndex, epochSeconds],
  )
  const previousEpochPda = useMemo(
    () => (epochSeconds > 0 && epochIndex > 0 ? addresses.epoch(BigInt(epochIndex - 1)) : null),
    [addresses, epochIndex, epochSeconds],
  )
  const currentEpoch = useAccount(currentEpochPda, decoders.faucetEpoch)
  const previousEpoch = useAccount(previousEpochPda, decoders.faucetEpoch)

  return {
    now,
    addresses,
    config: config.data,
    printer: printer.data,
    // A missing token account is a zero balance, not a failure: the escrow does
    // not exist until the first bid, and the page should say "nothing is
    // locked" rather than spin.
    supply: mint.data ?? 0n,
    vaultBalance: vault.data ?? 0n,
    escrowBalance: escrow.data ?? 0n,
    assets,
    // Same for an epoch: it is created lazily by the day's first claimer, so
    // "missing" is the normal morning state and reads as a pot of zero.
    currentEpoch: currentEpoch.data,
    previousEpoch: previousEpoch.data,
    loading: config.loading || printer.loading,
    uninitialised: config.missing,
    error: config.error ?? printer.error ?? mint.error,
  }
}
