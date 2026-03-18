# Budget-Calculator
designed to help students organize and understand their expenses. The system allows students to register their income and expenses, see how their money is distributed, and detect excessive spending.


import csv
import os
# External Library: Run 'pip install tabulate' in your terminal
from tabulate import tabulate 

DATA_FILE = "budget_data.csv"

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Source/Category", "Amount"])

def add_transaction(t_type, name, amount):
    """Saves a new income or expense to the CSV."""
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([t_type, name, amount])
    print(f"Successfully added {t_type}!")

def calculate_summary():
    """Reads data and calculates totals and balance."""
    total_income = 0
    total_expenses = 0
    transactions = []

    if not os.path.exists(DATA_FILE):
        return 0, 0, []

    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['Amount'])
            transactions.append(row)
            if row['Type'] == 'Income':
                total_income += amount
            else:
                total_expenses += amount
                
    return total_income, total_expenses, transactions

def show_dashboard():
    """Displays the Budget Summary Dashboard."""
    income, expenses, history = calculate_summary()
    balance = income - expenses
    
    print("\n--- STUDENT BUDGET DASHBOARD ---")
    print(tabulate(history, headers="keys", tablefmt="grid"))
    print(f"\nTotal Income:   ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")
    
    if balance < 0:
        print("!!! ALERT: You are overspending! ")

def main():
    initialize_file()
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Dashboard\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            source = input("Source (e.g., Scholarship, Job): ")
            amount = float(input("Amount: "))
            add_transaction("Income", source, amount)
        elif choice == '2':
            category = input("Category (e.g., Food, Transport): ")
            amount = float(input("Amount: "))
            add_transaction("Expense", category, amount)
        elif choice == '3':
            show_dashboard()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
