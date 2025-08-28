# coffee-machine.py
from machine import Machine

"""
Coffee machine class inheriting from Machine, managing resources
and coffee making.
"""

class CoffeeMachine(Machine):
     # Resource limits
    MAX_BEANS = 200
    MAX_CUPS = 10
    MAX_WATER = 2500
    MAX_MILK = 1000
    
    # Menu and resource limits of the coffee machine
    menu = {
        "espresso": {"water": 250, "milk":0, "beans":16, "price":4},
        "latte": {"water": 350, "milk":75, "beans":20, "price":7},
        "cappuccino": {"water": 200, "milk":100, "beans":12, "price":6}
    }

    # Creating a coffee machine object, set to max capacity
    def __init__(self):
        super().__init__()
        self.beans = self.MAX_BEANS
        self.cups = self.MAX_CUPS
        self.water = self.MAX_WATER
        self.milk = self.MAX_MILK

    # Display current resources in the coffee machine
    def show_data(self):
        print(f"The coffee machine has:\n",
              f"\t* {self.beans} g of beans\n",
              f"\t* {self.cups} units of cups\n",
              f"\t* {self.water} ml of water\n",
              f"\t* {self.milk} ml of milk\n",
              f"\t* ${self.money} of money\n")

    # Check if any resource is empty
    def is_empty(self):
        if self.beans == 0 or self.cups == 0 or self.water == 0 or self.milk == 0:
            print("One, or more, ingredients are missing.")
            return True
        return False

    # Check if all resources are at maximum capacity
    def is_full(self):
        if self.beans == self.MAX_BEANS and self.cups == self.MAX_CUPS and self.water == self.MAX_WATER and self.milk == self.MAX_MILK:
            print("The machine is already full.")
            return True
        return False

    # Replenish resources in the coffee machine
    def fill_the_machine(self):
        if self.is_full():
            return
        
        self.show_data()
    
        # Helper function to check for overflow
        def check_overflow(current, maximum, resource_name, unit=""):
            if current > maximum:
                print(f"The amount of {resource_name}{unit} cannot exceed {maximum}{unit}. Setting {resource_name} to {maximum}{unit}.")
                return maximum
            return current
        
        self.beans += self.set_amount("Insert g of beans: ")
        self.beans = check_overflow(self.beans, self.MAX_BEANS, "beans", "g")

        self.water += self.set_amount("Insert ml of water: ")
        self.water = check_overflow(self.water, self.MAX_WATER, "water", "ml")

        self.milk += self.set_amount("Insert ml of milk: ")
        self.milk = check_overflow(self.milk, self.MAX_MILK, "milk", "ml")

        self.cups += self.set_amount("Insert number of cups: ")
        self.cups = check_overflow(self.cups, self.MAX_CUPS, "cups")

    # Display the coffee menu
    def show_menu(self):
        pass

    # Make a coffee based on user choice
    def make_coffee(self):
        pass
