import { createContext, useState } from 'react';
import { DashboardContextInterface, DashboardSectionType } from '../types/context/dashboardContext';

export const DashboardContext = createContext<DashboardContextInterface | null>(null)

export const DashboardProvider = ({ children }: { children: JSX.Element }) => {
    const [dashboardSection, setDashboardSection] = useState<DashboardSectionType>(DashboardSectionType.Summary);
    const [requireOnboarding, setRequireOnboarding] = useState<boolean>(true);

    return <DashboardContext.Provider value={{ dashboardSection, setDashboardSection, requireOnboarding, setRequireOnboarding }}>
        {children}
    </DashboardContext.Provider>
}