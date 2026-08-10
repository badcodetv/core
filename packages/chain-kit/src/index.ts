/**
 * @badcode/chain-kit — framework-agnostic Solana client helpers.
 *
 * Portability contract: nothing in this package may reference a specific program,
 * coin, or project. It is meant to be copied wholesale into unrelated projects.
 * Program-specific accounts, instruction builders and IDLs belong in their own
 * package. See chain/README.md.
 */
export {
  type Cluster,
  type ExplorerKind,
  CLUSTERS,
  isCluster,
  parseCluster,
  rpcEndpoint,
  wsEndpoint,
  isMainnet,
  explorerUrl,
} from './clusters.js'

export {
  type ProgramRegistry,
  registry,
  knownPrograms,
  programId,
  isDeployed,
} from './registry.js'

export { type Seed, encodeSeed, u8, u64le, derive, deriveAddress } from './pda.js'
