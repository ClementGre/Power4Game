import tkinter as tk


class HomeFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.label, self.play_button, self.quit_button = None, None, None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Power4Game")
        self.label.pack()

        self.play_button = tk.Button(self, text="Play", command=self.play_button_clicked)
        self.play_button.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def play_button_clicked(self):
        self.master.start_game()

    def quit(self):
        self.master.destroy()
