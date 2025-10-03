# fetch_api/players/fetchPlayers.py
from flask import Blueprint, jsonify
from fetch_api.fetchHandler import FetchHandler  # Make sure this path matches your folder structure

# Blueprint for player-related routes
players_bp = Blueprint('players', __name__, url_prefix='/api/players')

# Initialize the fetch handler
fetch_handler = FetchHandler()

@players_bp.route('/', methods=['GET'])
def get_players():
    """
    GET /api/players/
    
    Returns the list of all players in JSON format.
    Frontend calls this endpoint to get the player list.
    
    Errors:
        404 - If the JSON file doesn't exist
        500 - Any other unexpected error
    """
    try:
        players = fetch_handler.get_players()
        return jsonify(players)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
