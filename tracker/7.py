# i want to create an expense tracker app. each day a new screen will be added displaying current date and list. the user can swipe to go back to past days screens
# at 00:00 the app will check

# create a demo add and work on it during summer to finish
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime, timedelta

class ExpenseTrackerApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.add_today_screen()
        return self.screen_manager
    
    def add_today_screen(self):
        today = datetime.now().strftime("%Y-%m-%d")
        screen = ExpenseScreen(name=today)
        self.screen_manager.add_widget(screen)
        return screen

class ExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text=self.name))
        self.expense_list = BoxLayout(orientation='vertical')
        self.add_widget(self.expense_list)
        self.add_widget(Button(text="Add Expense", on_press=self.add_expense))
    
    def add_expense(self, instance):
        expense_input = TextInput(hint_text="Enter expense")
        self.expense_list.add_widget(expense_input)

if __name__ == "__main__":
    ExpenseTrackerApp().run()

