import os
import tkinter as tk
from tkinter import PhotoImage
from src.utils.random_name import generate_random_name


class StartFrame(tk.Frame):

    def __init__(self, master, player_name):
        """
        :type master: GameFrame
        """
        super().__init__(master)
        self.difficulty = tk.IntVar(value=2)
        self.player_name = tk.StringVar(value=player_name if player_name is not None else generate_random_name())
        self.widgets = []

        self.create_widgets()

    def create_widgets(self):
        self.widgets.append(tk.Label(self, text="Welcome to Power4Game", font="Algerian 22 bold", fg="#2D323B"))
        self.widgets[-1].pack(pady=20)

        self.widgets.append(tk.Label(self, text="Please select the difficulty level"))
        self.widgets[-1].pack()

        self.widgets.append(tk.Scale(self, from_=1, to=6, orient=tk.HORIZONTAL, variable=self.difficulty))
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
            tk.Button(frame, text='Play as', command=self.play_as_red, image=self.red, compound=tk.BOTTOM,
                      width=70, height=70, border='0', bg='cyan'))
        self.widgets[-1].pack(side=tk.LEFT, padx=10)

        self.yellow = PhotoImage(file=os.path.join("src", "res", "jaune.png"))
        self.widgets.append(
            tk.Button(frame, text='Play as', command=self.play_as_yellow, image=self.yellow, compound=tk.BOTTOM,
                      width=70, height=70, border='0', bg='cyan'))
        self.widgets[-1].pack(side=tk.RIGHT, padx=10)

    def get_player_name(self):
        player_name = self.player_name.get()
        return "Unknown" if player_name == "" else player_name

    def play_as_red(self):
        self.master.start_game(self.difficulty.get(), self.get_player_name(), True)

    def play_as_yellow(self):
        self.master.start_game(self.difficulty.get(), self.get_player_name(), False)
