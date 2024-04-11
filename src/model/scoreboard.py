class Scoreboard:
    __slots__ = ['scores', 'is_first_start']

    """
    format scores :
    {
        "player1": [(23, 135, 10, "2024-02-15 15:12:43"), ...], # (nb_played, time, difficulty, score, date)
    }
    """

    def __init__(self):
        """Initialise le scoreboard qui contient un dictionnaire avec une liste de scores pour chaque joueur
        """
        self.scores = {}
        self.is_first_start = True
        self.load_scores()

    def load_scores(self):
        """Charge les scores depuis le fichier power4game_scores.json
        """

    def save_scores(self):
        """Sauvegarde les scores dans le fichier power4game_scores.json
        """

    def add_score(self, player_name, nb_played, time, date, difficulty):
        """Ajoute un score pour un joueur
        :return: score calculé
        """

    def calculate_score(self, nb_played, time, difficulty):
        """Calcule le score en fonction du nombre de coups joués et du temps
        :return: score calculé
        """

    def get_best_scores(self, nb_best_scores=5, player_name=None, difficulty=None):
        """Renvoie les meilleurs scores
        :param nb_best_scores: Nombre de meilleurs scores à renvoyer
        :type nb_best_scores: int
        :param player_name: Nom du joueur pour lequel on veut récupérer les meilleurs scores,
            si None, on récupère les meilleurs scores de tous les joueurs
        :type player_name: str
        """
