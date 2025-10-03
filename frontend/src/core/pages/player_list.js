// Players page component
// Fetches player data from the backend and displays it in a Material-UI table.

import React, { useEffect, useState } from 'react';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,
  CircularProgress, Alert
} from '@mui/material';

function Players() {
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/players') // backend URL
      .then((res) => {
        if (!res.ok) throw new Error('Network response not ok');
        return res.json();
      })
      .then((data) => {
        setPlayers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">Error: {error}</Alert>;

  return (
    <TableContainer component={Paper} sx={{ maxHeight: '80vh', overflow: 'auto' }}>
      <Table stickyHeader>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Nationality</TableCell>
            <TableCell>Shooting</TableCell>
            <TableCell>Passing</TableCell>
            <TableCell>Speed</TableCell>
            <TableCell>Stamina</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {players.map((p) => (
            <TableRow key={p.id}>
              <TableCell>{p.name}</TableCell>
              <TableCell>{p.nationality}</TableCell>
              <TableCell>{p.attributes.shooting}</TableCell>
              <TableCell>{p.attributes.passing}</TableCell>
              <TableCell>{p.attributes.speed}</TableCell>
              <TableCell>{p.attributes.stamina}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default Players;
