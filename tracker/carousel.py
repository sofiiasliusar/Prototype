from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from datetime import datetime, timedelta
# python carousel.py -m screen:phone_iphone_5,portrait,scale=.5

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
        main_layout = FloatLayout(size_hint=(1, 0.8))
        

        # Create a layout to hold the input fields in three columns
        # create input_layout and put it in the middle by x and y
        input_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, 0.6)) #spacing=10
        input_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        
       

        # Add grey squares to input sum
        sum_layout = BoxLayout(orientation='vertical')
        for _ in range(5):
            sum_input = TextInput(hint_text="Sum", multiline=False, height=50) #size_hint=(0.5, 1)
            sum_layout.add_widget(sum_input)
        input_layout.add_widget(sum_layout)

        # Add lines to input description
        description_layout = BoxLayout(orientation='vertical')
        for _ in range(5):
            description_input = TextInput(hint_text="Description", multiline=False, height=50)
        # description_input.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            description_layout.add_widget(description_input)
        input_layout.add_widget(description_layout)

        # Add drop-down list for categories
        category_layout = BoxLayout(orientation='vertical') #size_hint=(0.5, 1)
        categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
        for _ in range(5):
            category_spinner = Spinner(text='Category', values=categories, height=50) 
            category_layout.add_widget(category_spinner)
        input_layout.add_widget(category_layout)
        main_layout.add_widget(input_layout)
        self.add_widget(main_layout)

if __name__ == '__main__':
    ExpenseApp().run()

    # review layout mistake later
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.carousel import Carousel
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.spinner import Spinner
# from datetime import datetime, timedelta

# class ExpenseApp(App):

#     def build(self):
#         # Create a layout to hold the button and carousel
#         main_layout = BoxLayout(orientation='vertical')

#         # Create a button at the top left corner
#         menu_button = Button(text="Menu", size_hint=(None, None), size=(100, 50))
#         main_layout.add_widget(menu_button)

#         # Create a carousel to switch between dates
#         carousel = Carousel(direction='right')
        
#         # Add screens for each date
#         for i in range(5):  # Let's say 5 days for simplicity
#             date = datetime.now() - timedelta(days=i)
#             screen = ExpenseScreen(date=date)
#             carousel.add_widget(screen)

#         main_layout.add_widget(carousel)

#         return main_layout

# class ExpenseScreen(BoxLayout):

#     def __init__(self, date, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'

#         # Display the current date at the top
#         self.add_widget(Label(text=date.strftime("%Y-%m-%d"), size_hint=(1, 0.1)))

#         # Create a layout to hold the input fields in three columns
#         input_layout = BoxLayout(orientation='horizontal')

#         self.add_widget(input_layout)

#         # Add grey squares to input sum
#         sum_layout = BoxLayout(orientation='vertical')
#         for _ in range(5):
#             sum_input = TextInput(hint_text="Sum", multiline=False, size_hint_y=None, height=50)
#             sum_layout.add_widget(sum_input)
#         input_layout.add_widget(sum_layout)

#         # Add lines to input description
#         description_layout = BoxLayout(orientation='vertical')
#         for _ in range(5):
#             description_input = TextInput(hint_text="Description", multiline=False, size_hint_y=None, height=50)
#             description_layout.add_widget(description_input)
#         input_layout.add_widget(description_layout)

#         # Add drop-down list for categories
#         category_layout = BoxLayout(orientation='vertical')
#         categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
#         for _ in range(5):
#             category_spinner = Spinner(text='Category', values=categories, size_hint_y=None, height=50)
#             category_layout.add_widget(category_spinner)
#         input_layout.add_widget(category_layout)

# if __name__ == '__main__':
#     ExpenseApp().run()