from fastapi import APIRouter, HTTPException
from backend.database.queries.players_query import queryPlayers, queryPlayerById

router = APIRouter()

@router.get("/")
def get_players():
    # Return all players via query function
    return queryPlayers()

@router.get("/{player_id}")
def get_player(player_id: int):
    # Return a single player or raise 404 if not found
    player = queryPlayerById(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
