import { configureChains, createClient } from 'wagmi';
import { filecoinHyperspace } from 'wagmi/chains';
import { jsonRpcProvider } from 'wagmi/providers/jsonRpc';
import { CoinbaseWalletConnector } from 'wagmi/connectors/coinbaseWallet'
import { InjectedConnector } from 'wagmi/connectors/injected'
import { MetaMaskConnector } from 'wagmi/connectors/metaMask'
import { WalletConnectConnector } from 'wagmi/connectors/walletConnect'

export const wagmiInstance = () => {
    const { chains, provider, webSocketProvider } = configureChains(
        [filecoinHyperspace], [jsonRpcProvider({
            rpc: () => {
                return {
                    http: process.env.NEXT_PUBLIC_HYPERSPACE_RCP || ''
                };
            }
        })]
    );

    return createClient({
        autoConnect: true,
        connectors: [
            new MetaMaskConnector({
                chains
            }),
            new CoinbaseWalletConnector({
                chains,
                options: {
                    appName: 'wagmi',
                },
            }),
            new WalletConnectConnector({
                chains,
                options: {
                    qrcode: true,
                },
            }),
            new InjectedConnector({
                chains,
                options: {
                    name: 'Injected',
                    shimDisconnect: true,
                },
            }),
        ],
        provider,
        webSocketProvider
    })
}