# machine_operations.py

"""Base file for machine operations."""

# ATM password
PASSWORD = "1234"

# Set amount with input validation, for any resource
def set_amount(prompt: str) -> int:
    """
    Args: prompt (str): The prompt message to display to the user.
    Returns: int: The validated non-negative integer input from the user.
    Description: Prompts the user for a non-negative integer input,
    validates it, and returns the value. Repeats until valid input is received.
    """
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

def withdraw_money(password: str, machine_state: dict) -> None:
    """
    Args: password (str): The password to authorize withdrawal.
          machine_state (dict): The current state of the machine, including money.
    Returns: None
    Description: Withdraws money from the machine if the password is correct. 
    Offers an option to send the withdrawn money to charity.
    """
    if password != PASSWORD:
        print("Incorrect password. Access denied.")
        return
    amount = set_amount("Insert desired quantity of money to withdraw : ")
    if amount > machine_state["money"]:
        print(f"Cannot withdraw more than available (${machine_state['money']}). Withdrawing all available money.")
        amount = machine_state["money"]

    while True:
        purpose = input("Do you want to send charity? (yes/no): ").strip().lower()
        if purpose == "yes":
            print(f"Sending ${amount} to charity. Thank you!")
            machine_state["money"] -= amount
            break
        elif purpose == "no":
            print(f"Withdrawing ${amount}.")
            machine_state["money"] -= amount
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def deposit_money(machine_state: dict) -> None:
    """
    Args: machine_state (dict): The current state of the machine, including money.
    Returns: None
    Description: Allows users to deposit money into the machine.
    """
    amount = set_amount("Insert amount of money to deposit: $")
    machine_state["money"] += amount
    print(f"Deposited ${amount}. Total money in machine: ${machine_state['money']}")

def exit_program() -> None:
    print("Exiting the program. Goodbye!")
    exit()