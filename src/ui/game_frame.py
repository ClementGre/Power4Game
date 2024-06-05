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

        if not self.game.is_player_turn():
            self.after(500, self.computer_play)

    def update_time(self):
        self.time = time() - self.start_time
        self.widgets[2].update_time(self.time)
        self.after(100, self.update_time)

    def create_widgets(self):
        self.widgets.append(GameCanvas(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(GameButtonsFrame(self))

    def end_game(self):
        self.master.end_game()

    def player_play(self, column):
        if not self.game.is_player_turn() or self.game.is_game_done():
            print("Player tried to play when it's not his turn or the game is done")
            return None

        (won, coordinates) = self.game.play(column, True)
        if coordinates is None:
            print("Player played in a full column")
            return None
        if won or self.game.is_game_done():
            self.after(500, self.end_game)
            return coordinates

        return coordinates

    def computer_play(self):
        (won, coordinates) = self.game.play(get_computer_play_column(self.difficulty, self.game.grid), False)
        if coordinates is None:
            print(f"Computer play returned an invalid column {coordinates}")
            return None
        if won or self.game.is_game_done():
            # Computer wins game
            self.after(500, self.end_game)
            return coordinates

