# Exercise 1: Variables and Data Types
name = "Nadezda"
age = 45
city = "Shelomi , North Israel"
fav_color = "Blue"

print(f"Hello! My name is {name}, I'm {age} years old, I live in {city}, and my favorite color is {fav_color}.")

from datetime import datetime

# Ask the user for their birth year
birth_year = int(input("Enter your year of birth: "))

# Get the current year
current_year = datetime.now().year

# Calculate age
age = current_year - birth_year

# Display the result
print(f"You are {age} years old.")
