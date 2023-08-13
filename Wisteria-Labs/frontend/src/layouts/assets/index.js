// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Soft UI Assets React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Assets React examples
import AssetsLayout from "examples/LayoutContainers/AssetsLayout";
import AssetsNavbar from "examples/Navbars/AssetsNavbar";
import Footer from "examples/Footer";
import GradientLineChart from "examples/Charts/LineCharts/GradientLineChart";

// Soft UI Assets React base styles
import typography from "assets/theme/base/typography";

// Assets layout components
import Portfolio from "layouts/assets/components/Portfolio";
import Transactions from "layouts/assets/components/Transactions";

// Data
import gradientLineChartData from "layouts/assets/data/gradientLineChartData";

function Assets() {
  const { size } = typography;
  
  return (
    <AssetsLayout>
      <AssetsNavbar />
      <SoftBox py={3}>
        <SoftBox mb={3}>
          <Grid container spacing={3}>  
       
            <Grid item xs={12} lg={12}>
              <GradientLineChart
                title="Crypto Overview"
                description={
                  <SoftBox display="flex" alignItems="center">
                    <SoftBox fontSize={size.lg} color="success" mb={0.3} mr={0.5} lineHeight={0}>
                      <Icon className="font-bold">arrow_upward</Icon>
                    </SoftBox>
                    <SoftTypography variant="button" color="text" fontWeight="medium">
                      4% more{" "}
                      <SoftTypography variant="button" color="text" fontWeight="regular">
                        in 2023
                      </SoftTypography>
                    </SoftTypography>
                  </SoftBox>
                }
                height="22rem"
                chart={gradientLineChartData}
              />
            </Grid>
          </Grid>
        </SoftBox>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={8}>
            <Portfolio />
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <Transactions />
          </Grid>
        </Grid>
      </SoftBox>
      <Footer />
    </AssetsLayout>
  );
}

export default Assets;
