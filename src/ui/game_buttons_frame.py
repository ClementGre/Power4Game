import tkinter as tk
from src.utils.format import format_time_ms
bg = "#DB1A3D"


class GameButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg=bg)
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        """
        Crée les widgets du panneau de jeu.
        """
        self.buttons.append(tk.Button(self, text="Resign", bg=bg, command=self.master.resign))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(tk.Label(self, text="Time: 0.00", bg=bg, fg="#303030", font=("Courier", 16)))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)

    def game_ended(self):
        """
        Met à jour les boutons lorsque la partie est terminée.
        """
        self.buttons[0].config(text="Quit", command=self.master.master.end_game)

    def update_time(self, time):
        """
        Met à jour le temps affiché.
        :param time: Nombre de millisecondes écoulées
        :type time: int
        """
        self.buttons[1].config(text=format_time_ms(time))
