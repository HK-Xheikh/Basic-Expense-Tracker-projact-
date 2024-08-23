# expense tarcker projact
print("Basic Expense Tracker")
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, name, amount):
        self.expenses[name] = amount

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]

    def update_expense(self, name, amount):
        if name in self.expenses:
            self.expenses[name] = amount

    def get_expense(self, name):
        return self.expenses.get(name)

    def get_total_expenses(self):
        return sum(self.expenses.values())

def main():
    tracker = ExpenseTracker()
    while True:
        print("1. Add expense")
        print("2. Remove expense")
        print("3. Update expense")
        print("4. Get expense")
        print("5. Get total expenses")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(name, amount)
        elif choice == "2":
            name = input("Enter expense name: ")
            tracker.remove_expense(name)
        elif choice == "3":
            name = input("Enter expense name: ")
            amount = float(input("Enter new expense amount: "))
            tracker.update_expense(name, amount)
        elif choice == "4":
            name = input("Enter expense name: ")
            print(tracker.get_expense(name))
        elif choice == "5":
            print(tracker.get_total_expenses())
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
