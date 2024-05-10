import numpy as np


class Game:
    __slots__ = ['player_name', 'is_player_red', 'grid', 'nb_played', 'start_time']

    """
    grid: numpy array de taille 6x7
        0: case vide
        1: joueur rouge
        2: joueur jaune
    """

    def __init__(self, player_name, is_player_red):
        self.player_name = player_name
        self.is_player_red = is_player_red
        self.grid = np.zeros((6, 7), dtype=int)
        self.nb_played = 0

    def is_player_turn(self):
        """
        :return: True si c'est au joueur de jouer, False si c'est à l'ordinateur
        """
        return self.is_player_red if self.nb_played % 2 == 0 else not self.is_player_red

    def play(self, column, is_player):
        """
        :param column: colonne dans laquelle on veut jouer
        :type column: int
        :param is_player: True si c'est le joueur qui joue, False si c'est l'ordinateur
        :type is_player: bool
        :return: True si l'entité qui a joué a gagné, False sinon
        :rtype: bool
        """
        
        

    def is_game_done(self):
        """
        :return: True si la partie est finie, False sinon
        :rtype: bool
        """
        return self.nb_played == 42 or self.is_winner(1) or self.is_winner(2)

    def is_winner(self, player):
        """
        Renvoie True si l'entité a réussi à aligner 4 pions.
        :param player: True si on veut savoir si c'est le joueur qui a gagné, False si c'est l'ordinateur qui a gagné.
        :return: True si le joueur a gagné, False sinon
        """
        
