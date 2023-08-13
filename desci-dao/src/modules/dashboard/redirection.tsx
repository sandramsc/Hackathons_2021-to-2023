import { Loader } from "@/common/components/Loader";
import { useContext, useEffect, useState } from "react";
import { Dashboard } from ".";
import { DashboardContext } from "./context/DashboardContext";
import { OnBoard } from "./sections/OnBoard";
import { DashboardContextInterface } from "./types/context/dashboardContext";
import { useAccount, useContractRead } from "wagmi";

import { getUser } from "@/common/services/models/user";
import _ from "lodash";
import Link from "next/link";

export const RedirectionDashboard = () => {
    const { requireOnboarding, setRequireOnboarding } = useContext(DashboardContext) as DashboardContextInterface;
    const { address: userAddress } = useAccount();
    const [isLoading, setIsLoading] = useState<boolean>(true);

    useEffect(() => {
        const getUserFetch = async () => {
            const response = await getUser({ userAddress: userAddress || '' })
            if (!_.isEmpty(response?.data)) {
                setRequireOnboarding(false)
            }

            setIsLoading(false);
        }

        if (userAddress) {
            getUserFetch();
        }
    }, [userAddress])

    if (!userAddress) return <div className="w-screen h-screen flex justify-center items-center align-middle bg-transparent">
        <div className="alert shadow-lg mx-96">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="stroke-info flex-shrink-0 w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <span>You need to connect your wallet in order to upload a File 🧙🏼‍♂️</span>
            </div>
            <div className="flex-none">
                <Link href={'/'}><button className="btn btn-sm btn-primary">Accept</button></Link>
            </div>
        </div>
    </div>

    if (isLoading) return <div className="w-screen h-scree">
        <Loader fillScreen={true} />
    </div>

    return <>
        {!requireOnboarding && <Dashboard />}
        {requireOnboarding && <OnBoard />}
    </>
}