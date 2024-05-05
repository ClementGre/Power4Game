import tkinter as tk


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
        self.buttons.append(tk.Button(self, text="Resign", command=self.quit))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)

    def quit(self):
        self.master.end_game()


