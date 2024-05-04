import sqlite3
from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class CustomSpinner(Spinner):
    pass

class ImageSpinnerApp(App):
    connection = None
    cursor = None
    selected_value = ObjectProperty(None)

    images = {
        'blank': {'name': 'Blank', 'path': r"C:\Prototype-main\sprites\blank.png"},
        'food': {'name': 'Food', 'path': r"C:\Prototype-main\sprites\food.png"},
        'transport': {'name': 'Transport', 'path': r"C:\Prototype-main\sprites\transportation.png"},
        'rest': {'name': 'Rest', 'path': r"C:\Prototype-main\sprites\rest.png"},
    }

    def build(self):
        self.create_db_connection()
        self.create_table_if_not_exists()
        
        layout = BoxLayout(orientation='vertical')
        self.spinner = CustomSpinner(text='blank', size_hint=(None, None), size=(400, 50))
        self.spinner.bind(text=self.on_spinner_select)
        self.create_spinner_options()
        layout.add_widget(self.spinner)
        
        self.selected_image = Image(source=self.images['blank']['path'], size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.selected_image)
        
        return layout

    def create_db_connection(self):
        self.connection = sqlite3.connect('spinner_options.db')
        self.cursor = self.connection.cursor()

    def create_table_if_not_exists(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS selected_option
                            (id INTEGER PRIMARY KEY, name TEXT, path TEXT)''')
        self.connection.commit()

    def on_spinner_select(self, spinner, text):
        self.selected_value = text
        self.selected_image.source = self.images[text]['path']
        self.save_to_database(text, self.images[text]['path'])

    def save_to_database(self, name, path):
        self.cursor.execute("INSERT INTO selected_option (name, path) VALUES (?, ?)", (name, path))
        self.connection.commit()

    def create_spinner_options(self):
        dropdown = DropDown()
        for key in self.images.keys():
            btn = Button(text=key, size_hint_y=None, height=44)
            btn.background_normal = self.images[key]['path']
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: setattr(self.spinner, 'text', btn.text))
            dropdown.add_widget(btn)
        self.spinner.bind(on_release=dropdown.open)

if __name__ == '__main__':
    ImageSpinnerApp().run()
# just add image to default maybe from spinner_img.py