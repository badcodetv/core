import { isMainnet } from '@badcode/chain-kit'
import { useCluster } from './SolanaProvider.js'

const LABEL: Record<string, string> = {
  localnet: 'LOCALNET',
  devnet: 'DEVNET',
  'mainnet-beta': 'MAINNET',
}

/**
 * Which chain you are actually on.
 *
 * Not decoration: every test cluster's tokens are worthless and every mainnet
 * mistake is permanent, and the two look identical in a UI. Always visible.
 */
export function ClusterBadge({ className }: { className?: string }) {
  const cluster = useCluster()
  return (
    <span
      className={className}
      data-cluster={cluster}
      data-live={isMainnet(cluster) ? 'true' : 'false'}
      title={isMainnet(cluster) ? 'Real funds. Mistakes are permanent.' : 'Test network. Tokens here are worthless.'}
    >
      {LABEL[cluster] ?? cluster}
    </span>
  )
}
