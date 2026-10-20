"""Món Quà Nhỏ Dành Cho Em - bản Android Kivy."""

import random
from pathlib import Path

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = (1, 0.973, 0.961, 1)

PINK = (1, 0.863, 0.91, 1)
ROSE = (0.91, 0.365, 0.514, 1)
DEEP_ROSE = (0.72, 0.231, 0.384, 1)
TEXT = (0.443, 0.208, 0.302, 1)
WHITE = (1, 1, 1, 1)

KV = """
<GiftButton>:
    background_normal: ""
    background_color: 0, 0, 0, 0
    color: 1, 1, 1, 1
    bold: True
    font_size: "16sp"
    size_hint_y: None
    height: "50dp"
    padding: "14dp", "8dp"
    canvas.before:
        Color:
            rgba: app.rose
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [16, 16, 16, 16]

<CardLabel>:
    color: app.text_color
    halign: "center"
    valign: "middle"
    text_size: self.width - dp(30), None
"""


class GiftButton(Button):
    pass


class CardLabel(Label):
    pass


class FloatingDecor(FloatLayout):
    def start(self):
        Clock.schedule_interval(self.spawn, 0.65)

    def spawn(self, _dt):
        symbol = random.choice(("♥", "♡", "✦", "🌸", "🌷"))
        label = Label(
            text=symbol,
            font_size=random.randint(18, 32),
            color=random.choice((ROSE, DEEP_ROSE, (0.96, 0.74, 0.33, 1), WHITE)),
            size_hint=(None, None),
            size=(dp(38), dp(38)),
            pos=(random.uniform(0, max(1, self.width - 40)), -40),
        )
        self.add_widget(label)
        Animation(y=self.height + 30, x=label.x + random.uniform(-70, 70),
                  duration=random.uniform(3, 6), t="out_quad").start(label)
        Clock.schedule_once(lambda _x: self.remove_widget(label), 6.2)


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = FloatLayout()
        with self.background.canvas.before:
            Color(*PINK)
            self.bg_rect = RoundedRectangle(pos=self.background.pos, size=self.background.size)
        self.background.bind(pos=self._update_bg, size=self._update_bg)
        self.add_widget(self.background)

    def _update_bg(self, *_args):
        self.bg_rect.pos = self.background.pos
        self.bg_rect.size = self.background.size

    def add_title(self, title, subtitle=""):
        Label(text=title, font_size="27sp", bold=True, color=DEEP_ROSE,
              size_hint=(1, None), height="75dp", pos_hint={"top": 1}).add_to(self.background)
        if subtitle:
            Label(text=subtitle, font_size="13sp", color=TEXT,
                  size_hint=(1, None), height="35dp", pos_hint={"top": 0.9}).add_to(self.background)


def add_to(widget, parent):
    parent.add_widget(widget)
    return widget


Label.add_to = lambda self, parent: add_to(self, parent)


class WelcomeScreen(BaseScreen):
    def on_pre_enter(self, *_args):
        if self.background.children:
            return
        decor = FloatingDecor()
        self.background.add_widget(decor)
        decor.start()
        add_to(Label(text="MÓN QUÀ NHỎ\nDÀNH CHO EM ❤️", font_size="34sp", bold=True,
                     color=DEEP_ROSE, halign="center", text_size=(None, None),
                     size_hint=(1, None), height="150dp", pos_hint={"center_y": 0.72}), self.background)
        add_to(Label(text="Anh có một món quà nhỏ dành riêng cho em… 💗",
                     font_size="17sp", color=TEXT, halign="center",
                     size_hint=(1, None), height="50dp", pos_hint={"center_y": 0.53}), self.background)
        button = GiftButton(text="MỞ QUÀ NGAY  🎁", size_hint=(0.62, None),
                            pos_hint={"center_x": 0.5, "center_y": 0.38})
        button.bind(on_release=lambda *_: self.manager.show("letter"))
        self.background.add_widget(button)
        settings = Button(text="⚙  Tùy chỉnh món quà", color=DEEP_ROSE,
                          background_color=(0, 0, 0, 0), size_hint=(1, None),
                          height="45dp", pos_hint={"center_y": 0.25})
        settings.bind(on_release=lambda *_: self.manager.app.open_settings())
        self.background.add_widget(settings)


