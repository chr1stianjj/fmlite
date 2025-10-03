import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';

export default function TopBar() {
  return (
    <AppBar position="static" sx={{ backgroundColor: '#455a64', height: 70 }}>
      <Toolbar>
        <Typography variant="h5">The Manager App</Typography>
      </Toolbar>
    </AppBar>
  );
}