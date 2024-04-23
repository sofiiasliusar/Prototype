from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime, timedelta

# Set the window size to emulate a common smartphone size
Window.size = (375, 667)

# KV language string to define the user interface
kv = '''
<CustomScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.date
            font_size: '20sp'
        Label:
            text: "Expenses for " + root.date
            font_size: '16sp'

ScreenManager:
    id: manager
    Carousel:
        direction: 'right'
        loop: True
        CustomScreen:
            name: "Today"
            date: root.get_date(0)
        CustomScreen:
            name: "Yesterday"
            date: root.get_date(-1)
        CustomScreen:
            name: "Two Days Ago"
            date: root.get_date(-2)
'''

class CustomScreen(Screen):
    date = ""

    def get_date(self, offset):
        return (datetime.now() + timedelta(days=offset)).strftime("%Y-%m-%d")

class ScreenCarouselApp(App):
    def build(self):
        return Builder.load_string(kv)

# Run the application
if __name__ == '__main__':
    ScreenCarouselApp().run()
