import unittest

from game.cell import Cell

def calculate_word_value(word: list[Cell]):
    value: int = 0
    multiplier_word = None
    for cell in word:
        value = value + cell.calculate_value()
        if cell.multiplier_type == 'word':
            multiplier_word = cell.multiplier
            cell.multiplier = 1
    if multiplier_word != None:
        value = (value * multiplier_word)
    return value

class Tools_1:
    def move_pointer(self, orientation, row, column):
        if orientation == "H":
            column += 1
        elif orientation == "V":
            row += 1
        return row, column
    
    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'

    def format_placed_word_cell(self, cell):
        return f" {cell.letter.letter} "

    def format_active_cell(self, cell):
        if cell.status == 'active':
            return self.format_cell_contents(cell)

    def format_cell_contents(self, cell):
        if cell.letter is None:
            return self.format_multiplier(cell.multiplier, cell.multiplier_type)
        else:
            return self.format_placed_word_cell(cell)

    def format_multiplier(self, multiplier, multiplier_type):
            return f"{multiplier}{multiplier_type[0].upper()} "
    
    def filter_reapeted_column(self, list_tuples):
        columns = {}
        for row, column in list_tuples:
            if column not in columns:
                columns[column] = (row, column)
        list_tuples = list(columns.values())
        return list_tuples
    
    def filter_reapeted_row(self, list_tuples):
        rows = {}
        for row, column in list_tuples:
            if row not in rows:
                rows[row] = (row, column)
        list_tuples = list(rows.values())
        return list_tuples
