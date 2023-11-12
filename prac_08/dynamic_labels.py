from kivy.app import App
from kivy.app import Builder
from kivy.uix.label import Label
from random import randint


class DynamicLabels(App):

    def __init__(self):
        super().__init__()
        self.names = ['Caleb', 'Alebc', 'Lebca', 'Ebcal', 'Bcale']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dyanmic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            red = randint(0, 1)
            green = randint(0, 1)
            blue = randint(0, 1)
            temp_label = Label(text=name, color=(red, blue, green, 1))
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabels().run()
