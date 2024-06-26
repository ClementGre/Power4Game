# -*- coding: utf-8 -*-
import tkinter as tk


class AppButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        bg = "#DB1A3D"
        super().__init__(master, bg=bg)

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        """
        Crée les widgets du panneau d'application.
        """
        self.buttons.append(tk.Button(self, text="FullScreen", command=self.fullscreen))
        self.buttons[-1].pack(side=tk.LEFT, padx=10, pady=5)

    def fullscreen(self):
        """
        Active le mode plein écran.
        """
        self.master.master.attributes("-fullscreen", True)
        self.buttons[0].config(text="Exit FullScreen", command=self.exit_fullscreen)

    def exit_fullscreen(self):
        """
        Désactive le mode plein écran.
        """
        self.master.master.attributes("-fullscreen", False)
        self.buttons[0].config(text="FullScreen", command=self.fullscreen)
