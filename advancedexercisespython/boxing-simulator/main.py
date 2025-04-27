# Boxing Simulator
# This script simulates a boxing match between two fighters.
# Each fighter takes turns attacking the other until one loses all health.

import random  # Import random module to generate random damage values
import time    # Import time module to pause between punches for realism

# Function to simulate a punch from one fighter to another
def simulate_punch(attacker, defender):
    damage = random.randint(5, 15)  # Random damage between 5 and 15
    defender["health"] -= damage    # Subtract damage from defender's health
    # Print punch details and remaining health
    print(f"{attacker['name']} punches {defender['name']} for {damage} damage! {defender['name']}'s health is now {defender['health']}")
    time.sleep(1)  # Wait 1 second for dramatic effect

# Main function to start the boxing match
def main():
    # Initialize two fighters with names and health
    fighter1 = {"name": "Rocky", "health": 100}
    fighter2 = {"name": "Apollo", "health": 100}

    print(" Boxing Match: Rocky vs Apollo ")
    time.sleep(1)  # Small pause before starting the match

    # Loop continues until one fighter's health drops to 0 or below
    while fighter1["health"] > 0 and fighter2["health"] > 0:
        simulate_punch(fighter1, fighter2)  # Fighter1 attacks Fighter2
        if fighter2["health"] <= 0:
            break
        simulate_punch(fighter2, fighter1)  # Fighter2 attacks Fighter1

    # Determine the winner based on remaining health
    winner = fighter1 if fighter1["health"] > 0 else fighter2
    print(f"\n {winner['name']} wins the fight!")  # Announce the winner

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
