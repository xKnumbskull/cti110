def display_multiplication_table(number):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))

            if user_input < 0:
                print("Error: You cannot enter a negative value.")
            else:
                display_multiplication_table(user_input)

            # Ask if the user wants to run the program again
            again = input("Do you want to run the program again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thank you for using the program!")
                break

        except ValueError:
            print("This program does not handle negative numbers. Please enter a valid integer!23")

if __name__ == "__main__":
    main()

