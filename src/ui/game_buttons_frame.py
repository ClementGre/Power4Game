import tkinter as tk
from tkinter import PhotoImage

class GameButtonsFrame(tk.Frame):
    """
    Cadre des boutons de jeu pour l'application Power4Game.

    Gère les widgets spécifiques au jeu, comme le bouton d'abandon et l'affichage du temps écoulé.
    """
    def __init__(self, master):
        """
        Initialise le cadre des boutons de jeu.

        :param master: L'instance parent qui est un GameFrame.
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        """
        Crée et affiche les widgets de l'interface de boutons de jeu.

        Ajoute un bouton pour abandonner la partie et un label pour afficher le temps écoulé.
        """
        self.buttons.append(tk.Button(self, text="Resign", bg="#81ADC8", command=self.quit))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(tk.Label(self, text="Time: 0.00", bg="#81ADC8", fg="#303030", font=("Courier", 16)))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)

    def quit(self):
        """
        Abandonne la partie en appelant la méthode end_game de l'objet maître.
        """
        self.master.end_game()

    def update_time(self, time):
        """
        Met à jour l'affichage du temps écoulé.

        :param time: Le temps écoulé en secondes.
        :type time: float
        """
        minutes = int(time / 60)
        seconds = int(time % 60)
        ms = int(time * 1000) % 1000
        if minutes < 10:
            minutes = "0" + str(minutes)
        if seconds < 10:
            seconds = "0" + str(seconds)
        if ms < 10:
            ms = "00" + str(ms)
        elif ms < 100:
            ms = "0" + str(ms)

        self.buttons[1].config(text=f"{minutes}:{seconds}")


