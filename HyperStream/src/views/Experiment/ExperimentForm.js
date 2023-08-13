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

function ExperimentForm({control}) {


  return (
    <Stack>
    <Typography mb={4}>Create your experiment</Typography>
    <FormControl>
      <Controller
        name="experiment"
        control={control}
        rules={{
          required: "Experiment description is required"
        }}
        render={({
          field: { ref, ...fields },
          fieldState: { error },
        }) => (
          <TextField
            {...fields}
            variant="outlined"
            placeholder="Descripe your experiment"
            fullWidth
            multiline
            minRows={5}
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

export default ExperimentForm