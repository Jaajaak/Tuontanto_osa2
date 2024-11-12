import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_loytyyko_pelaaja_listassa(self):
        result = self.stats.search("Semenko")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Semenko")

    def test_olematon_pelaaja(self):
        result = self.stats.search("Selanne")
        self.assertIsNone(result)

    def test_loytyyko_joukkue(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        for player in team_players:
            self.assertEqual(player.team, "EDM")
    
    def test_vaara_joukkue(self):
        team_players = self.stats.team("FNC")
        self.assertEqual(len(team_players), 0)

    def test_top_oikeilla(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")