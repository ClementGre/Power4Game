import tkinter as tk

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
        self.buttons.append(tk.Button(self, text="Resign", bg=bg, command=self.master.resign))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(tk.Label(self, text="Time: 0.00", bg=bg, fg="#303030", font=("Courier", 16)))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)

    def game_ended(self):
        self.buttons[0].config(text="Quit", command=self.master.master.end_game)

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
