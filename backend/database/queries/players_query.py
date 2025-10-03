"""
players.py

Purpose: Provide functions to query player data from the storage layer (data.json for now).
This abstracts the storage details away from the API router.
"""

import json
from pathlib import Path

# Path to your JSON file
DATA_FILE = Path(__file__).parent.parent / "data.json"


def queryPlayers():
    """
    Retrieve all players from data.json.

    Why:
    - Keeps the router decoupled from storage.
    - Makes swapping JSON for a real database later easy.
    """
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data.get("players", [])


def queryPlayerById(player_id: int):
    """
    Retrieve a single player by ID.

    Why:
    - Allows routers to fetch one player without reading/filtering in the router.
    """
    players = queryPlayers()
    for player in players:
        if player["id"] == player_id:
            return player
    return None
