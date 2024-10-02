# Nathaniel Washington
# 09/25/2024
# P1HW2: Travel Budget Calculator
# This program calculates the remaining budget after entering travel expenses.

# Pseudocode:
# 1. Define the main function
# 2. Print a welcome message
# 3. Ask the user to enter their budget
# 4. Ask the user to enter their travel destination
# 5. Ask the user for the amount they will spend on gas
# 6. Ask the user for the amount they will spend on accommodation
# 7. Ask the user for the amount they will spend on food
# 8. Calculate total expenses (gas + accommodation + food)
# 9. Calculate remaining budget (budget - total expenses)
# 10. Display the travel destination, total expenses, and remaining budget
# 11. End the program

def main():
    print("Welcome to the Travel Budget Calculator!")

    budget = float(input("Please enter your budget: "))
    destination = input("Please enter your travel destination: ")
    gas_expense = float(input("Enter amount you will spend on gas: "))
    accommodation_expense = float(input("Enter amount you will spend on accommodation/hotel: "))
    food_expense = float(input("Enter amount you will spend on food: "))
    
    print("-----------Travel Expenses----------")
    total_expenses = gas_expense + accommodation_expense + food_expense
    
    remaining_budget = budget - total_expenses
    
    # Step 10: Display results
    print(f"\nLocation: {destination}")
    print(f"Initial Budget: {budget:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
