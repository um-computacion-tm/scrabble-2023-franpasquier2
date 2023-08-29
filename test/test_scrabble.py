import unittest
from game.scrabble import ScrabbleGame

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = ScrabbleGame(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
    def test_unique_id(self):
        game_1 = ScrabbleGame(1)
        game_2 = ScrabbleGame(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)

if __name__ == '__main__':
    unittest.main()
