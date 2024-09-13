from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.result = Label(text="0", font_size=32, halign='right', size_hint_y=None, height=70)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        grid_layout = BoxLayout(orientation='horizontal')
        for button in buttons:
            grid_layout.add_widget(Button(text=button, on_press=self.on_button_press))
        layout.add_widget(grid_layout)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = '0'
            self.last_was_operator = False
        elif button_text == '=':
            try:
                self.result.text = str(eval(current))
                self.last_was_operator = False
            except Exception:
                self.result.text = 'Error'
        else:
            if current == '0' or self.last_was_operator:
                self.result.text = button_text
            else:
                self.result.text += button_text
            self.last_was_operator = button_text in self.operators

if __name__ == '__main__':
    CalculatorApp().run()
