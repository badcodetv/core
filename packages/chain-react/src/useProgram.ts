import { AnchorProvider, type Idl, Program } from '@coral-xyz/anchor'
import { useAnchorWallet, useConnection } from '@solana/wallet-adapter-react'
import type { PublicKey } from '@solana/web3.js'
import { useMemo } from 'react'

/**
 * An Anchor program handle for the connected wallet.
 *
 * Takes the IDL and address as arguments rather than looking them up, so this
 * package never imports a specific program's types — that is what keeps it
 * liftable into an unrelated project.
 *
 * Returns null until a wallet is connected, since Anchor needs a signer to build
 * a provider. Read-only pages should fetch accounts through the connection
 * directly (see useAccount) instead of waiting on this.
 */
export function useProgram<T extends Idl>(idl: T, programId: PublicKey): Program<T> | null {
  const { connection } = useConnection()
  const wallet = useAnchorWallet()

  return useMemo(() => {
    if (!wallet) return null
    const provider = new AnchorProvider(connection, wallet, { commitment: 'confirmed' })
    // Anchor reads the address from the IDL, so keep them in step.
    return new Program<T>({ ...idl, address: programId.toBase58() }, provider)
  }, [connection, wallet, idl, programId])
}
