import tkinter as tk
from time import time

from src.computer.computer import get_computer_play_column
from src.model.game import Game
from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.game_buttons_frame import GameButtonsFrame
from src.ui.game_canvas import GameCanvas


class GameFrame(tk.Frame):
    def __init__(self, master, difficulty, player_name, is_player_red):
        """
        :type master: App
        :param master:
        """
        self.difficulty = difficulty
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        self.game = Game(player_name, is_player_red)

        self.widgets = []
        self.create_widgets()

        self.start_time = time()
        self.time = 0
        self.after(10, self.update_time)

    def update_time(self):
        self.time = time() - self.start_time
        self.widgets[0].update_time(self.time)
        self.after(10, self.update_time)

    def create_widgets(self):
        self.widgets.append(GameCanvas(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(GameButtonsFrame(self))

    def end_game(self):
        self.master.end_game()

    def player_play(self, column):
        if not self.game.is_player_turn():
            return True

        if self.game.play(column, True) or self.game.is_game_done():
            # Player wins game
            self.end_game()
            return False

        if self.game.is_game_done():
            self.end_game()
            return False

        # run after a second
        self.after(1000, self.computer_play)
        return True

    def computer_play(self):
        if self.game.play(get_computer_play_column(self.difficulty, self.game.grid), False):
            # Computer wins game
            self.end_game()
            return False

        if self.game.is_game_done():
            self.end_game()

        self.widgets[0].update_board()
