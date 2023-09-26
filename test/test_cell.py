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
        cell = Cell(1,'',Tile(letter='B', value=2))
        cell.remove_letter()
        self.assertEqual(self.cell.letter,None)

    def test_set_multiplier(self):
        cell = Cell()
        cell.set_multiplier(2, 'letter')
        self.assertEqual(cell.multiplier, 2)
        self.assertEqual(cell.multiplier_type, 'letter')

    def test_is_occupied(self):
        cell_occupied = Cell(letter=Tile('A', 1))
        cell_empty = Cell()
        self.assertTrue(cell_occupied.is_occupied())
        self.assertFalse(cell_empty.is_occupied())

    

if __name__ == '__main__':
    unittest.main()

