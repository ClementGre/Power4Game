import tkinter as tk

class GameCanvas(tk.Canvas):

    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master)


