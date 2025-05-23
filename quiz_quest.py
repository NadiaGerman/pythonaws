# quiz_quest.py

import random

# Question bank (single-answer system)
questions = {
    "science": [
        {"q": "What planet is known as the Red Planet?", "a": "Mars"},
        {"q": "What gas do plants absorb from the atmosphere?", "a": "Carbon dioxide"},
        {"q": "What is the chemical symbol for water?", "a": "H2O"},
        {"q": "What part of the cell contains genetic material?", "a": "Nucleus"},
        {"q": "How many bones are in the adult human body?", "a": "206"},
    ],
    "history": [
        {"q": "Who was the first President of the United States?", "a": "George Washington"},
        {"q": "In which year did World War II end?", "a": "1945"},
        {"q": "Who discovered America in 1492?", "a": "Christopher Columbus"},
        {"q": "What ancient civilization built the pyramids?", "a": "Egyptians"},
        {"q": "What wall divided Berlin from 1961 to 1989?", "a": "Berlin Wall"},
    ],
    "pop culture": [
        {"q": "Who is the artist behind the song 'Shake It Off'?", "a": "Taylor Swift"},
        {"q": "What movie features a clownfish searching for his son?", "a": "Finding Nemo"},
        {"q": "In which TV show would you find a character named 'Jon Snow'?", "a": "Game of Thrones"},
        {"q": "What is the name of the wizarding school in Harry Potter?", "a": "Hogwarts"},
        {"q": "Which superhero is known as the 'Caped Crusader'?", "a": "Batman"},
    ]
}

# Game state variables
players = []
scores = {}
rounds = 3

# -----------------------------------------------
# 🟡 Version 1 — Very simple version (one correct answer, string match)
# def ask_question(player, category):
#     question = random.choice(questions[category])
#     print(f"\n{player}, your question is:")
#     print(question["q"])
#     answer = input("Your answer: ")
#     if answer.strip().lower() == question["a"].lower():
#         print("Correct!")
#         scores[player] += 1
#     else:
#         print(f"Wrong. The correct answer was: {question['a']}.")
# -----------------------------------------------

# -----------------------------------------------
# 🟢 Version 2 — Improved version (accepts multiple possible answers)
# Use this version in main() by calling: ask_question(player, category)
def ask_question(player, category):
    question = random.choice(questions[category])
    print(f"\n{player}, your question is:")
    print(question["q"])
    answer = input("Your answer: ").strip().lower()
    
    # Handle both string or list of correct answers
    correct_answers = question["a"]
    if isinstance(correct_answers, str):
        correct_answers = [correct_answers.lower()]
    else:
        correct_answers = [ans.lower() for ans in correct_answers]

    if answer in correct_answers:
        print("Correct!")
        scores[player] += 1
    else:
        print(f"Wrong. Acceptable answers were: {', '.join(correct_answers)}.")
# -----------------------------------------------

# Function to show scores
def show_scores():
    print("\n--- Current Scores ---")
    for player, score in scores.items():
        print(f"{player}: {score} points")

# Function to declare the winner
def declare_winner():
    print("\n=== Final Leaderboard ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for player, score in sorted_scores:
        print(f"{player}: {score} points")
    winner = sorted_scores[0][0]
    print(f"\n🏆 Congratulations {winner}! You are the winner! 🏆")

# Main game loop
def main():
    print("🎉 Welcome to Quiz Quest! 🎉")
    print("Please enter the names of players. Type 'done' when finished:")

    # Register players
    while True:
        player = input("Enter player name: ").strip()
        if player.lower() == "done":
            break
        if player != "":
            players.append(player)
            scores[player] = 0

    if not players:
        print("No players entered. Exiting game.")
        return

    print("\n--- Let's Start the Game! ---")
    print(f"Players: {', '.join(players)}")

    # Mapping categories
    category_map = {
        "1": "science",
        "s": "science",
        "science": "science",
        "2": "history",
        "h": "history",
        "history": "history",
        "3": "pop culture",
        "p": "pop culture",
        "pop culture": "pop culture"
    }

    # Play rounds
    for round_num in range(1, rounds + 1):
        print(f"\n=== Round {round_num} ===")
        for player in players:
            print(f"\n{player}'s turn!")
            print("Choose a category:")
            print("1. Science")
            print("2. History")
            print("3. Pop Culture")
            choice = input("Enter category number, letter (s/h/p), or name: ").strip().lower()
            category = category_map.get(choice)

            if category:
                # 👉 Active version being used (change this line to test old version)
                ask_question(player, category)
                # To use the original version for testing:
                # ask_question_original(player, category)
            else:
                print("Invalid choice. Skipping turn.")

        show_scores()

    declare_winner()

# Always good practice in Python
if __name__ == "__main__":
    main()
