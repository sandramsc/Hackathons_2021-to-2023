
import { Dispatch, SetStateAction } from "react";

export interface DashboardContextInterface {
    dashboardSection: DashboardSectionType;
    setDashboardSection: Dispatch<SetStateAction<DashboardSectionType>>;
    requireOnboarding: boolean;
    setRequireOnboarding: Dispatch<SetStateAction<boolean>>;
}

export enum DashboardSectionType {
    Summary = 'Summary',
    FindPapers = 'Find Papers',
    Messages = 'Messages',
    Projects = 'Projects',
    Settings = 'Settings',
}