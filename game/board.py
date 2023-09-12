from game.cell import Cell
from game.models import Tile 

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

    def validate_word_inside_board(self, word, location: tuple, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        orientation = orientation.upper()

        if orientation == "H":
            if position_x + len_word > 15 or position_y >= 15:
                return False  # Verificar que no esté fuera del tablero
            for i in range(len_word):
                if self.grid[position_x + i][position_y].letter != '' and self.grid[position_x + i][position_y].letter != word[i]:
                    return False  # Verificar colisión con letras existentes
            return True  # Devuelve True si la palabra es válida en la posición y orientación dadas
        elif orientation == "V":
            if position_y + len_word > 15 or position_x >= 15:
                return False  # Verificar que no esté fuera del tablero
            for i in range(len_word):
                if self.grid[position_x][position_y + i].letter != '' and self.grid[position_x][position_y + i].letter != word[i]:
                    return False  # Verificar colisión con letras existentes
            return True  # Devuelve True si la palabra es válida en la posición y orientación dadas
        return False  # Devuelve False si la orientación no es ni "H" ni "V"



    


   