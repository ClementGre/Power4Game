import tkinter as tk
from PIL import Image, ImageTk


class HomeButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        image = Image.open("src\\res\\play.jpg")
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons.append(tk.Button(self, text="Quit", command=self.master.quit))
        img = tk.PhotoImage(file="")
        l = tk.Label(tk.Tk(), image=img)
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
