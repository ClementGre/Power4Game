import tkinter as tk


class AppButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="green", height=40)
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        pass
