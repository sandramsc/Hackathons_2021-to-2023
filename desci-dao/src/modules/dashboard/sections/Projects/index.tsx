import { useContext } from "react"
import { ProjectSectionContext } from "../../context/ProjectSectionContext"
import { ProjectSectionContextInterface, ProjectSectionStateType } from "../../types/context/registerProjectFormContext"
import { MyProjects } from "./MyProjects"
import { RegisterPaper } from "./RegisterPaper"

export const ProjectSection = () => {
    const { projectSectionState } = useContext(ProjectSectionContext) as ProjectSectionContextInterface

    return (
        <>
            {projectSectionState === ProjectSectionStateType.MyProjects && <MyProjects />}
            <RegisterPaper />
        </>
    )
}