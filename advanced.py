# Exercise Simple Calculator

# Ask the user for two numbers and an operation
num1 = float(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero!"
else:
    result = "Invalid operator."

print("Result:", result)
