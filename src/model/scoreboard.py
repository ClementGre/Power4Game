class Scoreboard:
    __slots__ = ['scores', 'is_first_start']

    """
    format scores :
    [
        {
            "player_name": "player1",
            "score": 0
        }
    ]
    """

    def __init__(self):
        """Initialise le scoreboard qui contient une liste de dictionnaire de chaque partie jouée"""
        self.scores = {}
        self.is_first_start = True
        self.load_scores()

    def load_scores(self):
        """Charge les scores depuis le fichier power4game_scores.json
        """

    def save_scores(self):
        """Sauvegarde les scores dans le fichier power4game_scores.json
        """

    def get_best_scores(self, nb_best_scores=5, player_name=None):
        """Renvoie les meilleurs scores
        :param nb_best_scores: Nombre de meilleurs scores à renvoyer
        :type nb_best_scores: int
        :param player_name: Nom du joueur pour lequel on veut récupérer les meilleurs scores,
            si None, on récupère les meilleurs scores de tous les joueurs
        :type player_name: str
        """
