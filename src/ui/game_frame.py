import tkinter as tk

from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.game_buttons_frame import GameButtonsFrame
from src.ui.game_canvas import GameCanvas


class GameFrame(tk.Frame):
    def __init__(self, master, difficulty, player_name, is_player_red):
        """
        :type master: App
        :param master:
        """
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        self.widgets.append(GameCanvas(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(GameButtonsFrame(self))

    def end_game(self):
        self.master.end_game()
