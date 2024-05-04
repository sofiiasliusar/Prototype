import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        
        self.images = {
            'Blank': {'label': 'Blank', 'background': r"C:\Prototype-main\sprites\blank.png"},
            'Food': {'label': 'Food', 'background': r"C:\Prototype-main\sprites\food.png"},
            'Transport': {'label': 'Transport', 'background': r"C:\Prototype-main\sprites\transportation.png"},
            'Rest': {'label': 'Rest', 'background': r"C:\Prototype-main\sprites\rest.png"},
        }

        self.spinner = Spinner(
            text=self.images['Blank']['label'],
            values=[value['label'] for value in self.images.values()],
            size_hint=(None, None),
            size=(150, 44),
            pos_hint={'center_x': 0.5}
        )

        self.image = Image(source=self.images['Blank']['background'])

        submit_button = Button(text="Submit", on_press=self.submit)

        self.add_widget(self.spinner)
        self.add_widget(self.image)
        self.add_widget(submit_button)

    def submit(self, instance):
        selected_label = self.spinner.text
        selected_background = self.images[selected_label]['background']
        # Update SQLite with the selected label
        self.update_sqlite(selected_label)
        # Update image with the selected background
        self.image.source = selected_background

    def update_sqlite(self, selected_label):
        # Here, you would implement code to store the selected label to SQLite
        # For demonstration purposes, I'm just printing the selected label
        print("Storing '{}' to SQLite".format(selected_label))

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
# submit to db but change instantly and change to backgroud - gpt first question