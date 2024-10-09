# Nathaniel Washington
# 10/08/2024
# P2HW1: Travel Budget Calculator
# This program calculates the remaining budget after entering travel expenses.
# The output is now formatted with aligned columns and two decimal places for monetary values.

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

    # Inputs
    budget = float(input("Please enter your budget: "))
    destination = input("Please enter your travel destination: ")
    gas_expense = float(input("Enter amount you will spend on gas: "))
    accommodation_expense = float(input("Enter amount you will spend on accommodation/hotel: "))
    food_expense = float(input("Enter amount you will spend on food: "))

    # Calculate total expenses and remaining budget
    total_expenses = gas_expense + accommodation_expense + food_expense
    remaining_budget = budget - total_expenses

    # Display results in a well-formatted table
    print("\n----------- Travel Expenses -----------")
    print(f"{'Location:':<20}{destination}")
    print(f"{'Initial Budget:':<20}${budget:,.2f}")
    print(f"{'Gas:':<20}${gas_expense:,.2f}")
    print(f"{'Accommodation:':<20}${accommodation_expense:,.2f}")
    print(f"{'Food:':<20}${food_expense:,.2f}")
    print(f"{'Total Expenses:':<20}${total_expenses:,.2f}")
    print(f"{'Remaining Budget:':<20}${remaining_budget:,.2f}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
