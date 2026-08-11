import { useConnection } from '@solana/wallet-adapter-react'
import type { PublicKey } from '@solana/web3.js'
import { useEffect, useState } from 'react'

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
 * `decode` must be stable (module scope or useCallback); it is intentionally not
 * in the dependency list, because an inline lambda would resubscribe every render.
 */
export function useAccount<T>(
  pubkey: PublicKey | null,
  decode: (data: Buffer) => T,
): AccountState<T> {
  const { connection } = useConnection()
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
        setState({ data: decode(raw.data), loading: false, error: null, missing: false })
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
    // eslint-disable-next-line react-hooks/exhaustive-deps -- decode must be stable by contract
  }, [connection, pubkey?.toBase58()])

  return state
}
