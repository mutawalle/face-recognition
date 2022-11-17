import os
import glob
import cv2 as cv
import data.configdata as cd
import eigen
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
    file = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.8, 0.8))
        self._popup.open()
    
    def load(self, filename):
        self.ids.test_image.source = filename[0]
        self.file = filename[0]
        self.dismiss_popup()

    def use_camera(self):
        cd.camera_use()
        path = self.getRootPath("/test/get_data/cap_cam_0.jpg")
        self.ids.test_image.source = path
        self.file = path

    def getRootPath(self, filePath):
        path = os.path.abspath(os.curdir)
        pathDir = list(filePath)
        pjg = len(pathDir)
        for i in range(pjg):
            if(pathDir[i] == '/'):
                pathDir[i] = chr(92)
        pathDir = "".join(pathDir)
        path += pathDir
        return path

    def press_check(self):
        path = self.ids.input_folder.text+chr(92)+"*.jpg"
        int_img = cd.Parser(path)
        listNamafile = glob.glob(path)
        img = cv.imread(self.file)
        img_resize = cv.resize(img,(256,256))
        grayscale_img = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
        int_img.append(grayscale_img)
        length = len(int_img)
        print("parser")
        print(length)
        print(int_img[0])
        print(int_img[length-1])
        x = cd.min_eigen_distance(eigen.convertGambar(eigen.eigenface(int_img)))
        self.ids.result_image.source = listNamafile[x]




class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()