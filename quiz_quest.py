# quiz_quest.py

import random

# Question bank
questions = {
    "science": [
        {"q": "What planet is known as the Red Planet?", "a": "Mars"},
        {"q": "What gas do plants absorb from the atmosphere?", "a": "Carbon dioxide"},
    ],
    "history": [
        {"q": "Who was the first President of the United States?", "a": "George Washington"},
        {"q": "In which year did World War II end?", "a": "1945"},
    ],
    "pop culture": [
        {"q": "Who is the artist behind the song 'Shake It Off'?", "a": "Taylor Swift"},
        {"q": "What movie features a clownfish searching for his son?", "a": "Finding Nemo"},
    ]
}

# Game state variables
players = []
scores = {}
rounds = 3

