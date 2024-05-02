import tkinter as tk


class GameButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="red", height=40)
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons.append(tk.Button(self, text="Quit", command=self.quit))
        self.buttons[-1].pack(side=tk.RIGHT)

    def quit(self):
        self.master.end_game()


