import tkinter as tk

class HomeButtonsFrame(tk.Frame):
    """
    Cadre des boutons spécifiques à l'accueil de l'application.

    Gère l'affichage et les actions des boutons de l'accueil.
    """

    def __init__(self, master):
        """
        Initialise le cadre des boutons d'accueil.

        :param master: L'instance parent qui est un GameFrame.
        :type master: GameFrame
        """
        super().__init__(master, bg="#81ADC8")
        self.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.buttons = []
        self.create_widgets()
        
    def create_widgets(self):
        """
        Crée et ajoute les widgets de l'interface de boutons d'accueil.

        Ajoute un bouton pour quitter l'application.
        """
        self.buttons.append(tk.Button(self, text="❌", command=self.master.quit, font=('Arial', 8)))
        self.buttons[-1].pack(side=tk.RIGHT, padx=10, pady=5)
