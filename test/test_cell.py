import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        # Caso 1: Valores válidos
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier, 2)
        self.assertEqual(cell.multiplier_type, 'letter')
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(), 0)

        # Caso 2: Valor de multiplicador no válido (debe generar un ValueError)
        with self.assertRaises(ValueError):
            cell = Cell(multiplier='invalid', multiplier_type='letter')

        # Caso 3: Tipo de multiplicador no válido (debe generar un ValueError)
        with self.assertRaises(ValueError):
            cell = Cell(multiplier=2, multiplier_type='invalid')

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(cell.calculate_value(), 6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(cell.calculate_value(), 3)

if __name__ == '__main__':
    unittest.main()

