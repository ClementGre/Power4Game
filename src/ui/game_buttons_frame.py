import tkinter as tk


class GameButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master)
        self.pack()
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        pass


