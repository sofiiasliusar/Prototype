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
from datetime import datetime, timedelta, date
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import ListProperty, DictProperty
from kivy.uix.image import Image
from kivy.uix.spinner import SpinnerOption, Spinner

class DescriptionInput(TextInput):
    pass
# Database setup
def init_db():
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS button_states (date TEXT PRIMARY KEY, button_state TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS totals (date TEXT PRIMARY KEY, total REAL)')  # Add initialization of totals table
    conn.commit()
    c.execute('SELECT * FROM expenses')
    data = c.fetchall()
    conn.close()
    return data

# Update or insert data into database
def update_db(date, sum, description, category):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO expenses (date, sum, description, category) VALUES (?, ?, ?, ?)', (date, sum, description, category))
    conn.commit()
    conn.close()

# Update or insert button state into database
def update_button_state(date, button_state):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO button_states (date, button_state) VALUES (?, ?)', (date, button_state))
    conn.commit()
    conn.close()
# button_states

# Get button state from database for a specific date
def get_button_state(date):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('SELECT button_state FROM button_states WHERE date=?', (date,))
    data = c.fetchone()
    conn.close()
    return data[0] if data else 'Submit'  # Default to 'Submit' if no button state is found
def create_table(date):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    table_name = "expenses_" + date.strftime("%d_%m_%Y")
    c.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, sum REAL, description TEXT, category TEXT)')
    conn.commit()
    conn.close()
def update_or_insert_row(table_name, row_id, sum_value, description, category):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM {table_name} WHERE id=?', (row_id,))
    data = c.fetchone()
    if data:
        # Update existing row
        c.execute(f'UPDATE {table_name} SET sum=?, description=?, category=? WHERE id=?', (sum_value, description, category, row_id))
    else:
        # Insert new row
        c.execute(f'INSERT INTO {table_name} (id, sum, description, category) VALUES (?, ?, ?, ?)', (row_id, sum_value, description, category))
    conn.commit()
    conn.close()
def delete_row(table_name, row_id):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute(f'DELETE FROM {table_name} WHERE id=?', (row_id,))
    conn.commit()
    conn.close()
def save_total(date, total):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO totals (date, total) VALUES (?, ?)', (date, total))
    conn.commit()
    conn.close()

def get_total(date):
    conn = sqlite3.connect('expenseapp.db')
    c = conn.cursor()
    c.execute('SELECT total FROM totals WHERE date=?', (date,))
    data = c.fetchone()
    conn.close()
    return data[0] if data else None
