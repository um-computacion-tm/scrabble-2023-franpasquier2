from game.models import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None):
        if not isinstance(multiplier, int):
            raise ValueError("El valor del multiplicador debe ser un número entero.")
        if multiplier_type not in ('', 'letter', 'word'):
            raise ValueError("El tipo de multiplicador debe ser '', 'letter' o 'word'.")

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter 

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def __str__(self):
        return f"Cell(multiplier={self.multiplier}, multiplier_type='{self.multiplier_type}', letter={self.letter})"
    
    def remove_letter(self):
        self.letter = None

    def add_letter(self, letter: Tile):
        if not isinstance(letter, Tile):
            raise ValueError("Only Tile objects can be added as letters.")
        self.letter = letter

    def set_multiplier(self, multiplier, multiplier_type):
        if not isinstance(multiplier, int):
            raise ValueError("El valor del multiplicador debe ser un número entero.")
        if multiplier_type not in ('', 'letter', 'word'):
            raise ValueError("El tipo de multiplicador debe ser '', 'letter' o 'word'.")
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type

    def is_occupied(self):
        return self.letter is not None
    
    
    def can_contain_letter(self):
        return not self.is_occupied() and self.multiplier_type in ('', 'letter')





