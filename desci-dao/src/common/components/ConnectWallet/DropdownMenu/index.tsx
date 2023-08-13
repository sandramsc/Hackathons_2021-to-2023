import Image from "next/image"
import Link from "next/link"
import { useRouter } from "next/router"
import { useAccount, useDisconnect } from "wagmi"

export const DropdownMenu = () => {
    const { address } = useAccount()
    const { disconnect } = useDisconnect()
    const router = useRouter()

    const handleDisconnect = () => {
        disconnect();
        router.replace('/')
    }

    return <div className="dropdown dropdown-end bg-transparent">
        <div tabIndex={0} className='cursor-pointer btn m-1 bg-transparent border-none hover:bg-gray-200'>
            <div className="flex flex-row gap-3 items-center">
                <div className="avatar">
                    <div className="w-10 rounded-full">
                        <Image
                            src="/assets/illustrations/raccoon.png"
                            alt="avatar"
                            width={40}
                            height={40}
                        />
                    </div>
                </div>
                <div className="font-medium text-start">
                    <div className="text-gray-700">
                        {address?.slice(0, 5) + '...' + address?.slice(address.length - 5, address.length)}
                    </div>
                    <div className="text-sm text-gray-500 dark:text-gray-400">
                        A Dump Raccoon
                    </div>
                </div>
            </div>
        </div>
        <ul tabIndex={0} className="dropdown-content menu p-2 shadow rounded-box w-52 bg-white">
            <li><Link href={'/'}>Home</Link></li>
            <li><Link href={'/dashboard'}>Dashboard</Link></li>
            <hr />
            <li><div onClick={handleDisconnect}>Disconnect</div></li>
        </ul>
    </div>
}