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
  Button,
} from "@mui/material";
import { Controller } from 'react-hook-form';

function AddParticipant({control, register, setValue}) {

  const emails = [];

  const [allEmails, setAllEmails] = React.useState(emails);
  const [teammate, setTeammate] = React.useState('');

  const handleChange = (event) => {
    setTeammate(event.target.value);
  };

  const handleAddTeammate = () => {
    setAllEmails( arr => [...arr, teammate])
    setTeammate('')
    console.log(allEmails)
    setValue("teammates", allEmails)

  }

  

  return (
    <Stack>
    <Typography mb={4}>Your experiment has been set!</Typography>
    <Typography mb={4}>Add a teammate</Typography>
    <TextField
        id="outlined-name"
        value={teammate}
        onChange={handleChange}
        placeholder="example@gmail.com"
        variant="outlined"
        fullWidth
      />
    <input {...register("teammates")}  type="hidden"/>
    <Button
      variant="contained"
      onClick={handleAddTeammate}
      sx={{ color: '#fff', borderRadius: '20px', margin: '1rem 0', width: '30%' }}
      >
      Add Teammate
      </Button>
    <Stack direction='row' spacing={2}>
      {allEmails.map((c) => (
          <Chip
            variant='filled'
            label={c}
            color="secondary"
          />
      ))}
    </Stack>
     
    </Stack>
  )
}

export default AddParticipant;