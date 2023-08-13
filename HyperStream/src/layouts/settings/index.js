// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

// Soft UI Dashboard React base styles
import typography from "assets/theme/base/typography";


function Dashboard() {
  const { size } = typography;

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox py={3}>
          IN PROGRESS...
      </SoftBox>
      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
