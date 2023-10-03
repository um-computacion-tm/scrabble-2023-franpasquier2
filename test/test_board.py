import unittest
from game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(len(self.board.grid), 15)
        self.assertEqual(len(self.board.grid[5]), 15)

    def test_validate_word_inside_board_horizontal(self):
        self.board.grid[3][10].letter = 'F'
        self.board.grid[4][10].letter = 'a'
        self.board.grid[5][10].letter = 'c'
        self.board.grid[6][10].letter = 'u'
        self.board.grid[7][10].letter = 'l'
        self.board.grid[8][10].letter = 't'
        self.board.grid[9][10].letter = 'a'
        self.board.grid[10][10].letter = 'd'
        
        # Caso 1: Palabra válida
        word = "Facultad"
        location = (3, 10)
        orientation = 'H'
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

        # Caso 2: Palabra inválida
        word = "Universidad"
        location = (6, 10)
        word_is_valid = self.board.validate_word_inside_board(word, location, 'H')
        self.assertFalse(word_is_valid)

    def test_validate_word_inside_board_vertical(self):
        self.board.grid[9][8].letter = 'T'
        self.board.grid[9][9].letter = 'e'
        self.board.grid[9][10].letter = 'r'
        self.board.grid[9][11].letter = 'r'
        self.board.grid[9][12].letter = 'e'
        self.board.grid[9][13].letter = 'n'
        self.board.grid[9][14].letter = 'o'
        
        # Caso 1: Palabra válida
        word = 'Terreno'
        location = (9, 8)
        orientation = 'V'
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

        # Caso 2: Palabra inválida
        word = 'Sierra'
        location = (15, 10)
        word_is_valid = self.board.validate_word_inside_board(word, location, 'V')
        self.assertFalse(word_is_valid)

    def test_validate_word_inside_board_without_orientation(self):
        # Caso 1: Palabra inválida (sin orientación)
        word = "Terreno"
        location = (0, 0)
        orientation = ''
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)

    def test_is_empty(self):
        # Caso 1: Tablero vacío (la celda en (7, 7) no tiene una letra)
        self.assertTrue(self.board.is_empty())

        # Caso 2: Tablero con una letra en la celda (7, 7)
        self.board.grid[7][7].letter = 'A'
        self.assertFalse(self.board.is_empty())


    def test_is_empty_board_single_letter(self):
        # Caso 1: Tablero con una letra
        self.board.grid[7][7].letter = 'A'
        self.assertFalse(self.board.is_empty())

    def test_is_empty_board_full(self):
        # Caso 1: Tablero lleno
        for i in range(15):
            for j in range(15):
                self.board.grid[i][j].letter = 'X'
        self.assertFalse(self.board.is_empty())

    def test_is_empty_board_mixed(self):
        # Caso 1: Tablero con una letra en una celda
        self.board.grid[5][5].letter = 'Y'
        self.assertTrue(self.board.is_empty())

    def test_word_passes_center_horizontal(self):
        # Caso 1: Palabra que pasa por el centro horizontalmente
        word = "Facultad"
        location = (7, 6)
        word_is_valid = self.board.validate_word_inside_board(word, location, 'H')
        self.assertFalse(word_is_valid, "La palabra debe pasar por el centro horizontalmente.")

    def test_word_passes_center_vertical(self):
        # Caso 1: Palabra que pasa por el centro verticalmente
        word = "Terreno"
        location = (6, 7)
        word_is_valid = self.board.validate_word_inside_board(word, location, 'V')
        self.assertFalse(word_is_valid, "La palabra debe pasar por el centro verticalmente.")

    def test_validate_word_passes_center_horizontal_valid(self):
        # Caso 1: Palabra que pasa por el centro horizontalmente (válida)
        word = "Facultad"
        location = (7, 6)  # Posición donde el centro está en (7, 7)
        orientation = 'H'
        word_is_valid = self.board.validate_word_passes_center(word, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_passes_center_horizontal_invalid(self):
        # Caso 2: Palabra que no pasa por el centro horizontalmente (inválida)
        word = "Universidad"
        orientation = 'H'
        word_is_valid = self.board.validate_word_passes_center(word, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_passes_center_vertical_invalid(self):
        # Caso 4: Palabra que no pasa por el centro verticalmente (inválida)
        word = "Sierra"
        orientation = 'V'
        word_is_valid = self.board.validate_word_passes_center(word, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_inside_board_horizontal_out_of_bounds(self):
        # Caso 1: Palabra horizontal que excede los límites del tablero (inválida)
        word = "Facultad"
        location = (14, 10)
        orientation = 'H'
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)

    def test_validate_word_inside_board_vertical_out_of_bounds(self):
        # Caso 2: Palabra vertical que excede los límites del tablero (inválida)
        word = "Facultad"
        location = (10, 14)
        orientation = 'V'
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)



if __name__ == '__main__':
    unittest.main()



    
