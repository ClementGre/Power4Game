import tkinter as tk


class StartFrame(tk.Frame):

    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="yellow")
        self.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.difficulty = 0
        self.widgets = []

        self.create_widgets()

    def create_widgets(self):
        self.widgets.append(tk.Label(self, text="Welcome to Power4Game"))
        self.widgets[-1].pack()

        self.widgets.append(tk.Label(self, text="Please select the game difficulty"))
        self.widgets[-1].pack()

        # scale widget for difficulty
        self.widgets.append(tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL))
        self.widgets[-1].pack()

        self.widgets.append(tk.Button(self, text="Play", command=self.play_button_clicked))
        self.widgets[-1].pack()


        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def play_button_clicked(self):
        self.master.start_game(self.widgets[2].get(), "r_name", True)
