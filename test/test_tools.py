import unittest
from game.cell import Cell
from game.models import Tile
from game.tools import Tools_1

class TestTools(unittest.TestCase):
    def test_format_cell_content(self):
        tool = Tools_1()
        cell = Cell(letter=Tile("A",1))
        self.assertEqual(tool.format_cell_contents(cell).strip(), "A")
    
    def test_format_multiplier_word_2(self):
        tool = Tools_1()
        multiplier = 2
        multiplier_type = 'word' 
        expected_result = '2w ' 
        result = tool.format_multiplier(multiplier, multiplier_type)
        self.assertEqual(result.lower(), expected_result)

    def test_format_multiplier_letter_3(self):
        tool = Tools_1()
        multiplier = 3
        multiplier_type = 'letter'
        expected_result = "3L "  # Es azul
        result = tool.format_multiplier(multiplier, multiplier_type)
        self.assertEqual(result, expected_result)

    def test_filter_reapeated_colums(self):
        tool = Tools_1()
        list = [(7,7), (9,7)]
        list = tool.filter_reapeted_column(list)
        self.assertEqual(list, [(7,7)])

    def test_filter_reapeated_rows(self):
        tool = Tools_1()
        list = [(7,7), (7,9)]
        list = tool.filter_reapeted_row(list)
        self.assertEqual(list, [(7,7)])

if __name__ == '__main__':
    unittest.main()