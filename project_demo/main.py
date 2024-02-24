from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from classes import Expense, ExpenseTracker

class ExpenseTrackerApp(App):
    def build(self):
        self.expense_tracker = ExpenseTracker()

        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Expense Amount:'))
        self.expense_amount = TextInput()
        layout.add_widget(self.expense_amount)

        layout.add_widget(Label(text='Expense Date:'))
        self.expense_date = TextInput()
        layout.add_widget(self.expense_date)

        layout.add_widget(Label(text='Expense Category:'))
        self.expense_category = TextInput()
        layout.add_widget(self.expense_category)

        self.add_button = Button(text='Add Expense', on_press=self.add_expense)
        layout.add_widget(self.add_button)

        return layout

    def add_expense(self, instance):
        amount = self.expense_amount.text
        date = self.expense_date.text
        category = self.expense_category.text

        expense = Expense(amount, date, category)
        self.expense_tracker.add_expense(expense)

if __name__ == '__main__':
    ExpenseTrackerApp().run()