import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from datetime import datetime, timedelta
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# Database setup
def init_db():
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, sum REAL, description TEXT, category TEXT)')
    conn.commit()
    conn.close()

# Update or insert data into database
def update_db(date, sum, description, category):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (date, sum, description, category) VALUES (?, ?, ?, ?)', (date, sum, description, category))
    conn.commit()
    conn.close()

class ExpenseScreen(BoxLayout):
    def __init__(self, date, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.date = date.strftime("%d-%m-%Y")

        self.add_widget(Label(text=self.date, size_hint=(1, 0.1)))
        main_layout = FloatLayout(size_hint=(1, 0.8))

        self.sum_inputs = []
        self.description_inputs = []
        self.category_spinners = []

        input_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        sum_layout = BoxLayout(orientation='vertical')
        description_layout = BoxLayout(orientation='vertical')
        category_layout = BoxLayout(orientation='vertical') 
        categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

        for _ in range(10):
            sum_input = TextInput(hint_text="Sum", multiline=False, height=50)
            description_input = TextInput(hint_text="Description", multiline=False, height=50)
            category_spinner = Spinner(text='Category', values=categories, height=50)
            
            self.sum_inputs.append(sum_input)
            self.description_inputs.append(description_input)
            self.category_spinners.append(category_spinner)

            sum_layout.add_widget(sum_input)
            description_layout.add_widget(description_input)
            category_layout.add_widget(category_spinner)

        input_layout.add_widget(sum_layout)
        input_layout.add_widget(description_layout)
        input_layout.add_widget(category_layout)
        
        main_layout.add_widget(input_layout)
        self.add_widget(main_layout)

        bottom_button = Button(text="Submit", size_hint=(1, 0.1))
        bottom_button.bind(on_press=self.submit_expenses)
        self.add_widget(bottom_button)

    def submit_expenses(self, instance):
        for sum_input, description_input, category_spinner in zip(self.sum_inputs, self.description_inputs, self.category_spinners):
            if sum_input.text and description_input.text:  # Ensure some basic validation
                update_db(self.date, float(sum_input.text), description_input.text, category_spinner.text)

class ReviewScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu_layout = BoxLayout(orientation='vertical')

        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_to_main)
        menu_layout.add_widget(back_button)

        menu_label = Label(text="Menu Screen", size_hint=(1, 0.9))
        menu_layout.add_widget(menu_label)

        self.add_widget(menu_layout)

    def go_to_main(self, instance):
        # Switch back to the main screen
        self.manager.current = 'main'

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical')

        # Create the menu button
        menu_button = Button(text="Menu", size_hint=(None, None), size=(100, 50))
        menu_button.bind(on_press=self.open_menu_popup)
        main_layout.add_widget(menu_button)

        # Create the carousel
        carousel = Carousel(direction='left')
        for i in range(5):  
            date = datetime.now() - timedelta(days=i)
            screen = ExpenseScreen(date=date)
            carousel.add_widget(screen)
        main_layout.add_widget(carousel)

        self.add_widget(main_layout)

    def open_menu_popup(self, instance):
        # Create the popup content
        popup_width = 0.5  # 30% of the screen width
        popup_height = 1  # 100% of the screen height

        # Create the popup content
        popup_content = BoxLayout(orientation='vertical')
        buttons_layout = BoxLayout(orientation='vertical', size_hint_y=0.33)
        spacer_layout = BoxLayout()  # This will take the remaining space

        # Create buttons for each option
        option_names = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        for option_name in option_names:
            button = Button(text=option_name, size_hint_y=None, height=50)
            button.bind(on_press=self.go_to_review)
            buttons_layout.add_widget(button)

        popup_content.add_widget(buttons_layout)
        popup_content.add_widget(spacer_layout)  # Add the spacer to fill space

        # Create and show the popup
        popup = Popup(title='Menu', content=popup_content,
                      size_hint=(popup_width, popup_height), pos_hint={'x': 0, 'top': 1})
        popup.open()

    def go_to_review(self, instance):
        self.manager.current = "review"

class ExpenseApp(App):
    def build(self):
        init_db()  # Initialize database
        self.screen_manager = ScreenManager(transition=SlideTransition(duration=0))
        
        main_screen = MainScreen(name='main')
        self.screen_manager.add_widget(main_screen)
        review_screen = ReviewScreen(name='review')
        self.screen_manager.add_widget(review_screen)
        
        return self.screen_manager

if __name__ == '__main__':
    ExpenseApp().run()
