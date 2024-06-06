import tkinter as tk


class HomeButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="#DB1A3D")
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons.append(tk.Button(self, text="Quit", command=self.master.quit, takefocus=0))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
