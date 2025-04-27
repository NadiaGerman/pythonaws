# Voting System - Simulates a simple voting process

# Dictionary to store votes
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Welcome message
print("Welcome to the Voting System!")
print("Candidates are:", ", ".join(votes.keys()))

# Number of voters
num_voters = int(input("Enter the number of voters: "))

# Voting loop
for i in range(num_voters):
    vote = input(f"Voter #{i + 1}, enter your vote: ")
    if vote in votes:
        votes[vote] += 1
        print("Vote recorded!\n")
    else:
        print("Invalid candidate. Vote not counted.\n")

# Print final results
print("\n--- Voting Results ---")
for candidate, count in votes.items():
    print(f"{candidate}: {count} vote(s)")

# Determine the winner(s)
max_votes = max(votes.values())
winners = [name for name, count in votes.items() if count == max_votes]

if len(winners) == 1:
    print(f"\nWinner: {winners[0]}")
else:
    print(f"\nIt's a tie between: {', '.join(winners)}")
