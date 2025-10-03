# fetch_api/fetchHandler.py
import json
from pathlib import Path

class FetchHandler:
    """
    Handles all data retrieval from the backend.
    Right now it reads from a JSON file.
    Later, you can replace this with database calls without changing the frontend.
    """

    def __init__(self, json_path=None):
        """
        Initialize the handler with the path to the JSON file.
        If no path is provided, it defaults to the data.json in backend/core/database/.
        """
        if json_path is None:
            json_path = Path(__file__).parent / 'backend/core/database/data.json'
        self.json_path = Path(json_path)

    def _load_data(self):
        """
        Internal method to read the JSON file and return the full data dictionary.
        Raises FileNotFoundError if the file is missing.
        """
        if not self.json_path.exists():
            raise FileNotFoundError(f"{self.json_path} does not exist")
        with open(self.json_path, 'r') as f:
            return json.load(f)

    def get_players(self):
        """
        Returns the list of players from the JSON file.
        Returns an empty list if 'players' section is missing.
        """
        data = self._load_data()
        return data.get('players', [])

    def get_teams(self):
        """
        Returns the list of teams from the JSON file.
        Returns an empty list if 'teams' section is missing.
        """
        data = self._load_data()
        return data.get('teams', [])

    def get_matches(self):
        """
        Returns the list of matches from the JSON file.
        Returns an empty list if 'matches' section is missing.
        """
        data = self._load_data()
        return data.get('matches', [])
