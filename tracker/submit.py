from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('appdata.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)')
    c.execute('SELECT content FROM data WHERE id = 1')
    initial_content = c.fetchone()
    conn.commit()
    conn.close()
    return initial_content[0] if initial_content else ""

# Update or insert data into database
def update_db(content):
    conn = sqlite3.connect('appdata.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO data (id, content) VALUES (1, ?)', (content,))
    conn.commit()
    conn.close()

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        # Load initial content from database
        initial_content = init_db()

        self.text_input = TextInput(text=initial_content, size_hint=(1, .8), multiline=False, readonly=False)
        self.add_widget(self.text_input)

        self.button = Button(text='Edit' if initial_content else 'Submit', size_hint=(1, .2))
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

        # Set readonly status based on whether text was loaded
        self.text_input.readonly = True if initial_content else False

    def on_button_press(self, instance):
        if self.button.text == 'Submit':
            update_db(self.text_input.text)
            self.text_input.readonly = True  # Make the text input non-editable
            self.button.text = 'Edit'
        elif self.button.text == 'Edit':
            self.text_input.readonly = False  # Make the text input editable
            self.button.text = 'Submit'

class MyApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MyApp().run()

# python submit.py -m screen:phone_iphone_6,portrait,scale=.5