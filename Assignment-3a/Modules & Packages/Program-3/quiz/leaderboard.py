import os

LEADERBOARD_FILE = "leaderboard.txt"

def save_score(player_name, score):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{player_name}:{score}\n")

def display_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("No leaderboard yet.")
        return

    print("\n🏆 Leaderboard 🏆")
    scores = []
    with open(LEADERBOARD_FILE, "r") as f:
        for line in f:
            name, score = line.strip().split(":")
            scores.append((name, int(score)))

    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(scores[:5], start=1):  # top 5
        print(f"{i}. {name} - {score}")