from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.spinner import SpinnerOption, Spinner


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

class DefaultImageOption(BoxLayout):
    def __init__(self, image_path, **kwargs):
        super(DefaultImageOption, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = '50dp'
        
        
        # Create an image widget and add it to the option
        self.image = Image(source=image_path, size_hint=(None, None), size=(50, 50), allow_stretch=True)
        self.add_widget(self.image)
        

class ImageSpinner(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageSpinner, self).__init__(**kwargs)

        # List of image paths
        self.image_paths = [
            r"C:\Prototype-main\sprites\blank.png",
            r"C:\Prototype-main\sprites\food.png",
            r"\Prototype-main\sprites\transportation.png",
            r"\Prototype-main\sprites\rest.png",
        ]

        # Spinner widget to select images
        self.spinner = Spinner(
            option_cls=ImageSpinnerOption,
            values=self.image_paths[1:],  # Exclude the blank image from the values
            text=self.image_paths[0],  # Set the first image as default, before it was 1 - displayed blank and wrote food. I changed to 0 - displays and writes blank
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5},
        )
        self.spinner.bind(text=self.on_spinner_select)

        # Add default image within the spinner
        default_image_option = DefaultImageOption(image_path=self.image_paths[0])
        self.spinner.values.append(self.image_paths[0])
        self.spinner.add_widget(default_image_option)

        self.add_widget(self.spinner)

    def on_spinner_select(self, spinner, text):
        # Update image, otherwise just text is changed
        self.spinner.children[0].image.source = text

class ImageSpinnerApp(App):
    def build(self):
        return ImageSpinner()


if __name__ == "__main__":
    ImageSpinnerApp().run()

# take away the label and add storage
# has default display