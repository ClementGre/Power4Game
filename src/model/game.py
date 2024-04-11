from tkinter import Button

import numpy as np

class Game:

    __slots__ = ['player_name', 'is_player_red', 'grid', 'nb_played']

    def __init__(self, player_name, is_player_red):
        self.player_name = player_name
        self.is_player_red = is_player_red
        self.grid = np.zeros((6, 7), dtype=int)
        self.nb_played = 0