class ExpenseScreen(BoxLayout):
    def __init__(self, date, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.date = date.strftime("%d-%m-%Y")
        self.weekday = date.strftime("%A") 
        self.table_name = "expenses_" + date.strftime("%d_%m_%Y")
        create_table(date)  # Create table for the specific date if not exists

        self.add_widget(Label(text=self.date, size_hint=(1, 0.1)))
        self.add_widget(Label(text=self.weekday, size_hint=(1, 0.1)))
        
        main_layout = FloatLayout(size_hint=(1, 0.7))

        self.sum_inputs = []
        self.description_inputs = []
        self.category_spinners = []

        input_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        sum_layout = BoxLayout(orientation='vertical', size_hint=(0.2, 1))
        description_layout = BoxLayout(orientation='vertical', size_hint=(0.6, 1))
        category_layout = BoxLayout(orientation='vertical', size_hint=(0.1, 1))
        # categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"] + [""]
        category_images = {
            "Food": r"C:\Prototype-main\sprites\food.png",
            "Transportation": r"\Prototype-main\sprites\transportation.png",
            "Rest": r"\Prototype-main\sprites\rest.png",
            "Utilities": r"\Prototype-main\sprites\utilities.png",
            "Beauty": r"\Prototype-main\sprites\beauty_health.png",
            "": r"\Prototype-main\sprites\blank.png"

        }

        # Add image paths to the categories list
        categories = list(category_images.keys()) 
        for _ in range(10):
            sum_input = TextInput(hint_text="Sum", multiline=False, height=50)
            description_input = DescriptionInput(hint_text="Description", multiline=False, height=50)
            category_spinner = ImageSpinner(text='', values=categories, height=50, category_images=category_images)

            
            self.sum_inputs.append(sum_input)
            self.description_inputs.append(description_input)
            self.category_spinners.append(category_spinner)

            sum_layout.add_widget(sum_input)
            description_layout.add_widget(description_input)
            category_layout.add_widget(category_spinner)

        input_layout.add_widget(sum_layout)
        input_layout.add_widget(BoxLayout(size_hint=(0.05, 1)))
        input_layout.add_widget(description_layout)
        input_layout.add_widget(BoxLayout(size_hint=(0.05, 1)))
        input_layout.add_widget(category_layout)
        
        main_layout.add_widget(input_layout)
        self.add_widget(main_layout)
        self.total_label = Label(text="", size_hint=(1, 0.1))
        self.add_widget(self.total_label)
        self.submit_button = Button(text=get_button_state(self.date), size_hint=(1, 0.1))
        self.submit_button.bind(on_press=self.on_button_press)
        self.add_widget(self.submit_button)
        self.load_data()
        self.load_total()
        # Load existing data into input fields
        data = init_db()
        for i, row in enumerate(data):
            if row[1] == self.date:
                self.sum_inputs[i].text = str(row[2])
                self.description_inputs[i].text = row[3]
                self.category_spinners[i].text = row[4]
                self.set_readonly(True)  # Set fields to readonly if already submitted

    def on_button_press(self, instance):
        if instance.text == 'Submit':
            total = 0
            for i, (sum_input, description_input, category_spinner) in enumerate(zip(self.sum_inputs, self.description_inputs, self.category_spinners), start=1):
                if sum_input.text and description_input.text:  # Ensure basic validation
                    update_or_insert_row(self.table_name, i, float(sum_input.text), description_input.text, category_spinner.text)
                    total += float(sum_input.text)  
                else:
                    # If sum or description is empty, delete the row from the database
                    delete_row(self.table_name, i)
            update_button_state(self.date, 'Edit')  # Update button state to 'Edit'
            self.set_readonly(True)
            instance.text = 'Edit'
             # Update total label
            self.total_label.text = f"Total: {total}"
            # Save total to separate table
            save_total(self.date, total)
        elif instance.text == 'Edit':
            self.set_readonly(False)
            update_button_state(self.date, 'Submit')  # Update button state to 'Submit'
            instance.text = 'Submit'
            # Clear total label when in 'Edit' mode
            self.total_label.text = ""
            
    def load_total(self):
        total = get_total(self.date)
        if total is not None:
            self.total_label.text = f"Total: {total}"
    def set_readonly(self, readonly):
        for sum_input, description_input, category_spinner in zip(self.sum_inputs, self.description_inputs, self.category_spinners):
            sum_input.readonly = readonly
            description_input.disabled = readonly
            category_spinner.disabled = readonly
    def on_pre_enter(self, *args):
        # Load existing data into input fields every time the screen is shown
        self.load_data()
        button_state = get_button_state(self.date)
        if button_state == 'Edit':
            total = get_total(self.date)
            if total is not None:
                self.total_label.text = f"Total: {total}"
            else:
                self.total_label.text = ""

        # Set readonly state based on button state
        self.set_readonly(button_state == 'Edit')
    def load_data(self):
        conn = sqlite3.connect('expenseapp.db')
        c = conn.cursor()
        c.execute(f'SELECT * FROM {self.table_name}')
        data = c.fetchall()
        conn.close()

        for i, row in enumerate(data):
            if i < len(self.sum_inputs):
                self.sum_inputs[i].text = str(row[1])
                self.description_inputs[i].text = row[2]
                self.category_spinners[i].text = row[3]
        self.set_readonly(get_button_state(self.date) == 'Edit')

class ImageSpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super(ImageSpinnerOption, self).__init__(**kwargs)

        # Create an image widget and add it to the spinner option
        self.image = Image(source=kwargs['text'], size_hint=(None, None), allow_stretch=True)
        self.bind(size=self.update_image_pos)
        self.add_widget(self.image)
        self.text = "" 

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
# 'assets/Sacramento-Regular.ttf'

class ImageSpinner(Spinner):
    category_images = DictProperty({})  # Define category_images as a DictProperty

    def __init__(self, **kwargs):
        super(ImageSpinner, self).__init__(**kwargs)
        self.category_images = kwargs.get('category_images', {})  # Initialize category_images

    def on_text(self, instance, value):
        if value in self.category_images:
            # Set the background image based on the selected value
            self.background_normal = self.category_images[value]

class ReviewScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu_layout = BoxLayout(orientation='vertical')

        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_to_main)
        menu_layout.add_widget(back_button)

        self.menu_label = Label(text="Review Screen", size_hint=(1, 0.9))
        menu_layout.add_widget(self.menu_label)

        self.add_widget(menu_layout)

    def go_to_main(self, instance):
        # Switch back to the main screen
        self.manager.current = 'main'

