from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file("ComicCreator.kv")

class ComicCreator(AnchorLayout):
    pass

class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()

if __name__=="__main__":
    ComicCreatorApp().run()        