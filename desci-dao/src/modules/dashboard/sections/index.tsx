import { useContext } from "react";
import { DashboardContext } from "../context/DashboardContext";
import { DashboardContextInterface, DashboardSectionType } from "../types/context/dashboardContext";
import { MessageSection } from "./Message";
import { ResumeSection } from "./Resume";
import { ProjectSection } from "./Projects";
import { ProjectSectionProvider } from "../context/ProjectSectionContext";

export const DashboardSection = () => {
    const { dashboardSection } = useContext(DashboardContext) as DashboardContextInterface;

    return <>
        {dashboardSection === DashboardSectionType.Summary && <ResumeSection />}
        {dashboardSection === DashboardSectionType.Messages && <MessageSection />}
        {dashboardSection === DashboardSectionType.Projects && <ProjectSectionProvider><ProjectSection /></ProjectSectionProvider>}
    </>
}