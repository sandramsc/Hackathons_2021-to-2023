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

function MeasurementForm({control}) {


  return (
    <Stack>
    <Typography mb={4}>What is the measurement of the experiment?</Typography>
    <FormControl>
      <Controller
        name="measurement"
        control={control}
        rules={{
          required: "Measurement is required"
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
    <Typography mb={4}>Set your values to measure success:</Typography>
    <Stack spacing={4}>
    <Stack direction="row" spacing={4}>
    <Typography>Expectations:</Typography>
        <FormControl>
        <Controller
            name="expectation"
            control={control}
            
            rules={{
            required: "Expectation is required"
            }}
            render={({
            field: { ref, ...fields },
            fieldState: { error },
            }) => (
            <TextField
                {...fields}
                variant="outlined"
                placeholder="50"
                fullWidth
                inputRef={ref}
                error={Boolean(error?.message)}
                helperText={error?.message || " "}
            />
            )}
        />
        </FormControl>
    </Stack>
    <Stack direction="row" spacing={4}>
        <Typography>Success:</Typography>
        <FormControl>
        <Controller
            name="successFrom"
            control={control}
            rules={{
            required: "Expectation is required"
            }}
            render={({
            field: { ref, ...fields },
            fieldState: { error },
            }) => (
            <TextField
                {...fields}
                variant="outlined"
                InputLabelProps={{
                    shrink: true,
                  }}
                  label='From'
                placeholder="50"
                fullWidth
                inputRef={ref}
                error={Boolean(error?.message)}
                helperText={error?.message || " "}
            />
            )}
        />
        </FormControl>
        <FormControl>
        <Controller
            name="successTo"
            control={control}
            rules={{
            required: "required"
            }}
            render={({
            field: { ref, ...fields },
            fieldState: { error },
            }) => (
            <TextField
                {...fields}
                variant="outlined"
                InputLabelProps={{
                    shrink: true,
                  }}
                  label='To'
                placeholder="100"
                fullWidth
                inputRef={ref}
                error={Boolean(error?.message)}
                helperText={error?.message || " "}
            />
            )}
        />
        </FormControl>
    </Stack>
    <Stack direction="row" spacing={4}>
        <Typography>Failure:</Typography>
        <FormControl>
        <Controller
            name="failureFrom"
            control={control}
            rules={{
            required: "required"
            }}
            render={({
            field: { ref, ...fields },
            fieldState: { error },
            }) => (
            <TextField
                {...fields}
                label='From'
                InputLabelProps={{
                    shrink: true,
                  }}
                variant="outlined"
                placeholder="0"
                fullWidth
                inputRef={ref}
                error={Boolean(error?.message)}
                helperText={error?.message || " "}
            />
            )}
        />
        </FormControl>
        <FormControl>
        <Controller
            name="failureTo"
            control={control}
            rules={{
            required: "required"
            }}
            render={({
            field: { ref, ...fields },
            fieldState: { error },
            }) => (
            <TextField
                {...fields}
                label='To'
                InputLabelProps={{
                    shrink: true,
                  }}
                variant="outlined"
                fullWidth
                placeholder="49"
                inputRef={ref}
                error={Boolean(error?.message)}
                helperText={error?.message || " "}
            />
            )}
        />
        </FormControl>
    </Stack>
    </Stack>
    
    </Stack>
  )
}

export default MeasurementForm