from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
import matplotlib.pyplot as plt
from collections import OrderedDict

class MoodTrackerApp(App):
    def build(self):
        self.store = JsonStore('moods.json')

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.mood_input = TextInput(text='', hint_text='Enter your mood (1-10)', multiline=False)
        submit_btn = Button(text='Submit', size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.submit_mood)

        layout.add_widget(Label(text='How are you feeling today?'))
        layout.add_widget(self.mood_input)
        layout.add_widget(submit_btn)

        return layout

    
    def submit_mood(self, instance):
        mood_score = self.mood_input.text
        if mood_score.isdigit() and 1 <= int(mood_score) <= 10:
            self.store.put('mood_{}'.format(self.store.count()), mood=int(mood_score))
            self.update_mood_trend_graph()  # Update the mood trend graph
            self.mood_input.text = ''  # Reset the input after storing
        else:
            self.mood_input.text = 'Please enter a valid number between 1 and 10'

# Add a method to update the mood trend graph
    def update_mood_trend_graph(self):
        moods = OrderedDict(sorted(self.store.items()))  # Sort the stored moods by key
        dates = list(moods.keys())
        mood_scores = [moods[key]['mood'] for key in dates]

        plt.plot(dates, mood_scores, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Mood Score')
        plt.title('Mood Trend Over Time')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.savefig('mood_trend.png')  # Save the plot as an image
        plt.close()  # Close the plot to free up memory
if __name__ == '__main__':
    MoodTrackerApp().run()
