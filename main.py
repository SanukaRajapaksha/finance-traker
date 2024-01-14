from customtkinter import *
import time
import json

# Initialize finance data as an empty list
finance_data = []

def load_data():
    global finance_data
    try:
        with open("finance_data.json", "r") as file:
            finance_data = json.load(file)
    except FileNotFoundError:
        finance_data = []

def save_data():
    with open("finance_data.json", "w") as file:
        json.dump(finance_data, file)

def record_entry(entry_type, amount, category, date):
    entry = {
        "type": entry_type,
        "amount": amount,
        "category": category,
        "date": date
    }
    finance_data.append(entry)
    save_data()

def view_all_entries():
    for entry in finance_data:
        print(entry)

def calculate_totals():
    total_income = sum(entry["amount"] for entry in finance_data if entry["type"] == "income")
    total_expenses = sum(entry["amount"] for entry in finance_data if entry["type"] == "expense")
    net_income = total_income - total_expenses
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Net Income:", net_income)

def view_summary_month(month):
    monthly_entries = [entry for entry in finance_data if entry["date"].startswith(month)]
    print("Summary for", month)
    for entry in monthly_entries:
        print(entry)

def record_new_entry():
    entry_type = input("Enter type (income/expense): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (yyyy-mm-dd): ")
    record_entry(entry_type, amount, category, date)
    print("Entry recorded successfully!")

def main_menu():
    while True:
        print("\n===== Finance Tracker =====")
        print("1. Record a new income or expense entry")
        print("2. View all recorded entries")
        print("3. Calculate total income and total expenses")
        print("4. View summary of transactions for a specific month")
        print("5. Save and load financial data to and from a text file")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            record_new_entry()
        elif choice == 2:
            view_all_entries()
        elif choice == 3:
            calculate_totals()
        elif choice == 4:
            month = input("Enter month (yyyy-mm): ")
            view_summary_month(month)
        elif choice == 5:
            save_data()
            load_data()
            print("Data saved and loaded successfully!")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    load_data()
    main_menu()
