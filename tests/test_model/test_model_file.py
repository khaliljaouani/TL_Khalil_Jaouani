# Importez la classe de modèle à tester
from Models.Model import Player


import unittest


class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player("Alice", 0)
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.score, 0)

    def test_increase_score(self):
        player = Player("Bob", 10)
        player.increase_score(5)
        self.assertEqual(player.score, 15)


if __name__ == "__main__":
    unittest.main()
