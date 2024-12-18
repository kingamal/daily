import os
import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return
    
    print("\n--- All Expenses ---")
    print(f"{'Date':<12}| {'Category':<15}| {'Description':<20}| {'Amount':<10}")
    print("-" * 60)
    for expense in expenses:
        print(f"{expense['date']:<12}| {expense['category']:<15}| {expense['description']:<20}| ${expense['amount']:<10.2f}")

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    category = input("Enter category: ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    expenses.append({"date": date, "category": category, "description": description, "amount": amount})
    print("Expense added successfully!")

def search_expenses_by_date(expenses):
    print("Enter a single date (YYYY-MM-DD) or a date range (YYYY-MM-DD to YYYY-MM-DD).")
    date_input = input("Enter date or range: ")
    
    if " to " in date_input:
        try:
            start_date, end_date = date_input.split(" to ")
            start_date = datetime.strptime(start_date.strip(), "%Y-%m-%d")
            end_date = datetime.strptime(end_date.strip(), "%Y-%m-%d")
        except ValueError:
            print("Invalid date range format. Please use 'YYYY-MM-DD to YYYY-MM-DD'.")
            return
    else:
        try:
            start_date = end_date = datetime.strptime(date_input.strip(), "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    filtered_expenses = [
        exp for exp in expenses 
        if start_date <= datetime.strptime(exp['date'], "%Y-%m-%d") <= end_date
    ]

    if not filtered_expenses:
        print("\nNo expenses found for the given date or range.")
    else:
        display_expenses(filtered_expenses)

def calculate_total_spending(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Spending: ${total:.2f}")

def expense_tracker():
    expenses = load_expenses()
    print("\nWelcome to the Expense Tracker!")

    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Search expenses by date")
        print("4. Calculate total spending")
        print("5. Exit")
        
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if option == 1:
            add_expense(expenses)
        elif option == 2:
            display_expenses(expenses)
        elif option == 3:
            search_expenses_by_date(expenses)
        elif option == 4:
            calculate_total_spending(expenses)
        elif option == 5:
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    expense_tracker()
