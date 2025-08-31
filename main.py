# main.py

from coffee_machine import (
    create_coffee_machine, show_data, fill_the_machine,
    make_coffee, is_empty
)
from machine_operations import withdraw_money, deposit_money, exit_program

def main():
    print("=== Welcome to the Coffee Machine ===")
    machine = create_coffee_machine()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. View machine status")
        print("2. Fill machine")
        print("3. Buy coffee")
        print("4. Deposit money (Admin)")
        print("5. Withdraw money (Admin)")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == '1':
            show_data(machine)
            
        elif choice == '2':
            fill_the_machine(machine)
            
        elif choice == '3':
            make_coffee(machine)
            
        elif choice == '4':
            deposit_money(machine)
            
        elif choice == '5':
            password = input("Enter admin password: ")
            withdraw_money(password, machine)
            
        elif choice == '6':
            exit_program()
            
        else:
            print("Invalid option. Please select 1-6.")

if __name__ == "__main__":
    main()