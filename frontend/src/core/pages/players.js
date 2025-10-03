import React, { useState, useEffect } from 'react';
import { Box, Grid, Avatar, Typography, Button, Drawer, TextField, IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';

export default function PlayersPage() {
  const [players, setPlayers] = useState([]);
  const [selectedPlayerIndex, setSelectedPlayerIndex] = useState(null);
  const [editingPlayer, setEditingPlayer] = useState(null);

  // Fetch players from backend on mount
  useEffect(() => {
    fetch('/api/players/')
      .then(res => res.json())
      .then(data => setPlayers(data))
      .catch(err => console.error('Failed to fetch players:', err));
  }, []);

  const handleSelectPlayer = (index) => {
    setSelectedPlayerIndex(index);
    setEditingPlayer({ ...players[index] });
  };

  const handleCloseDrawer = () => {
    setSelectedPlayerIndex(null);
    setEditingPlayer(null);
  };

  const handleChange = (field, value) => {
    if (field in editingPlayer.attributes) {
      setEditingPlayer({
        ...editingPlayer,
        attributes: { ...editingPlayer.attributes, [field]: value }
      });
    } else {
      setEditingPlayer({ ...editingPlayer, [field]: value });
    }
  };

  const handleSave = () => {
    const updatedPlayers = [...players];
    updatedPlayers[selectedPlayerIndex] = editingPlayer;
    setPlayers(updatedPlayers);
    handleCloseDrawer();
  };

  const handleAddPlayer = () => {
    const newPlayer = {
      id: players.length + 1,
      name: `Player ${players.length + 1}`,
      nationality: 'Unknown',
      teamId: 0,
      attributes: { shooting: 70, passing: 70, speed: 70, stamina: 70 }
    };
    setPlayers([...players, newPlayer]);
  };

  return (
    <Box sx={{ padding: 4 }}>
      <Button variant="contained" color="primary" onClick={handleAddPlayer} sx={{ marginBottom: 3 }}>
        Add Player
      </Button>

      <Grid container spacing={1} direction="column">
        {players.map((player, index) => (
          <Grid item key={player.id}>
            <Box
              sx={{
                display: 'flex',
                alignItems: 'center',
                padding: 1,
                backgroundColor: index % 2 === 0 ? '#f5f5f5' : '#eceff1',
                borderRadius: 1,
                cursor: 'pointer',
                '&:hover': { boxShadow: 2 }
              }}
              onClick={() => handleSelectPlayer(index)}
            >
              <Avatar sx={{ marginRight: 2 }}>{player.name.split(' ').map(n => n[0]).join('')}</Avatar>

              <Box sx={{ width: 200 }}>
                <Typography variant="subtitle1">{player.name}</Typography>
                <Typography variant="body2">Nationality: {player.nationality}</Typography>
                <Typography variant="body2">Team ID: {player.teamId}</Typography>
              </Box>

              <Box sx={{ display: 'flex', flex: 1, justifyContent: 'space-around' }}>
                <Typography>Shooting: {player.attributes?.shooting}</Typography>
                <Typography>Passing: {player.attributes?.passing}</Typography>
                <Typography>Speed: {player.attributes?.speed}</Typography>
                <Typography>Stamina: {player.attributes?.stamina}</Typography>
              </Box>
            </Box>
          </Grid>
        ))}
      </Grid>

      <Drawer
        anchor="right"
        open={selectedPlayerIndex !== null}
        onClose={handleCloseDrawer}
        PaperProps={{ sx: { width: 300, padding: 2, backgroundColor: '#eceff1' } }}
      >
        {editingPlayer && (
          <>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <Typography variant="h5">Edit Player</Typography>
              <IconButton onClick={handleCloseDrawer}><CloseIcon /></IconButton>
            </Box>

            <Box sx={{ marginTop: 2, display: 'flex', flexDirection: 'column', gap: 2 }}>
              <TextField
                label="Name"
                value={editingPlayer.name}
                onChange={(e) => handleChange('name', e.target.value)}
              />
              <TextField
                label="Shooting"
                type="number"
                value={editingPlayer.attributes?.shooting}
                onChange={(e) => handleChange('shooting', Number(e.target.value))}
              />
              <TextField
                label="Passing"
                type="number"
                value={editingPlayer.attributes?.passing}
                onChange={(e) => handleChange('passing', Number(e.target.value))}
              />
              <TextField
                label="Speed"
                type="number"
                value={editingPlayer.attributes?.speed}
                onChange={(e) => handleChange('speed', Number(e.target.value))}
              />
              <TextField
                label="Stamina"
                type="number"
                value={editingPlayer.attributes?.stamina}
                onChange={(e) => handleChange('stamina', Number(e.target.value))}
              />
              <Button variant="contained" color="primary" onClick={handleSave}>Save</Button>
            </Box>
          </>
        )}
      </Drawer>
    </Box>
  );
}
