/* eslint-disable */

import React from 'react'
import {
  Box,
  Stack,
  styled,
  TextField,
  Typography,
  FormControl,
  Tooltip,
  InputAdornment,
  CircularProgress,
  Chip,
  Grid,
} from "@mui/material";
import { Controller } from 'react-hook-form';

function Feasibility({control}) {

  return (
    <Stack>
    <Typography mb={4}>When do you want to achieve this?</Typography>
    <FormControl>
      <Controller
        name="deadline"
        control={control}
        rules={{
          required: "Deadline is required"
        }}
        render={({
          field: { ref, ...fields },
          fieldState: { error },
        }) => (
          <TextField
            {...fields}
            variant="outlined"
            placeholder="DD/MM/YYYY"
            fullWidth
            inputRef={ref}
            error={Boolean(error?.message)}
            helperText={error?.message || " "}
          />
        )}
      />
    </FormControl>
    <Typography mb={4}>What is the budget for this experiment?</Typography>
    <FormControl>
      <Controller
        name="budget"
        control={control}
        rules={{
          required: "Budget is required"
        }}
        render={({
          field: { ref, ...fields },
          fieldState: { error },
        }) => (
          <TextField
            {...fields}
            variant="outlined"
            placeholder="Start tapping here..."
            fullWidth
            inputRef={ref}
            error={Boolean(error?.message)}
            helperText={error?.message || " "}
          />
        )}
      />
    </FormControl>
    </Stack>
  )
}

export default Feasibility;