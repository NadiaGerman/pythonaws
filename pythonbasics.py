# # Exercise 1: Variables and Data Types
# name = "Nadezda"
# age = 45
# city = "Shelomi , North Israel"
# fav_color = "Blue"

# print(f"Hello! My name is {name}, I'm {age} years old, I live in {city}, and my favorite color is {fav_color}.")

# from datetime import datetime

# # Ask the user for their birth year
# birth_year = int(input("Enter your year of birth: "))

# # Get the current year
# current_year = datetime.now().year

# # Calculate age
# age = current_year - birth_year

# # Display the result
# print(f"You are {age} years old.")


# # Task 4: Even or Odd Checker

# # Ask the user to input a number
# number = int(input("Enter a number: "))

# # Check if the number is even or odd using modulo operator
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# # Task 5: Simple Calculator

# # Get user input
# num1 = float(input("Enter first number: "))
# operation = input("Enter operation (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # Perform the operation
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operation."

# print("Result:", result)

# # Task 6: Even or Odd Checker
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


#     # Task 7: Basic Calculator

# num1 = float(input("Enter the first number: "))
# operator = input("Enter an operation (+, -, *, /): ")
# num2 = float(input("Enter the second number: "))

# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operator.")

# # Task 8: Even or Odd Checker

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# # Task 9: Multiplication Table Generator

# number = int(input("Enter a number to generate its multiplication table: "))

# print(f"\nMultiplication Table for {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# # Task 9: Multiplication Table Generator

# number = int(input("Enter a number to generate its multiplication table: "))

# print(f"\nMultiplication Table for {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# # Task 10: Vowel Counter

# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# count = 0

# for char in sentence:
#     if char in vowels:
#         count += 1

# print(f"The number of vowels in your sentence is: {count}")

# # Task 11: FizzBuzz

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # Task 12: Palindrome Checker

# word = input("Enter a word: ").lower()

# if word == word[::-1]:
#     print(f"'{word}' is a palindrome!")
# else:
#     print(f"'{word}' is not a palindrome.")

#     # Task 13: Factorial Calculator

# num = int(input("Enter a positive integer: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")



# # Task 14: Palindrome Checker

# word = input("Enter a word: ").lower()

# if word == word[::-1]:
#     print(f"'{word}' is a palindrome ")
# else:
#     print(f"'{word}' is not a palindrome ")



# # Task 15: FizzBuzz

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# # Task 16: Factorial Calculator

# number = int(input("Enter a number: "))
# factorial = 1

# if number < 0:
#     print("Factorial does not exist for negative numbers.")
# elif number == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, number + 1):
#         factorial *= i
#     print(f"The factorial of {number} is {factorial}")


# # Task 17: Number Guessing Game

# import random

# secret_number = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))

# if guess == secret_number:
#     print(" Congratulations! You guessed right!")
# else:
#     print(f" Wrong! The number was {secret_number}")

# Task 18: Password Validator

# password = input("Enter a  valid password:  ")

# if len(password) < 8:
#     print(" Password is too short!")
# elif not any(char.isdigit() for char in password):
#     print(" Password must contain at least one digit.")
# elif not any(char.isupper() for char in password):
#     print(" Password must contain at least one uppercase letter.")
# else:
#     print(" Password is valid!")

# # Task 19: Even or Odd Counter

# num = int(input("Enter a number: "))

# even_count = 0
# odd_count = 0

# for i in range(1, num + 1):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)

# # Task 20: Password Strength Checker

# password = input("Enter password: ")

# errors = []

# if len(password) < 6:
#     errors.append("Too short")
# if not any(char.isdigit() for char in password):
#     errors.append("Must include at least one number")
# if not any(char.isupper() for char in password):
#     errors.append("Must include at least one uppercase letter")

# if not errors:
#     print("Strong password")
# else:
#     for error in errors:
#         print(error)

# # Task 21: FizzBuzz

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # Task 22: Prime number checker

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# # Check numbers from 1 to 20
# for num in range(1, 21):
#     if is_prime(num):
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")


# # Task 23: Student grades dictionary

# students = {
#     "Alice": 90,
#     "Bob": 78,
#     "Charlie": 85,
#     "Diana": 86
# }

# # Calculate average
# average = sum(students.values()) / len(students)
# print(f"Average grade: {average}")

# # Find top student(s)
# highest = max(students.values())
# top_students = [name for name, grade in students.items() if grade == highest]
# print("Top student(s):", ", ".join(top_students))

# # Task 24: Prime number checker

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Check numbers from 1 to 20
# for num in range(1, 21):
#     if is_prime(num):
#         print(f"{num} is prime")
#     else:
#         print(f"{num} is not prime")

# # Task26 Simple Calculator using Functions

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero!"
#     return a / b

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print("Result:", add(num1, num2))
# elif choice == '2':
#     print("Result:", subtract(num1, num2))
# elif choice == '3':
#     print("Result:", multiply(num1, num2))
# elif choice == '4':
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid input")

# Task 27: Check if input is a palindrome

# def is_palindrome(text):
#     cleaned = ''.join(char.lower() for char in text if char.isalnum())
#     return cleaned == cleaned[::-1]

# user_input = input("Enter a string to check if it's a palindrome: ")

# if is_palindrome(user_input):
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome.")


# # Exercise 28: Count Vowels in a String

# # Ask the user to enter a sentence
# sentence = input("Enter a sentence: ").lower()

# # Dictionary to store counts of each vowel
# vowel_counts = {
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
# }

# # Count vowels in the sentence
# for char in sentence:
#     if char in vowel_counts:
#         vowel_counts[char] += 1

# # Print the results
# for vowel, count in vowel_counts.items():
#     print(f"{vowel}: {count}")

# # Exercise 29: Check if input is a palindrome

# # Ask the user for a word or sentence
# text = input("Enter a word or sentence: ")

# # Remove spaces and convert to lowercase
# cleaned = text.replace(" ", "").lower()

# # Check if it's a palindrome
# if cleaned == cleaned[::-1]:
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")


# # Exercise 32: Prime Number Checker

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")# Exercise 33: Password Strength Checker

# # Exercise 33: Password Strength Checker

# password = input("Enter your password: ")

# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)
# has_digit = any(char.isdigit() for char in password)

# if len(password) >= 8 and has_upper and has_lower and has_digit:
#     print("Password is strong")
# else:
#     print("Password is weak")


