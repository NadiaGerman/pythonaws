# # Variables
# name = "Nadezda"
# age = 46
# address = "Tel Aviv, Israel"
# favorite_movie = "Inception"

# # Output
# print("Name:", name)
# print("Age:", age)
# print("Address:", address)
# print("Favorite Movie:", favorite_movie)

# # Variables
# name = "Nadezda"
# age = 46
# address = "Tel Aviv, Israel"
# favorite_movie = "Inception"

# # Output using string interpolation (f-string)
# print(f"My name is {name}, I'm {age} years old, I live in {address}, and my favorite movie is '{favorite_movie}'.")


# from datetime import datetime

# # Ask for the user's date of birth
# dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# # Convert the input string into a datetime object
# dob = datetime.strptime(dob_input, "%Y-%m-%d")

# # Get the current date
# today = datetime.today()

# # Calculate the age
# age = today.year - dob.year

# # Adjust if birthday hasn't happened yet this year
# if (today.month, today.day) < (dob.month, dob.day):
#     age -= 1

# # Output the result
# print(f"You are {age} years old.")


# Task 4: Bank Robbery Recruitment

# age = int(input("Enter your age: "))
# height = int(input("Enter your height in cm: "))
# profession = input("Enter your profession: ").strip().lower()

# if profession == "cop":
#     print("Sorry, we don't work with cops.")
# elif age < 18:
#     print(" You're too young for this... 'adventure'.")
# elif height < 100:
#     print("You must be at least 100 cm tall to join the team.")
# else:
#     print("Welcome to the crew! Get ready for the heist!")

