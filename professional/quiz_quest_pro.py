# Professional Version of Quiz Quest (Multiple-Choice Questions)

import random

# Question bank for Professional Version (multiple-choice system)
questions = {
    "science": [
        {
            "q": "What planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": 2
        },
        {
            "q": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "correct": 2
        },
        {
            "q": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "N2"],
            "correct": 1
        },
        {
            "q": "What part of the cell contains genetic material?",
            "options": ["Nucleus", "Cytoplasm", "Cell Wall", "Membrane"],
            "correct": 1
        },
        {
            "q": "How many bones are in the adult human body?",
            "options": ["198", "206", "212", "250"],
            "correct": 2
        },
    ],
    "history": [
        {
            "q": "Who was the first President of the United States?",
            "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
            "correct": 3
        },
        {
            "q": "In which year did World War II end?",
            "options": ["1945", "1939", "1918", "1950"],
            "correct": 1
        },
        {
            "q": "Who discovered America in 1492?",
            "options": ["Christopher Columbus", "Marco Polo", "Amerigo Vespucci", "Ferdinand Magellan"],
            "correct": 1
        },
        {
            "q": "What ancient civilization built the pyramids?",
            "options": ["Romans", "Greeks", "Egyptians", "Persians"],
            "correct": 3
        },
        {
            "q": "What wall divided Berlin from 1961 to 1989?",
            "options": ["Great Wall", "Berlin Wall", "Iron Curtain", "Hadrian's Wall"],
            "correct": 2
        },
    ],
    "pop culture": [
        {
            "q": "Who sings 'Shake It Off'?",
            "options": ["Selena Gomez", "Ariana Grande", "Taylor Swift", "Katy Perry"],
            "correct": 3
        },
        {
            "q": "What movie features a clownfish searching for his son?",
            "options": ["Finding Nemo", "Toy Story", "The Incredibles", "Shrek"],
            "correct": 1
        },
        {
            "q": "In which TV show would you find a character named 'Jon Snow'?",
            "options": ["The Witcher", "Game of Thrones", "Breaking Bad", "Vikings"],
            "correct": 2
        },
        {
            "q": "What is the name of the wizarding school in Harry Potter?",
            "options": ["Hogwarts", "Ilvermorny", "Durmstrang", "Beauxbatons"],
            "correct": 1
        },
        {
            "q": "Which superhero is known as the 'Caped Crusader'?",
            "options": ["Superman", "Batman", "Spiderman", "Iron Man"],
            "correct": 2
        },
    ]
}

# Game state variables
players = []
scores = {}
rounds = 3

# Multiple-choice question function
def ask_question_pro(player, category):
    """
    Asks a multiple-choice question to the player.
    Player inputs a number (1-4) to select the answer.
    Validates input to avoid invalid choices.
    """
    question = random.choice(questions[category])
    print(f"\n{player}, your question is:")
    print(question["q"])

    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")

    try:
        answer = int(input("Enter the number of your answer (1-4): ").strip())
        if 1 <= answer <= 4:
            if answer == question["correct"]:
                print("Correct!")
                scores[player] += 1
            else:
                correct_answer_text = question["options"][question["correct"] - 1]
                print(f"Wrong. The correct answer was: {correct_answer_text}.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Show current scores
def show_scores():
    print("\n--- Current Scores ---")
    for player, score in scores.items():
        print(f"{player}: {score} points")

# Declare the winner or tie
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

# Main game loop
def main():
    print("-" * 50)
    print("Welcome to Quiz Quest! (Professional Version)".center(50))
    print("-" * 50)
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

    # Mapping category choices
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
            
            while True:
                choice = input("Enter category number, letter (s/h/p), or full name: ").strip().lower()
                category = category_map.get(choice)
                if category:
                    ask_question_pro(player, category)
                    break
                else:
                    print("Invalid category. Please try again.")

        show_scores()

    declare_winner()

if __name__ == "__main__":
    main()
