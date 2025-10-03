import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Box, Typography, Card, CardContent } from '@mui/material';

export default function PlayerView() {
  const { id } = useParams(); // read player ID from URL
  const [player, setPlayer] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/players/${id}`)
      .then(res => res.json())
      .then(data => setPlayer(data))
      .catch(err => console.error(err));
  }, [id]);

  if (!player) return <div>Loading...</div>;

  return (
    <Box sx={{ p: 4 }}>
      <Card>
        <CardContent>
          <Typography variant="h4">{player.name}</Typography>
          <Typography>Nationality: {player.nationality}</Typography>
          <Typography>Date of Birth: {player.dob}</Typography>
          <Typography>Shooting: {player.attributes.shooting}</Typography>
          <Typography>Passing: {player.attributes.passing}</Typography>
          <Typography>Speed: {player.attributes.speed}</Typography>
          <Typography>Stamina: {player.attributes.stamina}</Typography>
        </CardContent>
      </Card>
    </Box>
  );
}
