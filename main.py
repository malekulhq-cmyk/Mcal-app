from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def calculate(self, operation):

        try:
            number1 = float(self.number1.text)
            number2 = float(self.number2.text)

            if operation == "+":
                result = number1 + number2

            elif operation == "-":
                result = number1 - number2

            elif operation == "*":
                result = number1 * number2

            elif operation == "/":
                if number2 == 0:
                    self.result.text = "Cannot divide by zero"
                    return

                result = number1 / number2

            self.result.text = f"Result: {result}"

        except ValueError:
            self.result.text = "Please enter valid numbers"


    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="Simple Calculator",
            font_size=28
        )

        self.number1 = TextInput(
            hint_text="First number",
            input_filter="float",
            multiline=False,
            font_size=22
        )

        self.number2 = TextInput(
            hint_text="Second number",
            input_filter="float",
            multiline=False,
            font_size=22
        )

        buttons = BoxLayout(
            spacing=10,
            size_hint_y=None,
            height=60
        )

        add_button = Button(text="+")
        subtract_button = Button(text="-")
        multiply_button = Button(text="×")
        divide_button = Button(text="÷")

        add_button.bind(
            on_press=lambda x: self.calculate("+")
        )

        subtract_button.bind(
            on_press=lambda x: self.calculate("-")
        )

        multiply_button.bind(
            on_press=lambda x: self.calculate("*")
        )

        divide_button.bind(
            on_press=lambda x: self.calculate("/")
        )

        buttons.add_widget(add_button)
        buttons.add_widget(subtract_button)
        buttons.add_widget(multiply_button)
        buttons.add_widget(divide_button)

        self.result = Label(
            text="Result: ",
            font_size=24
        )

        layout.add_widget(title)
        layout.add_widget(self.number1)
        layout.add_widget(self.number2)
        layout.add_widget(buttons)
        layout.add_widget(self.result)

        return layout


if __name__ == "__main__":
    CalculatorApp().run()
