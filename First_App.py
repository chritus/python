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

        self.press = Button(text = "Click Me")
        self.press.bind(on_click = self.Click_me)
        self.add_widget(self.press)
        
    def Click_me(self, instance):
        print("Your name is " + self.name.text)
        print("Your marks is " + self.marks.text)
        print("Your gender is " + self.gender.text)
        print("")

class parentApp(App):
    def build(self):
        return childApp()
    
if __name__ == "__main__":
    parentApp().run()
