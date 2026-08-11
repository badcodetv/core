/** The three clusters this toolchain targets. */
export type Cluster = 'localnet' | 'devnet' | 'mainnet-beta'

export const CLUSTERS: readonly Cluster[] = ['localnet', 'devnet', 'mainnet-beta'] as const

export function isCluster(value: string): value is Cluster {
  return (CLUSTERS as readonly string[]).includes(value)
}

/** Throws with the valid options rather than letting a typo reach the network. */
export function parseCluster(value: string): Cluster {
  if (!isCluster(value)) {
    throw new Error(`Unknown cluster "${value}". Expected one of: ${CLUSTERS.join(', ')}`)
  }
  return value
}

const RPC: Record<Cluster, string> = {
  localnet: 'http://127.0.0.1:8899',
  devnet: 'https://api.devnet.solana.com',
  'mainnet-beta': 'https://api.mainnet-beta.solana.com',
}

const WS: Record<Cluster, string> = {
  localnet: 'ws://127.0.0.1:8900',
  devnet: 'wss://api.devnet.solana.com',
  'mainnet-beta': 'wss://api.mainnet-beta.solana.com',
}

/**
 * JSON-RPC endpoint for a cluster.
 *
 * `override` exists because the public mainnet endpoint is rate-limited hard
 * enough to be unusable for anything real — production deployments pass their
 * own provider's URL.
 */
export function rpcEndpoint(cluster: Cluster, override?: string): string {
  return override ?? RPC[cluster]
}

/** Websocket endpoint, used for live account subscriptions. */
export function wsEndpoint(cluster: Cluster, override?: string): string {
  return override ?? WS[cluster]
}

/** True when the cluster handles real money and mistakes are permanent. */
export function isMainnet(cluster: Cluster): boolean {
  return cluster === 'mainnet-beta'
}

export type ExplorerKind = 'tx' | 'address' | 'block'

/**
 * Link into Solana Explorer.
 *
 * Localnet needs `customUrl` rather than a named cluster, and the explorer only
 * resolves it if the validator is actually reachable from the browser.
 */
export function explorerUrl(cluster: Cluster, kind: ExplorerKind, id: string): string {
  const base = `https://explorer.solana.com/${kind}/${id}`
  if (cluster === 'mainnet-beta') return base
  if (cluster === 'devnet') return `${base}?cluster=devnet`
  return `${base}?cluster=custom&customUrl=${encodeURIComponent(RPC.localnet)}`
}
