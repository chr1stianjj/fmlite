import json
from random import randint, choice

teams = [
    {"id": 1, "name": "Team Argentina", "playerIds": []},
    {"id": 2, "name": "Team Brazil", "playerIds": []},
    {"id": 3, "name": "Team Spain", "playerIds": []},
    {"id": 4, "name": "Team Germany", "playerIds": []},
]

nationalities = ["Argentina", "Brazil", "Spain", "Germany"]
players = []

player_id = 1
for team in teams:
    for i in range(12):  # 11+1 players per team
        dob_year = randint(1990, 2002)
        dob_month = randint(1, 12)
        dob_day = randint(1, 28)  # avoid invalid dates
        player = {
            "id": player_id,
            "name": f"Player {player_id}",
            "dob": f"{dob_year}-{dob_month:02}-{dob_day:02}",
            "nationality": choice(nationalities),
            "attributes": {
                "shooting": randint(65, 90),
                "passing": randint(65, 90),
                "speed": randint(65, 90),
                "stamina": randint(65, 90)
            },
            "teamId": team["id"]
        }
        players.append(player)
        team["playerIds"].append(player_id)
        player_id += 1

matches = [
    {
        "id": 1,
        "homeTeamId": 1,
        "awayTeamId": 2,
        "homeScore": randint(0,5),
        "awayScore": randint(0,5),
        "date": "2025-10-01"
    },
    {
        "id": 2,
        "homeTeamId": 3,
        "awayTeamId": 4,
        "homeScore": randint(0,5),
        "awayScore": randint(0,5),
        "date": "2025-10-02"
    }
]

data = {
    "players": players,
    "teams": [{"id": t["id"], "name": t["name"], "playerIds": t["playerIds"]} for t in teams],
    "matches": matches
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("data.json generated with 48 players, 4 teams, 2 matches.")