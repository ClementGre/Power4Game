import json

import numpy as np

from src.utils.format import format_time_ms


def calculate_score(nb_played, time, difficulty):
    """Calcule le score en fonction du nombre de coups joués et du temps
    :return: score calculé
    """
    score = nb_played * np.exp(-time / difficulty) * 10 ** 4
    return int(score)


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
        with open('power4game_scores.json', 'w', encoding='utf-8') as mon_fichier:
            json.dump(self.scores, mon_fichier)

    def add_score(self, player_name, nb_played, time, difficulty, is_red, score, date):
        """Ajoute un score pour un joueur
        :return: score calculé
        """
        score = (nb_played, format_time_ms(time), difficulty, is_red, score, date)
        if player_name in self.scores.keys():
            self.scores[player_name].append(score)
        else:
            self.scores[player_name] = [score]

        self.save_scores()

    def calculate_score(self, nb_played, time, difficulty):
        """Calcule le score en fonction du nombre de coups joués et du temps
        :return: score calculé
        """
        score = nb_played * 10 ** (-time / (difficulty * 1e3))
        return score

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

        filtered_scores = []

        for player, player_scores in self.scores.items():
            for score in player_scores:
                filtered_scores.append([player] + list(score))

        if player_name is not None:
            filtered_scores = [v for v in filtered_scores if player_name in v[0]]
        if difficulty is not None:
            filtered_scores = [v for v in filtered_scores if v[3] == difficulty]

        best_scores = sorted(filtered_scores, key=lambda x: x[5], reverse=True)[:nb_best_scores]
        return best_scores
