import os
import tkinter as tk
from tkinter import PhotoImage


class StartFrame(tk.Frame):

    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, pady=10)
        self.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.difficulty = tk.IntVar(value=2)
        self.player_name = tk.StringVar(value="")
        self.widgets = []

        self.create_widgets()

    def create_widgets(self):
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
        player_name = self.player_name.get()
        return "Unknown" if player_name == "" else player_name

    def play_as_red(self):
        self.master.start_game(self.difficulty.get(), self.get_player_name(), True)

    def play_as_yellow(self):
        self.master.start_game(self.difficulty.get(), self.get_player_name(), False)
