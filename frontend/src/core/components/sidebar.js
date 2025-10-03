import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import GroupIcon from '@mui/icons-material/Group';
import LeagueIcon from '@mui/icons-material/EmojiEvents';

export default function SidebarNav({ setCurrentPage }) {
  const sidebarItems = [
    { name: 'Players', icon: <PersonIcon /> },
    { name: 'Teams', icon: <GroupIcon /> },
    { name: 'Leagues', icon: <LeagueIcon /> }
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