class LetterScreen(BaseScreen):
    def on_pre_enter(self, *_args):
        self.background.clear_widgets()
        self.add_title("Một bức thư nhỏ gửi đến em 💌",
                       f"Gửi {self.manager.app.recipient} — từ {self.manager.app.sender}")
        self.letter = CardLabel(font_size="16sp", halign="left", valign="top",
                                text_size=(None, None), padding=(22, 22),
                                size_hint=(0.88, 0.62), pos_hint={"center_x": 0.5, "top": 0.82})
        self.background.add_widget(self.letter)
        buttons = BoxLayout(spacing=8, padding=10, size_hint=(0.96, None),
                            height="62dp", pos_hint={"center_x": 0.5, "y": 0.02})
        secret = GiftButton(text="Điều anh muốn nói…")
        secret.bind(on_release=lambda *_: self.manager.show("secret"))
        album = GiftButton(text="Album 📷")
        album.bind(on_release=lambda *_: self.manager.show("album"))
        buttons.add_widget(secret)
        buttons.add_widget(album)
        self.background.add_widget(buttons)
        self._typewrite(self.manager.app.letter_text)
        self._burst()

    def _typewrite(self, text):
        self.letter.text = ""
        state = {"index": 0}

        def tick(_dt):
            state["index"] += 1
            self.letter.text = text[:state["index"]]
            if state["index"] >= len(text):
                return False
            return True

        Clock.schedule_interval(tick, 0.018)

    def _burst(self):
        for _ in range(18):
            heart = Label(text=random.choice(("♥", "❤", "💗", "✦")),
                          font_size="24sp", color=ROSE, size_hint=(None, None),
                          size=(dp(40), dp(40)), pos_hint={"x": random.random(), "y": 0.1})
            self.background.add_widget(heart)
            Animation(y=0.88, opacity=0, duration=random.uniform(2, 4)).start(heart)


class SecretScreen(BaseScreen):
    def on_pre_enter(self, *_args):
        self.background.clear_widgets()
        self.add_title("Điều anh muốn nói… ✨")
        add_to(CardLabel(
            text=("Nếu có một điều anh muốn em luôn nhớ, thì đó là:\n\n"
                  "Em không cần phải trở thành ai khác để được yêu thương. "
                  "Em của hiện tại đã rất đáng quý rồi. Cảm ơn em vì đã là chính em "
                  "và vì đã cho anh cơ hội được đồng hành cùng em. 💗"),
            font_size="18sp", size_hint=(0.88, 0.58),
            pos_hint={"center_x": 0.5, "center_y": 0.52}), self.background)
        button = GiftButton(text="Mở album kỷ niệm 📷", size_hint=(0.7, None),
                            pos_hint={"center_x": 0.5, "y": 0.12})
        button.bind(on_release=lambda *_: self.manager.show("album"))
        self.background.add_widget(button)


