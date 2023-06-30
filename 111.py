import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = 50
        
        self.number1_input = TextInput(multiline=False)
        self.number2_input = TextInput(multiline=False)
        self.add_widget(self.number1_input)
        self.add_widget(self.number2_input)
        
        self.add_widget(Label(text="Результат:"))
        self.result_label = Label()
        self.add_widget(self.result_label)

        self.add_widget(Button(text="Сложить", on_press=self.add_numbers))

    def add_numbers(self, *args):
        try:
            number1 = float(self.number1_input.text)
            number2 = float(self.number2_input.text)
            result = number1 + number2
            self.result_label.text = str(result)
        except ValueError:
            self.result_label.text = "Некорректный ввод"

class MyApp(App):
    def build(self):
        return MyBoxLayout()

MyApp().run()
