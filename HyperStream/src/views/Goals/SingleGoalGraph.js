/**
=========================================================
* Soft UI Dashboard React - v4.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/soft-ui-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import Card from "@mui/material/Card";
import typography from "assets/theme/base/typography";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

// Data
import { styled } from "@mui/system";
import { Box,  Grid, Stack, Typography } from "@mui/material";
import { Link, useNavigate } from "react-router-dom";
import GradientLineChart from "examples/Charts/LineCharts/GradientLineChart";
import gradientLineChartData from "layouts/dashboard/data/gradientLineChartData";

function SingleGoalGraph() {
  const navigate = useNavigate();
  const { size } = typography;


  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox py={3}>
        <Stack direction= 'row' spacing={3} mb={4}>
        <StyledGoal sx={{backgroundColor: '#FCDFE2', }} variant='body2'>Awareness</StyledGoal>
        <Typography alignSelf='center'>Goal: Increase user sign ups by 12,000</Typography>
        </Stack>
            <Card sx={{padding: '1.5rem', marginBottom: '2rem'}}>
            <Grid container spacing={2} >
                        <Grid item xs={6}>
                                <Box >
                                    <Typography  color='#515152'variant='subtitle2'>Experiment #07</Typography>
                                    <Typography color='#515152' variant='h5'>Website Analytics</Typography>
                                </Box>
                        </Grid>
                        <Grid item xs={6}>
                            <Grid container spacing={2} >
                                <Grid item xs={4}>
                                        <Box>
                                            <Typography variant='subtitle2'>Time left</Typography>
                                            <Typography color='#515152' variant='h5'>4 days</Typography>
                                        </Box>
                                </Grid>
                                <Grid item xs={4}>
                                        <Box >
                                            <Typography variant='subtitle2'>Budget</Typography>
                                            <Typography color='#515152' variant='h5'>£1,000</Typography>
                                        </Box>
                                </Grid>
                                <Grid item xs={4}>
                                        <Box >
                                            <Typography variant='subtitle2'>On track</Typography>
                                            <Typography color='#515152' variant='h5'>Y</Typography>
                                        </Box>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
            </Card>
            <GradientLineChart
            title="Analytics Overview"
            description={
                <SoftBox display="flex" alignItems="center">
                <SoftBox fontSize={size.lg} color="success" mb={0.3} mr={0.5} lineHeight={0}>
                    <Icon className="font-bold">arrow_upward</Icon>
                </SoftBox>
                <SoftTypography variant="button" color="text" fontWeight="medium">
                    4% more{" "}
                    <SoftTypography variant="button" color="text" fontWeight="regular">
                    in 2021
                    </SoftTypography>
                </SoftTypography>
                </SoftBox>
            }
            height="20.25rem"
            chart={gradientLineChartData}
            />
       
      </SoftBox>
    </DashboardLayout>
  );
}

export default SingleGoalGraph;

const StyledGoal = styled(Typography)({
 borderRadius: '40px',
 textAlign: 'center',
 color: 'black',
 padding: '0.5rem 1rem'
});



