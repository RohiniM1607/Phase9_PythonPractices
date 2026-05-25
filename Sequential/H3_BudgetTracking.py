income = float(input("Enter your monthly income: "))
expenses = input("Enter your expenses (space-separated): ").split()
total_expense = 0
for expense in expenses:
    total_expense += float(expense)
remaining_budget = income - total_expense
print("Remaining budget: ${:.2f}".format(remaining_budget))