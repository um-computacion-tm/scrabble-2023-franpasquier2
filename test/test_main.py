import unittest
from game.scrabble import Scrabble

class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.game = Scrabble(2)  # Cambia el número de jugadores según sea necesario

    def test_is_valid_orientation(self):
        self.assertTrue(self.game.is_valid_orientation("H"))
        self.assertTrue(self.game.is_valid_orientation("V"))
        self.assertFalse(self.game.is_valid_orientation("D"))

    def test_word_fits_on_board(self):
        self.assertTrue(self.game.word_fits_on_board("PALABRA", (0, 0), (1, 0)))  # Horizontal
        self.assertTrue(self.game.word_fits_on_board("PALABRA", (0, 0), (0, 1)))  # Vertical
        self.assertFalse(self.game.word_fits_on_board("PALABRA", (14, 0), (1, 0)))  # Fuera de límites horizontal
        self.assertFalse(self.game.word_fits_on_board("PALABRA", (0, 14), (0, 1)))  # Fuera de límites vertical

    """def test_crosses_existing_word(self):
        # Configura un tablero con una palabra existente
        self.game.board.cells[0][0].add_letter("P")
        self.game.board.cells[0][1].add_letter("A")
        self.game.board.cells[0][2].add_letter("L")
        self.game.board.cells[0][3].add_letter("A")

        self.assertTrue(self.game.crosses_existing_word("PALABRA", (0, 0), (0, 1)))  # Cruza con palabra existente
        self.assertFalse(self.game.crosses_existing_word("BARCO", (0, 0),(1, 0)))  # No cruza con palabra existente"""

if __name__ == '__main__':
    unittest.main()
