# backend/core/backend_emulator.py
from flask import Flask, jsonify
from flask_cors import CORS

# Correct import path for your structure
from fetch_api.players.fetchPlayers import players_bp

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Register the players blueprint
app.register_blueprint(players_bp)

click_count = 0

@app.route('/api/button')
def button():
    global click_count
    click_count += 1
    return jsonify({"message": f"Clicked {click_count} times!"})

if __name__ == '__main__':
    # Set working directory to core to avoid import errors
    import os, sys
    sys.path.append(os.path.dirname(__file__))
    app.run(debug=True)
