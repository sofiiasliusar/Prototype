from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from datetime import datetime, timedelta

class ExpenseApp(App):

    def build(self):
        # Create the ScreenManager to manage multiple screens
        self.screen_manager = ScreenManager(transition=SlideTransition(duration=0))

        # Create and add the main screen
        main_screen = MainScreen(name='main')
        self.screen_manager.add_widget(main_screen)
        review_screen = ReviewScreen(name='review')
        self.screen_manager.add_widget(review_screen)
        week_screen = WeekScreen(name='week')
        self.screen_manager.add_widget(week_screen)
        month_screen = MonthScreen(name='month')
        self.screen_manager.add_widget(month_screen)
        reminder_screen = ReminderScreen(name='reminder')
        self.screen_manager.add_widget(reminder_screen)
        settings_screen = SettingsScreen(name='settings')
        self.screen_manager.add_widget(settings_screen)
    
        # Create the five screens that buttons in the menu will lead to
        for i in range(1, 6):
            screen_name = f'screen_{i}'
            screen = ExpenseScreen(name=screen_name)
            self.screen_manager.add_widget(screen)

        return self.screen_manager

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical')

        menu_button = Button(text="Menu", size_hint=(None, None), size=(100, 50))
        menu_button.bind(on_press=self.open_menu_popup)
        main_layout.add_widget(menu_button)

        carousel = Carousel(direction='left')
        
        for i in range(5):  
            date = datetime.now() - timedelta(days=i)
            screen = ExpenseScreen(date=date)
            carousel.add_widget(screen)

        main_layout.add_widget(carousel)

        self.add_widget(main_layout)

    def open_menu_popup(self, instance):
        # Create the popup content
        popup_content = BoxLayout(orientation='vertical')
        popup = Popup(title='Menu', content=popup_content, size_hint=(None, None), size=(200, 200))

        # Create buttons for each option
        button_1 = Button(text="Review", size_hint=(None, None), size=(100, 50))
        button_1.on_press=self.go_to_review
        # TypeError: 'NoneType' object is not callable
        #The issue arises from how I'm assigning the on_press attribute to the buttons in open_menu_popup method. 
        #When I do button_1.on_press=self.go_to_review(), 
        # I'm actually calling the go_to_review() method immediately and assigning its return value (which is None) to the on_press attribute.
        # To fix this, I should remove the parentheses () when assigning the on_press attribute, like so: button_1.on_press = self.go_to_review.
        popup_content.add_widget(button_1)
        button_2 = Button(text="Week", size_hint=(None, None), size=(100, 50))
        button_2.on_press=self.go_to_week
        popup_content.add_widget(button_2)
        button_3 = Button(text="Month", size_hint=(None, None), size=(100, 50))
        button_3.on_press=self.go_to_month
        popup_content.add_widget(button_3)
        button_4 = Button(text="Reminder", size_hint=(None, None), size=(100, 50))
        button_4.on_press=self.go_to_reminder
        popup_content.add_widget(button_4)
        button_5 = Button(text="Settings", size_hint=(None, None), size=(100, 50)) #!!!also good for app with monitoring
        button_5.on_press=self.go_to_settings
        popup_content.add_widget(button_5)
    

        # option_names = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5"]
        # for option_name in option_names:
        #     button = Button(text=option_name, size_hint=(None, None), size=(200, 50))
        #     button.bind(on_press=self.switch_to_screen)
        #     popup_content.add_widget(button)

        # Open the popup
        popup.open()
    def go_to_review(self):
        self.manager.current = "review"
    def go_to_week(self):
        self.manager.current = "week"
    def go_to_month(self):
        self.manager.current = "month"
    def go_to_reminder(self):
        self.manager.current = "reminder"
    def go_to_settings(self):
        self.manager.current = "settings"
    # def switch_to_screen(self, instance):
    #     # Get the text of the button pressed
    #     screen_name = instance.text.lower().replace(" ", "_")
    #     # Switch to the corresponding screen
    #     self.manager.current = screen_name
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
        self.manager.current = 'main'

class WeekScreen(ReviewScreen):
    pass
class MonthScreen(ReviewScreen):
    pass
class ReminderScreen(ReviewScreen):
    pass
class SettingsScreen(ReviewScreen):
    pass

    def go_to_main(self, instance):
        # Switch back to the main screen
        self.manager.current = 'main'
class ExpenseScreen(Screen):

    def __init__(self, date=None, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        if date:
            self.add_widget(Label(text=date.strftime("%d-%m-%Y"), size_hint=(1, 0.1)))
        main_layout = FloatLayout(size_hint=(1, 0.8))

        input_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, 0.6))
        input_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        sum_layout = BoxLayout(orientation='vertical')
        for _ in range(5):
            sum_input = TextInput(hint_text="Sum", multiline=False, height=50)
            sum_layout.add_widget(sum_input)
        input_layout.add_widget(sum_layout)

        description_layout = BoxLayout(orientation='vertical')
        for _ in range(5):
            description_input = TextInput(hint_text="Description", multiline=False, height=50)
            description_layout.add_widget(description_input)
        input_layout.add_widget(description_layout)

        category_layout = BoxLayout(orientation='vertical') 
        categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
        for _ in range(5):
            category_spinner = Spinner(text='Category', values=categories, height=50) 
            category_layout.add_widget(category_spinner)
        input_layout.add_widget(category_layout)
        main_layout.add_widget(input_layout)
        self.add_widget(main_layout)

if __name__ == '__main__':
    ExpenseApp().run()

# python menu.py -m screen:phone_iphone_6,portrait,scale=.5