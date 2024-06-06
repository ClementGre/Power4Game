import tkinter as tk
from time import time

from src.computer.computer import get_computer_play_column
from src.model.game import Game
from src.ui.app_buttons_frame import AppButtonsFrame
from src.ui.game_buttons_frame import GameButtonsFrame
from src.ui.game_canvas import GameCanvas

class GameFrame(tk.Frame):
    """
    Cadre principal du jeu Power4Game.

    Gère l'affichage du jeu, la gestion des tours de jeu, le suivi du temps et les interactions joueur/ordinateur.
    """
    def __init__(self, master, difficulty, player_name, is_player_red):
        """
        Initialise le cadre de jeu.

        :param master: L'instance parent qui est une App.
        :type master: App
        :param difficulty: Le niveau de difficulté du jeu.
        :type difficulty: int
        :param player_name: Le nom du joueur.
        :type player_name: str
        :param is_player_red: Détermine si le joueur joue avec les jetons rouges.
        :type is_player_red: bool
        """
        self.difficulty = difficulty
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        self.game = Game(player_name, is_player_red)

        self.widgets = []
        self.create_widgets()

        self.start_time = time()
        self.time = 0
        self.after(10, self.update_time)

        if not self.game.is_player_turn():
            self.after(500, self.computer_play)

    def update_time(self):
        """
        Met à jour le temps écoulé depuis le début du jeu et met à jour le widget d'affichage du temps.

        Cette méthode est appelée de manière répétée toutes les 100 millisecondes.
        """
        self.time = time() - self.start_time
        self.widgets[2].update_time(self.time)
        self.after(100, self.update_time)

    def create_widgets(self):
        """
        Crée et ajoute les widgets nécessaires pour l'interface de jeu.

        Les widgets incluent le canevas de jeu, les boutons de l'application et les boutons de jeu.
        """
        self.widgets.append(GameCanvas(self))
        self.widgets.append(AppButtonsFrame(self))
        self.widgets.append(GameButtonsFrame(self))

    def end_game(self):
        """
        Termine le jeu en appelant la méthode end_game de l'objet maître.
        """
        self.master.end_game()

    def messageBox_won(self):
        """
        Affiche une boîte de dialogue de victoire et demande à l'utilisateur s'il souhaite quitter le jeu.

        Si l'utilisateur clique sur "OK", la méthode end_game est appelée.
        """
        tk.messagebox.showinfo("Victory !!!", "Player won game")
        self.end_game()

    def messageBox_lose(self):
        """
        Affiche une boîte de dialogue de défaite et demande à l'utilisateur s'il souhaite quitter le jeu.

        Si l'utilisateur clique sur "OK", la méthode end_game est appelée.
        """
        tk.messagebox.showinfo("Loosing !!!", "Computer won game")
        self.end_game()
            
    def messageBox_draw(self):
        """
        Affiche une boîte de dialogue de nul et demande à l'utilisateur s'il souhaite quitter le jeu.

        Si l'utilisateur clique sur "OK", la méthode end_game est appelée.
        """
        tk.messagebox.showinfo("Draw !!!", "Nice try")
        self.end_game()

    def player_play(self, column):
        """
        Gère le tour de jeu du joueur.

        :param column: La colonne dans laquelle le joueur souhaite jouer.
        :type column: int
        :return: Les coordonnées du jeton joué ou None si le coup est invalide.
        :rtype: tuple or None
        """
        if not self.game.is_player_turn() or self.game.is_game_done():
            print("Player tried to play when it's not his turn or the game is done")
            return None

        (won, coordinates) = self.game.play(column, True)
        if coordinates is None:
            print("Player played in a full column")
            
        if won or self.game.is_game_done():
            print("Player won game" if won else "Game is done")
            if won : 
                self.messageBox_won()
            if self.game.is_game_done() :
                self.messageBox_draw()
            return coordinates
        
        print("Player played in column", column, "token at coordinates", coordinates)
        
        return coordinates

    def computer_play(self):
        """
        Gère le tour de jeu de l'ordinateur.

        :return: Les coordonnées du jeton joué ou None si le coup est invalide.
        :rtype: tuple or None
        """
        (won, coordinates) = self.game.play(get_computer_play_column(self.difficulty, self.game.grid), False)
        while coordinates is None:
            print(f"Computer play returned an invalid column {coordinates}")
            (won, coordinates) = self.game.play(get_computer_play_column(self.difficulty, self.game.grid), False)
        
        if won or self.game.is_game_done():
            # Computer wins game
            print("Computer won game" if won else "Game is done")
            if won : 
                self.messageBox_lose()
            if self.game.is_game_done() :
                self.messageBox_draw()
            return coordinates

        print("Computer played in column", coordinates[1], "token at coordinates", coordinates)
        return coordinates
