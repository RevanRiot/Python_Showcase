# File: personal_finance_tracker.py

import csv

def add_transaction(file, description, amount):
    """Adds a transaction to the finance tracker."""
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([description, amount])
    print("Transaction added.")

def view_transactions(file):
    """Displays all transactions in the finance tracker."""
    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print(f"{'Description':<20} {'Amount':<10}")
            print("-" * 30)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<10}")
    except FileNotFoundError:
        print("No transactions found.")

if __name__ == "__main__":
    tracker_file = "finance.csv"
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            desc = input("Enter transaction description: ")
            amt = input("Enter transaction amount: ")
            add_transaction(tracker_file, desc, amt)
        elif choice == '2':
            view_transactions(tracker_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
