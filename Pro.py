from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="اضغط هنا", on_press=lambda x: print("تم الضغط!"))

MyApp().run()
