import tkinter as tk


class ScoreboardFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="blue")
        self.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        pass
