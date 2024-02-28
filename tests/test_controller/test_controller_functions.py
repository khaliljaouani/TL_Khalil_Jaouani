# Import du module à tester
# Avant
from Models.Model import Player
from Controllers.MatchController import fonction_utilisee

# Après (en utilisant la fonction importée)
resultat = fonction_utilisee()


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def increase_score(self, points):
        self.score += points
