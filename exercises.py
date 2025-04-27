# Task 1: build two greeting lists from two name lists
# define function that builds a greeting list
def build_greetings(name_list):
    greetings = []
    for name in name_list:
        greetings.append(f"Hello, {name}!")
    return greetings

# define the two teams
names_team1 = ["Jan", "Inna"]
names_team2 = ["Vadim", "Dania"]

# get greetings lists
greetings1 = build_greetings(names_team1)
greetings2 = build_greetings(names_team2)

# Print the greetings lists
print("Team 1 Greetings:", greetings1)
print("Team 2 Greetings:", greetings2)

# Short version with list comprehension
def build_greetings(name_list):
    return [f"Hello, {name}!" for name in name_list]

# define the two teams again
names_team1 = ["Jan", "Inna"]
names_team2 = ["Vadim", "Dania"]

# get greetings lists again
greetings1 = build_greetings(names_team1)
greetings2 = build_greetings(names_team2)

# Print the greetings lists
print("Team 1 Greetings:", greetings1)
print("Team 2 Greetings:", greetings2)
