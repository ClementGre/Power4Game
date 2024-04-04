from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Power4Game")
        self.geometry("300x200")
        self.label = Label(self, text="Welcome to Power4Game!")
        self.label.pack()

        self.mainloop()
