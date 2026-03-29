from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="Ali Sher Printer Ready", font_size='25sp'))
        btn = Button(text="Welcome", size_hint=(1, 0.2))
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MainApp().run()
