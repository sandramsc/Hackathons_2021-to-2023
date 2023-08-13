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

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

// Data
import { styled } from "@mui/system";
import { Box, Divider, Grid, Stack, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { collection,  getDocs } from "firebase/firestore";
import {db} from '../../firebase';
import { useEffect, useState } from "react";

function Goals() {
  const navigate = useNavigate();
  const [goals, setGoals] = useState([]);

  const navigateToSIngleGoal = (id) => {
    navigate(`/goals/${id}`);
  }

  const fetchPost = async () => {
       
    await getDocs(collection(db, "growthapp"))
        .then((querySnapshot)=>{              
            const newData = querySnapshot.docs
                .map((doc) => ({...doc.data(), id:doc.id }));
                setGoals(newData);                
            console.log(goals, newData);
        })
      
    }

    console.log('amaka', goals)

    useEffect(()=>{
        fetchPost();
    }, [])

    // const 

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox py={3}>
      <Grid container spacing={5}>
          {
            dummyData?.map((val) => (
              <Grid item xs={6} key={val.id} onClick={() => navigateToSIngleGoal(val.id)}>
                  <StyledCard  >
                    <StyledGoal variant="body2" mb={4} sx={{backgroundColor: val.bgColor}}>{val.goal}</StyledGoal>
                    <Stack direction='row' justifyContent='space-around'>
                      <Box sx={{textAlign: 'center'}}>
                        <Typography variant="h1" >{val.goalNo}</Typography>
                        <Typography>Goals</Typography>
                      </Box>
                      <Divider sx={{backgroundColor: 'red'}}/>
                      <Box sx={{textAlign: 'center'}}>
                        <Typography variant="h1" >{val.experimentNo}</Typography>
                        <Typography >Experiments</Typography>
                      </Box>
                    </Stack>
                  </StyledCard>
              </Grid>
            ))
          }
          
      </Grid>
        <Card>
          
        </Card>
      </SoftBox>
    </DashboardLayout>
  );
}

export default Goals;

const StyledGoal = styled(Typography)({
 borderRadius: '40px',
 width: '50%',
 textAlign: 'center',
 color: 'black',
 padding: '0.5rem'
});

const StyledCard = styled(Card)({
  padding: '1rem',

  "&:hover": {
      cursor: 'pointer',
      padding: '1.5rem',
  },
 });


const dummyData = [
  {
    id: '3992',
    goal: 'Awarness',
    bgColor: '#FCDFE2',
    goalNo: 6,
    experimentNo: 9
  },
  {
    id: '3332',
    goal: 'Aquisition',
    bgColor: '#CDCCF1',
    goalNo: 1,
    experimentNo: 3
  },
  {
    id: '30004',
    goal: 'Activation',
    bgColor: '#E6E5F8',
    goalNo: 0,
    experimentNo: 3
  },
  {
    id: '32304',
    goal: 'Revenue',
    bgColor: '#FEDCC4',
    goalNo: 2,
    experimentNo: 3
  },
  {
    id: '32304',
    goal: 'Referral',
    bgColor: '#FACED4',
    goalNo: 2,
    experimentNo: 3
  },
  {
    id: '32304',
    goal: 'Retention',
    bgColor: '#FFF3EB',
    goalNo: 2,
    experimentNo: 3
  },
]
