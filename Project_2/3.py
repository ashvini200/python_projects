import csv
import os
from datetime import datetime

# Define file path
DATA_FILE = 'expenses.csv'

def initialize_file():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])

def save_expense(date, amount, category, description):
    """Save a new expense entry to the CSV file."""
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

def view_expenses():
    """Display all expenses from the CSV file."""
    if not os.path.isfile(DATA_FILE):
        print("No expense data found.")
        return

    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        print(f"\n{' | '.join(headers)}")
        for row in reader:
            print(f"{' | '.join(row)}")

def get_expenses_by_category():
    """Get expenses categorized by type."""
    categories = {}
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            _, amount, category, _ = row
            amount = float(amount)
            if category not in categories:
                categories[category] = 0
            categories[category] += amount
    return categories

def get_expenses_summary():
    """Generate and print summaries of expenses by category and month."""
    expenses_by_category = get_expenses_by_category()
    monthly_expenses = {}

    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date, amount, _, _ = row
            amount = float(amount)
            month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
            if month not in monthly_expenses:
                monthly_expenses[month] = 0
            monthly_expenses[month] += amount

    print("\nExpense Summary by Category:")
    for category, total in expenses_by_category.items():
        print(f"{category}: ${total:.2f}")

    print("\nMonthly Expense Summary:")
    for month, total in monthly_expenses.items():
        print(f"{month}: ${total:.2f}")

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    """Validate amount as a positive float."""
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False

def get_user_input():
    """Collect and validate user input."""
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None, None, None, None

    amount = input("Enter the amount: ").strip()
    if not validate_amount(amount):
        print("Invalid amount. Please enter a positive number.")
        return None, None, None, None

    category = input("Enter the category (e.g., Food, Transportation, Entertainment): ").strip()
    description = input("Enter a description: ").strip()
    return date, float(amount), category, description

def main():
    initialize_file()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            date, amount, category, description = get_user_input()
            if date:
                save_expense(date, amount, category, description)
                print("Expense added successfully!")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            get_expenses_summary()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

