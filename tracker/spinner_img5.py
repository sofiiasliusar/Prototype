from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.spinner import SpinnerOption, Spinner
from kivy.properties import ObjectProperty
import sqlite3

class ImageSpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super(ImageSpinnerOption, self).__init__(**kwargs)

        # Create an image widget and add it to the spinner option
        self.image = Image(source=kwargs['text'], size_hint=(None, None), allow_stretch=True)
        self.bind(size=self.update_image_pos)
        self.add_widget(self.image)
        
    def update_image_pos(self, *args):
        # Center the image within the spinner option
        self.image.size = self.size
        self.image.pos = self.pos

class CustomSpinner(Spinner):
    pass

class ImageSpinner(BoxLayout):
    selected_value = ObjectProperty(None)

    images = {
        'blank': {'name': 'Blank', 'path': r"C:\Prototype-main\sprites\blank.png"},
        'food': {'name': 'Food', 'path': r"C:\Prototype-main\sprites\food.png"},
        'transport': {'name': 'Transport', 'path': r"C:\Prototype-main\sprites\transportation.png"},
        'rest': {'name': 'Rest', 'path': r"C:\Prototype-main\sprites\rest.png"},
    }

    def __init__(self, **kwargs):
        super(ImageSpinner, self).__init__(**kwargs)

        # List of image paths
        self.image_paths = [self.images[key]['path'] for key in self.images.keys()]

        # Spinner widget to select images
        self.spinner = Spinner(
            option_cls=ImageSpinnerOption,
            values=self.image_paths,
            text=self.image_paths[0],
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5},
        )
        self.spinner.bind(text=self.on_spinner_select)

        # Add default image within the spinner
        default_image_option = ImageSpinnerOption(text=self.image_paths[0])
        self.spinner.values.append(self.image_paths[0])
        self.spinner.add_widget(default_image_option)

        self.add_widget(self.spinner)

    def on_spinner_select(self, spinner, text):
        # Update image, otherwise just text is changed
        self.spinner.children[0].image.source = text

class ImageSpinnerApp(App):
    connection = None
    cursor = None

    def build(self):
        self.create_db_connection()
        self.create_table_if_not_exists()
        
        layout = BoxLayout(orientation='vertical')
        
        self.image_spinner = ImageSpinner()
        layout.add_widget(self.image_spinner)
        
        self.selected_image = Image(source=self.image_spinner.images['blank']['path'], size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.selected_image)
        
        return layout

    def create_db_connection(self):
        self.connection = sqlite3.connect('spinner_options.db')
        self.cursor = self.connection.cursor()

    def create_table_if_not_exists(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS selected_option
                            (id INTEGER PRIMARY KEY, name TEXT, path TEXT)''')
        self.connection.commit()

if __name__ == "__main__":
    ImageSpinnerApp().run()
