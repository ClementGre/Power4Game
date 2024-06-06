import tkinter as tk

from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.home_buttons_frame import HomeButtonsFrame
from src.ui.scoreboard_frame import ScoreboardFrame
from src.ui.start_frame import StartFrame


class HomeFrame(tk.Frame):
    """
    Cadre principal de l'accueil de l'application.

    Gère l'affichage des widgets d'accueil, y compris le tableau des scores, le cadre de démarrage,
    les boutons de l'application et les boutons spécifiques à l'accueil.
    """

    def __init__(self, master):
        """
        Initialise le cadre d'accueil.

        :param master: L'instance parent qui est une App.
        :type master: App
        """
        super().__init__(master, bg="#E2E2E2")
        self.pack(fill=tk.BOTH, expand=True)
        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        """
        Crée et ajoute les widgets de l'interface d'accueil.

        Ajoute le tableau des scores, le cadre de démarrage, les boutons de l'application
        et les boutons spécifiques à l'accueil.
        """
        self.widgets.append(ScoreboardFrame(self))
        self.widgets.append(StartFrame(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(HomeButtonsFrame(self))

    def start_game(self, difficulty, player_name, is_player_red):
        """
        Démarre une nouvelle partie avec les paramètres fournis.

        :param difficulty: Le niveau de difficulté du jeu.
        :type difficulty: int
        :param player_name: Le nom du joueur.
        :type player_name: str
        :param is_player_red: Détermine si le joueur joue avec les jetons rouges.
        :type is_player_red: bool
        """
        self.master.start_game(difficulty, player_name, is_player_red)

    def quit(self):
        """
        Quitte l'application en détruisant la fenêtre principale.
        """
        self.master.destroy()
