/**
 * @badcode/chain-react — React layer for Solana.
 *
 * Portability contract: nothing here may reference a specific program, coin, or
 * project. Program identity arrives as arguments (`useProgram(idl, programId)`),
 * never as an import. See chain/README.md.
 *
 * Consumers must import the wallet-adapter stylesheet once:
 *   import '@solana/wallet-adapter-react-ui/styles.css'
 */
export { SolanaProvider, useCluster, type SolanaProviderProps } from './SolanaProvider.js'
export { useProgram } from './useProgram.js'
export { useAccount, type AccountState } from './useAccount.js'
export { useSendTransaction, humanizeError, type SendState } from './useSendTransaction.js'
export { ClusterBadge } from './ClusterBadge.js'
export { ConnectWallet, useWalletAddress, shortAddress } from './ConnectWallet.js'
