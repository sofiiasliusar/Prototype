from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

# Adjusting window size to emulate a smartphone (iPhone 11 Pro Max size in portrait)
Window.size = (414, 896)

# Writing kv language
kv = '''
# Creating screen
MDScreen:

    # Defining MDSwiper
    MDSwiper:
        size_hint: 1, 1  # Ensure it uses the full size of its parent
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        padding: 0  # Remove any padding around the swiper
        spacing: 0  # Eliminates any space between items
        loop: True  # Allows infinite looping through swiper items

        # Defining items for swiper, each with its own content
        MDSwiperItem:
            MDScreen:
                MDLabel:
                    text: "Screen 1: Welcome!"
                    halign: 'center'
                    valign: 'center'
                    font_style: 'H2'
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: '10dp'
                    spacing: '10dp'
                    MDTextField:
                        hint_text: "Enter text here"

        MDSwiperItem:
            MDScreen:
                MDLabel:
                    text: "Screen 2: Gallery"
                    halign: 'center'
                    valign: 'center'
                    font_style: 'H2'
                MDFloatLayout:
                    FitImage:
                        source: "5.png"
                        size_hint: 1, 1
                        radius: [20, 0]

        MDSwiperItem:
            MDScreen:
                MDLabel:
                    text: "Screen 3: Profile"
                    halign: 'center'
                    valign: 'center'
                    font_style: 'H2'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTextField:
                        hint_text: "User Name"
                    MDTextField:
                        hint_text: "Email"
'''

# App class
class Main(MDApp):

    def build(self):
        # This will load kv language
        screen = Builder.load_string(kv)

        # Returning screen
        return screen

# Running app
Main().run()
