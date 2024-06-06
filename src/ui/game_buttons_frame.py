import tkinter as tk
from tkinter import PhotoImage


class GameButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons.append(tk.Button(self, text="Resign", bg="#81ADC8", command=self.quit))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(tk.Label(self, text="Time: 0.00", bg="#81ADC8", fg="#303030", font=("Courier", 16)))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)

    def quit(self):
        self.master.end_game()

    def update_time(self, time):
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


