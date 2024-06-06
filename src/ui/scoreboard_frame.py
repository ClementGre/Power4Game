import tkinter as tk


bg = "#E2E2E2"

class ScoreboardFrame(tk.Frame):
    """
    Cadre du tableau des scores pour l'application Power4Game.

    Affiche les scores des joueurs dans une liste déroulante.
    """
    def __init__(self, master):
        """
        Initialiser le cadre du tableau de bord des scores.

        :param master: L'instance parent qui est un GameFrame.
        :type master: GameFrame
        """
        super().__init__(master, bg=bg)
        self.pack(side=tk.BOTTOM, fill=tk.Y, expand=True, pady=10)
        self.widgets = []

        self.master.master.scoreboard.load_dummy_scores()
        self.create_widgets()

    def create_widgets(self):
        """
        Créer et afficher les widgets du tableau de bord des scores.

        Dessine une liste déroulante contenant les informations sur les parties enregistrées
        """
        # for each score in self.master.master.scoreboard.scores:
        # draw a line of the table with the score : Player name, nb_played, time, difficulty, score, date

        # append title line
        self.widgets.append(tk.Label(self, text="Scoreboard", bg=bg, font=("Helvetica", 16), fg="#2D323B"))
        self.widgets[-1].grid(row=0, column=0, columnspan=6)

        self.widgets.append(tk.Label(self, text="Player name", bg=bg))
        self.widgets.append(tk.Label(self, text="Nb played", bg=bg))
        self.widgets.append(tk.Label(self, text="Time", bg=bg))
        self.widgets.append(tk.Label(self, text="Difficulty", bg=bg))
        self.widgets.append(tk.Label(self, text="Score", bg=bg))
        self.widgets.append(tk.Label(self, text="Date", bg=bg))

        for (player, scores) in self.master.master.scoreboard.scores.items():
            for score in scores:
                self.widgets.append(tk.Label(self, text=player, bg=bg))
                self.widgets.append(tk.Label(self, text=score[0], bg=bg))
                self.widgets.append(tk.Label(self, text=score[1], bg=bg))
                self.widgets.append(tk.Label(self, text=score[2], bg=bg))
                self.widgets.append(tk.Label(self, text=score[3], bg=bg))
                self.widgets.append(tk.Label(self, text=score[4], bg=bg))

        for i in range(1, len(self.widgets)):
            j = i - 1
            self.widgets[i].grid(row=1 + int(j / 6), column=j % 6)
