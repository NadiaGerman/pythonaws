# Simple Version of Quiz Quest - Manual Text Answers, Full Category Names Only

import random

# Question bank
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

# Simple version question function
def ask_question_simple(player, category):
    """
    Simple version using text-based answer input.
    Player types the answer manually.
    """
    question = random.choice(questions[category])
    print(f"\n{player}, your question is:")
    print(question["q"])
    answer = input("Your answer: ").strip().lower()
    if answer == question["a"].lower():
        print("Correct!")
        scores[player] += 1
    else:
        print(f"Wrong. The correct answer was: {question['a']}.")

def show_scores():
    print("\n--- Current Scores ---")
    for player, score in scores.items():
        print(f"{player}: {score} points")

def declare_winner():
    print("\n=== Final Leaderboard ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for player, score in sorted_scores:
        print(f"{player}: {score} points")

    highest_score = sorted_scores[0][1]
    winners = [player for player, score in sorted_scores if score == highest_score]

    if len(winners) > 1:
        print(f"\n It's a tie! Congratulations to: {', '.join(winners)}!")
    else:
        print(f"\n Congratulations {winners[0]}! You are the winner! ")

def main():
    print(" Welcome to Quiz Quest! (Simple Version) ")
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

    # Available categories
    categories = ["science", "history", "pop culture"]

    # Play rounds
    for round_num in range(1, rounds + 1):
        print(f"\n=== Round {round_num} ===")
        for player in players:
            print(f"\n{player}'s turn!")
            print("Available categories: science, history, pop culture")
            choice = input("Enter full category name: ").strip().lower()
            if choice in categories:
                ask_question_simple(player, choice)
            else:
                print("Invalid category. Skipping turn.")

        show_scores()

    declare_winner()

if __name__ == "__main__":
    main()
