import { type ComponentType, lazy } from 'react'
import { homeSteps } from '../home/timeline'

export type CoinResolution =
  | { kind: 'live'; title: string; Component: ComponentType }
  | { kind: 'coming-soon'; title: string }
  | { kind: 'not-found' }

/**
 * Live coins: slug → component. Add an entry here when a coin ships.
 *
 * Lazy on purpose. The wallet adapter and web3.js are heavy, and nobody reading
 * a comic should download them — this keeps them in their own chunk, loaded only
 * when a coin route is actually visited.
 */
const liveCoins: Record<string, ComponentType> = {
  enc: lazy(() => import('./enc/EncPage').then((m) => ({ default: m.EncPage }))),
}

/** Timeline nodes that point at a coin route, so titles stay in one place. */
function nodeFor(slug: string) {
  return homeSteps.find((n) => n.route === `/coins/${slug}`)
}

/**
 * A registered component is live, full stop. The timeline's `status` governs how
 * the homepage presents the node, not whether the route works — otherwise a coin
 * would be unreachable during the weeks it is being built.
 */
export function resolveCoin(slug: string): CoinResolution {
  const Component = liveCoins[slug]
  const node = nodeFor(slug)
  if (Component) return { kind: 'live', title: node?.title ?? slug, Component }
  if (node) return { kind: 'coming-soon', title: node.title }
  return { kind: 'not-found' }
}
