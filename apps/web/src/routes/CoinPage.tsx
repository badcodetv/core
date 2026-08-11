import { Suspense } from 'react'
import { useParams } from 'react-router-dom'
import { resolveCoin } from '../coins/coins'
import { NotFound } from './NotFound'
import { TextPage } from './TextPage'

function Loading() {
  return <TextPage title="Loading"><p>Fetching the printer&hellip;</p></TextPage>
}

export function CoinPage() {
  const { slug = '' } = useParams()
  const r = resolveCoin(slug)

  if (r.kind === 'live') {
    // Suspense is required here: coin components are lazy so the wallet libraries
    // stay out of the main bundle.
    return (
      <Suspense fallback={<Loading />}>
        <r.Component />
      </Suspense>
    )
  }

  if (r.kind === 'coming-soon') {
    return (
      <TextPage title={r.title}>
        <p>Not minted yet.</p>
      </TextPage>
    )
  }

  return <NotFound />
}
