from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.spinner import Spinner

class ExpenseTrackerApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10)

        date_label = Label(text="Current Date: Tuesday, March 19, 2024")
        layout.add_widget(date_label)

        amount_input = TextInput(multiline=False)
        layout.add_widget(amount_input)

        category_button = Button(text='Select category')
        categories = ['Food', 'Entertainment', 'Housing', 'Transportation', 'Other']
        category_spinner = Spinner(text=categories[0], values=categories)
        category_button.bind(on_release=category_button.open_spinner)
        category_button.spinner = category_spinner
        layout.add_widget(category_button)

        description_input = TextInput(multiline=True)
        layout.add_widget(description_input)

        total_label = Label(text="Total expenses: $0.00")
        layout.add_widget(total_label)

        return layout

if __name__ == '__main__':
    ExpenseTrackerApp().run()