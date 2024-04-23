# from kivy.app import App
# from kivy.uix.carousel import Carousel
# from kivy.uix.screenmanager import Screen
# from kivy.core.window import Window

# # Set the window size to emulate a common smartphone size
# Window.size = (375, 667)

# class CustomScreen(Screen):
#     def __init__(self, content, **kwargs):
#         super().__init__(**kwargs)
#         # Add whatever content is passed to the screen
#         self.add_widget(content)

# class ScreenCarouselApp(App):
#     def build(self):
#         carousel = Carousel(direction='right', loop=True)

#         # Create different content for each screen
#         contents = [
#             CustomScreen(content=Label(text="First Screen")),
#             CustomScreen(content=Label(text="Second Screen")),
#             CustomScreen(content=Label(text="Third Screen"))
#         ]

#         # Add screens to the Carousel
#         for screen in contents:
#             carousel.add_widget(screen)

#         return carousel

# # Run the application
# if __name__ == '__main__':
#     ScreenCarouselApp().run()
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window

# Set the window size to emulate a common smartphone size
Window.size = (375, 667)

# KV language string to define the user interface
kv = '''
<CustomScreen>:
    Label:
        text: root.name

Carousel:
    direction: 'right'
    loop: True
    CustomScreen:
        name: "First Screen"
    CustomScreen:
        name: "Second Screen"
    CustomScreen:
        name: "Third Screen"
'''

class CustomScreen(Screen):
    pass

class ScreenCarouselApp(App):
    def build(self):
        return Builder.load_string(kv)

# Run the application
if __name__ == '__main__':
    ScreenCarouselApp().run()
