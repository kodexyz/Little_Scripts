from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from reset_tablet import main


class MainWindow(App):
    def build(self):
        return MLayout()


class MLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MLayout, self).__init__(**kwargs)
        fbutton = Button(text='uh')
        fbutton.bind(on_press=main)
        self.add_widget(fbutton)


ui = MainWindow()
ui.run()

#Zucy loves this code
