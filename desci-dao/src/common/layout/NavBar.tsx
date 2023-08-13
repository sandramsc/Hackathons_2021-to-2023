import _ from "lodash";
import Image from "next/image";
import Link from "next/link";
import { useAccount, useDisconnect } from 'wagmi'
import { ConnectWallet } from "../components/ConnectWallet";
import ClientRehydration from "../utils/ClientRehydration";

export const NavBar = ({ showNavigation = false }: { showNavigation?: boolean }) => {
    return <ClientRehydration>
        <div className="navbar bg-transparent flex justify-between">
            <div>
                <Link href={'/'} className="btn btn-ghost normal-case text-xl">
                    <Image
                        alt="logo"
                        width={36}
                        height={36}
                        src={'/assets/logo.png'}
                    />
                </Link>

            </div>
            {showNavigation && <div className="flex flex-row gap-8">
                <Link href={'/paper-search'}><p className="text-gray-800 hover:text-gray-500 text-md font-bold border-b-2 border-gray-600  hover:border-gray-500">PUBLIC LIBRARY</p></Link>
                <Link href={"mailto: soulsci.noreply@gmail.com"}><p className="text-gray-800 hover:text-gray-500 text-md font-bold border-b-2 border-gray-600  hover:border-gray-500" >CONTACT US</p></Link>
            </div>}

            <ConnectWallet />
        </div>
    </ClientRehydration>
}