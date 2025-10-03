import React, { useState } from 'react';
import { Box, Typography } from '@mui/material';
import TopBar from './core/components/topbar';
import Sidebar from './core/components/sidebar';
import Players from './core/pages/players';

function App() {
  const [currentPage, setCurrentPage] = useState('Players');

  const drawerWidth = 240; // must match Sidebar width

  return (
    <div>
      {/* Top Bar */}
      <TopBar />

      <Box sx={{ display: 'flex' }}>
        {/* Permanent Sidebar */}
        <Sidebar setCurrentPage={setCurrentPage} />

        {/* Main content */}
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            p: 4,
            marginLeft: `${drawerWidth}px`, // offset so content is not behind sidebar
            minHeight: '100vh',
            backgroundColor: '#f9f9f9'
          }}
        >
          {currentPage === 'Players' ? (
            <Players />
          ) : (
            <Typography variant="h6" sx={{ mt: 4 }}>
              {currentPage} page under development
            </Typography>
          )}
        </Box>
      </Box>
    </div>
  );
}

export default App;
