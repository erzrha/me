import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
kivy.require('1.9.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_num(self):
        self.random_label.text=str(random.randint(0,1000))
        return

class Erzapp(App):

    def build(self):
        return MyRoot()
my_app = Erzapp()
my_app.run()