class WeekScreen(ReviewScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_label.text = "Week Total"

class MonthScreen(ReviewScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_label.text = "Month Total"

class ReminderScreen(ReviewScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_label.text = "Set a reminder"

class SettingsScreen(ReviewScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_label.text = "Change language"
class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical')

        # Create the menu button
        menu_button = Button(text="Menu", size_hint=(None, None), size=(100, 50))
        menu_button.bind(on_press=self.open_menu_popup)
        main_layout.add_widget(menu_button)

        # Create the carousel
        carousel = Carousel(direction='right')
        
        today = datetime.now().date()
        # Calculate Monday of the current week
        monday = today - timedelta(days=today.weekday())
        
        for i in range(7):
            current_date = monday + timedelta(days=i)
            screen = ExpenseScreen(date=current_date)
            carousel.add_widget(screen)
        main_layout.add_widget(carousel)

        self.add_widget(main_layout)
        current_index = (today - monday).days
        carousel.load_slide(carousel.slides[current_index])
    def open_menu_popup(self, instance):
        # Create the popup content
        popup_width = 0.5  # 30% of the screen width
        popup_height = 1  # 100% of the screen height

        # Create the popup content
        popup_content = BoxLayout(orientation='vertical')
        buttons_layout = BoxLayout(orientation='vertical', size_hint_y=0.33)
        spacer_layout = BoxLayout()  # This will take the remaining space

        # Create buttons for each option
        option_names = ["Review", "Week", "Month", "Reminder", "Settings"]
        for option_name in option_names:
            button = Button(text=option_name, size_hint_y=None, height=50)
            button.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(button)

        popup_content.add_widget(buttons_layout)
        popup_content.add_widget(spacer_layout)  # Add the spacer to fill space

        # Create and show the popup
        popup = Popup(title='Menu', content=popup_content,
                      size_hint=(popup_width, popup_height), pos_hint={'x': 0, 'top': 1})
        popup.open()
    def on_button_press(self, instance):
        # This method will be called each time a button is pressed
        if instance.text == "Review":
            self.go_to_review(instance)
        elif instance.text == "Week":
            self.go_to_week(instance)
        elif instance.text == "Month":
            self.go_to_month(instance)
        elif instance.text == "Reminder":
            self.set_reminder(instance)
        elif instance.text == "Settings":
            self.open_settings(instance)
    def go_to_review(self, instance):
        self.manager.current = "review"
    def go_to_week(self, instance):
        self.manager.current = "week"
    def go_to_month(self, instance):
        self.manager.current = "month"
    def set_reminder(self, instance):
        self.manager.current = "reminder"
    def open_settings(self, instance):
        self.manager.current = "settings"
    

class ExpenseApp(App):
    def build(self):
        Builder.load_file('expense.kv')
        init_db()  # Initialize database
        self.screen_manager = ScreenManager(transition=SlideTransition(duration=0))
        
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

        
        return self.screen_manager

if __name__ == '__main__':
    ExpenseApp().run()
# python data_storage.py -m screen:phone_iphone_6,portrait,scale=.5
