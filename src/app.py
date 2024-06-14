import time
import tkinter as tk

from src.model.scoreboard import Scoreboard
from src.model.scoreboard import calculate_score
from src.ui.game_frame import GameFrame
from src.ui.home_frame import HomeFrame


class App(tk.Tk):
    __slots__ = ['scoreboard', 'home_frame', 'game_frame']

    def __init__(self):
        """
        Initialise l'application Power4Game.
        """
        super().__init__()
        self.title("Power4Game")
        self.geometry("900x600")

        self.scoreboard = Scoreboard()

        self.home_frame = None
        self.game_frame = None

        self.home_frame = HomeFrame(self)

        self.mainloop()

    def start_game(self, difficulty, player_name, is_player_red):
        """
        Démarre une nouvelle partie de Power4Game.
        :param difficulty: difficulté du jeu
        :param player_name: nom du joueur
        :param is_player_red: True si le joueur joue avec les jetons rouges
        """
        self.home_frame.destroy()

        self.game_frame = GameFrame(self, difficulty, player_name, is_player_red)
        self.game_frame.pack()

    def end_game(self):
        """
        Sauvegarde les scores et termine une partie de Power4Game.
        """
        # Logique de récupération du score et de sauvegarde
        if self.game_frame.game.is_player_winner():
            score = calculate_score(self.game_frame.game.nb_played, self.game_frame.time, self.game_frame.difficulty)
            self.scoreboard.add_score(self.game_frame.game.player_name, self.game_frame.game.nb_played,
                                      self.game_frame.time,
                                      self.game_frame.difficulty, self.game_frame.game.is_player_red, score,
                                      time.strftime("%d/%m/%Y %H:%M:%S"))

        # Suppression du panneau de jeu
        self.home_frame = HomeFrame(self, self.game_frame.game.player_name)
        self.game_frame.destroy()
        self.home_frame.pack()
