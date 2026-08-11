import { type Cluster, rpcEndpoint, wsEndpoint } from '@badcode/chain-kit'
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom'
import { ConnectionProvider, WalletProvider } from '@solana/wallet-adapter-react'
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui'
import { type ReactNode, createContext, useContext, useMemo } from 'react'

const ClusterContext = createContext<Cluster>('localnet')

/** Which cluster the surrounding provider is pointed at. */
export function useCluster(): Cluster {
  return useContext(ClusterContext)
}

export interface SolanaProviderProps {
  cluster: Cluster
  children: ReactNode
  /** Override the RPC endpoint — the public mainnet one is rate-limited hard. */
  endpoint?: string
}

/**
 * Connection + wallet provider stack.
 *
 * Deliberately says nothing about which program you are talking to; that arrives
 * per-call via `useProgram(idl, programId)`. Autoconnect is on so a returning
 * visitor who already approved the site does not have to click again.
 */
export function SolanaProvider({ cluster, children, endpoint }: SolanaProviderProps) {
  const url = useMemo(() => rpcEndpoint(cluster, endpoint), [cluster, endpoint])
  const wallets = useMemo(() => [new PhantomWalletAdapter()], [])
  const config = useMemo(() => ({ wsEndpoint: wsEndpoint(cluster) }), [cluster])

  return (
    <ClusterContext.Provider value={cluster}>
      <ConnectionProvider endpoint={url} config={config}>
        <WalletProvider wallets={wallets} autoConnect>
          <WalletModalProvider>{children}</WalletModalProvider>
        </WalletProvider>
      </ConnectionProvider>
    </ClusterContext.Provider>
  )
}
