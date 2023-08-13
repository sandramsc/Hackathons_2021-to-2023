
import { Dispatch, SetStateAction } from "react";
import { IPaperForm } from "../models/paper";

export interface ProjectSectionContextInterface {
    paper: IPaperForm | null;
    setPaper: Dispatch<SetStateAction<IPaperForm | null>>
    projectSectionState: ProjectSectionStateType;
    setProjectSectionState: Dispatch<SetStateAction<ProjectSectionStateType>>;
}

export enum ProjectSectionStateType {
    MyProjects = 'My Projects',
    UploadMetadata = 'Upload Metadata',
    Mint = 'Mint',
}