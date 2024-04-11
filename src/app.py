import tkinter as tk

from src.model.scoreboard import Scoreboard
from src.ui.game_frame import GameFrame
from src.ui.home_frame import HomeFrame


class App(tk.Tk):
    __slots__ = ['scoreboard', 'home_frame', 'game_frame']

    def __init__(self):
        super().__init__()
        self.title("Power4Game")
        self.geometry("300x200")

        self.scoreboard = Scoreboard()

        self.home_frame = None
        self.game_frame = None

        self.home_frame = HomeFrame(self)
        self.home_frame.pack()

        self.after(1000, self.start_game)

        self.mainloop()

    def start_game(self):
        self.home_frame.destroy()

        self.game_frame = GameFrame(self)
        self.game_frame.pack()

    def end_game(self):
        # Logique de récupération du score et de sauvegarde
        self.game_frame.destroy()

        self.home_frame = HomeFrame(self)
        self.home_frame.pack()
        
