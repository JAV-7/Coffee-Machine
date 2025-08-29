# machine.py

"""Base class for different types of machines, handling money operations."""

class Machine:

    def __init__(self):
        self.money = 0

    # Helper function to get valid input
    def set_amount(self, prompt):
        while True:
            try:
                amount = int(input(prompt))
                if amount < 0:
                    print("Please enter a non-negative integer.")
                    continue
                return amount
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
                continue

    # Withdraw money from the machine, or send to charity
    def withdraw_money(self):
        amount = 0
        amount = self.set_amount("Insert desired quantity of money to withdraw : ")
        if amount > self.money:
                print(f"Cannot withdraw more than available (${self.money}). Withdrawing all available money.")
                amount = self.money

        # Ask user if they want to send money to charity
        while True:
            purpose = input("Do you want to send charity? (yes/no): ").strip().lower()
            if purpose == "yes":
                print(f"Sending ${amount} to charity. Thank you!")
                self.money -= amount
                break
            elif purpose == "no":
                print(f"Withdrawing ${amount}.")
                self.money -= amount
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    # Deposit money into the machine
    def deposit_money(self):
        amount = self.set_amount("Insert desired quantity of money to deposit : ")
        self.money += amount
        print(f"Deposited ${amount}. Current balance: ${self.money}.")

    # Exit the program
    def exit(self):
        print("Exiting the program. Goodbye!")
        exit()