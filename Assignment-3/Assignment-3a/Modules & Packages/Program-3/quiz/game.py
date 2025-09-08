from .questions import questions

def conduct_quiz(player_name):
    print(f"\nWelcome {player_name}! Let's start the quiz\n")
    score = 0
    total = len(questions)

    for q, ans in questions.items():
        user_ans = input(f"{q} ").strip()
        if user_ans.lower() == ans.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {ans}\n")

    print(f"Your score: {score}/{total}")
    return score