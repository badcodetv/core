import { useWallet } from '@solana/wallet-adapter-react'
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui'

/** Shorten a base58 address for display. */
export function shortAddress(address: string, keep = 4): string {
  return address.length <= keep * 2 + 1 ? address : `${address.slice(0, keep)}…${address.slice(-keep)}`
}

/**
 * Connect / disconnect button.
 *
 * Thin wrapper over the adapter's own button so callers get the wallet-selection
 * modal for free. Consumers must import the adapter UI stylesheet once:
 *   import '@solana/wallet-adapter-react-ui/styles.css'
 */
export function ConnectWallet({ className }: { className?: string }) {
  return <WalletMultiButton className={className} />
}

/** The connected address, or null. Handy for showing state without the button. */
export function useWalletAddress(): string | null {
  const { publicKey } = useWallet()
  return publicKey?.toBase58() ?? null
}
