from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.spinner import SpinnerOption, Spinner
import sqlite3

class ImageSpinnerOption(SpinnerOption):
    def __init__(self, text='', **kwargs):
        super(ImageSpinnerOption, self).__init__(text=text, **kwargs)
        image_path = text  # Assuming `text` will directly be the image path
        self.image = Image(source=image_path, size_hint=(None, None), allow_stretch=True)
        self.bind(size=self.update_image_pos)
        self.add_widget(self.image)


    def update_image_pos(self, *args):
        self.image.size = self.size
        self.image.pos = self.pos

class ImageSpinner(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageSpinner, self).__init__(**kwargs)
        
        # Dictionary of image keys and paths
        self.images = {
            'blank': {'name': 'Blank', 'path': r"C:\Prototype-main\sprites\blank.png"},
            'food': {'name': 'Food', 'path': r"C:\Prototype-main\sprites\food.png"},
            'transport': {'name': 'Transport', 'path': r"C:\Prototype-main\sprites\transportation.png"},
            'rest': {'name': 'Rest', 'path': r"C:\Prototype-main\sprites\rest.png"},
        }

        # Initialize database and store keys
        self.init_db()

        # Create a spinner with images
        self.spinner = Spinner(
            option_cls=ImageSpinnerOption,
            values=list(self.images.values()),  # Ensuring these are image paths
            text=self.images['blank'],  # Default image path
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5},
        )

        self.spinner.bind(text=self.on_spinner_select)
        
        default_image_option = DefaultImageOption(image_path=self.images['blank'])
        self.spinner.values.append(self.images['blank'])
        self.spinner.add_widget(default_image_option)


        self.add_widget(self.spinner)

    def init_db(self):
        self.conn = sqlite3.connect('image_keys.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, key TEXT)
        ''')
        for key in self.images.keys():
            self.c.execute('INSERT OR IGNORE INTO images (key) VALUES (?)', (key,))
        self.conn.commit()

    def on_spinner_select(self, spinner, text):
        # Find the key corresponding to the selected image path
        key = next(key for key, value in self.images.items() if value == text)
        self.spinner.children[0].image.source = text
        print(f"Selected key: {key}")  # For debug purposes
class DefaultImageOption(BoxLayout):
    def __init__(self, image_path, **kwargs):
        super(DefaultImageOption, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = '50dp'
        self.image = Image(source=image_path, size_hint=(None, None), size=(50, 50), allow_stretch=True)
        self.add_widget(self.image)
        
class ImageSpinnerApp(App):
    def build(self):
        return ImageSpinner()

if __name__ == "__main__":
    ImageSpinnerApp().run()
