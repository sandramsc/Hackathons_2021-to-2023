// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

// @mui icons
import FacebookIcon from "@mui/icons-material/Facebook";
import TwitterIcon from "@mui/icons-material/Twitter";
import InstagramIcon from "@mui/icons-material/Instagram";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import Footer from "examples/Footer";
import DefaultProjectCard from "examples/Cards/ProjectCards/DefaultProjectCard";
import PlaceholderCard from "examples/Cards/PlaceholderCard";
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
// Images
// import SeeLess from "assets/svgs/seeless.svg";
import Avatar from '@mui/material/Avatar';
import AvatarGroup from '@mui/material/AvatarGroup';

import { ReactComponent as SeeLess } from "assets/svgs/seeless.svg";
import { ReactComponent as SeeMore } from "assets/svgs/seemore.svg";
import { ReactComponent as PlayBtn } from "assets/svgs/play.svg";
import { ReactComponent as PauseBtn } from "assets/svgs/pause.svg";


import homeDecor2 from "assets/images/home-decor-2.jpg";
import homeDecor3 from "assets/images/home-decor-3.jpg";
import team1 from "assets/images/team-1.jpg";
import team2 from "assets/images/team-2.jpg";
import team3 from "assets/images/team-3.jpg";
import team4 from "assets/images/team-4.jpg";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import { Box, Chip, IconButton, Stack, Typography } from "@mui/material";
import AddIcon from '@mui/icons-material/Add';
import { styled } from "@mui/system";
import Collapse from '@mui/material/Collapse';
import { useState } from "react";

function Overview() {
  const [openGoals, setOpenGoals] = useState({
    acquisition: false,
    referral: false,
    awareness: false,
    revenue: false,
    activation: false,
    retention: false,
    
  })

  console.log('amaka', openGoals)

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <Stack spacing={3} mt={4}>
        <Grid container spacing={5}>
          <Grid item xs={4}>
            <Stack direction='row' justifyContent='space-between'>
              <Stack direction='row' spacing={1}>
                <Typography>Scheduled</Typography>
                <Chip label="2" variant="outlined" color='error'/>
              </Stack>
              <IconButton aria-label="delete">
                <AddIcon />
              </IconButton>
            </Stack>
          </Grid>
          <Grid item xs={4}>
            <Stack direction='row' justifyContent='space-between'>
              <Stack direction='row' spacing={1}>
                <Typography>In progress</Typography>
                <Chip label="2" variant="outlined" color='info'/>
              </Stack>
              <IconButton aria-label="delete">
                <AddIcon />
              </IconButton>
            </Stack>
          </Grid>
          <Grid item xs={4}>
              <Stack direction='row' spacing={1}>
                <Typography>Completed</Typography>
                <Chip label="2" variant="outlined" color='success'/>
              </Stack>
          </Grid>
        </Grid>
        <Grid container spacing={2}>
          <Grid item xs={4}>
            <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: '#FCDFE2', width: '50%', marginBottom: '1rem'}} variant='body2'>Awareness</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.awareness ? 
                  <IconButton onClick={() => setOpenGoals({awareness: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({awareness: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.awareness} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={10}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>START</Typography>
                <IconButton >
                    <PlayBtn />
                </IconButton>
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>
          <Grid item xs={4}>
          <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: '#CDCCF1', width: '50%', marginBottom: '1rem'}} variant='body2'>Referral</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.referral ? 
                  <IconButton onClick={() => setOpenGoals({referral: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({referral: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.referral} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={4}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>In Progress 45%</Typography>
                <IconButton >
                    <PauseBtn />
                </IconButton>
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>
          <Grid item xs={4}>
          <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: ' #E6E5F8', width: '50%', marginBottom: '1rem'}} variant='body2'>Acquisition</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.acquisition ? 
                  <IconButton onClick={() => setOpenGoals({acquisition: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({acquisition: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.acquisition} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={7}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom sx={{backgroundColor: 'rgba(155, 222, 170, 0.26)'}}>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>SUCCESSFUL</Typography>
                {/* <IconButton >
                    <PlayBtn />
                </IconButton> */}
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>

          <Grid item xs={4}>
            <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: '#FFF3EB', width: '50%', marginBottom: '1rem'}} variant='body2'>Revenue</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.revenue ? 
                  <IconButton onClick={() => setOpenGoals({revenue: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({revenue: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.revenue} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={8}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>START</Typography>
                <IconButton >
                    <PlayBtn />
                </IconButton>
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>
          <Grid item xs={4}>
          <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: '#FACED4', width: '50%', marginBottom: '1rem'}} variant='body2'>Activation</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.activation ? 
                  <IconButton onClick={() => setOpenGoals({activation: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({activation: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.activation} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={5}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom sx={{backgroundColor: '#E6E5F8'}}>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>Paused 15%</Typography>
                <IconButton >
                    <PlayBtn />
                </IconButton>
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>
          <Grid item xs={4}>
          <StyledCard>
              <Box style={{padding: '0 1rem 0.5rem 1rem'}}>
                <StyledGoal sx={{backgroundColor: ' #E6E5F8', width: '50%', marginBottom: '1rem'}} variant='body2'>Retention</StyledGoal>
                <Stack direction='row' justifyContent='space-between'>
                  <Typography alignSelf='center'>Host an event</Typography>
                  {openGoals.retention ? 
                  <IconButton onClick={() => setOpenGoals({retention: false})}>
                    <SeeMore /> 
                  </IconButton>
                  :
                  <IconButton onClick={() => setOpenGoals({retention: true})}>
                      <SeeLess />
                  </IconButton> }
                </Stack>
                <Collapse in={openGoals.retention} timeout="auto" unmountOnExit>
                    <Typography variant='body2'>Increase purchases via website for 45%</Typography>
                    <Typography variant='subtitle2'>Start date: 25/12/2022</Typography>
                    <AvatarGroup total={5}>
                      <Avatar alt="Remy Sharp" src={team1} />
                      <Avatar alt="Travis Howard" src={team2} />
                      <Avatar alt="Agnes Walker" src={team3} />
                      <Avatar alt="Trevor Henderson" src={team4} />
                    </AvatarGroup>
                </Collapse>
              </Box>
              <StyledBottom sx={{backgroundColor: 'rgba(247, 174, 183, 0.2)'}}>
              <Stack direction='row' spacing={1} justifyContent='center'>
                <Typography alignSelf='center'>FAILED</Typography>
                {/* <IconButton >
                    <PlayBtn />
                </IconButton> */}
              </Stack>
              </StyledBottom>
            </StyledCard>
          </Grid>
        </Grid>
      </Stack>

    </DashboardLayout>
  );
}

export default Overview;

const StyledGoal = styled(Typography)({
  borderRadius: '40px',
  textAlign: 'center',
  color: 'black',
  padding: '0.5rem 1rem'
 });

 const StyledCard = styled(Box)({
  background: '#F0F0FB',
  borderRadius: '45px',
  paddingTop: '1rem'
 });

 const StyledBottom = styled(Box)({
    backgroundColor: '#D4EFF5',
    borderRadius: '0 0 45px 45px',
    padding: '1rem',
    textAlign: 'center'
});
