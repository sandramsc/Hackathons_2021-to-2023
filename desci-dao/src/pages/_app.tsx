import '@/styles/globals.css'
import { wagmiInstance } from '@/common/core/clients/wagmi'
import type { AppProps } from 'next/app'
import { WagmiConfig } from 'wagmi'
import MetaData from './_seo';

const wagmiClient = wagmiInstance();

export default function App({ Component, pageProps }: AppProps) {
  return <>
    <MetaData />
    <WagmiConfig client={wagmiClient}>
      <Component {...pageProps} />
    </WagmiConfig >
  </>
}
