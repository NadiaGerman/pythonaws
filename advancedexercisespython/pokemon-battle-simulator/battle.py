# battle.py
# Pokemon Battle Simulator
# Simulates a turn-based battle between two Pokemon characters

import random

# Define Pokémon with their health and moves
pikachu = {"name": "Pikachu", "health": 100, "moves": {"Thunderbolt": 25, "Quick Attack": 15}}
charmander = {"name": "Charmander", "health": 100, "moves": {"Ember": 20, "Scratch": 10}}

# Function to simulate a Pokémon attack
def attack(attacker, defender):
    move = random.choice(list(attacker["moves"].keys()))
    damage = attacker["moves"][move]
    defender["health"] -= damage
    print(f"{attacker['name']} uses {move} and deals {damage} damage!")
    print(f"{defender['name']} has {max(defender['health'], 0)} HP left.\n")

# Game loop
print(" Pokémon Battle Begins! \n")
while pikachu["health"] > 0 and charmander["health"] > 0:
    attack(pikachu, charmander)
    if charmander["health"] <= 0:
        print(" Pikachu wins!")
        break
    attack(charmander, pikachu)
    if pikachu["health"] <= 0:
        print("⚡️ Charmander wins!")
        break
