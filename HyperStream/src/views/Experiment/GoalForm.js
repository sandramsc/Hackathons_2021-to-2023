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

function GoalForm({control, setValue, register}) {

  const listOfChips = [
    { id: "4", name: "Awareness" },
    { id: "5", name: "Acquisition" },
    { id: "6", name: "Activation" },
    { id: "7", name: "Retention" },
    { id: "8", name: "Revenue" },
    { id: "10", name: "Referral" }
  ]
  const [selected, setSelected] = React.useState('');

  function handleSelectionChanged(name) {
    setSelected(name)
    setValue("category", name)
  }


  return (
    <Stack>
    <Typography mb={4}>Give your goal a name</Typography>
    <FormControl>
      <Controller
        name="goalName"
        control={control}
        rules={{
          required: "Goal name is required"
        }}
        render={({
          field: { ref, ...fields },
          fieldState: { error },
        }) => (
          <TextField
            {...fields}
            variant="outlined"
            placeholder="Name of the goal"
            fullWidth
            inputRef={ref}
            error={Boolean(error?.message)}
            helperText={error?.message || " "}
          />
        )}
      />
    </FormControl>
    <input {...register("category")}  type="hidden"/>
    <Typography mb={4}>Which area are you looking to improve?</Typography>
          <Grid container spacing={2}>
            {listOfChips.map((c) => (
              <Grid item xs={4} key={c.id}>
                <Chip
                  onClick={() => handleSelectionChanged(c.name)}
                  variant={selected === c.name ? "filled" : "outlined"}
                  label={c.name}
                  color="primary"
                />
              </Grid>
            ))}
          </Grid>
      <Stack direction="row" spacing={4}>
      
      </Stack>
      
    </Stack>
  )
}

export default GoalForm