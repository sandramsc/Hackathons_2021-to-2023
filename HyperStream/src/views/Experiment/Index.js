import { Box, Button, CircularProgress, Grid, Stack, Typography } from '@mui/material'
import DashboardLayout from 'examples/LayoutContainers/DashboardLayout'
import DashboardNavbar from 'examples/Navbars/DashboardNavbar'
import React from 'react'
import CustomStepper from './Stepper'
import { useForm } from "react-hook-form";
import GoalForm from './GoalForm'
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ExperimentForm from './ExperimentForm'
import MeasurementForm from './MeasurementForm'
import Feasibility from './Feasibility'
import AddParticipant from './AddParticipant'
import { collection, addDoc, getDocs } from "firebase/firestore";
import {db} from '../../firebase';


function Index() {
    const [loading, setLoading] = React.useState(false)
    const [activeStep, setActiveStep] = React.useState(0);

    const {
        handleSubmit,
        control,
        register,
        setValue,
        formState: { isDirty, isValid },
      } = useForm({ mode: "onChange" });


    const handleNext = () => {
      setActiveStep((prevActiveStep) => prevActiveStep + 1);
    };
  
    const handleBack = () => {
      setActiveStep((prevActiveStep) => prevActiveStep - 1);
    };

    const onSubmit = async(data) => {
        console.log(data)
        // setLoading(true)
        try {
          const docRef = await addDoc(collection(db, "Goal"), data);
          setLoading(false)
          console.log("Document written with ID: ", docRef.id);
        } catch (e) {
          console.error("Error adding document: ", e);
        }

    } 

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <Typography>New Experiment</Typography>
      <Grid container spacing={1}>
          <Grid item xs={3}>
            <CustomStepper activeStep={activeStep} setActiveStep={setActiveStep}/>
          </Grid>
          <Grid item xs={7}>
            {
                activeStep === 0 ?
                <GoalForm control={control} setValue={setValue} register={register}/> :
                activeStep === 1 ?
                <ExperimentForm control={control}/> :
                activeStep === 2 ?
                <MeasurementForm control={control}/> :
                activeStep === 3 ?
                <Feasibility control={control}/> :
                activeStep === 4 ?
                <MeasurementForm control={control}/> :
                <AddParticipant control={control} setValue={setValue} register={register}/>
            }
            <Stack sx={{ mt: 9}} direction='row' justifyContent='space-between'>
                
                <Button
                disabled={activeStep === 0}
                onClick={handleBack}
                variant="outlined"
                startIcon={<ArrowBackIosIcon />}
                sx={{ mt: 1, mr: 1, color: '#29B1CE', borderRadius:  '20px'}}
                >
                Back
                </Button>
                
                  <Button
                  variant="contained"
                  endIcon={<ArrowForwardIosIcon />}
                  onClick={activeStep < 5 ? handleNext : handleSubmit(onSubmit)}
                  sx={{ mt: 1, mr: 1, color: '#fff', borderRadius: '20px' }}
                  >
                    {
                      loading ? 
                      <CircularProgress color="secondary" size='small'/>:
                        activeStep === 5 ? 'Finish' : 'Continue'
                    }
                  </Button>
            </Stack>
          </Grid>
      </Grid>
      
    </DashboardLayout>
  )
}

export default Index