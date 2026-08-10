import { useConnection, useWallet } from '@solana/wallet-adapter-react'
import { type TransactionInstruction, Transaction } from '@solana/web3.js'
import { useCallback, useState } from 'react'

/** Turn Solana's error soup into something a person can act on. */
export function humanizeError(err: unknown): string {
  const raw = err instanceof Error ? err.message : String(err)
  if (/User rejected|rejected the request/i.test(raw)) return 'You cancelled the transaction.'
  if (/insufficient lamports|insufficient funds/i.test(raw)) return 'Not enough SOL to pay the fee.'
  if (/Blockhash not found/i.test(raw)) return 'The network moved on before this was sent. Try again.'
  if (/0x1771|slippage/i.test(raw)) return 'The price moved before this landed. Try again.'
  const custom = raw.match(/custom program error: (0x[0-9a-f]+)/i)
  if (custom) return `The program rejected this (error ${custom[1]}).`
  return raw
}

export interface SendState {
  send: (instructions: TransactionInstruction[]) => Promise<string>
  pending: boolean
  error: string | null
  /** Signature of the last successful send. */
  signature: string | null
}

/**
 * Send instructions with the connected wallet, confirm, and surface a readable
 * error. Deliberately returns the signature so a caller can link to an explorer.
 */
export function useSendTransaction(): SendState {
  const { connection } = useConnection()
  const { publicKey, sendTransaction } = useWallet()
  const [pending, setPending] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [signature, setSignature] = useState<string | null>(null)

  const send = useCallback(
    async (instructions: TransactionInstruction[]): Promise<string> => {
      if (!publicKey) throw new Error('Connect a wallet first.')
      setPending(true)
      setError(null)
      try {
        const tx = new Transaction().add(...instructions)
        const sig = await sendTransaction(tx, connection)
        const bh = await connection.getLatestBlockhash()
        await connection.confirmTransaction({ signature: sig, ...bh }, 'confirmed')
        setSignature(sig)
        return sig
      } catch (err) {
        const message = humanizeError(err)
        setError(message)
        throw new Error(message)
      } finally {
        setPending(false)
      }
    },
    [connection, publicKey, sendTransaction],
  )

  return { send, pending, error, signature }
}
