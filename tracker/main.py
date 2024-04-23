from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

Window.size = (414, 896)

# sqlite3: This module provides an interface for working with SQLite databases, which can be useful for storing and managing expense data.
#The SQLite database is a lightweight, self-contained, serverless, and transactional SQL database engine. It is a good choice for storing and managing expense data in a mobile or desktop application.
#  datetime: This module provides classes for manipulating dates and times, which you might need for recording the date of expenses and performing date-based calculations.
# The datetime module can be used to format and manipulate the date parameter before inserting it into the database.
#  os: The os module provides a portable way of using operating system-dependent functionality, such as interacting with the file system, which might be useful for managing files or directories related to your app.
# kivy.storage: Kivy's storage module provides a simple way to store and retrieve application data persistently, which can be useful for saving user preferences or settings.
# JSON files (.json): JSON files are commonly used for storing data, such as configuration settings or predefined data structures. You can read JSON data from a file in Python using the json module and then use the data within your application.
# YAML files (.yaml or .yml): Similar to JSON, YAML files are used for configuration settings and data storage. Python has libraries like PyYAML that allow you to parse YAML files and work with the data in your application.

class Day(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#         self.db = sqlite3.connect('expenses.db')
#         self.c = self.db.cursor()
#         self.c.execute('''CREATE TABLE IF NOT EXISTS expenses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             amount REAL,
#             date TEXT,
#             category TEXT,
#             notes TEXT
#         )''')
#         self.db.commit()
#         self.db.close()
# # i want aech day to have a Day screen:
#     def add_expense(self):
#         self.db = sqlite3.connect('expenses.db')
#         self.c = self.db.cursor()
#         self.c.execute('''INSERT INTO expenses (name, amount, date, category, notes)
#             VALUES (?, ?, ?, ?, ?)''', (self.name.text, self.amount.text, self.date.text, self.category.text, self.notes.text))
#         self.db.commit()
#         self.db.close()
#         self.name.text = ''
#         self.amount.text = ''
#         self.date.text = ''
#         self.category.text = ''
#         self.notes.text = ''
#         self.c.execute('''SELECT * FROM expenses''')
#         self.expenses = self.c.fetchall()
#         self.ids.expenses_list.data = self.expenses
#         self.ids.expenses_list.refresh()
#         self.ids.expenses_list.selection_mode = 'single'
#         self.ids.expenses_list.bind(on_selection_change=self.on_selection_change)
#         self.ids.expenses_list.bind(on_item_press=self.on_item_press)
#         self.ids.expenses_list.bind(on_item_release=self.on_item_release)
#         self.ids.expenses_list.bind(on_item_double_tap=self.on_item_double_tap)
#         self.ids.expenses_list.bind(on_item_tapped=self.on_item_tapped)
#         self.ids.expenses_list.bind(on_item_long_press=self.on_item_long_press)
#         self.ids.expenses_list.bind(on_item_moved=self.on_item_moved)
#         self.ids.expenses_list.bind(on_item_selected=self.on_item_selected)
#         self.ids.expenses_list.bind(on_item_unselected=self.on_item_unselected)
#         self.ids.expenses_list.bind(on_item_deselected=self.on_item_deselected)
#         self.ids.expenses_list.bind(on_item_activated=self.on_item_activated)
#         self.ids.expenses_list.bind(on_item_deactivated=self.on_item_deactivated)
#         self.ids.expenses_list.bind(on_item_highlighted=self.on_item_highlighted)
#     def on_selection_change(self, instance, value):
#         self.ids.expenses_list.selection_mode = 'single'
#         self.ids.expenses_list.bind(on_selection_change=self.on_selection_change)
#         self.ids.expenses_list.bind(on_item_press=self.on_item_press)
#         self.ids.expenses_list.bind(on_item_release=self.on_item_release)
#         self.ids.expenses_list.bind(on_item_double_tap=self.on_item_double_tap)
#         self.ids.expenses_list.bind(on_item_tapped=self.on_item_tapped)
#         self.ids.expenses_list.bind(on_item_long_press=self.on_item_long_press)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Day(name = 'day'))
        return sm
    
if "__name__" == "__main__":
    MainApp().run()