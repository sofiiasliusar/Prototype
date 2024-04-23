from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from datetime import datetime, timedelta

class ExpenseApp(App):

    def build(self):
        # Create a layout to hold the button and carousel
        main_layout = BoxLayout(orientation='vertical')

        # Create a button at the top left corner
        menu_button = Button(text="Menu", size_hint=(None, None), size=(100, 50))
        main_layout.add_widget(menu_button)

        # Create a carousel to switch between dates
        carousel = Carousel(direction='left')
        
        # Add screens for each date
        for i in range(5):  # Let's say 5 days for simplicity
            date = datetime.now() - timedelta(days=i)
            screen = ExpenseScreen(date=date)
            carousel.add_widget(screen)

        main_layout.add_widget(carousel)

        return main_layout

class ExpenseScreen(BoxLayout):

    def __init__(self, date, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Display the current date at the top
        self.add_widget(Label(text=date.strftime("%Y-%m-%d"), size_hint=(1, 0.1)))

        # Display a list of expenses (dummy data for now)
        expenses = [
            "Coffee: $2.50",
            "Lunch: $10.00",
            "Transportation: $5.00"
        ]
        for expense in expenses:
            self.add_widget(Label(text=expense, size_hint=(1, 0.1)))

if __name__ == '__main__':
    ExpenseApp().run()

