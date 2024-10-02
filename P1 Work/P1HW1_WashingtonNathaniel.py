# Nathaniel Washington
# 09/25/2024
# Assignment: P1HW1
# This program takes input from the user to perform mathematical expressions.

# ------- Calculating Exponents -------
print("------- Calculating Exponents -------")
base = int(input("Please enter a base number: "))
exponent = int(input("Please enter an exponent: "))
result = base ** exponent

print(base, "raised to the power of", exponent, "is", result, "!!")

# ------- Addition and Subtraction -------
print("------- Addition and Subtraction -------")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))
total = (num1 + num2) - num3

print("(", num1, "+", num2, ") -", num3, "is equal to", total,)