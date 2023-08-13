/* eslint-disable */

import * as React from 'react';
import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import StepContent from '@mui/material/StepContent';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

const steps = [
  {
    label: 'Goal',
  },
  {
    label: 'Experiment',
  },
  {
    label: 'Measurements',
  },
  {
    label: 'Feasibility',
  },
  {
    label: 'Summary',
  },
  {
    label: 'Participants',
  },
];

export default function CustomStepper({activeStep, setActiveStep}) {


  return (
    <Box sx={{ maxWidth: 400 }}>
      <Stepper activeStep={activeStep} orientation="vertical">
        {steps.map((step, index) => (
          <Step key={step.label}>
            <StepLabel>
              {step.label}
            </StepLabel>
          </Step>
        ))}
      </Stepper>
    </Box>
  );
}