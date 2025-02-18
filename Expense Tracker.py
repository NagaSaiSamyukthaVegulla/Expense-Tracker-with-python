from datetime import datetime

# Global list to store expenses
expenses = []

def add_expense(amount, category, description):
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    print("All Expenses:")
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}")

def delete_expense(date):
    global expenses
    expenses = [expense for expense in expenses if expense['date'] != date]
    print("Expense deleted successfully!")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
            delete_expense(date)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()