from flask import Flask, render_template, request
import requests
from config import API_KEY  # Make sure this exists

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_runs = None
    recent_scores = []

    if request.method == "POST":
        player_name = request.form["player"]
        print(f"🔍 Searching for player: {player_name}")

        try:
            # Step 1: Search player by name
            player_search_url = f"https://api.cricapi.com/v1/players?apikey={API_KEY}&search={player_name}"
            search_response = requests.get(player_search_url).json()
            print("📥 Player Search API Response:", search_response)

            matched_player = None
            for player in search_response.get("data", []):
                if player["name"].lower() == player_name.lower():
                    matched_player = player
                    break

            if not matched_player:
                predicted_runs = "⚠️ Player not found"
                print("❌ No exact player match")
            else:
                print("✅ Matched Player:", matched_player)

                # ✅ Use dummy data for last 10 matches
                recent_scores = [34, 56, 45, 78, 49, 62, 50, 38, 70, 59]
                predicted_runs = round(sum(recent_scores) / len(recent_scores))

        except Exception as e:
            predicted_runs = "⚠️ Could not fetch player stats"
            print("🔥 Error occurred:", e)

    return render_template("index.html", predicted_runs=predicted_runs, recent_scores=recent_scores)

if __name__ == "__main__":
    app.run(debug=True)



