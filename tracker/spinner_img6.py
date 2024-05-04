import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty

class MySpinner(BoxLayout):
    spinner = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.images = {
            'blank': {'label': 'Blank', 'background': r"C:\Prototype-main\sprites\blank.png"},
            'food': {'label': 'Food', 'background': r"C:\Prototype-main\sprites\food.png"},
            'transport': {'label': 'Transport', 'background': r"C:\Prototype-main\sprites\transportation.png"},
            'rest': {'label': 'Rest', 'background': r"C:\Prototype-main\sprites\rest.png"},
        }
        self.create_spinner()
        self.create_table_if_not_exists()

    def create_spinner(self):
        self.spinner = Spinner(text='Blank', values=list(self.images.keys()), size_hint=(None, None), size=(100, 44))
        self.spinner.bind(text=self.on_spinner_select)
        self.add_widget(self.spinner)

    def create_table_if_not_exists(self):
        conn = sqlite3.connect('your_database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS your_table (
                        selected_option TEXT
                     )''')
        conn.commit()
        conn.close()

    def on_spinner_select(self, instance, value):
        selected_image = self.images.get(value, None)
        if selected_image:
            self.spinner.background_normal = selected_image['background']
            # Store the selected option in SQLite
            self.store_to_sqlite(value)

    def store_to_sqlite(self, selected_option):
        conn = sqlite3.connect('your_database.db')
        c = conn.cursor()
        c.execute("UPDATE your_table SET selected_option = ?", (selected_option,))
        conn.commit()
        conn.close()

class MyApp(App):
    def build(self):
        return MySpinner()

if __name__ == '__main__':
    MyApp().run()
# options background and save data