import tkinter as tk

from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.home_buttons_frame import HomeButtonsFrame
from src.ui.scoreboard_frame import ScoreboardFrame
from src.ui.start_frame import StartFrame


class HomeFrame(tk.Frame):

    def __init__(self, master, player_name=None):
        super().__init__(master, bg="#E2E2E2")
        self.player_name = player_name
        self.pack(fill=tk.BOTH, expand=True)
        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)

        self.app_buttons_frame = AppButtonsFrame(self)
        self.app_buttons_frame.grid(row=0, column=0, sticky="ew")

        self.home_buttons_frame = HomeButtonsFrame(self)
        self.home_buttons_frame.grid(row=0, column=1, sticky="ew")

        self.start_frame = StartFrame(self, self.player_name)
        self.start_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.scoreboard_frame = ScoreboardFrame(self)
        self.scoreboard_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Set weights for rows to allow ScoreboardFrame to expand
        self.grid_rowconfigure(0, weight=0, minsize=40)
        self.grid_rowconfigure(1, weight=0, minsize=40)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=2)

    def start_game(self, difficulty, player_name, is_player_red):
        self.master.start_game(difficulty, player_name, is_player_red)

    def quit(self):
        self.master.destroy()
