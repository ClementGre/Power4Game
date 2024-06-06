import os
import tkinter as tk
from tkinter import PhotoImage


class StartFrame(tk.Frame):
    """
    Cadre de démarrage du jeu Power4Game.

    Gère l'interface utilisateur pour la sélection de la difficulté et l'entrée du nom du joueur.
    """

    def __init__(self, master):
        """
        Initialise le cadre de démarrage.

        :param master: L'instance parent qui est un GameFrame.
        :type master: GameFrame
        """
        super().__init__(master, pady=10)
        self.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.difficulty = tk.IntVar(value=2)
        self.player_name = tk.StringVar(value="")
        self.widgets = []

        self.create_widgets()

    def create_widgets(self):
        """
        Crée et affiche les widgets de l'interface de démarrage.

        Affiche un message de bienvenue, un sélecteur de difficulté, une entrée de nom
        de joueur, et des boutons pour commencer à jouer en tant que joueur rouge ou jaune.
        """
        self.widgets.append(tk.Label(self, text="Welcome to Power4Game", font=("Algerian", 16), fg="#2D323B"))
        self.widgets[-1].pack(pady=20)

        self.widgets.append(tk.Label(self, text="Please select the difficulty level"))
        self.widgets[-1].pack()

        self.widgets.append(tk.Scale(self, from_=1, to=8, orient=tk.HORIZONTAL, variable=self.difficulty))
        self.widgets[-1].pack(pady=(0, 20))

        # name entry
        self.widgets.append(tk.Label(self, text="Enter your name"))
        self.widgets[-1].pack()
        self.widgets.append(tk.Entry(self, textvariable=self.player_name))
        self.widgets[-1].pack()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        self.red = PhotoImage(file=os.path.join("src", "res", "rouge.png"))
        self.widgets.append(
            tk.Button(frame, text='Jouer', command=self.play_as_red, image=self.red, compound=tk.BOTTOM, width=70,
                      height=70))
        self.widgets[-1].pack(side=tk.LEFT, padx=10)

        self.yellow = PhotoImage(file=os.path.join("src", "res", "jaune.png"))
        self.widgets.append(tk.Button(frame, text='Jouer', command=self.play_as_yellow, image=self.yellow, compound=tk.BOTTOM, width=70, height=70))
        self.widgets[-1].pack(side=tk.RIGHT, padx=10)

    def get_player_name(self):
        """
        Récupère le nom du joueur saisi.

        :return: Le nom du joueur ou "Unknown" si aucun nom n'a été saisi.
        :rtype: str
        """
        player_name = self.player_name.get()
        return "Unknown" if player_name == "" else player_name

    def play_as_red(self):
        """
        Commence le jeu en tant que joueur rouge.

        Appelle la méthode start_game du parent avec la difficulté, le nom du joueur,
        et True pour indiquer que le joueur est rouge.
        """
        self.master.start_game(self.difficulty.get(), self.get_player_name(), True)

    def play_as_yellow(self):
        """
        Commence le jeu en tant que joueur jaune.

        Appelle la méthode start_game du parent avec la difficulté, le nom du joueur,
        et False pour indiquer que le joueur est jaune.
        """
        self.master.start_game(self.difficulty.get(), self.get_player_name(), False)
