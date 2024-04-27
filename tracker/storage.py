from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import sqlite3
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# SQLite connection and cursor
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (amount REAL)''')
conn.commit()



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout = self.create_layout()
        self.load_last_expense()

    def load_last_expense(self):
        try:
            cursor.execute("SELECT amount FROM expenses ORDER BY ROWID DESC LIMIT 1")
            last_expense = cursor.fetchone()
            if last_expense:
                self.text_input.text = str(last_expense[0])
        except sqlite3.OperationalError:
        # Handle the case when there are no expenses in the table
            pass
    
    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Enter your expense:")
        self.text_input = TextInput(text="", multiline=False)
        add_button = Button(text="Add", on_press=self.add_expense)
        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(add_button)
        return layout

    def add_expense(self, instance):
        amount = float(self.text_input.text)
        cursor.execute("INSERT INTO expenses (amount) VALUES (?)", (amount,))
        conn.commit()
        self.text_input.text = ""

class ExpenseApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)
        return sm

if __name__ == '__main__':
    ExpenseApp().run()
# python storage.py -m screen:phone_iphone_6,portrait,scale=.5