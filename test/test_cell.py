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

    def setUp(self):
        self.cell = Cell()

    def test_add_letter_valid(self):
        letter = Tile(letter='A', value=1)
        self.cell.add_letter(letter)
        self.assertEqual(self.cell.letter, letter)

    def test_add_letter_invalid(self):
        with self.assertRaises(ValueError):
            self.cell.add_letter('InvalidLetter')  # Intenta agregar un objeto que no es Tile
        self.assertIsNone(self.cell.letter)  # La letra no debe haberse agregado

    def test_remove_letter(self):
        letter = Tile(letter='B', value=2)
        self.cell.add_letter(letter)
        self.cell.remove_letter()
        self.assertIsNone(self.cell.letter)

if __name__ == '__main__':
    unittest.main()