class AlbumScreen(BaseScreen):
    def on_pre_enter(self, *_args):
        self.background.clear_widgets()
        self.add_title("Album kỷ niệm của chúng mình 📷",
                       "Thêm những khoảnh khắc khiến em mỉm cười nhé")
        add_to(GiftButton(text="Thêm ảnh từ điện thoại +", size_hint=(0.72, None),
                          pos_hint={"center_x": 0.5, "top": 0.83},
                          on_release=lambda *_: self.pick_photo()), self.background)
        self.message = CardLabel(text="Album đang chờ những kỷ niệm của chúng mình 🌷",
                                 font_size="16sp", size_hint=(0.9, 0.5),
                                 pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.background.add_widget(self.message)
        buttons = BoxLayout(spacing=10, size_hint=(0.9, None), height="55dp",
                            pos_hint={"center_x": 0.5, "y": 0.05})
        back = GiftButton(text="Quay lại thư")
        back.bind(on_release=lambda *_: self.manager.show("letter"))
        ending = GiftButton(text="Lời kết ❤️")
        ending.bind(on_release=lambda *_: self.manager.show("ending"))
        buttons.add_widget(back)
        buttons.add_widget(ending)
        self.background.add_widget(buttons)

    def pick_photo(self):
        chooser = FileChooserListView(filters=["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"])
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(chooser)
        choose = GiftButton(text="Chọn ảnh", size_hint_y=None)
        layout.add_widget(choose)
        popup = Popup(title="Chọn ảnh kỷ niệm", content=layout, size_hint=(0.95, 0.85))

        def selected(_button):
            if chooser.selection:
                self.message.text = f"Đã thêm ảnh:\n{Path(chooser.selection[0]).name}\n\n"
                try:
                    self.background.add_widget(Image(source=chooser.selection[0],
                                                     size_hint=(0.75, 0.38),
                                                     pos_hint={"center_x": 0.5, "center_y": 0.42}))
                except (OSError, ValueError):
                    self.message.text += "Ảnh đã được chọn."
            popup.dismiss()

        choose.bind(on_release=selected)
        popup.open()


class EndingScreen(BaseScreen):
    def on_pre_enter(self, *_args):
        self.background.clear_widgets()
        app = self.manager.app
        self.add_title("Dành riêng cho cô gái anh thương 🌷")
        text = app.ending_text
        add_to(CardLabel(text=text, font_size="13sp", halign="left", valign="top",
                         size_hint=(0.9, 0.73), pos_hint={"center_x": 0.5, "top": 0.86}), self.background)
        replay = GiftButton(text="Xem lại từ đầu ↻", size_hint=(0.65, None),
                            pos_hint={"center_x": 0.5, "y": 0.04})
        replay.bind(on_release=lambda *_: self.manager.show("welcome"))
        self.background.add_widget(replay)


class GiftManager(ScreenManager):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def show(self, name):
        self.current = name


class LoveGiftApp(App):
    rose = ROSE
    text_color = TEXT
    recipient = "em yêu"
    sender = "anh"
    custom_message = "Cảm ơn em vì đã đến bên anh. Chỉ cần em luôn vui vẻ, bình an và mỉm cười, với anh đó đã là một điều thật tuyệt vời."

    def build(self):
        self.title = "Món Quà Nhỏ Dành Cho Em ❤️"
        Builder.load_string(KV)
        manager = GiftManager(self)
        for name, screen in (("welcome", WelcomeScreen()), ("letter", LetterScreen()),
                             ("secret", SecretScreen()), ("album", AlbumScreen()),
                             ("ending", EndingScreen())):
            screen.name = name
            manager.add_widget(screen)
        return manager

    @property
    def letter_text(self):
        return (f"{self.recipient} à,\n\nChúc em một ngày 20/10 thật vui vẻ, xinh đẹp và hạnh phúc. "
                f"Mong em luôn được yêu thương, trân trọng và có thật nhiều nụ cười.\n\n"
                f"{self.custom_message}\n\nAnh không phải lúc nào cũng giỏi nói lời ngọt ngào, "
                f"nhưng anh luôn trân trọng những khoảnh khắc có em trong cuộc đời mình.\n\n"
                f"Thương em nhiều,\n{self.sender} ❤️")

    @property
    def ending_text(self):
        return (f"Chúc {self.recipient} yêu của anh một ngày 20/10 thật vui vẻ và hạnh phúc nhé ❤️🌷\n\n"
                "Anh mong em sẽ luôn xinh đẹp, bình an, luôn mỉm cười và gặp thật nhiều điều tốt đẹp "
                "trong cuộc sống. Anh biết đôi khi anh không phải là người giỏi nói những lời ngọt ngào, "
                "nhưng anh muốn em biết rằng em là một người rất đặc biệt đối với anh.\n\n"
                "Cảm ơn em vì đã xuất hiện trong cuộc đời anh, vì những niềm vui, những khoảnh khắc đáng nhớ "
                "và cả những điều nhỏ bé mà em mang đến mỗi ngày. Anh không hứa sẽ khiến mọi ngày của em đều "
                "hoàn hảo, nhưng anh sẽ cố gắng để khi em mệt mỏi, em có một người để sẻ chia; khi em buồn, "
                "em có một người để dựa vào; và khi em hạnh phúc, anh sẽ luôn là người vui cùng em.\n\n"
                "Mong rằng không chỉ riêng ngày 20/10 mà cả những ngày bình thường sau này, em đều cảm nhận "
                "được mình được yêu thương, trân trọng và nâng niu. Anh thương em nhiều lắm! ❤️🥰\n\n"
                f"— {self.sender}")

    def open_settings(self):
        layout = BoxLayout(orientation="vertical", spacing=8, padding=12)
        recipient = TextInput(text=self.recipient, hint_text="Tên người yêu", multiline=False)
        sender = TextInput(text=self.sender, hint_text="Tên người tặng", multiline=False)
        message = TextInput(text=self.custom_message, hint_text="Lời nhắn riêng", multiline=True)
        save = GiftButton(text="Lưu thay đổi")
        for field in (recipient, sender, message, save):
            layout.add_widget(field)
        popup = Popup(title="Tùy chỉnh món quà", content=layout, size_hint=(0.92, 0.65))

        def save_values(_button):
            self.recipient = recipient.text.strip() or "em yêu"
            self.sender = sender.text.strip() or "anh"
            self.custom_message = message.text.strip() or self.custom_message
            popup.dismiss()

        save.bind(on_release=save_values)
        popup.open()


if __name__ == "__main__":
    LoveGiftApp().run()
