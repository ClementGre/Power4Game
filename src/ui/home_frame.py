import tkinter as tk

from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.home_buttons_frame import HomeButtonsFrame
from src.ui.scoreboard_frame import ScoreboardFrame
from src.ui.start_frame import StartFrame


class HomeFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        self.widgets.append(ScoreboardFrame(self))
        self.widgets.append(StartFrame(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(HomeButtonsFrame(self))

    def start_game(self, difficulty, player_name, is_player_red):
        self.master.start_game(difficulty, player_name, is_player_red)

    def quit(self):
        self.master.destroy()
