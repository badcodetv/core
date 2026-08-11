import { useConnection } from '@solana/wallet-adapter-react'
import type { PublicKey } from '@solana/web3.js'
import { useEffect, useRef, useState } from 'react'

export interface AccountState<T> {
  data: T | null
  loading: boolean
  error: Error | null
  /** True when the account genuinely does not exist, as opposed to not-loaded-yet. */
  missing: boolean
}

/**
 * Subscribe to an account and decode it, re-rendering whenever it changes.
 *
 * Works without a connected wallet — reading the chain needs no signer, which
 * matters because the interesting pages should be legible to a visitor who never
 * connects anything.
 *
 * `decode` may be an inline lambda. It is held in a ref rather than depended on,
 * so a new function identity each render neither resubscribes nor goes stale —
 * requiring callers to memoise it was a footgun that bought nothing.
 */
export function useAccount<T>(
  pubkey: PublicKey | null,
  decode: (data: Buffer) => T,
): AccountState<T> {
  const { connection } = useConnection()
  const decodeRef = useRef(decode)
  decodeRef.current = decode
  const [state, setState] = useState<AccountState<T>>({
    data: null,
    loading: pubkey !== null,
    error: null,
    missing: false,
  })

  useEffect(() => {
    if (!pubkey) {
      setState({ data: null, loading: false, error: null, missing: false })
      return
    }

    let live = true
    const apply = (raw: { data: Buffer } | null) => {
      if (!live) return
      if (!raw) {
        setState({ data: null, loading: false, error: null, missing: true })
        return
      }
      try {
        setState({ data: decodeRef.current(raw.data), loading: false, error: null, missing: false })
      } catch (err) {
        setState({ data: null, loading: false, error: err as Error, missing: false })
      }
    }

    setState((s) => ({ ...s, loading: true }))
    connection
      .getAccountInfo(pubkey)
      .then(apply)
      .catch((err: Error) => live && setState({ data: null, loading: false, error: err, missing: false }))

    const sub = connection.onAccountChange(pubkey, apply)
    return () => {
      live = false
      // Leaking subscriptions keeps the websocket busy and the component alive.
      void connection.removeAccountChangeListener(sub)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- decode is held in a ref
  }, [connection, pubkey?.toBase58()])

  return state
}
