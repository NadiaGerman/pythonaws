# simple-elevator/main.py

# This program simulates an elevator that moves between floors -2 to 10.

def elevator_simulator():
    print("Welcome to the Simple Elevator Simulator!")

    # The elevator starts at ground floor (0)
    current_floor = 0

    # Define the elevator's allowed range
    max_floor = 10
    min_floor = -2

    # Start a loop to keep asking the user for floor input
    while True:
        print(f"\nYou are currently on floor {current_floor}.")
        
        # Ask the user where they want to go or if they want to quit
        user_input = input(f"Enter the floor number ({min_floor} to {max_floor}) you want to go to, or 'q' to quit: ")

        # Allow user to exit the simulation
        if user_input.lower() == 'q':
            print("Exiting elevator. Goodbye!")
            break

        # Check if input is a valid number (including negative floors)
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        # Convert input to integer
        target_floor = int(user_input)

        # Check if requested floor is within the allowed range
        if target_floor < min_floor or target_floor > max_floor:
            print(f"Floor {target_floor} is out of range. Please choose between {min_floor} and {max_floor}.")
        elif target_floor == current_floor:
            print("You are already on that floor!")
        else:
            # Simulate moving the elevator
            print(f"Moving from floor {current_floor} to floor {target_floor}...")
            current_floor = target_floor
            print(f"Arrived at floor {current_floor}.")

# Call the simulator function if this script is run directly
if __name__ == "__main__":
    elevator_simulator()
