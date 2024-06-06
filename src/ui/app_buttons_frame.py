# -*- coding: utf-8 -*-
import tkinter as tk


class AppButtonsFrame(tk.Frame):
    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons.append(tk.Button(self, text="FullScreen", command=self.fullscreen))
        self.buttons[-1].pack(side=tk.LEFT, padx=10, pady=5)
        

    def fullscreen(self):
        self.master.master.attributes("-fullscreen", True)
        self.buttons[0].config(text="Exit FullScreen", command=self.exit_fullscreen)

    def exit_fullscreen(self):
        self.master.master.attributes("-fullscreen", False)
        self.buttons[0].config(text="FullScreen", command=self.fullscreen)
