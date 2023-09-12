
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
