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
        :param column: colonne dans laquelle l'ordinateur veut jouer
        :type column: int
        :param is_player: True si c'est le joueur qui joue, False si c'est l'ordinateur
        :type is_player: bool
        :return: True si l'ordinateur a gagné, False sinon
        :rtype: bool
        """
