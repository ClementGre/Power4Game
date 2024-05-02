import tkinter as tk


class ScoreboardFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="blue")
        self.pack(side=tk.BOTTOM, expand=True)
        self.widgets = []

        self.master.master.scoreboard.load_dummy_scores()
        self.create_widgets()

    def create_widgets(self):
        # for each score in self.master.master.scoreboard.scores:
        # draw a line of the table with the score : Player name, nb_played, time, difficulty, score, date

        # append title line

        self.widgets.append(tk.Label(self, text="Player name"))
        self.widgets.append(tk.Label(self, text="Nb played"))
        self.widgets.append(tk.Label(self, text="Time"))
        self.widgets.append(tk.Label(self, text="Difficulty"))
        self.widgets.append(tk.Label(self, text="Score"))
        self.widgets.append(tk.Label(self, text="Date"))

        for (player, scores) in self.master.master.scoreboard.scores.items():
            for score in scores:
                self.widgets.append(tk.Label(self, text=player))
                self.widgets.append(tk.Label(self, text=score[0]))
                self.widgets.append(tk.Label(self, text=score[1]))
                self.widgets.append(tk.Label(self, text=score[2]))
                self.widgets.append(tk.Label(self, text=score[3]))
                self.widgets.append(tk.Label(self, text=score[4]))

        for i in range(len(self.widgets)):
            self.widgets[i].grid(row=int(i / 6), column=i % 6)

