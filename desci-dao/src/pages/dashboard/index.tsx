import ClientRehydration from "@/common/utils/ClientRehydration";
import { DashboardProvider } from "@/modules/dashboard/context/DashboardContext";
import { RedirectionDashboard } from "@/modules/dashboard/redirection";

export default function DashboardPage() {
    return (
        <ClientRehydration>
            <DashboardProvider>
                <RedirectionDashboard />
            </DashboardProvider>
        </ClientRehydration>
    );
}