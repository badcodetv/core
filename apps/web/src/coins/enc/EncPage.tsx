import { ClusterBadge, ConnectWallet, SolanaProvider, useWalletAddress } from '@badcode/chain-react'
import type { Cluster } from '@badcode/chain-kit'
import { useNavigate } from 'react-router-dom'
import '@solana/wallet-adapter-react-ui/styles.css'
import './enc.css'

/**
 * Which chain the page talks to. Localnet while the program is being built;
 * flipped to devnet when it is deployed there (see the plan's T22).
 */
const CLUSTER: Cluster = 'localnet'

function BackToIndex() {
  const navigate = useNavigate()
  return (
    <button className="enc-back" onClick={() => navigate('/')}>
      ← badcode
    </button>
  )
}

function Wallet() {
  const address = useWalletAddress()
  return (
    <div className="enc-wallet">
      <ConnectWallet />
      {address ? null : <p className="enc-hint">Connect a wallet to take part. Nothing here costs real money.</p>}
    </div>
  )
}

export function EncPage() {
  return (
    <SolanaProvider cluster={CLUSTER}>
      <BackToIndex />
      <main className="enc">
        <header className="enc-header">
          <ClusterBadge className="enc-cluster" />
          <h1>Emperor&rsquo;s New Coin</h1>
          <p className="enc-strap">
            The first currency honest about what it is. When the Fed prints, we print. Nobody
            here can change that, including us.
          </p>
        </header>

        <Wallet />

        <section className="enc-pending">
          <p>The printer is still being built.</p>
        </section>
      </main>
    </SolanaProvider>
  )
}
