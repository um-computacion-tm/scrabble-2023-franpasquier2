
from game.cell import Cell
from game.models import Tile


class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    def validate_word_inside_board(self, word, location: tuple, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        orientation = orientation.upper()
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            elif position_y + len_word > 1:
                return True 
        elif orientation == "V":
            if position_y + len_word > 15:
                return False
            elif position_x + len_word > 1:
                return True 

    


   