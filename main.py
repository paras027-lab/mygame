from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=40, spacing=20, **kwargs)
        self.count = 0
        self.label = Label(text="Taps: 0", font_size="40sp")
        btn = Button(text="Tap me", font_size="30sp", size_hint_y=0.3)
        btn.bind(on_release=self.tap)
        self.add_widget(self.label)
        self.add_widget(btn)

    def tap(self, *_):
        self.count += 1
        self.label.text = f"Taps: {self.count}"


class GameApp(App):
    def build(self):
        return Root()


GameApp().run()
