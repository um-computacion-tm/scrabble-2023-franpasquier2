from game.board import Board
from game.player import Player
from game.models import BagTiles
import uuid

class Scrabble:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.gameid = str(uuid.uuid4())
        for _ in range(players_count):
            self.players.append(Player())

        self.current_player_index = 0
        self.turn = 0

    def playing(self):
        # Simplificamos la lógica, el juego continúa mientras la bolsa no esté vacía
        return len(self.bag_tiles.tiles) > 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.turn += 1

    def validate_word(self, word, location, orientation):
    # Obtener la dirección (horizontal o vertical)
        x, y = location
        if orientation == "H":
            direction = (1, 0)
        elif orientation == "V":
            direction = (0, 1)
        else:
            return False # Orientación no válida

    # Verificar si la palabra cabe en el tablero
        if x + len(word) * direction[0] > self.board.width or y + len(word) * direction[1] > self.board.height:
            return False

    # Verificar si la palabra cruza con alguna palabra existente en el tablero (implementación simplificada)
        for i in range(len(word)):
            cell_x, cell_y = x + i * direction[0], y + i * direction[1]
        if self.board.cells[cell_x][cell_y].letter is not None:
            return False

    # Otras reglas de validación pueden agregarse aquí

        return True


    def get_current_player(self):
        return self.players[self.current_player_index]

    def draw_tile(self):
        if len(self.bag_tiles.tiles) > 0:
            
            return self.bag_tiles.tiles.pop()
        else:
            return None 



