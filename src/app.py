import time
import tkinter as tk

from src.model.scoreboard import Scoreboard
from src.model.scoreboard import calculate_score
from src.ui.game_frame import GameFrame
from src.ui.home_frame import HomeFrame


class App(tk.Tk):
    """
    La classe principale de l'application Power4Game.

    Hérite de tk.Tk et gère les différents cadres de l'application, y compris le cadre d'accueil
    et le cadre de jeu, ainsi que le tableau des scores.
    """
    __slots__ = ['scoreboard', 'home_frame', 'game_frame']

    def __init__(self):
        """
        Initialise l'application Power4Game.

        Configure la fenêtre principale, initialise le tableau des scores, et crée le cadre d'accueil.
        """
        super().__init__()
        self.title("Power4Game")
        self.geometry("900x600")

        self.scoreboard = Scoreboard()

        self.home_frame = None
        self.game_frame = None

        self.home_frame = HomeFrame(self)
        # self.after(1000, self.start_game)

        self.mainloop()

    def start_game(self, difficulty, player_name, is_player_red):
        """
        Démarre une nouvelle partie.

        Détruit le cadre d'accueil et crée un nouveau cadre de jeu avec les paramètres fournis.

        :param difficulty: Le niveau de difficulté du jeu.
        :type difficulty: int
        :param player_name: Le nom du joueur.
        :type player_name: str
        :param is_player_red: Détermine si le joueur joue avec les jetons rouges.
        :type is_player_red: bool
        """
        self.home_frame.destroy()

        self.game_frame = GameFrame(self, difficulty, player_name, is_player_red)
        self.game_frame.pack()

    def end_game(self):
        """
        Termine la partie en cours.

        Calcule et enregistre le score du joueur, détruit le cadre de jeu, et recrée le cadre d'accueil.
        """
        # Logique de récupération du score et de sauvegarde
        score = calculate_score(self.game_frame.game.nb_played, self.game_frame.time, self.game_frame.difficulty)
        self.scoreboard.add_score(self.game_frame.game.player_name, self.game_frame.game.nb_played,
                                  self.game_frame.time,
                                  self.game_frame.difficulty, self.game_frame.game.is_player_red, score,
                                  time.strftime("%d/%m/%Y %H:%M:%S"))

        # Cleaning up the game frame
        self.game_frame.destroy()
        self.home_frame = HomeFrame(self)
        self.home_frame.pack()
