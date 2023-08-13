import Link from "next/link";
import { useAccount, useConnect, useDisconnect } from "wagmi";
import { DropdownMenu } from "./DropdownMenu";

export const ConnectWallet = () => {
    const { connectors, isLoading, connect, error, pendingConnector } = useConnect()
    const { isConnected } = useAccount()

    return <>
        {
            isConnected ?
               <DropdownMenu/>
                :
                <>
                    <label htmlFor="my-modal" className="btn bg-transparent border-none text-gray-700 hover:bg-transparent hover:text-grey-400">Login</label>
                    <input type="checkbox" id="my-modal" className="modal-toggle" />

                    <div className="modal">
                        <div className="modal-box relative bg-white">
                            <label htmlFor="my-modal" className="btn btn-sm btn-circle absolute right-2 top-2 bg-white border-none">✕</label>
                            <div className="flex flex-col ">
                                {connectors.map((connector) => (
                                    <button
                                        disabled={!connector.ready}
                                        key={connector.id}
                                        onClick={() => connect({ connector })}
                                        className="py-4 hover:bg-gray-300"
                                    >
                                        <p>{connector.name}</p>
                                        <p>{!connector.ready ? '(unsupported)' : ''}</p>
                                        {isLoading &&
                                            connector.id === pendingConnector?.id &&
                                            <p>{'(connecting)'}</p>
                                        }
                                    </button>
                                ))}
                                {error && <div>{error.message}</div>}
                            </div>
                        </div>
                    </div>
                </>
        }
    </>
}