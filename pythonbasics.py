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


# Task 4: Even or Odd Checker

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using modulo operator
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Task 5: Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print("Result:", result)

# Task 6: Even or Odd Checker
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


    # Task 7: Basic Calculator

num1 = float(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")

# Task 8: Even or Odd Checker

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Task 9: Multiplication Table Generator

number = int(input("Enter a number to generate its multiplication table: "))

print(f"\nMultiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

