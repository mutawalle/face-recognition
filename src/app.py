import os
import time
import glob
import configdata as cd
import eigen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

Window.size = (900,500)
Builder.load_file('my.kv')

class LoadDirDialog(FloatLayout):
    loadDir = ObjectProperty(None)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)

class Root(Widget):
    file = ObjectProperty(None)
    dir = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load_dir(self):
        content = LoadDirDialog(loadDir = self.load_dir)
        self._popup = Popup(title="Load Dataset Folder", content=content,
                            size_hint=(0.8, 0.8))
        self._popup.open()
    
    def load_dir(self, filename):
        self.dir = filename[0]
        self.dismiss_popup()

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
        path = self.dir+"/*.jpg"
        listNamafile = glob.glob(path)
        y1 = time.time()
        x = eigen.face_reg_func(path, self.file)
        y2 = time.time()
        s = "Time execution : " + str(y2-y1) + " s"
        self.ids.time_exec.text = s
        self.ids.result_image.source = listNamafile[x]




class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()