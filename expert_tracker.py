expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return
    
    print("\nYour Expenses:")
    total = 0
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₦{expense['amount']}")
        total += expense["amount"]
    
    print(f"\nTotal Spending: ₦{total}\n")


def delete_expense():
    view_expenses()
    
    try:
        num = int(input("Enter expense number to delete: "))
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            print(f"Deleted: {removed['name']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("==== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()