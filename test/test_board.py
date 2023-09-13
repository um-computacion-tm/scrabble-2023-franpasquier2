
import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[5]), 15)

    def test_H_True_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (3, 10)
        orientation = 'H'
        board.grid[3][10].letter = 'F'  # Simular una letra existente en la ubicación
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_H_False_word_inside_board(self):
        board = Board()
        word = "Universidad"
        location = (6, 10)
        orientation = 'h'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_V_True_word_inside_board(self):
        board = Board()
        word = 'Terreno'
        location = (9, 8)
        orientation = 'v'
        board.grid[9][8].letter = 'T'  # Simular una letra existente en la ubicación
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_V_False_word_inside_board(self):
        board = Board()
        word = 'Sierra'
        location = (15, 10)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_validate_word_inside_board_horizontal(self):
        board = Board()
        board.grid[3][10].letter = 'F'
        board.grid[4][10].letter = 'a'
        board.grid[5][10].letter = 'c'
        board.grid[6][10].letter = 'u'
        board.grid[7][10].letter = 'l'
        board.grid[8][10].letter = 't'
        board.grid[9][10].letter = 'a'
        board.grid[10][10].letter = 'd'
        word = "Facultad"
        location = (3, 10)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_inside_board_vertical(self):
        board = Board()
        board.grid[9][8].letter = 'T'
        board.grid[9][9].letter = 'e'
        board.grid[9][10].letter = 'r'
        board.grid[9][11].letter = 'r'
        board.grid[9][12].letter = 'e'
        board.grid[9][13].letter = 'n'
        board.grid[9][14].letter = 'o'
        word = "Terreno"
        location = (9, 8)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_inside_board_without_orientation(self):
        board = Board()
        word = "Terreno"
        location = (0, 0)  # Out of bounds
        orientation = ''
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)