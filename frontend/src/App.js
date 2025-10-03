import React, { useState } from 'react';
import { Box } from '@mui/material';
import TopBar from './core/components/topbar';
import Sidebar from './core/components/sidebar';
import Players from './core/pages/players';

function App() {
  const [currentPage, setCurrentPage] = useState('Main');
  const drawerWidth = 240;

  let pageContent;
  if (currentPage === 'Players') {
    pageContent = <Players />;
  } else {
    pageContent = <div>Main page (empty)</div>;
  }

  return (
    <div>
      <TopBar />
      <Box sx={{ display: 'flex' }}>
        <Sidebar setCurrentPage={setCurrentPage} />
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            p: 4,
            marginLeft: `${drawerWidth}px`,
            minHeight: '100vh',
            backgroundColor: '#f9f9f9'
          }}
        >
          {pageContent}
        </Box>
      </Box>
    </div>
  );
}

export default App;
