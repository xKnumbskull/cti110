# Nathaniel Washington  
# 11/24/2024
# P5HW - MathQuiz
# This program is a math quiz that generates random addition or subtraction problems,allows the user to guess the answer, 
# provides feedback on whether the guess is too high or too low, and displays a menu for user options.

import random

def display_menu():
    print("\nMAIN MENU")
    print("-------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"{num1} + {num2}")
    guess = None
    guesses = 0
    while guess != correct_answer:
        try:
            guess = int(input("Enter answer: "))
            guesses += 1
            if guess < correct_answer:
                print("Sorry, guess is too low.")
            elif guess > correct_answer:
                print("Sorry, guess is too high.")
            else:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
        except ValueError:
            print("Please enter a valid number.")

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Ensure positive results for subtraction
    if num1 < num2:
        num1, num2 = num2, num1
    correct_answer = num1 - num2
    print(f"{num1} - {num2}")
    guess = None
    guesses = 0
    while guess != correct_answer:
        try:
            guess = int(input("Enter answer: "))
            guesses += 1
            if guess < correct_answer:
                print("Sorry, guess is too low.")
            elif guess > correct_answer:
                print("Sorry, guess is too high.")
            else:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Please choose one of the menu options: "))
            if choice == 1:
                add_numbers()
            elif choice == 2:
                subtract_numbers()
            elif choice == 3:
                print("Thank you for playing...\nBye!!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
