from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.num1 = TextInput(
            hint_text="প্রথম সংখ্যা",
            input_filter="float"
        )

        self.num2 = TextInput(
            hint_text="দ্বিতীয় সংখ্যা",
            input_filter="float"
        )

        add_button = Button(
            text="+ যোগ করুন"
        )

        self.result = Label(
            text="ফলাফল এখানে দেখাবে"
        )

        add_button.bind(on_press=self.add_numbers)

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(add_button)
        layout.add_widget(self.result)

        return layout

    def add_numbers(self, instance):
        number1 = float(self.num1.text)
        number2 = float(self.num2.text)

        result = number1 + number2

        self.result.text = f"ফলাফল = {result}"


CalculatorApp().run()
