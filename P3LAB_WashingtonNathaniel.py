# P3LAB_WashingtonNathaniel.py
# This program calculates the number of dollars, quarters, dimes, nickels, and pennies
# needed to make a given amount of money.

def main():
    money = float(input("Enter an amount of money as a float: $"))
    total_cents = int(money * 100)

    coin_values = {
        "Dollars": 100,
        "Quarters": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennies": 1
    }

    for coin, value in coin_values.items():
        count = total_cents // value
        total_cents %= value
        if count > 0:
            print(f"{count} {coin}{'s' if count > 1 else ''}")

if __name__ == "__main__":
    main()