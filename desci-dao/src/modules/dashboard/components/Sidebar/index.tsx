import classNames from "classnames";
import Link from "next/link";
import { useContext } from "react";
import { DashboardContext } from "../../context/DashboardContext";
import { DashboardContextInterface } from "../../types/context/dashboardContext";
import { ISideBarOption, sideBardOptions } from "./sideBardOptions";

export const Sidebar = () => {
    const { dashboardSection, setDashboardSection } = useContext(DashboardContext) as DashboardContextInterface;;

    return <div className="fixed inset-y-0 left-0 bg-white shadow-md max-h-screen w-60">
        <div className="flex flex-col justify-between h-full">
            <div className="flex-grow">
                <div className="px-4 py-6 text-center border-b">
                    <Link href={'/'}><h1 className="text-xl font-bold leading-none"><span className="text-yellow-700">Soul-Sci</span> App</h1></Link>
                </div>
                <div className="p-4">
                    <ul className="space-y-1">
                        {
                            sideBardOptions.map((option: ISideBarOption) => {
                                return <li key={option.name}>
                                    <div onClick={() => setDashboardSection(option.name)}
                                        className={classNames([
                                            "cursor-pointer flex items-center  rounded-xl font-bold text-sm  py-3 px-4",
                                            dashboardSection === option.name ? 'bg-yellow-200 text-yellow-900' : 'bg-transparent'
                                        ])}


                                    >
                                        {option.icon}{option.name}
                                    </div>
                                </li>
                            })
                        }
                    </ul>
                </div>
            </div>
          
        </div>
    </div>
}