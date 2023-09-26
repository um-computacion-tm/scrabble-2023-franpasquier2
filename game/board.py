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
    
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
        
    def validate_word_passes_center(self, word, orientation):
        center_x, center_y = 7, 7  # Coordenadas del centro del tablero

        if orientation == "H":
            len_word = len(word)
            start_x = center_x - (len_word // 2)
            end_x = start_x + len_word

            if 0 <= start_x < 15 and 0 <= end_x < 15:
                return True
            else:
                return False
            
        elif orientation == "V":
            len_word = len(word)
            start_y = center_y - (len_word // 2)
            end_y = start_y + len_word

            if 0 <= start_y < 15 and 0 <= end_y < 15:
                return True
            else:
                return False
    
    
    
    