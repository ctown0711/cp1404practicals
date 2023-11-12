from kivy.app import App
from kivy.app import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934


class ConvertMiles(App):
    """Kivy app to convert miles to kilometres."""
    kilometres = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        """Convert users input of miles into kilometres within the GUI."""
        try:
            conversion = float(self.root.ids.input_number.text) * MILES_TO_KM_CONVERSION
            self.kilometres = str(conversion)
        except ValueError:
            self.root.ids.input_number.text = '0.0'

    def handle_increment(self, increment):
        """Increase or decrease the users input by one"""
        try:
            new_value = float(self.root.ids.input_number.text) + increment
        except ValueError:
            new_value = 0 + increment
        self.root.ids.input_number.text = str(new_value)


ConvertMiles().run()
