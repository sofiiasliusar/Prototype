class Expense:
    def __init__(self, amount, date, category):
        self.amount = amount
        self.date = date
        self.category = category

    def __str__(self):
        return f"Amount: {self.amount}, Date: {self.date}, Category: {self.category}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Expense added: {expense}")