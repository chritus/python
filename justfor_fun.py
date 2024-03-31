import kivy
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class childApp(GridLayout):
    def  __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        # Create the widgets we'll be
        self.add_widget(Label(text="Name"))
        self.name = TextInput()
        self.add_widget(self.name)


        self.add_widget(Label(text="Marks"))
        self.marks = TextInput()
        self.add_widget(self.marks)


        self.add_widget(Label(text="gender"))
        self.gender = TextInput()
        self.add_widget(self.gender)


class parentApp(App):
    def build(self):
        return childApp()
    
if __name__ == "__main__":
    parentApp().run()