import { Suspense, lazy } from 'react'
import { TextPage } from './TextPage'

// Lazy for the same reason the coin pages are: the wallet adapters are ~500 kB
// and no visitor to the site proper should pay for them.
const CounterPage = lazy(() =>
  import('../chain-demo/CounterPage').then((m) => ({ default: m.CounterPage })),
)

/** The toolchain demo, at /dev/counter. Unlisted — nothing links to it. */
export function DevCounter() {
  return (
    <Suspense fallback={<TextPage title="Counter"><p>Connecting&hellip;</p></TextPage>}>
      <CounterPage />
    </Suspense>
  )
}
