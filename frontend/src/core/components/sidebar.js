import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import HomeIcon from '@mui/icons-material/Home';
import PersonIcon from '@mui/icons-material/Person';
import GroupIcon from '@mui/icons-material/Group';
import SportsSoccerIcon from '@mui/icons-material/SportsSoccer';

export default function Sidebar({ setCurrentPage }) {
  const sidebarItems = [
    { name: 'Main', icon: <HomeIcon /> },
    { name: 'Players', icon: <PersonIcon /> },
    { name: 'Teams', icon: <GroupIcon /> },
    { name: 'Matches', icon: <SportsSoccerIcon /> }
  ];

  return (
    <Drawer
      variant="permanent"
      anchor="left"
      PaperProps={{ sx: { width: 240, top: 70, height: 'calc(100% - 70px)' } }}
    >
      <List>
        {sidebarItems.map((item) => (
          <ListItem button key={item.name} onClick={() => setCurrentPage(item.name)}>
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.name} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}
