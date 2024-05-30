import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage


class HomeButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()
        
    def create_widgets(self):
        img_quit = PhotoImage(file="\\Power4Game\\src\\ui\\Quitter.png")
        quit_button = tk.Button(self, command=self.master.quit, image=img_quit, compound=tk.CENTER)
        quit_button.image = img_quit  # Conserver une référence à l'image
        quit_button.pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(quit_button)
        """
        self.buttons.append(tk.Button(self, command=self.master.quit,compound=tk))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        """