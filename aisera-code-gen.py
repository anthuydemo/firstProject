EXPENSES = []

def add_expense(expense_details, amount):
    expense = {"details": expense_details, "amount": amount}
    EXPENSES.append(expense)

def delete_expense(expense_index):
    del EXPENSES[expense_index]

def update_expense(expense_index, new_details, new_amount):
    EXPENSES[expense_index]["details"] = new_details
    EXPENSES[expense_index]["amount"] = new_amount

def view_expenses():
    for expense in EXPENSES:
        print(f"{expense['details']}: {expense['amount']}")

while True:
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. View Expenses")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        expense_details = input("Enter expense details: ")
        amount = input("Enter amount: ")
        add_expense(expense_details, amount)
    elif choice == 2:
        expense_index = int(input("Enter expense index to delete: "))
        delete_expense(expense_index)
    elif choice == 3:
        expense_index = int(input("Enter expense index to update: "))
        new_details = input("Enter new details: ")
        new_amount = input("Enter new amount: ")
        update_expense(expense_index, new_details, new_amount)
    elif choice == 4:
        view_expenses()
    elif choice == 5:
        break
