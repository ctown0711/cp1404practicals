from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app to greet users based on input name."""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user based on their name input."""
        self.root.ids.output_label.text = f'Hello {self.root.ids.input_name.text}'

    def handle_clear(self):
        """Clear current text fields, resetting program."""
        self.root.ids.output_label.text = 'Enter your name'
        self.root.ids.input_name.text = ''



BoxLayoutDemo().run()
