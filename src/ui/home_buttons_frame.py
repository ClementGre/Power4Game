import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os

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
        # self.buttons.append(tk.Button(self, command=self.master.quit))
        # self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_directory, "Power4Game", "src", "ui", "Quitter.png")
        
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return
        
        img_quit = Image.open(image_path)
        img_quit = ImageTk.PhotoImage(img_quit)
        
        quit_button = tk.Button(self, command=self.master.quit, image=img_quit, compound=tk.CENTER)
        quit_button.image = img_quit
        quit_button.pack(side=tk.RIGHT, padx=10, pady=5)
        self.buttons.append(quit_button)
