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

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import Table from "examples/Tables/Table";

// Data
import { styled } from "@mui/system";
import { Box,Grid, Stack, Typography } from "@mui/material";
import { Link, useNavigate, useParams } from "react-router-dom";
import SoftButton from "components/SoftButton";

function SingleGoal() {
  const navigate = useNavigate();
  const { id } = useParams();

  const navigateToSIngleGoal = () => {
    navigate(`/goals/${id}/graph`);
  }

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox py={3}>
        <Stack direction= 'row' spacing={3} mb={4}>
        <StyledGoal sx={{backgroundColor: '#FCDFE2'}} variant='body2'>Awareness</StyledGoal>
        <Typography alignSelf='center' color='#515152'>Goal: Increase user sign ups by 12,000</Typography>
        </Stack>
      <Grid container spacing={2} >
            <Grid item xs={4} onClick={() => navigateToSIngleGoal()}>
                <Card sx={{ padding: '1rem'}} >
                <Box >
                    <Typography color='#515152' variant="h1" fontWeight={700}>7</Typography>
                    <Typography color='#515152'>Completed experiments</Typography>
                </Box>
                </Card>
            </Grid>
              <Grid item xs={4} onClick={() => navigateToSIngleGoal()}>
                  <Card sx={{ padding: '1rem'}} >
                    <Box >
                        <Typography color='#515152' variant="h1" fontWeight={700}>4</Typography>
                        <Typography color='#515152'>Successful experiments</Typography>
                    </Box>
                  </Card>
              </Grid>
              <Grid item xs={4} onClick={() => navigateToSIngleGoal()}>
                  <Card sx={{ padding: '1rem'}} >
                    <Box >
                        <Typography color='#515152' variant="h1" fontWeight={700}>3</Typography>
                        <Typography color='#515152'>Unsuccessful experiments</Typography>
                    </Box>
                  </Card>
              </Grid>
      </Grid>
        <Box mt={4} mb={4} textAlign="center">
        <SoftButton
              component={Link}
              to='/new-experiment'
              color='primary'
                sx={{borderRadius: '20px'}}
            >
              Run a new experiment
            </SoftButton>
        </Box>
        <Box>
            <Typography color='#515152'>Ongoing experiments</Typography>
            <Stack my={4}>
                <ExperimentCard >
                    <Grid container spacing={2} onClick={() => navigateToSIngleGoal()}>
                        <Grid item xs={6}>
                                <Box >
                                    <Typography variant='subtitle2' color='#515152'>Experiment #02</Typography>
                                    <Typography variant='h5' color='#515152'>Run an Instagram ad</Typography>
                                </Box>
                        </Grid>
                        <Grid item xs={6}>
                            <Grid container spacing={2} >
                                <Grid item xs={4}>
                                        <Box>
                                            <Typography  variant='subtitle2' color='#515152'>Time left</Typography>
                                            <Typography variant='h5' color='#515152'>4 days</Typography>
                                        </Box>
                                </Grid>
                                <Grid item xs={4}>
                                        <Box >
                                            <Typography  variant='subtitle2' color='#515152'>Budget</Typography>
                                            <Typography variant='h5' color='#515152'>£1,000</Typography>
                                        </Box>
                                </Grid>
                                <Grid item xs={4}>
                                        <Box >
                                            <Typography  variant='subtitle2' color='#515152'>On track</Typography>
                                            <Typography variant='h5' color='#515152'>Y</Typography>
                                        </Box>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
                </ExperimentCard>
            </Stack>
        </Box>
        <Box>
            <Typography>Successful experiments</Typography>
            <Stack spacing={3} my={4}>
                <ExperimentCard >
                    <Grid container spacing={2} onClick={() => navigateToSIngleGoal()}>
                        <Grid item xs={6}>
                                <Box >
                                    <Typography  color='#515152'variant='subtitle2'>Experiment #04</Typography>
                                    <Typography color='#515152' variant='h5'>Collaborate with an influencer</Typography>
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
                </ExperimentCard>
                <ExperimentCard >
                    <Grid container spacing={2} onClick={() => navigateToSIngleGoal()}>
                        <Grid item xs={6}>
                                <Box >
                                    <Typography  color='#515152'variant='subtitle2'>Experiment #03</Typography>
                                    <Typography color='#515152' variant='h5'>Host an event</Typography>
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
                </ExperimentCard>
            </Stack>
        </Box>
        <Box>
            <Typography>Unsuccessful experiments</Typography>
            <Stack spacing={3} my={4}>
                <ExperimentCard >
                    <Grid container spacing={2} onClick={() => navigateToSIngleGoal()}>
                        <Grid item xs={6}>
                                <Box >
                                    <Typography  color='#515152'variant='subtitle2'>Experiment #07</Typography>
                                    <Typography color='#515152' variant='h5'>Email marketing</Typography>
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
                </ExperimentCard>
                <ExperimentCard >
                    <Grid container spacing={2} onClick={() => navigateToSIngleGoal()}>
                        <Grid item xs={6}>
                                <Box >
                                    <Typography  color='#515152'variant='subtitle2'>Experiment #10</Typography>
                                    <Typography color='#515152' variant='h5'>SEO</Typography>
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
                </ExperimentCard>
            </Stack>
        </Box>
      </SoftBox>
    </DashboardLayout>
  );
}

export default SingleGoal;

const StyledGoal = styled(Typography)({
 borderRadius: '40px',
 textAlign: 'center',
 color: 'black',
 padding: '0.5rem 1rem'
});


const ExperimentCard = styled(Card)({
    padding: '1.5rem',

    "&:hover": {
        cursor: 'pointer',
        padding: '2rem',
    },
});




//   // Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getFirestore } from 'firebase/firestore';
// // TODO: Add SDKs for Firebase products that you want to use
// // https://firebase.google.com/docs/web/setup#available-libraries

// // Your web app's Firebase configuration
// const firebaseConfig = {
//   apiKey: "AIzaSyAeRm28trEfelFpc4YCoCoujRGtZy5iZ8o",
//   authDomain: "growth-tool.firebaseapp.com",
//   projectId: "growth-tool",
//   storageBucket: "growth-tool.appspot.com",
//   messagingSenderId: "75430112024",
//   appId: "1:75430112024:web:b5f313bbe1fda9ea788c6d"
// };

// // Initialize Firebase
// const app = initializeApp(firebaseConfig);

// export const db = getFirestore(app);



