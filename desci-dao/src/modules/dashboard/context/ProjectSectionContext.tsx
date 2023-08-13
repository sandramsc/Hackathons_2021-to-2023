import { createContext, useState } from 'react';
import { ProjectSectionContextInterface, ProjectSectionStateType } from '../types/context/registerProjectFormContext';
import { IPaperForm } from '../types/models/paper';

export const ProjectSectionContext = createContext<ProjectSectionContextInterface | null>(null)

export const ProjectSectionProvider = ({ children }: { children: JSX.Element }) => {
    const [paper, setPaper] = useState<IPaperForm | null>(null);
    const [projectSectionState, setProjectSectionState] = useState<ProjectSectionStateType>(ProjectSectionStateType.MyProjects)

    return <ProjectSectionContext.Provider value={{ paper, setPaper, projectSectionState, setProjectSectionState }}>
        {children}
    </ProjectSectionContext.Provider>
}