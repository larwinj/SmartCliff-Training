from quiz import conduct_quiz, save_score, display_leaderboard

def main():
    player_name = input("Enter your name: ")
    score = conduct_quiz(player_name)
    save_score(player_name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()