import { IPaper } from "@/common/@types/models/IPaper"
import { Loader } from "@/common/components/Loader"
import { getPapers } from "@/common/services/models/paper"
import _ from "lodash"
import { useContext, useEffect, useState } from "react"
import { useAccount } from "wagmi"
import { ProjectBox } from "../../../components/ProjectBox"
import { ProjectSectionContext } from "../../../context/ProjectSectionContext"
import { ProjectSectionContextInterface, ProjectSectionStateType } from "../../../types/context/registerProjectFormContext"
import { ImFileEmpty } from 'react-icons/im';

export const MyProjects = () => {
    const { setProjectSectionState } = useContext(ProjectSectionContext) as ProjectSectionContextInterface
    const [projects, setProjects] = useState<IPaper[] | any>([])
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const { address } = useAccount();

    useEffect(() => {
        const fetchPapers = async () => {
            setIsLoading(true)
            const response = await getPapers({ ownerAddress: address }, 4, true);
            if (response?.data) {
                setProjects(response?.data || [])
            }
            setIsLoading(false)
        }

        if (address) {
            fetchPapers();
        }
    }, [address])

    return <div className="ml-60 max-h-screen overflow-auto">
        <div className="px-6 py-8">
            <div className="max-w-6xl mx-auto">
                <div className="bg-white rounded-3xl p-8 mb-5">
                    <div className="flex flex-row items-center justify-between">
                        <h1 className="text-3xl font-bold my-auto">My Projects</h1>
                        <button className="btn btn-outline" onClick={() => setProjectSectionState(ProjectSectionStateType.UploadMetadata)}><span className="text-xl">+</span>&nbsp;&nbsp;New Project </button>
                    </div>

                    <hr className="my-10" />
                    {
                        isLoading ? <Loader /> :
                            <div>
                                {
                                    _.isEmpty(projects) ?
                                        <div className="flex flex-col gap-8 justify-center items-center">
                                            <p className="text-gray-600">You don&apos;t have any Project yet, upload one now! 🧙🏼‍♂️</p>
                                            <ImFileEmpty className="text-gray-500 text-6xl" />
                                        </div>
                                        :
                                        <div className="grid grid-cols-2 gap-y-8 gap-x-16">
                                            {
                                                projects.map((paper: IPaper) => {
                                                    return <ProjectBox paper={paper} key={paper._id} />
                                                })
                                            }
                                        </div>
                                }
                            </div>
                    }
                </div>
            </div>
        </div>
    </div >
}