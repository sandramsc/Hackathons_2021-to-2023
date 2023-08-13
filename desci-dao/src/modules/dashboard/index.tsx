import { ContainerX } from "@/common/layout/Container"
import { NavBar } from "@/common/layout/NavBar"
import { Sidebar } from "./components/Sidebar"
import { DashboardSection } from "./sections"

export const Dashboard = () => {

    return <div data-theme="emerald" className="relative bg-yellow-50 overflow-hidden h-screen flex flex-col">
        <Sidebar />
        <div className="flex flex-col justify-evenly">
            <NavBar />
            <DashboardSection />
        </div>
    </div>
}