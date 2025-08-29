# coffee-machine.py
"""
Coffee machine class inheriting from Machine, managing resources
and coffee making.
"""
from machine_operations import set_amount

# Resource maximums
MAX_BEANS = 200
MAX_CUPS = 10
MAX_WATER = 2500
MAX_MILK = 1000

# Menu definitions
MENU = {
    "espresso": {"water": 250, "milk": 0, "beans": 16, "price": 4},
    "latte": {"water": 350, "milk": 75, "beans": 20, "price": 7},
    "cappuccino": {"water": 200, "milk": 100, "beans": 12, "price": 6}
}


def create_coffee_machine() -> dict:
    """
    Returns: dict: A new coffee machine initialized with maximum resources and zero money.
    """
    return {
    "beans": MAX_BEANS,
    "cups": MAX_CUPS,
    "water": MAX_WATER,
    "milk": MAX_MILK,
    "money": 0
    }

def show_data(machine: dict) -> None:
    """
    Args: machine (dict): The current state of the machine.
    Returns: None
    """
    print(f"The coffee machine has:\n"
          f"\t* {machine['beans']} g of beans\n"
          f"\t* {machine['cups']} units of cups\n"
          f"\t* {machine['water']} ml of water\n"
          f"\t* {machine['milk']} ml of milk\n"
          f"\t* ${machine['money']} of money\n")

# Check if the machine is empty
def is_empty(machine: dict) -> bool:
    """
    Args: machine (dict): The current state of the machine.
    Returns: bool: True if any resource is zero, False otherwise.
    """
    if machine['beans'] == 0 or machine['cups'] == 0 or machine['water'] == 0 or machine['milk'] == 0:
        print("One, or more, ingredients are missing.")
        return True
    return False

# Check if the machine is full
def is_full(machine: dict) -> bool:
    """
    Args: machine (dict): The current state of the machine.
    Returns: bool: True if all resources are at maximum capacity, False otherwise.
    """
    if (machine['beans'] == MAX_BEANS and machine['cups'] == MAX_CUPS and
        machine['water'] == MAX_WATER and machine['milk'] == MAX_MILK):
        print("The machine is already full.")
        return True
    return False

# Fill the machine with resources
def fill_the_machine(machine: dict) -> None:
    """
    Args: machine (dict): The current state of the machine.
    Returns: None
    Description: Prompts the user to add resources to the machine,
    ensuring no resource exceeds its maximum capacity.
    """
    if is_full(machine):
        return

    show_data(machine)

    # Helper function to check for overflow
    def check_overflow(current, maximum, resource_name, unit=""):
        if current > maximum:
            print(f"The amount of {resource_name}{unit} cannot exceed {maximum}{unit}. Setting {resource_name} to {maximum}{unit}.")
            return maximum
        return current

    machine['beans'] += set_amount("Insert g of beans: ")
    machine['beans'] = check_overflow(machine['beans'], MAX_BEANS, "beans", "g")

    machine['water'] += set_amount("Insert ml of water: ")
    machine['water'] = check_overflow(machine['water'], MAX_WATER, "water", "ml")

    machine['milk'] += set_amount("Insert ml of milk: ")
    machine['milk'] = check_overflow(machine['milk'], MAX_MILK, "milk", "ml")

    machine['cups'] += set_amount("Insert number of cups: ")
    machine['cups'] = check_overflow(machine['cups'], MAX_CUPS, "cups")

# Display menu options
def show_menu() -> None:
    pass

# Make coffee based on user choice
def make_coffee(machine: dict) -> None:
    pass
