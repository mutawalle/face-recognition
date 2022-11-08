import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (900,500)
Builder.load_file('my.kv')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)

class Root(Widget):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.8, 0.8))
        self._popup.open()
    
    def load(self, filename):
        self.ids.test_image.source = filename[0]

        self.dismiss_popup()


class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()