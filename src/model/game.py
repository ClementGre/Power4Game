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
        if self.nb_played % 2 == 0:
            return self.is_player_red
        else:
            return not self.is_player_red

    def play(self, column, is_player):
        """
        Insère un jeton dans la colonne column, et vérifie si cette insertion a provoqué une victoire
        :param column: colonne dans laquelle on veut jouer
        :type column: int
        :param is_player: True si c'est le joueur qui joue, False si c'est l'ordinateur
        :type is_player: bool
        :return: Si un jeton peut être insérer dans la colonne indiqué : (True, coordinates) si l'entité qui a joué a gagné a, (False, coordinates) sinon
                 Sinon : (None, coordinates)
                 Avec coordinates = (row,column), row étant la ligne de la première cellule vide dans la colonne choisie
        :rtype: (bool, tuple)
        """
        # Insertion du jeton dans la colonne column
        if self.grid[0, column] != 0:
            return (False, None)

        n = 2
        if is_player:
            if self.is_player_red:
                n = 1
            else:
                n = 2
        else:
            if self.is_player_red:
                n = 2
            else:
                n = 1

        row = 0
        while row <= 5 and self.grid[row][column] == 0:
            row += 1

        row = row - 1
        self.grid[row, column] = n
        self.nb_played += 1

        # Colonne
        for i in range(3):
            if n == self.grid[i, column] == self.grid[i + 1, column] == self.grid[i + 2, column] == self.grid[i + 3, column]:
                return (True, (row, column))

        # Ligne
        for i in range(4):
            if n == self.grid[row, i] == self.grid[row, i + 1] == self.grid[row, i + 2] == self.grid[row, i + 3]:
                return (True, (row, column))

        # Diagonale Nord-Ouest/Sud-Est
        i = 0
        while (row - i) >= 0 and (column - i) >= 0 and (n == self.grid[row - i, column - i] == self.grid[row, column]):
            i += 1
        j = 0
        while (row + j) <= 5 and (column + j) <= 6 and (n == self.grid[row + j, column + j] == self.grid[row, column]):
            j += 1
        if (i + j) >= 5 :
            return (True, (row, column))

        # Diagonale Nord-Est/Sud-Ouest
        i = 0
        while (row - i) >= 0 and (column + i) <= 6 and (n == self.grid[row - i, column + i] == self.grid[row, column]):
            i += 1
        j = 0
        while (row + j) <= 5 and (column - j) >= 0 and (n == self.grid[row + j, column - j] == self.grid[row, column]):
            j += 1
        if (i + j) >= 5 :
            return (True, (row, column))

        return (False, (row, column))

    def is_game_done(self):
        """
        :return: True si la partie est finie, False sinon
        :rtype: bool
        """
        res = False
        if self.nb_played == 42:
            res = True
        return res
