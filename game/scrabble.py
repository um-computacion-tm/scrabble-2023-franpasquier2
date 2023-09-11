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

    def is_valid_orientation(self, orientation):
        return orientation in ("H", "V")

    def word_fits_on_board(self, word, location, direction):
        x, y = location
        return (
            0 <= x < self.board.width and
            0 <= y < self.board.height and
            x + len(word) * direction[0] <= self.board.width and
            y + len(word) * direction[1] <= self.board.height
        )

    
    """def crosses_existing_word(self, word, location, direction):
        x, y = location
        for i in range(len(word)):
            cell_x, cell_y = x + i * direction[0], y + i * direction[1]
            if not (0 <= cell_x < self.board.width and 0 <= cell_y < self.board.height):
                continue
            if self.board.cells[cell_x][cell_y].letter is not None:
                return True
        return False"""
               
    def validate_word(self, word, location, orientation):
        if not self.is_valid_orientation(orientation):
            return False

        direction = (1, 0) if orientation == "H" else (0, 1)

        if not self.word_fits_on_board(word, location, direction):
            return False

        if self.crosses_existing_word(word, location, direction):
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



