import json

import numpy as np


def calculate_score(nb_played, time, difficulty):
    """Calcule le score en fonction du nombre de coups joués et du temps
    :return: score calculé
    """
    score = nb_played * np.exp(-time / difficulty) * 10 ** 4
    return score


class Scoreboard:
    __slots__ = ['scores', 'is_first_start']

    """
    format scores :
    {
        "player1": [(23, 135, 6, True, "2024-02-15 15:12:43", 589), ...], # (nb_played, time, difficulty, is_red, date, score)
    }
    """

    def __init__(self):
        """Initialise le scoreboard qui contient un dictionnaire avec une liste de scores pour chaque joueur
        """
        self.scores = {}
        self.is_first_start = True
        self.load_scores()

    def load_dummy_scores(self):
        """Charge des scores de test
        """
        self.scores = {
            "player1": [(12, 135, 10, 100, "2024-02-15 15:12:43"), (23, 135, 10, 100, "2024-02-15 15:12:43")],
            "player2": [(23, 135, 10, 100, "2024-02-15 15:12:43"), (23, 135, 10, 100, "2024-02-15 15:12:43")],
            "player3": [(23, 135, 10, 100, "2024-02-15 15:12:43"), (23, 135, 10, 100, "2024-02-15 15:12:43")],
            "player4": [(23, 135, 10, 100, "2024-02-15 15:12:43"), (23, 135, 10, 100, "2024-02-15 15:12:43")],
            "player5": [(23, 135, 10, 100, "2024-02-15 15:12:43"), (23, 135, 10, 100, "2024-02-15 15:12:43")],
        }

    def load_scores(self):
        """Charge les scores depuis le fichier power4game_scores.json
        """
        try:
            file = open('power4game_scores.json', 'r', encoding='utf-8')
        except FileNotFoundError:
            print('scores file not found')
        else:
            with file:
                self.scores = json.load(file)

    def save_scores(self):
        """Sauvegarde les scores dans le fichier power4game_scores.json
        """
        with open('power4game_scores', 'w', encoding='utf-8') as mon_fichier:
            json.dump(self.scores, mon_fichier)

    def add_score(self, player_name, nb_played, time, difficulty, is_red, score, date):
        """Ajoute un score pour un joueur
        :return: score calculé
        """
        score_now = (nb_played, time, difficulty, is_red, score, date)
        if player_name in self.scores.keys():
            list_scores = self.scores[player_name]
            position = 0
            while score_now[5] <= list_scores[position][5]:
                position += 1
            list_scores.insert(position + 1, score_now)
        else:
            self.scores[player_name] = [score_now]

    def get_best_scores(self, nb_best_scores=5, player_name=None, difficulty=None):
        """Renvoie les meilleurs scores
        :param nb_best_scores: Nombre de meilleurs scores à renvoyer
        :type nb_best_scores: int
        :param player_name: Nom du joueur pour lequel on veut récupérer les meilleurs scores,
            si None, on récupère les meilleurs scores de tous les joueurs
        :type player_name: str
        :param difficulty: Difficulté pour laquelle on veut récupérer les meilleurs scores,
            si None, on récupère les meilleurs scores pour toutes les difficultés
        """
        best_scores = []
        for i in range(0, nb_best_scores):
            best_scores.append(self.scores[player_name][i])
        return best_scores
