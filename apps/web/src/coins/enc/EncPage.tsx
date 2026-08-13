import { ClusterBadge, ConnectWallet, SolanaProvider } from '@badcode/chain-react'
import type { Cluster } from '@badcode/chain-kit'
import { ENC_PROGRAM_ID } from '@badcode/enc'
import { useNavigate } from 'react-router-dom'
import { AssetGrid } from './AssetGrid'
import { Printer } from './Printer'
import { Wallet } from './Wallet'
import { useEncActions } from './useEncActions'
import { useEncChain } from './useEncChain'
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

/**
 * Everything the chain says, and nothing you have to sign for.
 *
 * The whole page reads without a wallet. That is deliberate and it is the point
 * of the coin: a claim that nobody can change the supply is worth nothing if
 * you have to install something to check it.
 */
function EncBody() {
  const state = useEncChain()
  // Additive, and deliberately unconditional: the actions hook subscribes to
  // nothing at all until a wallet connects, so the read-only page above costs
  // exactly what it cost before T20.
  const actions = useEncActions(state)

  if (state.error) {
    return (
      <section className="enc-pending">
        <p>
          Nothing is answering on {CLUSTER}. The coin is fine; the pipe is not.
          {import.meta.env.DEV ? ' Locally, that is usually `./stack start`.' : ''}
        </p>
        <p className="enc-hint">{state.error.message}</p>
      </section>
    )
  }

  if (state.uninitialised) {
    return (
      <section className="enc-pending">
        <p>
          The program is deployed here and has never been switched on — no mint, no vault, no
          slots. A coin nobody has initialised is the purest form of this joke, but it is not the
          one we meant.
        </p>
        <p className="enc-hint">Program {ENC_PROGRAM_ID.toBase58()}</p>
      </section>
    )
  }

  if (state.loading || !state.config || !state.printer) {
    return (
      <section className="enc-pending">
        <p>Asking the chain how much money there is…</p>
      </section>
    )
  }

  return (
    <>
      <Printer state={state} />
      <Wallet state={state} actions={actions} />
      <AssetGrid
        assets={state.assets}
        config={state.config}
        vault={state.addresses.vault}
        supply={state.supply}
        now={state.now}
        actions={actions}
      />
    </>
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

        <div className="enc-wallet">
          <ConnectWallet />
          <p className="enc-hint">
            Everything below is readable without connecting anything — it is a public chain and we
            are not the ones holding it. A wallet only becomes useful when you want to take part:
            the faucet, the ten auctions, and the one field on this page anybody can write in.
          </p>
        </div>

        <EncBody />
      </main>
    </SolanaProvider>
  )
}
